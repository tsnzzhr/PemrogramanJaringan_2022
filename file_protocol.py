import json
import logging

from file_interface import FileInterface

"""
* class FileProtocol bertugas untuk memproses 
data yang masuk, dan menerjemahkannya apakah sesuai dengan
protokol/aturan yang dibuat

* data yang masuk dari client adalah dalam bentuk bytes yang 
pada akhirnya akan diproses dalam bentuk string

* class FileProtocol akan memproses data yang masuk dalam bentuk
string
"""



class FileProtocol:
    def __init__(self):
        self.file = FileInterface()
    def proses_string(self,string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        c = string_datamasuk.split(" ")
        try:
            c_request = c[0].strip()
            print(f"{c_request}")
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            if (c_request=='LIST'):
                return json.dumps(self.file.list())
            elif (c_request=='GET'):
                return json.dumps(self.file.get(params))
            elif (c_request=='ADD'):
                return json.dumps(self.file.add(params))
            elif (c_request=='REMOVE'):
                return json.dumps(self.file.remove(params))
            else:
                return json.dumps(dict(status='ERROR', data='request tidak dikenali'))
        except Exception:
            return json.dumps(dict(status='ERROR',data='Exception Trigger'))


if __name__=='__main__':
    #contoh pemakaian
    fp = FileProtocol()
    print(fp.proses_string("LIST"))
    print(fp.proses_string("GET pokijan.jpg"))
