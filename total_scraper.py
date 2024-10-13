from bs4 import BeautifulSoup
import requests

def scrape_all(loc): #give it the address
    page = requests.get(loc)
    soup = BeautifulSoup(page.text, 'lxml')
    locationid = ""
    name = ""
    address =""
    line1 = ""

    #print(soup)
    if(str(soup).lower().find("freefood")> -1 or str(soup).lower().find("free food") >-1):
        if(str(soup).lower().find("locationid")> -1):
            astr =str(soup).lower().find("locationid")
            start =12
            tmpstr =""
            while True:
                if(str(soup).lower()[astr+start]==","):
                    break
                tmpstr += str(soup).lower()[astr+start]
                astr+=1
            
        locationid = tmpstr
        astr += start

        #name
        astr+=8 #to miss the "name:" part and go to something else
        start =0
        tmpstr=""
        while True:
            if(str(soup).lower()[astr+start]==","):
                break
            tmpstr += str(soup).lower()[astr+start]
            astr+=1
        
        name = tmpstr

        #address
        astr+=1
        tmpstr=""
        while True:
            if(tmpstr[len(tmpstr)-5:]=="line1"):
                break
            tmpstr += str(soup).lower()[astr+start]
            astr+=1
        
        address= tmpstr[tmpstr.find(":")+1:len(tmpstr)-7]

        #StartOn
        strts=""
        tmpstr = ""
        astr = str(soup).lower().find("startson")
        astr+=10
        while True:
            if(str(soup).lower()[astr]==","):
                break
            tmpstr += str(soup).lower()[astr]
            astr+=1

        strts=tmpstr

        #Endson
        ends=""
        tmpstr = ""
        astr = str(soup).lower().find("endson")
        astr+=8
        while True:
            if(str(soup).lower()[astr]==","):
                break
            tmpstr += str(soup).lower()[astr]
            astr+=1

        ends=tmpstr
        



        print("Free Food Available")
        print("locationid: ",locationid)
        print("address: ", address)
        print("name: ",name)
        print("Start Time: ", strts)
        print("End Time: ", ends)
    else:
        print("No free food")





