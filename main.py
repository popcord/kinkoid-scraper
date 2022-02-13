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
║   1: Hentai Heroes  ║
║   2:   Gay Harem    ║
║   3:  Comix Harem   ║
║   4: Horny Heroes   ║
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
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (h_h)
    count = 0
    id = input("put the girl id:")
    
    try:
        os.makedirs("HentaiHeroes/girls/")
    except:
        pass
    try:
        os.mkdir(f"HentaiHeroes/girls/girl_{str(id)}/")
    except:
        print(f"girl already downloaded or delete the file girl_{str(id)}")
        time.sleep(3)
        comix_harem()

        
    for i in range (6):
        try:
            f = open(f"HentaiHeroes/girls/girl_{str(id)}/" + str(count)+".webp",'wb')
            f.write(requests.get(f"https://hh2.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = f"HentaiHeroes/girls/girl_{str(id)}/"+str(count)+".webp"
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
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (h_h)
    count = 1
    
    try:
        os.makedirs("HentaiHeroes/avatars/")
    except:
        pass
    try:
        os.mkdir("HentaiHeroes/avatars/")
    except:
        pass


    for i in range (2000):
        try:
            f = open("HentaiHeroes/avatars/"+str(count)+".jpg",'wb')
            f.write(requests.get(f"https://hh2.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = "HentaiHeroes/avatars/"+str(count)+".jpg"
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
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (h_h)
    count = 0
    id = input("put the girl id:")
    
    try:
        os.makedirs("ComixHarem/girls/")
    except:
        pass
    try:
        os.mkdir(f"ComixHarem/girls/girl_{str(id)}/")
    except:
        print(f"girl already downloaded or delete the file girl_{str(id)}")
        time.sleep(3)
        comix_harem()

        
    for i in range (6):
        try:
            f = open(f"ComixHarem/girls/girl_{str(id)}/" + str(count)+".webp",'wb')
            f.write(requests.get(f"https://ch.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = f"ComixHarem/girls/girl_{str(id)}/"+str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    comix_harem()
    
###
#####################==ICONES
###
def ch_ico():
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (c_h)
    count = 1
    
    try:
        os.makedirs("ComixHarem/avatars/")
    except:
        pass
    try:
        os.mkdir("ComixHarem/avatars/")
    except:
        pass


    for i in range (2000):
        try:
            f = open("ComixHarem/avatars/"+str(count)+".jpg",'wb')
            f.write(requests.get(f"https://ch.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = "ComixHarem/avatars/"+str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    comix_harem()

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
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (g_h + g_ht)
    count = 0
    id = input("put the boy id:")

    
    try:
        os.makedirs("GayHarem/boys/")
    except:
        pass
    try:
        os.mkdir(f"GayHarem/boys/boy_{str(id)}/")
    except:
        print(f"boy already downloaded or delete the file boy_{str(id)}")
        time.sleep(3)
        gay_harem()

      
    for i in range (6):
        try:
            f = open(f"GayHarem/boys/boy_{str(id)}/" + str(count)+".webp",'wb')
            f.write(requests.get(f"https://gh1.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()
        
            file = f"GayHarem/boys/boy_{str(id)}/"+str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    gay_harem()

    
###
#####################==ICONES
###
def gh_ico():
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (g_h)
    count = 1
    
    try:
        os.makedirs("GayHarem/avatars/")
    except:
        pass
    try:
        os.mkdir("GayHarem/avatars/")
    except:
        pass


    for i in range (2000):
        try:
            f = open("GayHarem/avatars/"+str(count)+".jpg",'wb')
            f.write(requests.get(f"https://gh1.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = "GayHarem/avatars/"+str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    gay_harem()

###


###################==GAY HAREM==###################
s_h = """
╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║██╗  ██╗ ██████╗ ██████╗ ███╗   ██╗██╗   ██╗    ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗ ║
║██║  ██║██╔═══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝    ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝ ║
║███████║██║   ██║██████╔╝██╔██╗ ██║ ╚████╔╝     ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗ ║
║██╔══██║██║   ██║██╔══██╗██║╚██╗██║  ╚██╔╝      ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║ ║
║██║  ██║╚██████╔╝██║  ██║██║ ╚████║   ██║       ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║ ║
║╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
s_ht = """
           ╔════════════╗╔══════════════════════╗╔══════════╗
           ║ 1 : avatar ║║ 2 : girls evolutions ║║ 3 : Home ║
           ╚════════════╝╚══════════════════════╝╚══════════╝
"""
###
#####################==boys
###
def sh_girls():
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (s_h + s_ht)
    count = 0
    id = input("put the girl id:")

    
    try:
        os.makedirs("HornyHeroes/girls/")
    except:
        pass
    try:
        os.mkdir(f"HornyHeroes/girls/girl_{str(id)}/")
    except:
        print(f"girl already downloaded or delete the file girl_{str(id)}")
        time.sleep(3)
        horny_heroes()

        
    for i in range (6):
        try:
            f = open(f"HornyHeroes/girls/girl_{str(id)}/" + str(count)+".webp",'wb')
            f.write(requests.get(f"https://sh.hh-content.com/pictures/girls/{str(id)}/ava"+str(count)+"-300x.webp").content)
            f.close()

            file = f"HornyHeroes/girls/girl_{str(id)}/"+str(count)+".webp"
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1

    print ('finish')
    horny_heroes()

    
###
#####################==ICONES
###
def sh_ico():
    try:
        os.system("cls")
    except:
        os.system("clear")
    print (s_h)
    count = 1
    
    try:
        os.makedirs("HornyHeroes/avatars/")
    except:
        pass
    try:
        os.mkdir("HornyHeroes/avatars/")
    except:
        pass


    
    for i in range (2000):
        try:
            f = open("HornyHeroes/avatars/"+str(count)+".jpg",'wb')
            f.write(requests.get(f"https://sh.hh-content.com/pictures/hero/ico/"+str(count)+".jpg").content)
            f.close()
            file = "HornyHeroes/avatars/"+str(count)+".jpg"
            stat = os.path.getsize(file)
            count += 1

            if os.path.getsize(file) < 1024:
                os.remove(file)
            
        except:
            continue
            count += 1
    print ('finish')
    horny_heroes()

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

def horny_heroes():
    os.system("cls")
    print(s_h + s_ht)
    sh = input ("what you want : ")
    if sh == "1" :
        sh_ico()
    if sh == "2":
        sh_girls()
    if sh == "3":
        start()
    else:
        print("tag not found in database!!")
        time.sleep(2)
        horny_heroes()


  
def start():
    os.system("cls")
    print(kinkoid)
    main = input ("what you want : ")
    if main == "1" :
        hentai_heroes()
    if main == "2" :
        gay_harem()
    if main == "3" :
        comix_harem()
    if main == "4" :
        horny_heroes()
    else:
        print("number not found in database!!")
        time.sleep(2)
        start()
start()
