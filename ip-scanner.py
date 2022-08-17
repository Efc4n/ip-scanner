import colorama
from turtle import clear, color
import requests
import os
os.system('cls' if os.name=='nt' else 'clear')

class color:
    red = '\033[91m'


print(color.red + """
██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║██║         ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                           
----| https://github.com/Efc4n |----
""")


def check(): 
    r = requests.get("https://ipinfo.io/") 
    if r.status_code == 200: 
        print("\nSorgu Yapılıyor..\n") 
    else:
        print("\nSorgu Yapılamıyor!!\n") 
        exit() 


ip = input("\nip address: ") 

check() 

ulke = requests.get("https://ipinfo.io/{}/country/".format(ip)).text 
sehir = requests.get("https://ipinfo.io/{}/city/".format(ip)).text
bolge = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
zamandilimi = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
organizasyon = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
konum =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text

print("IP: "+ip)
print("Country: "+ulke)
print("City: "+sehir)
print("Region: "+bolge)
print("Time Zone: "+zamandilimi)
print("Organization: "+organizasyon)
print("Location: "+konum)