import os
import requests


kinkoid = """
██╗  ██╗   ██╗  ██╗
██║ ██╔╝   ██║  ██║
█████╔╝    ███████║
██╔═██╗    ██╔══██║
██║  ██╗██╗██║  ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                   
"""

h_h ="""
██╗  ██╗███████╗███╗   ██╗████████╗ █████╗ ██╗    ██╗  ██╗███████╗██████╗  ██████╗ ███████╗███████╗
██║  ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║    ██║  ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
███████║█████╗  ██╔██╗ ██║   ██║   ███████║██║    ███████║█████╗  ██████╔╝██║   ██║█████╗  ███████╗
██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║    ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ╚════██║
██║  ██║███████╗██║ ╚████║   ██║   ██║  ██║██║    ██║  ██║███████╗██║  ██║╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                                   
"""




###################==HENTAI HEROES==###################

###
#####################==GIRLS
###
def girls():
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
#####################==STORY (comming soon)
###



###################==COMIX HAREM==###################











def hentai_heroes():
    os.system("cls")
    print(h_h)
    hh = input ("what you want? (icones , girls)")
    girl = ("girl", "girls",)
    if hh in girl:
        girls()
    ico = ("ico", "icone", "icones")
    if hh in ico :
        hh_ico()
    else:
        print("tag not found in database!!")
        hentai_heroes()


    
def start():
    print(kinkoid)
    start = input ("what you want?(hentai heroes)")
    if start == "hentai heroes" :
        hentai_heroes()
    else:
        print("tag not found in database!!")
        start()
start()
