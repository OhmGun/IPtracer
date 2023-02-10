# IPTrace

# Author - Guntur Sulistyo Raharjo

# github - https://github.com/ohmgun



import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
 _ ______  __________  _______    ________      _____  _______
| (_____ )(____   ____)|______)   ||     ||    / ____| |  ____|
| |_____) )    |  |    | |   / /  ||_____||   / /      | |____
| |  ____/     |  |    | |  / /   ||_____||  / /       |  ____|
| | |          |  |    | |  \ \   ||     ||   \ \_____ | |____
|_|_|          |__|    | |   \ \  ||     ||    \______||______| """+Y+"""v1.2"""+G+"""

     Simple IP Address Tracker
"""+R+""">>"""+Y+"""----"""+CY+""" Author - Guntur Sulistyo Raharjo """+Y+"""----"""+R+"""<<""")
        
    def m3():
        try:
            print(R+"""\n
#"""+Y+""" Silahkan pilih"""+G+""" >>"""+Y+"""
1)"""+G+""" Trace IP Anda"""+Y+"""
2)"""+G+""" Trace IP info Lainnya"""+Y+"""
3)"""+G+""" Keluar
""")
            ch=int(input(CY+"Enter Your choice: "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                print(Y+"Keluar................"+W)
            else:
                print(R+"\nPilihan anda salah! Silahkan coba lagi\n")
                m3()
        except ValueError:
            print(R+"\nPilihan anda salah! Silahkan coba lagi\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(Y+'\n>>>'+CY+' IP address details\n ')
                print(G+"1) IP Address : "+Y,data['query'],'\n')
                print(G+"2) Upstream : "+Y,data['org'],'\n')
                print(G+"3) Provider : "+Y,data['isp'],'\n')
                print(G+"4) Kota : "+Y,data['city'],'\n')
                print(G+"5) Kode Pos : "+Y,data['zip'],'\n')
                print(G+"6) Provinsi : "+Y,data['regionName'],'\n')
                print(G+"7) Negara : "+Y,data['country'],'\n')
                print(G+"8) Koordinat\n")
                print(G+"\tLattitude : "+Y,data['lat'],'\n')
                print(G+"\tLongitude : "+Y,data['lon'],'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(R+"\n#"+Y+" Google Map link : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Buka Map diBrowser?"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nTrace IP lainnya atau keluar menggunakan Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nPilihan anda salah! Silahkan coba lagi\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Buka Map diBrowser?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y+"\nTrace IP lainnya atau keluar menggunakan "+R+"Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\nPilihan anda salah! Silahkan coba lagi\n")
                        m3()
                return
            except KeyError:
                print(R+"\nError! Indikasi IP Private atau alamat IP/Alamat Website Salah!\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" Silahkan cek koneksi internet anda!\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"Masukan IP Address/Alamat Website tujuan:"+W+" ")
        if u=="":
            print(R+"\nmasukan IP Address/website address yang benar!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nInterrupted ! Have a nice day :)"+W)
