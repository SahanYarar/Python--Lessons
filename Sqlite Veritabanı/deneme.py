import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle():
    isim=input("İsim:")
    yazar=input("Yazar:")
    yayınevi=input("Yayınevi:")
    sayfa_sayısı=int(input("Sayfa sayısı:"))
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık") 
    data = cursor.fetchall() 
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def veri_sil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?",(yazar,))
    con.commit()
    
    
verileri_al()
con.close()
