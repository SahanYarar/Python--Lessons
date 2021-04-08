import sqlite3

con=sqlite3.connect("kütüphane.db")

cursor=con.cursor()

def tablo_oluştur():
    cursor.execute("CREATE TABLE İF NOT EXİSTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()

def değer_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert İnto kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    data=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri....")
    for i in data:
        print(i)

def verileriguncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi= ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
def verilerisil(yazar):
    cursor.execute("Delete From kitaplık where Yazar = ?",(yazar,))
    con.commit()
    
    
verileri_al()  

con.close()        
