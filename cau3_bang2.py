import os
def tap_tin_nhi_phan():
    f=open("C:/Users/MINH QUY/Downloads/wallpaperflare.com_wallpaper.jpg","wb")
    data=bytearray(" ghi nhi phan ".encode("ascii"))
    f.write(data)
    f.close()
    f = open("C:/Users/MINH QUY/Downloads/wallpaperflare.com_wallpaper.jpg", "rb")
    print(f.read())
    f.close()

tap_tin_nhi_phan()

