import os
def cau_6():
    try:
        f=open('E:/docoday.txt.txt',encoding="utf-8")
        print(f.read())
    finally:
        f.close()
z=cau_6()