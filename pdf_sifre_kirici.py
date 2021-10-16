#coding:utf-8
import pikepdf
from tqdm import tqdm


oku=open("rockyou.txt","rb")
pass1=oku.readlines()
sifreler=[]
for i in pass1:
    dex=str(i).replace("\n","").replace("\r","")
    sifreler.append(dex)
oku.close()


for sifre in tqdm(sifreler, "Decode PDF"):
    try:
        with pikepdf.open("siberguvenlikicinpython.pdf", password=sifre) as pdf:
            print("[+] Şifre Bulundu = ", sifre)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
