from lib import get_list
import sys
import socket
import time
import datetime
import logging
import json
import dicttoxml
import threading
import os
import ssl

def versi():
    return "versi 0.0.1"

def proses_request(request_string):
    #format request
    # NAMACOMMAND spasi PARAMETER
    alldata = get_list();
    cstring = request_string.split(" ")
    hasil = None
    try:
        command = cstring[0].strip()
        if (command == 'getdatapemain'):
            # getdata spasi parameter1
            # parameter1 harus berupa nomor pemain
            logging.warning("getdata")
            nomorpemain = cstring[1].strip()
            try:
                hasil = alldata[nomorpemain]
                if(hasil):
                    logging.warning(f"######### Data Nomor Pemain : {nomorpemain} Ditemukan! ##########")
            except:
                hasil = None
                logging.warning(f"######### !!!!!! DATA NOMOR PEMAIN : {nomorpemain} TIDAK DITEMUKAN !!!!!! ########")
        elif (command == 'versi'):
            hasil = versi()
    except:
        hasil = None
    return hasil


def serialisasi(a):
    #print(a)
    #serialized = str(dicttoxml.dicttoxml(a))
    serialized =  json.dumps(a)
    logging.warning("=== DATA TER-SERIALISASI ===")
    logging.warning(serialized)
    return serialized

def run_server(server_address,is_secure=False):
    # ------------------------------ SECURE SOCKET INITIALIZATION ----
    if is_secure == True:
        print(os.getcwd())
        cert_location = os.getcwd() + '/certs_server/'
        #print(cert_location)
        socket_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        socket_context.load_cert_chain(
            certfile=cert_location + 'domain.crt',
            keyfile=cert_location + 'domain.key'
        )
    # ---------------------------------

    #--- INISIALISATION ---
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    logging.warning(f"==== DIMULAI DARI SERVER : {server_address} ====")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1000)


    while True:
        # Wait for a connection
        logging.warning("waiting for a connection")
        koneksi, client_address = sock.accept()
        logging.warning(f"==== KONEKSI MASUK DARI : {client_address} ====")
        # Receive the data in small chunks and retransmit it
        
        try:    
            if is_secure == True:
                connection = socket_context.wrap_socket(koneksi, server_side=True)
            else:
                connection = koneksi

            selesai=False
            data_received="" #string
            while True:
                data = connection.recv(32)
                logging.warning(f"===== DITERIMA : {data}")
                if data:        
                        #catat_awal = datetime.datetime.now()
                        data_received += data.decode('utf-8')
                        if "\r\n\r\n" in data_received:
                            selesai=True
                        if (selesai==True):
                            hasil = proses_request(data_received)
                            logging.warning(f"=== RESPONSE/RESULT : {hasil} ===")
                            hasil = serialisasi(hasil)
                            hasil += "\r\n\r\n"
                            connection.sendall(hasil.encode())
                            selesai = False
                            data_received = ""  # string
                            #catat_akhir = datetime.datetime.now()
                            #selesai = catat_akhir - catat_awal
                            #logging.warning(f"<><><> Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir} <><><>")
                            break
                else:
                    logging.warning(f"=== No More Data From : {client_address} ===")
                    break
            # Clean up the connection
        except ssl.SSLError as error_ssl:
            logging.warning(f"SSL Error: {str(error_ssl)}")

if __name__=='__main__':
    try:
        run_server(('0.0.0.0',12000),is_secure=False)
    except KeyboardInterrupt:
        logging.warning("Ctrl-C: Program Terminated")
        exit(0)
    finally:
        logging.warning(f"===== SELESAI =====")
