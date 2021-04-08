import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri........")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi=?",(yayınevi,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
    
verileri_al3("Everest")

con.close()
