import _sqlite3
import time
import random
import hashlib



baglanti=_sqlite3.connect('database/rehber.db')
cursor=baglanti.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS birimler (
    birim_no INTEGER PRIMARY KEY AUTOINCREMENT,
    birim_adi VARCHAR(50)
    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS kisiler (
    kisi_no INTEGER PRIMARY KEY,
    unvani VARCHAR(50),
    soyadi VARCHAR(50),
    calistigi_birim INTEGER,
    telefonu VARCHAR(10),
    FOREIGN KEY (calistigi_birim) REFERENCES birimler(birim_no)
)""")


cursor.execute("""CREATE TABLE IF NOT EXISTS kullanicilar (
    kullanici_no INTEGER PRIMARY KEY,
    kullanici_adi VARCHAR(50),
    kullanici_parolasi VARCHAR(50),
    kullanici_oturumu VARCHAR(32) DEFAULT NULL     
    
)""")

baglanti.commit()


import os,time,sqlite3
from http import cookies

class REHBER():
    def __init__(self):
        self.form.get=self.form.getvalue
        self.betik=os.environ['SCRİPT NAME']

        self.ust=[]
        self.alt=[]
        self.hata=[]

        self.formAction=''
        self.renkler=['']
        self.onayli=false

        self.cerezler=cookies.SimpleCookie()
        try:self.cerezler.load(os.environ["HTTP_COOKIE"])
        except:pass

        self.path=os.environ['PATH_INFO'].split('/')
        self.baglanti.row_factory=_sqlite3.Row


