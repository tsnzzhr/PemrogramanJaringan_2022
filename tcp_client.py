import sys
import socket
import json
import time
import datetime
import random
import threading
import logging
import xmltodict
import ssl
import os

server_address = ('172.16.16.104', 15000)

#server_address = ('172.16.16.104', 12000)

def make_socket(destination_address='localhost',port=10000):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (destination_address, port)
        logging.warning(f"=== MENGHUBUNGKAN KE SERVER : {server_address} ===")
        sock.connect(server_address)
        return sock
    except Exception as ee:
        logging.warning(f"ERROR : {str(ee)}")

def make_secure_socket(destination_address='localhost',port=10000):
    try:
        #get it from https://curl.se/docs/caextract.html

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.verify_mode=ssl.CERT_OPTIONAL
        context.load_verify_locations(os.getcwd() + '/certs_client/domain.crt')

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (destination_address, port)
        logging.warning(f"=== MENGHUBUNGKAN KE ALAMAT SERVER : {server_address} ===")
        sock.connect(server_address)
        secure_socket = context.wrap_socket(sock,server_hostname=destination_address)
        logging.warning(secure_socket.getpeercert())
        return secure_socket
    except Exception as ee:
        logging.warning(f"ERROR : {str(ee)}")

def deserialisasi(s):
    logging.warning(f"=== DESERIALISASI : {s.strip()} ===")
    return json.loads(s)
    

def send_command(command_str,is_secure=False):
    alamat_server = server_address[0]
    port_server = server_address[1]
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# gunakan fungsi diatas
    if is_secure == True:
        sock = make_secure_socket(alamat_server,port_server)
    else:
        sock = make_socket(alamat_server,port_server)

    logging.warning(f"connecting to {server_address}")
    try:
        logging.warning(f"sending message ")
        sock.sendall(command_str.encode())
        # Look for the response, waiting until socket is done (no more data)
        data_received="" #empty string
        while True:
            #socket does not receive all data at once, data comes in part, need to be concatenated at the end of process
            data = sock.recv(16)
            if data:
                #data is not empty, concat with previous content
                data_received += data.decode('utf-8')
                if "\r\n\r\n" in data_received:
                    break
            else:
                # no more data, stop the process by break
                break
        # at this point, data_received (string) will contain all data coming from the socket
        # to be able to use the data_received as a dict, need to load it using json.loads()
        hasil = deserialisasi(data_received)
        if (hasil):
            logging.warning(f"data received from server: {hasil}")
        else:
            logging.warning('<><><><><><><><><>< Data Tidak Ditemukan ><><><><><><><><<><><><')
        return hasil
    except Exception as ee:
        logging.warning(f"error during data receiving {str(ee)}")
        return False



def getdatapemain(nomor=0,is_secure=False):
    cmd=f"getdatapemain {nomor}\r\n\r\n"
    hasil = send_command(cmd,is_secure=is_secure)
    return hasil

def lihatversi(is_secure=False):
    cmd=f"versi \r\n\r\n"
    hasil = send_command(cmd,is_secure=is_secure)
    return hasil
    


if __name__=='__main__':
    #h = lihatversi(is_secure=False)
    #if (h):
    #    print(h)
    is_secure = True
    """
    print("========== ONE THREAD [NON-SECURED] ============/n")
    th_satu = dict()
    catat_awal = datetime.datetime.now()
    th_satu = threading.Thread(target=getdatapemain,args=(3,))
    th_satu.start()
    th_satu.join()
        
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    """
    print("========== ONE THREAD [SECURED] ============/n")
    th_satu_s = dict()
    catat_awal = datetime.datetime.now()
    th_satu_s = threading.Thread(target=getdatapemain,args=(3,is_secure))
    th_satu_s.start()
    th_satu_s.join()
        
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    """
    
    
    print("========== 5 THREAD [NON-SECURED] ============/n")
    th_lima = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 6):
        th_lima[x] = threading.Thread(target=getdatapemain,args=(x,))
        th_lima[x].start()
    
    for x in range(1, 6):
        th_lima[x].join()
                       
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    """
    print("========== 5 THREAD [SECURED] ============/n")
    th_lima_s = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 6):
        th_lima_s[x] = threading.Thread(target=getdatapemain,args=(x,is_secure))
        th_lima_s[x].start()
    
    for x in range(1, 6):
        th_lima_s[x].join()
                       
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    """
    print("========== 10 THREAD [NON-SECURED] ============/n")
    th_spulu = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 11):
        th_spulu[x] = threading.Thread(target=getdatapemain,args=(x,))
        th_spulu[x].start()
        
    for x in range(1, 11):
        th_spulu[x].join()
            
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    
    """
    print("========== 10 THREAD [SECURED] ============/n")
    th_spulu_s = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 11):
        th_spulu_s[x] = threading.Thread(target=getdatapemain,args=(x,is_secure))
        th_spulu_s[x].start()
        
    for x in range(1, 11):
        th_spulu_s[x].join()
            
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    """
    print("========== 20 THREAD [NON-SECURED] ============/n")
    th_duapulu = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 21):
        th_duapulu[x] = threading.Thread(target=getdatapemain,args=(x,))
        th_duapulu[x].start()
    
    for x in range(1,21):
        th_duapulu[x].join()
            
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
    
    """
    print("========== 20 THREAD [SECURED] ============/n")
    th_duapulu_s = dict()
    catat_awal = datetime.datetime.now()
    for x in range(1, 21):
        th_duapulu_s[x] = threading.Thread(target=getdatapemain,args=(x,is_secure))
        th_duapulu_s[x].start()
    
    for x in range(1,21):
        th_duapulu_s[x].join()
            
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")