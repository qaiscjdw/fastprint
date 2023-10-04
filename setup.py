import datetime
import requests
import hashlib
import mysql.connector
import json

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database = 'db_testfastprint'
)
sql = db.cursor(buffered=True)

def insert_kategori(kategori, same):
    for ulang2 in list_kategori:
        if ulang2 == kategori:
            same = True
            break
        else:
            same = False
    if same == False:
        list_kategori.append(kategori)
        sql.execute("INSERT INTO kategori (nama_kategori) VALUES (\'{}\')".format(kategori))
        db.commit()
        
def insert_status():
    sql.execute("INSERT INTO status (nama_status) VALUES (\'bisa dijual\')")
    db.commit()
    sql.execute("INSERT INTO status (nama_status) VALUES (\'tidak bisa dijual\')")
    db.commit()
    
def insert_produk(id,nama,harga,kategori,status):
    sql.execute("SELECT id_kategori FROM kategori WHERE nama_kategori = \'{}\'".format(kategori))
    id_kategori = sql.fetchone()[0]
    sql.execute("SELECT id_status FROM status WHERE nama_status = \'{}\'".format(status))
    id_status = sql.fetchone()[0]
    sql.execute("INSERT INTO produk (id_product,nama_produk,harga,kategori_id,status_id) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(id,nama,harga,id_kategori,id_status))
    db.commit()

now = datetime.datetime.now()
api = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
date = now.strftime("%d%m%y")
set_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
hour = set_hour.hour
username = "tesprogrammer"+date+"C"+str(hour)
date = now.strftime("%d-%m-%y")
txtpas = "bisacoding-"+str(now.strftime("%d-%m-%y"))
password = hashlib.md5(txtpas.encode())
md5pass = password.hexdigest()

session = requests.Session()
login_data = {
        'username': username,
        'password': md5pass 
    }
response = session.post(api, data=login_data)
try :
    if(response.status_code == 200):
        tmp = response.content
        my_json = tmp.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        list_kategori = []
        same = False

        insert_status()
        for ulang in data["data"]:
            id_produk = ulang["id_produk"]
            nama_produk = ulang["nama_produk"]
            harga = ulang["harga"]
            kategori = ulang["kategori"]
            status = ulang["status"]
            insert_kategori(kategori=kategori,same=same)
            insert_produk(id=id_produk,nama=nama_produk,harga=harga,kategori=kategori,status=status)
except Exception as err:
    print(err)
        
