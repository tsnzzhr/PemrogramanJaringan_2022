import logging
import requests
import os
import time
import datetime
import urllib

dean = "https://disk.mediaindonesia.com/thumbs/1800x1200/news/2020/08/2458323918fcf2a260361ea333b03657.jpg"
luke = "https://static.republika.co.id/uploads/images/inpicture_slide/luke-shaw-menjadi-model-jersey-baru-kandang-manchester-united_210715222339-444.png"
aaron = "https://www.wharfedaleobserver.co.uk/resources/images/13313868/"
victor = "https://ceritabola.com/wp-content/uploads/2021/03/PRI_88335064.jpg"
pogba = "https://cdns.klimg.com/bola.net/library/upload/21/2021/08/645x430/pogba1_5b1c208.jpg"
cr = "https://cloud.jpnn.com/photo/arsip/normal/2021/09/30/bintan-manchester-united-cristiano-ronaldo-tampak-emosional-b3gh.jpg"
elanga = "https://www.footballdatabase.eu/images/photos/players/a_378/378794.jpg"
degea = "https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/bltf153e19e2c57d08d/62068fb6d55b52791df4a719/David_de_Gea.jpg?auto=webp&fit=crop&format=jpg&height=800&quality=60&width=1200"
joe = "https://assets.manutd.com/AssetPicker/images/0/0/10/126/687715/Legends-Profile_Ryan-Giggs11523461897441_thumb.jpg"
dick = "https://i2-prod.manchestereveningnews.co.uk/incoming/article22370440.ece/ALTERNATES/s1200/1_GettyImages-1357289371.jpg"
billy = "https://www.scotsman.com/webimg/b25lY21zOjdiMDk3ODQxLWRjNzMtNGY1MS1hMzg5LWZkYmMxNDM4NzljMToxM2I0OTY5ZS01N2Y1LTRkYTEtOThmYi1jMGI5MTdkOWQwNTU=.jpg?width=2048&enable=upscale"
vince = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQNQRzsSnGuq44XuSAXxMWDh98QsYpZfwIVV3YyvVZsqZ-lvUh-1lzGvCHfiE4gw0jS0k&usqp=CAU"
meredith = "https://pbs.twimg.com/media/EZax2OjX0AAHTCX.jpg"
alex = "https://pbs.twimg.com/media/EX4kk0TXQAARZ0v.jpg"
spence = "https://assets.manutd.com/AssetPicker/images/0/0/10/126/687699/Legends-Profile_Arthur-Albiston11523460090173_thumb.jpg"

def get_list():
    data = dict()
    data['1']=dict(nomor=1, nama="Dean Henderson", posisi="Goal-Keeper", foto=dean)
    data['3']=dict(nomor=3, nama="Luke Shaw", posisi="Left-Defender", foto=luke)
    data['5']=dict(nomor=5, nama="Aaron Wan-bissaka", posisi="Right-Defender", foto=aaron)
    data['7']=dict(nomor=7, nama="Victor Lindelof", posisi="Midfielder", foto=victor)
    data['9']=dict(nomor=9, nama="Paul Pogba", posisi="Midfielder", foto=pogba)
    data['11']=dict(nomor=11, nama="Christiano Ronaldo", posisi="Forward", foto=cr)
    data['13']=dict(nomor=13, nama="Anthony Elanga", posisi="Forward", foto=elanga)
    data['15']=dict(nomor=15, nama="David De Gea", posisi="Goal-Keeper", foto=degea) 
    data['17']=dict(nomor=17, nama="Joe Cassidy", posisi="Goal-Keeper", foto=joe) 
    data['19']=dict(nomor=19, nama="Dick Smith", posisi="Goal-Keeper", foto=dick)  
    data['21']=dict(nomor=21, nama="Billy Morgan", posisi="Goal-Keeper", foto=billy)  
    data['23']=dict(nomor=23, nama="Vince Hayes", posisi="Goal-Keeper", foto=vince)  
    data['25']=dict(nomor=25, nama="Billie Meredith", posisi="Goal-Keeper", foto=meredith)
    data['27']=dict(nomor=27, nama="Alex Bell", posisi="Goal-Keeper", foto=alex)  
    data['29']=dict(nomor=29, nama="Joe Spence", posisi="Goal-Keeper", foto=spence)          
    return data


def download_image(url=None,tuliskefile=True):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/gif']='gif'
    tipe['image/jpeg']='jpg'
    tipe['application/zip']='jpg'
    tipe['video/quicktime']='mov'
    time.sleep(1) #untuk simulasi

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"thread_download_result/{namafile}","wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"====(BERHASIL!)==== Download {namafile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False

