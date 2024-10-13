from bs4 import BeautifulSoup
import requests

def snack_all(loc): #give it the address
    page = requests.get(loc)
    soup = BeautifulSoup(page.text, 'lxml')
    locationid = ""
    name = ""
    address =""
    line1 = ""

    #print(soup)
    if(str(soup).lower().find("snack")> -1):
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



        print("Free Food Available")
        print("locationid: ",locationid)
        print("address: ", address)
        print("name: ",name)
    else:
        print("No free food")



