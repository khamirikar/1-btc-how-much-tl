from tkinter import *
btc = Tk()
btc.geometry("750x450")
btc.title("Kac TL?")
btc.iconbitmap('bitcoin.ico')
btc_ust = Frame(btc, bg="grey")
btc_ust.place(relx=0.1, rely=0.1, relheight=0.5, relwidth=0.8)
btc_sonuc = Frame(btc, bg="blue")
btc_sonuc.place(relx=0.1, rely=0.7, relheight=0.2, relwidth=0.8)
btc_yazi = Label(btc_ust, text="Uygulama Hep Gunceldir (NMK)", font="Verdana 18 bold",bg="blue").pack()

import requests
from bs4 import BeautifulSoup


def sonuc():

    headers = {'User-Agent' : 'Mozilla/5.0'}
    url = 'https://www.icrypex.com/tr/teknoloji/kripto-para-cevirici'
    content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(content, "html.parser")

    result = soup.find("strong", attrs={"class" : "cryrptmoney-02"})
    bitcoin = float(result.text.strip().split()[0])
    cikti = Label(btc_sonuc,text=bitcoin).pack()
    



btc_button = Button(btc_ust,text="Bitcoin Kac TL?", font="Verdana 10 bold",command=sonuc).pack()
btc.mainloop()
