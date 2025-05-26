import qrcode

url = input("gave me url to change it into qrcode")
myqr = qrcode.make(url)

name = input("give me the name of img =>")
myqr.save(name+".png")
