from flask import Flask,render_template,redirect, url_for,request,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

import youtube_dl

with open('config.json','r') as c:
    param=json.load(c)['params']
lk=[]
lj=[]
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = param['local_url']
db = SQLAlchemy(app)
class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.DateTime, nullable=True,default=datetime.utcnow)

class project(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=True,default=datetime.utcnow)

    
@app.route('/index')
def index():
    return render_template('index.html',param=param)
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts',methods=['GET','POST'])
def contacts():
    if (request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        mobile=request.form.get('mobile')
        message=request.form.get('message')
        entry=contact(name=name,email=email,mobile=mobile,message=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if 'user' in session and (session['user']==param['admin']):
        posts=project.query.filter_by().all()
        return render_template('dashboard.html',posts=posts)
    if (request.method=='POST'):
        if (request.form.get('uname')==param['admin']) and (request.form.get('password')==param['password']):
            session['user']=request.form.get('uname')
            posts=project.query.filter_by().all()
            return render_template('dashboard.html',posts=posts)
        else:
            flash("incorrect credential")
            return render_template('admin.html',param=param)
    else:
        flash("incorrect credential")
        return render_template('admin.html',param=param)

@app.route('/project')
def project1():
    posts=project.query.filter_by().all()[0:5]
    return render_template('project.html',param=param,data=posts)
@app.route('/project/<int:sno>',methods=['GET','POST'])
def projects(sno):
    data=project.query.filter_by(sno=sno).first()
    return render_template('post.html',data=data,param=param)


@app.route('/edit/<int:sno>',methods=['GET','POST'])
def edit(sno):
    if 'user' in session and (session['user']==param['admin']):
        if request.method=='POST':
            title=request.form.get('title')
            content=request.form.get('content')
            date=datetime.now()
            if sno==0:
                post=project(title=title,content=content,date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post=project.query.filter_by(sno=sno).first()
                post.title=title
                post.content=content
                db.session.commit()
                return redirect(url_for('dashboard')) 
                 
        post=project.query.filter_by(sno=sno).first()
        return render_template('edit.html',param=param,post=post,sno=sno)

    post=project.query.filter_by().first()
    return render_template('edit.html',param=param,post=post)
@app.route('/delete/<int:sno>',methods=['GET','POST'])
def delete(sno):
    if 'user' in session and (session['user']==param['admin']):
        
        post=project.query.filter_by(sno=sno).one()
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
   session.pop('user', None)
   flash("you have been logged out ")
   return render_template('admin.html')

@app.route('/download')
def download():
    return render_template('download.html')
@app.route('/link',methods=['GET','POST'])
def links():
    link=request.form.get('name')
    with youtube_dl.YoutubeDL() as ydl:

        url=ydl.extract_info(link,download=False)
        # data=url["formats"][-1]['url']
        data=url
        # lk.append(link)
        # yt=YouTube(link) 
        # a=yt.streams.all()
        
        # return redirect(data)
        return render_template('yt.html',data=data)
@app.route('/links/<int:c>',methods=['POST','GET'])
def downloading(c):
    global lk
    b=c
    # if request.method=='POST':
    link=lk[0]
    yt=YouTube(link) 
    a=yt.streams.all()
    for i in a:
        lj.append(i)
    like=lj[c]
    like.download()
    lj.clear()
    lk.clear()
    
        # return redirect(url_for('links'))
    # return render_template('download.html')
    return render_template('download.html',b=b)
# for i in links:
#     print(j,'>',(i.filesize)/1024000,'mb',i)
#     j+=1
# a=int(input('which video:'))
# downloaded_link=links[a]
# downloaded_link.download('E:/web')
# print('downloaded')
if __name__ == "__main__":
    app.config['SECRET_KEY'] = "flash"
    app.run(debug=True)