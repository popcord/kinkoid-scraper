import os
import requests
import time

kinkoid = """
╔═════════════════════╗
║ ██╗  ██╗   ██╗  ██╗ ║
║ ██║ ██╔╝   ██║  ██║ ║
║ █████╔╝    ███████║ ║
║ ██╔═██╗    ██╔══██║ ║
║ ██║  ██╗██╗██║  ██║ ║
║ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ║
║   1: hentai heroes  ║
║   2:   gay harem    ║
║   3:  comix harem   ║
╚═════════════════════╝
"""






###################==HENTAI HEROES==###################
h_h = """
╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ ██╗  ██╗███████╗███╗   ██╗████████╗ █████╗ ██╗    ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗ ║
║ ██║  ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║    ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝ ║
║ ███████║█████╗  ██╔██╗ ██║   ██║   ███████║██║    ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗ ║
║ ██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║    ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║ ║
║ ██║  ██║███████╗██║ ╚████║   ██║   ██║  ██║██║    ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║ ║
║ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
h_ht = """
                        ╔════════════╗╔══════════════════════╗╔══════════╗
                        ║ 1 : avatar ║║ 2 : girls evolutions ║║ 3 : Home ║
                        ╚════════════╝╚══════════════════════╝╚══════════╝
"""
###
#####################==GIRLS
###
def hh_girls():
    os.system("cls")
    print (h_h)
    count = 0
    id = input("put the girl id:")

    for i in range (6):
        try:
            f = open(str(count)+".webp",'wb')
            f.write(requests.get(f"https://hh2.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    hentai_heroes()

    
###
#####################==ICONES
###
def hh_ico():
    os.system("cls")
    print (h_h)
    count = 1
    for i in range (2000):
        try:
            f = open(str(count)+".jpg",'wb')
            f.write(requests.get(f"https://hh2.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    hentai_heroes()

###



###################==COMIX HAREM==###################
c_h = """
╔════════════════════════════════════════════════════════════════════════════════════════╗
║  ██████╗ ██████╗ ███╗   ███╗██╗██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ███████╗███╗   ███╗ ║
║ ██╔════╝██╔═══██╗████╗ ████║██║╚██╗██╔╝    ██║  ██║██╔══██╗██╔══██╗██╔════╝████╗ ████║ ║
║ ██║     ██║   ██║██╔████╔██║██║ ╚███╔╝     ███████║███████║██████╔╝█████╗  ██╔████╔██║ ║
║ ██║     ██║   ██║██║╚██╔╝██║██║ ██╔██╗     ██╔══██║██╔══██║██╔══██╗██╔══╝  ██║╚██╔╝██║ ║
║ ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██╔╝ ██╗    ██║  ██║██║  ██║██║  ██║███████╗██║ ╚═╝ ██║ ║
║  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ║
╚════════════════════════════════════════════════════════════════════════════════════════╝
"""
c_ht ="""
                    ╔════════════╗╔══════════════════════╗╔══════════╗
                    ║ 1 : avatar ║║ 2 : girls evolutions ║║ 3 : Home ║
                    ╚════════════╝╚══════════════════════╝╚══════════╝
"""
###
#####################==GIRLS
###
def ch_girls():
    os.system("cls")
    print (h_h)
    count = 0
    id = input("put the girl id:")

    for i in range (6):
        try:
            f = open(str(count)+".webp",'wb')
            f.write(requests.get(f"https://ch.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    hentai_heroes()

    
###
#####################==ICONES
###
def ch_ico():
    os.system("cls")
    print (h_h)
    count = 1
    for i in range (2000):
        try:
            f = open(str(count)+".jpg",'wb')
            f.write(requests.get(f"https://ch.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    hentai_heroes()

###


###################==GAY HAREM==###################
g_h = """
╔══════════════════════════════════════════════════════════════════════════╗
║ ██████╗  █████╗ ██╗   ██╗    ██╗  ██╗ █████╗ ██████╗ ███████╗███╗   ███╗ ║
║██╔════╝ ██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔══██╗██╔════╝████╗ ████║ ║
║██║  ███╗███████║ ╚████╔╝     ███████║███████║██████╔╝█████╗  ██╔████╔██║ ║
║██║   ██║██╔══██║  ╚██╔╝      ██╔══██║██╔══██║██╔══██╗██╔══╝  ██║╚██╔╝██║ ║
║╚██████╔╝██║  ██║   ██║       ██║  ██║██║  ██║██║  ██║███████╗██║ ╚═╝ ██║ ║
║ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
g_ht = """
           ╔════════════╗╔═════════════════════╗╔══════════╗
           ║ 1 : avatar ║║ 2 : boys evolutions ║║ 3 : Home ║
           ╚════════════╝╚═════════════════════╝╚══════════╝
"""
###
#####################==boys
###
def gh_boys():
    os.system("cls")
    print (h_h)
    count = 0
    id = input("put the girl id:")

    for i in range (6):
        try:
            f = open(str(count)+".webp",'wb')
            f.write(requests.get(f"https://gh1.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    hentai_heroes()

    
###
#####################==ICONES
###
def gh_ico():
    os.system("cls")
    print (h_h)
    count = 1
    for i in range (2000):
        try:
            f = open(str(count)+".jpg",'wb')
            f.write(requests.get(f"https://gh1.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    hentai_heroes()

###














def hentai_heroes():
    os.system("cls")
    print(h_h + h_ht)
    hh = input ("what you want : ")
    if hh == "1" :
        hh_ico()
    if hh == "2":
        hh_girls()
    if hh == "3":
        start()

    else:
        print("tag not found in database!!")
        time.sleep(2)
        hentai_heroes()


def gay_harem():
    os.system("cls")
    print(g_h + g_ht)
    gh = input ("what you want : ")
    if gh == "1" :
        gh_ico()
    if gh == "2":
        gh_boys()
    if gh == "3":
        start()
    else:
        print("tag not found in database!!")
        time.sleep(2)
        gay_harem()


def comix_harem():
    os.system("cls")
    print(c_h + c_ht)
    ch = input ("what you want : ")
    if ch == "1" :
        ch_ico()
    if ch == "2":
        ch_girls()
    if ch == "3":
        start()
    else:
        print("tag not found in database!!")
        time.sleep(2)
        comix_harem()


  
def start():
    os.system("cls")
    print(kinkoid)
    start = input ("what you want : ")
    if start == "1" :
        hentai_heroes()
    if start == "2" :
        gay_harem()
    if start == "3" :
        comix_harem()
    else:
        print("number not found in database!!")
        time.sleep(2)
        return
start()
