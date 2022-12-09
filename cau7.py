# BẢNG 1 BÀI 7 
import os
def xoa_file():
    os.remove('E:/filedexoa.txt.txt')
    print("xóa file thành công")
def xoa_thu_muc():
    os.rmdir('E:/thumucdexoa')
    print("xóa thư mục thành công ")
z1=xoa_thu_muc()
z2=xoa_file()