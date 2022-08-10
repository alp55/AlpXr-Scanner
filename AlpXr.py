import os
from turtle import delay
from termcolor import colored
import pyfiglet 
import socket
import time

alpxr_figlet=colored(pyfiglet.figlet_format("AlpXr", font = "standard"),'red')
print(alpxr_figlet)

def mac():
    os.system("clear")
    print("""
1.wlan0 
2.eth0 
0.geri         """)
    secim=input("secim:")
    if secim=="1":
        os.system("clear")
        os.system("macchanger -r wlan0")

    elif secim=="2":
        os.system("clear")
        os.system("macchanger -r eth0")
        print("mac adresi degiştirildi")
        anapg()
    elif secim=="0":
        os.system("clear")
        
        
        anapg()
    else:
        os.system("clear")
        print("yanlış tuşama yaptınız")
        time.sleep(2)
        mac()


def nmap():
    os.system("clear")
    print("""
1. Hedef Sitenin IP Adersini Ögren
2. Hedef Sitenin Açık IP adreslerini Öğren
3. Hedef Sitenin Açık Portlarını Öğrenme
4. Hedef Sitenin Servis Versiyon Taraması
5. Udp Scan
6. OS İzi Belirleme
7. SPOOFİNG
0. geri git

""")
    secim=input("secim:")
    if secim=="1":
        os.system("clear")
        url=input(str("sitenin urlsini giriniz: "))
        b=socket.gethostbyname(url)
        print(b)
        delay(2)
        nmap()
    elif secim=="2":
        os.system("clear")
        ip=input(str("sitenin ip adersini giriniz: "))
        os.system(f"nmap -sn -n -v --open {ip}/24")
        nmap()
    elif secim=="3":
        os.system("clear")
        ip=input(str("sitenin ip adersini giriniz: "))
        os.system(f"sudo nmap -Pn -sS -n -v --reason --open {ip}")
        nmap()
    elif secim=="4":
        os.system("clear")
        ip=input(str("sitenin ip adersini giriniz: "))
        os.system(f"sudo nmap -sS -sV -sC -n -v -p 21,53,80,139,445,1001,1900 {ip}")
        nmap()
    
    elif secim=="5":
        os.system("clear")
        ip=input(str("sitenin ip adersini giriniz: "))
        os.system(f"nmap -sU -v {ip}")
        nmap()
    elif secim=="6":
        os.system("clear")
        ip=input(str("sitenin ip adersini giriniz: "))
        os.system(f"nmap {ip} -O -n ")
        nmap()
    elif secim=="7":
       
        
        os.system("clear")   
        Spoofed_ip=input("Spoofed_ip")
        Target_IP=input("Target_IP")
        os.system(f"nmap -S {Spoofed_ip} -e eth 0 -sS -sV -v -n -PN {Target_IP}")
        nmap()
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        nmap()
    
    
    




def anapg():
    
    print(""""
1.Mac Adresi Degiş
2.Pasif bilgi toplama
0.Çıkış





""")

    islem=input("secim:")
    
    if islem=="1":
        mac()
    elif islem=="2":
        nmap()
    elif islem=="0":
        exit()
    else:
        os.system("clear")
        print("yanlış tuşama yaptınız")
        


anapg()
        


   
    


    