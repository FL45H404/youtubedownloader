
import youtube_dl
import json

link={}
with youtube_dl.YoutubeDL() as ydl:

    url=ydl.extract_info('https://www.youtube.com/watch?v=ecP56OZ-ggU',download=False)
#     with open('sample.json','w') as f:
#         f.write(json.dumps(url,indent=1))
    print(url['id'][0])
# with open('sample.json','r+') as f:
#     data=json.load(f)["formats"][0]['url']
# #     print(data)
# https://r6---sn-gwpa-cagd.googlevideo.com/videoplayback?expire=1603839806&ei=3lKYX9ebCsyN1Aah05y4Cg&ip=2409%3A4071%3A238e%3A1671%3Af941%3A8ced%3Abf5%3Aed03&id=o-AOJ0PHhYoEvhmmcizvwXLfC6ePgijnP8WhA2za9O9wcv&itag=22&source=youtube&requiressl=yes&mh=7m&mm=31%2C29&mn=sn-gwpa-cagd%2Csn-h5576n7k&ms=au%2Crdu&mv=m&mvi=6&pl=41&initcwndbps=133750&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=40.936&lmt=1586749015963040&mt=1603818049&fvip=5&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgOmUYb9hQnU-mJzp5XhMPvc325xQL1mgdLIa1Ps7MNvQCIGsIlEh3N3og14EghvdHqvOLD5hiqDbxy8OZTgScvlne&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgCbibhtPyMXPR8jvWdD77EfHsJsmE0HnecQJxEnhTx30CIHTFb7jFkeAYOWwS1JTHeyld31LJYCdk6hg7wJjFvhULdl-l
# https://r5---sn-gwpa-cagk.googlevideo.com/videoplayback?expire=1603832632&ei=1zaYX929PNCuwgPzjo2IBw&ip=2409%3A4071%3A238e%3A1671%3Aa095%3A3ce8%3A7a48%3A3d30&id=o-ABeOQVGp2DVqrAbfBoxVj7f-dbL2FzO_EwA_ONPwfxBR&itag=22&source=youtube&requiressl=yes&mh=6a&mm=31%2C29&mn=sn-gwpa-cagk%2Csn-h557sns7&ms=au%2Crdu&mv=m&mvi=5&pl=41&initcwndbps=152500&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=163.305&lmt=1603701466677493&mt=1603810847&fvip=5&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgcCvRFYaMDFRKh8yo6qkvpFuSVeNxmHH_fkCJf0_fAzQCIBoMBfd-SFzO2uEoUC11VIGaWLWKw9D3-URQh9z2soRK&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgTepl_BgCOkQJ4GIxqDNP4Jslby09PFnNtQNoDGzIMZ4CIE6N6SEFoHfchR_WpbVW0GuYKRBINOQjE6-TppIJ2hsT
