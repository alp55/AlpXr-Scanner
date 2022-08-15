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
1. Wlan0 
2. Eth0 
0. Geri         """)
    secim=input("secim:")
    if secim=="1":
        os.system("clear")
        os.system("macchanger -r wlan0")

    elif secim=="2":
        os.system("clear")
        os.system("macchanger -r eth0")
        print("mac adresi degiştirildi")
        time.sleep(1)
        os.system("clear")
        anapg()
    elif secim=="0":
        os.system("clear")
        
        
        anapg()
    else:
        os.system("clear")
        print("yanlış tuşama yaptınız")
        time.sleep(1)
        os.system("clear")
        mac()

def bilgi():
    print("""
1. Whois Sorgusu
2. TheHarvester Taraması
3. Local Ağdaki Cihazların Tespiti
4. Dizin Taraması
5. Dns Sorgusu
0. geri""")
    secim=input("secim:")
    
    
    if secim=="1":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"dmitry -winsep {ip}")
        bilgi()

    elif secim=="2":
        os.system("clear")
        
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"theHarvester -d {ip} -l 500 -b all")
        bilgi()
    
    elif secim=="3":
        os.system("clear")
        os.system("netdiscover")
        bilgi()
    elif secim=="4":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"wafw00f -a {ip}")
        bilgi()
    elif secim=="5":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"dnsenum {ip}")
        bilgi()
    elif secim=="0":
        os.system("clear")
        anapg()
    
    else:
        os.system("clear")
        print("yanlış tuşama yaptınız")
        time.sleep(1)
        bilgi()


    



def nmap():
    os.system("clear")
    print("""
1. Hedef Sitenin IP Adresini Ögren
2. Hedef Sitenin Açık IP adreslerini Öğren
3. Hedef Sitenin Açık Portlarını Öğrenme
4. Hedef Sitenin Servis Versiyon Taraması
5. Udp Scan
6. OS İzi Belirleme
7. SPOOFİNG
0. Geri

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
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"nmap -sn -n -v --open {ip}/24")
        nmap()
    elif secim=="3":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"sudo nmap -Pn -sS -n -v --reason --open {ip}")
        nmap()
    elif secim=="4":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"sudo nmap -sS -sV -sC -n -v -p 21,53,80,139,445,1001,1900 {ip}")
        nmap()
    
    elif secim=="5":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"nmap -sU -v {ip}")
        nmap()
    elif secim=="6":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz: "))
        os.system(f"nmap {ip} -O -n ")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
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
    
    
def wppres():
    print("""
1. WPScan Güncelleme
2. WPScan Versiyon bilgisi
3. WordPress Taraması
4. WordPress Hedef Site (yönetici, yazar, editor..) Taraması
5. WordPress Hedef Site Eklenti Taraması
6. WordPress Hedef Site Eklenti Açıkları Taranması
7. WordPress Hedef Site Tema Bilgisi
8. WordPress Hedef Site Tema Zafiyeti 
9. WordPress Hedef Sitenin Kullanıcı Adi İle BruteForce Atak Saldırısı
0. Geri 
    
    """)
    secim=input("secim:")

    if secim=="1":
        os.system("clear")
        os.system("wpscan --update")
        os.system("clear")
        wppres()

    if secim=="2":
        os.system("clear")
        os.system("wpscan --version")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
        

    if secim=="3":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f" wpscan --url {ip}")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if secim=="4":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f" wpscan --url {ip} --enumerate u")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if secim=="5":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f" wpscan --url {ip} --enumerate p")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if secim=="6":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f" wpscan --url {ip} --enumerate ap")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if secim=="7":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f"wpscan --url {ip} –enumerate t ")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
        
    if secim=="8":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        os.system(f"wpscan --url {ip} –enumerate at ")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if secim=="9":
        os.system("clear")
        ip=input(str("sitenin ip adresini giriniz (www.alanadi.com): "))
        kulad=input(str("kullanıcı ad bilgisi giriniz :"))
        wordlist=input(str("wordlist yolunu giriniz:"))
        os.system(f"wpscan --url {ip} –wordlist {wordlist} --username {kulad}")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()



    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        nmap()



def anapg():
    
    print("""
1. Mac Adresi Degiştirme
2. Pasif Ve Aktif Bilgi Toplama
3. Ağ Taraması
4. WordPress Zafiyet Taraması
0. Çıkış





""")

    islem=input("secim:")
    
    if islem=="1":
        os.system("clear")
        mac()
    elif islem=="2":
        os.system("clear")
        bilgi()
    elif islem=="3":
        os.system("clear")
        nmap()
    elif islem=="4":
        os.system("clear")
        wppres()
    elif islem=="0":
        os.system("clear")
        exit()
    else:
        os.system("clear")
        print("yanlış tuşlama yaptınız")
        time.sleep(1)
        os.system("clear")
        anapg()
        


anapg()
        


   
    


    
