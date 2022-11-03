import os
from termcolor import colored
import socket
import time
import webbrowser

print(colored("""                                                                                                     
               AAA               lllllll                    XXXXXXX       XXXXXXX                    
              A:::A              l:::::l                    X:::::X       X:::::X                    
             A:::::A             l:::::l                    X:::::X       X:::::X                    
            A:::::::A            l:::::l                    X::::::X     X::::::X                    
           A:::::::::A            l::::lppppp   ppppppppp   XXX:::::X   X:::::XXXrrrrr   rrrrrrrrr   
          A:::::A:::::A           l::::lp::::ppp:::::::::p     X:::::X X:::::X   r::::rrr:::::::::r  
         A:::::A A:::::A          l::::lp:::::::::::::::::p     X:::::X:::::X    r:::::::::::::::::r 
        A:::::A   A:::::A         l::::lpp::::::ppppp::::::p     X:::::::::X     rr::::::rrrrr::::::r
       A:::::A     A:::::A        l::::l p:::::p     p:::::p     X:::::::::X      r:::::r     r:::::r
      A:::::AAAAAAAAA:::::A       l::::l p:::::p     p:::::p    X:::::X:::::X     r:::::r     rrrrrrr
     A:::::::::::::::::::::A      l::::l p:::::p     p:::::p   X:::::X X:::::X    r:::::r            
    A:::::AAAAAAAAAAAAA:::::A     l::::l p:::::p    p::::::pXXX:::::X   X:::::XXX r:::::r            
   A:::::A             A:::::A   l::::::lp:::::ppppp:::::::pX::::::X     X::::::X r:::::r            
  A:::::A               A:::::A  l::::::lp::::::::::::::::p X:::::X       X:::::X r:::::r            
 A:::::A                 A:::::A l::::::lp::::::::::::::pp  X:::::X       X:::::X r:::::r            
AAAAAAA                   AAAAAAAllllllllp::::::pppppppp    XXXXXXX       XXXXXXX rrrrrrr            
                                         p:::::p                                                     
                                         p:::::p                                                     
                                        p:::::::p                                                    
                                        p:::::::p                                                    
                                        p:::::::p                                                    
                                        ppppppppp                                                    
                                                   """,'red'))

######################################################################

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
        time.sleep(1)
        os.system("clear")
        anapg()

    elif secim=="2":
        os.system("clear")
        os.system("macchanger -r eth0")
        print("mac adresi değiştirildi")
        time.sleep(1)
        os.system("clear")
        anapg()
    elif secim=="0":
        os.system("clear")
        
        
        anapg()
    else:
        os.system("clear")
        print("yanlış tuşlama yaptınız")
        time.sleep(1)
        os.system("clear")
        mac()


######################################################################


def bilgi():
    print("""
1. Whois Sorgusu
2. TheHarvester Taraması
3. Local Ağdaki Cihazların Tespiti
4. Dizin Taraması
5. DNSenum
0. geri""")
    secim=input("secim:")
    
    
    if secim=="1":
        os.system("clear")
        ip=input(str("Hedef sitenin url adresini giriniz: "))
        os.system(f"dmitry -winsep {ip}")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif secim=="2":
        os.system("clear")
        
        ip=input(str("Hedef sitenin url adresini giriniz: "))
        os.system(f"theHarvester -d {ip} -l 500 -b all")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()
    
    elif secim=="3":
        os.system("clear")
        os.system("netdiscover")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif secim=="4":
        os.system("clear")
        ip=input(str("Hedef sitenin url adresini giriniz: "))
        os.system(f"wafw00f -a {ip}")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()
    elif secim=="5":
        os.system("clear")
        ip=input(str("Hedef sitenin url adresini giriniz: "))
        os.system(f"dnsenum {ip}")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()
    elif secim=="0":
        os.system("clear")
        anapg()
    
    else:
        os.system("clear")
        print("yanlış tuşlama yaptınız")
        time.sleep(1)
        bilgi()


    
######################################################################


def nmap():
    os.system("clear")
    print("""
1. Hedef Sitenin IP Adresini Öğren
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
        url=input(str("Hedef sitenin url sini giriniz: "))
        b=socket.gethostbyname(url)
        print(b)
        time.sleep(2)
        nmap()
    elif secim=="2":
        os.system("clear")
        ip=input(str("Hedef sitenin ip adresini giriniz: "))
        os.system(f"nmap -sn -n -v --open {ip}/24")
        nmap()
    elif secim=="3":
        os.system("clear")
        ip=input(str("Hedef sitenin ip adresini giriniz: "))
        os.system(f"sudo nmap -Pn -sS -n -v --reason --open {ip}")
        nmap()
    elif secim=="4":
        os.system("clear")
        ip=input(str("Hedef sitenin ip adresini giriniz: "))
        os.system(f"sudo nmap -sS -sV -sC -n -v -p 21,53,80,139,445,1001,1900 {ip}")
        nmap()
    
    elif secim=="5":
        os.system("clear")
        ip=input(str("Hedef sitenin ip adresini giriniz: "))
        os.system(f"nmap -sU -v {ip}")
        nmap()
    elif secim=="6":
        os.system("clear")
        ip=input(str("Hedef sitenin ip adresini giriniz: "))
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

######################################################################   
    
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
9. WordPress Hedef Sitenin Kullanıcı Adı İle Brute Force Atak Saldırısı
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        ip=input(str("Hedef sitenin url adresini giriniz (www.alanadi.com): "))
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
        time.sleep(2)
        nmap()

######################################################################

def sqlxss():
    os.system("clear")
    print("""
1. Web Standart Tarama
2. SQL İnjection Taraması
3. XSS Taraması
0. Geri""")
    
    secim=input("secim: ")
    
    if secim == "1":
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))

        os.system(f"nikto -h {url}")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
            
                
    elif secim == "2":
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))

        os.system(f"nikto -h {url} -Cgidirs none -Tuning 9")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
                
    elif secim =="3":
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))

        os.system(f"nikto -h {url} -Cgidirs none -Tuning 4")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
    
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        time.sleep(2)
        nmap()

######################################################################

def lynis():
    print("""

1. Lynis Versiyon
2. Lynis Komutları
3. Lynis Sistem Taraması
4. Lynis Kurulu Değilse
0. Geri
    
    """

    )
    
    secim=input("secim: ")
    if secim=="1":
        os.system("clear")
        os.system("lynis show version")
        time.sleep(2)
        lynis()
    elif secim=="2":
        os.system("clear")
        os.system("lynis show commands")
        time.sleep(2)

        lynis()
    elif secim=="3":
        os.system("clear")
        os.system("lynis audit system")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            lynis()
        else :
            os.system("clear")
            lynis()
        
    elif secim=="4":
        os.system("clear")
        os.system("sudo apt install lynis")
        time.sleep(2)

        lynis()
    
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        time.sleep(2)

        lynis()
        

######################################################################

def hydra():
    print("""
1. Hydra İle FTP Saldırısı(Brute Force)
2. Hydra İle SSH Saldırısı(Brute Force)
0. Geri   
    """)
    secim=input("secim: ")
    if secim=="1":
        os.system("clear")
        ftp=input(str("Hedef ftp adresini giriniz: "))

        os.system(f"""
hydra -l admin -p password ftp://{ftp}
hydra -L /usr/share/wordlists/rockyou.txt.gz -P /usr/share/wordlists/rockyou.txt.gz ftp://{ftp}""")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            hydra()
        else :
            os.system("clear")
            hydra()
        
    elif secim=="2":
        os.system("clear")
        ssh=input(str("Hedef ssh adresini giriniz: "))
        os.system(f"""hydra -l admin -p password {ssh} -t 4 ssh
hydra -L /usr/share/wordlists/rockyou.txt.gz -P /usr/share/wordlists/rockyou.txt.gz {ssh} -t 4 ssh""")
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            hydra()
        else :
            os.system("clear")
            hydra()
    
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        time.sleep(2)

        hydra()
######################################################################

def exiftool():
    print("""
1. Fotograf Tara
0. Geri   
""")   
    secim=input("secim: ")
    if secim=="1":
        os.system("clear")
        yol=input(str("fotograf yolunu yazınız veya sürükleyebilirsiniz :"))
        os.system(f"exiftool {yol}")
        
        print("0. Geri Git")
        tıkla=input("secim: ")
        if tıkla=="0":
            os.system("clear")
            exiftool()
        else :
            os.system("clear")
            exiftool()
    
    
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        
        time.sleep(2)
        exiftool()
######################################################################
def skipfish():
    print(""""
1. Basit Tarama
2. Orta Ölcekli Tarama
3. Derin Tarama
0. Geri  """)
    secim=input("secim: ")
    
    if secim=="1":
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 2 {url}")
        os.system(f"open {sinifla}/index.html")       
        os.system("clear")
        skipfish()
        
        
    elif secim=="2":
        
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 8 {url}")
        os.system(f"open {sinifla}/index.html")
        os.system("clear")
        skipfish()
    
    elif secim=="3":
        
        os.system("clear")
        url=input(str("Hedef sitenin url sini giriniz: "))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 16 {url}")
        os.system(f"open {sinifla}/index.html")
        os.system("clear")
        skipfish()
    
    
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        
        time.sleep(2)
        skipfish()
#####################################################################

def apktool():
    print("""
1. Apk Tool Kur
2. Apk Dosyasını Ayrıştır
0. Geri""")
    secim=input("secim: ")
    if secim=="1":
        os.system("clear")
        os.system("sudo apt install apktool")
        os.system("clear")
        apktool()
    elif secim=="2":
        os.system("clear")
        print("apk dosyasını bulungunuz dinize taşımalısınız")
        ad=input("Apk dosyasının adını giriniz (test.apk)")
        
        os.system(f"apktool d -f -r {ad}")        
        apktool()
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        
        time.sleep(2)
        apktool()

#####################################################################
def cupp():
    print("""
1. Wordlist Oluşturma Aracını yükle
2. Wordlist Oluşturma
0. Geri """)
    secim=input("secim: ")
    if secim=="1":
        os.system("clear")
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("Arac yüklenmiştir")
        time.sleep(2)
        os.system("clear")
        cupp()
    elif secim=="2":
        os.system("clear")
        
        os.system("python3 ./cupp/cupp.py -i")
        os.system("clear")
        cupp()
    elif secim=="0":
        os.system("clear")
        anapg()


    else:
        print("yanlış tuşlama yaptınız tekrar deneyiniz")
        
        time.sleep(2)
        cupp()

   
######################################################################
def anapg():
    
    print("""
1. Mac Adresi Değiştirme
2. Pasif Ve Aktif Bilgi Toplama
3. Ağ Taraması
4. WordPress Zafiyet Taraması
5. SQL Ve XSS Zafiyet Taraması
6. Local Makine Üzerinde Zafiyet Tespiti
7. FTP Ve SSH Saldırısı
8. Fotoğraf Analizi
9. Skipfish Taraması
10. Andiroid 
11. Özleştirilmiş Wordlist Oluşturma
0. Çıkış""")

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
    elif islem=="5":
        os.system("clear")
        sqlxss()
    elif islem=="6":
        os.system("clear")
        lynis()
    elif islem=="7":
        os.system("clear")
        hydra()
    elif islem=="8":
        os.system("clear")
        exiftool()
    elif islem=="9":
        os.system("clear")
        skipfish()
    elif islem=="10":
        os.system("clear")
        apktool()
    elif islem=="11":
        os.system("clear")
        cupp()
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
        


   
    


    
