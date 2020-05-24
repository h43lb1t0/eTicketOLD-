import pyqrcodeng

def qrCode(URL,evt): #A function that can be called via main.py and generates qr-codes from the links stored in the links.py file#
    i = 0
    for x in URL:
        data = URL[i]
        i = i+1
        qr = pyqrcodeng.create(data)
        qr.png(evt + 'qr_'+ str(i)+'.png', scale = 9)
        print('QR-Code:', str(i))
    



