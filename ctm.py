#rxvxrsx
#coding/bin/python3
#coding=utf-8
from core.headers import *
from core.logo import *
import os
try:
  import requests
except:
  os.system("pip install requests")
import json, requests ,os, random, time, sys
from requests import post as rp
rs=requests.session()
rg=rs.get
rxvxrsxmailex=""
mailmes=""
currenteversion="v1.0"
def logop(z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.01)
def rxvxrsxgit():
  os.system("xdg-open https://github.com/rxvxrsx/")
def ext():
  exit("\n{BBlack}[{BRed} !{BBlack} ] {BGreen}THANKS FOR USING {BBlack}[{BRed} !{BBlack} ]\n".format(BBlack=BBlack,BRed=BRed,BGreen=BGreen))
def viewmail():
  if os.path.exists("core/domain.txt"):
    with open("core/domain.txt","r",encoding="utf-8") as cmmail:
      cmmail = cmmail.read()
    print(f"\n{BBlack}>>>{BGreen} CUREENT_EMAIL{BBlack} :{BWhite} {cmmail}")  
    x_X=input(f"\n{BYellow} BACK MAIN MANU {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
    if x_X=="y":
      main()
    elif x_X=="n":
      ext()  
  else:
    main()
def coustomnewdomains():
  domain=(json.loads(rg("https://api.internal.temp-mail.io/api/v3/domains",headers=header).text))["domains"]
  email_name=str(input(f"\n{BBlack}>>> {BGreen}ENTER EMAIL NAME {BBlack}:{BWhite} "))
  for domainsrow,domains in enumerate(domain):
      print(f"{BBlack}[{BGreen}",domainsrow+1,f"{BBlack}]{BWhite}",domains["name"],f" {BGreen}!{Color_Reset}")
  ma=int(input(f"{BBlack}>>>{BGreen} SELECT YOUR DOMAIN {BBlack}:{BWhite} "))
  if domainsrow+1 >= ma:
    inputdomain=ma-1
    print(f"{BBlack}[ {BYellow}>>> {BBlack}]{BYellow} SELECTED DOMAIN {BBlack}:{BWhite} "+domain[inputdomain]["name"])
    coustom_domain=domain[inputdomain]["name"]
    
    coustom={
	"name":email_name,
	"domain":coustom_domain
}
    digite=len(email_name)
    newdomain="https://api.internal.temp-mail.io/api/v3/email/new"
    domainr=rp(newdomain,json=coustom,headers=header)
    emailcoustom=email_name+"@"+coustom_domain
    domaincon=(json.loads(domainr.text))["email"]==emailcoustom
    mailtoken=(json.loads(domainr.text))["token"]
    if domaincon:

      logop(f"\n{BBlack}[{BGreen} !{BBlack} ] {BGreen}SUCCESSFULLY CREATE A NEW EMAIL {BBlack}[{BGreen} !{BBlack} ]")
      logop("{BBlack}[{BGreen} !{BBlack} ]{BGreen} CREATED EMAIL {BBlack}:{BWhite} {newemail}".format(newemail=(json.loads(domainr.text))["email"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))

    with open("all_domain.json","r+",encoding="utf-8") as alldr:
      filesdata=alldr.read()
      domall=int(len(filesdata))-2
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(emailcoustom,mailtoken,(str(digite)))+']}'
     
    with open("all_domain.json","w",encoding="utf-8") as alldr:
      alldr.write(str(addingmail))
    with open("core/domain.txt","w",encoding="utf-8") as currend:
      currend.write(emailcoustom)
    inboxchkdef()  
  else:
    print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} SELECTED DOMAIN NOT FOUNDED {BBlack}[{BRed} !{BBlack} ]")
    
    coustomnewdomains()
def seemail():
  with open("all_domain.json","r",encoding="utf-8") as read:
    read=(json.loads(read.read()))["domains"]
  os.system("clear")
  print(manuhome)
  for num , mail in enumerate(read):
    print("{BBlack}[{BGreen} {rxvxrsx} {BBlack}]{BWhite} ".format(rxvxrsx=num+1,BBlack=BBlack,BBlue=BBlue,BYellow=BYellow,BWhite=BWhite,BGreen=BGreen)+mail["email"])
  x_X=input(f"\n{BYellow} BACK MAIN MANU {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
  if x_X=="y":
    main()
  elif x_X=="n":
    ext()
def historylog():
  url='https://api.internal.temp-mail.io/api/v3/email/new'
  with open("all_domain.json","r",encoding="utf-8") as read:
    read=(json.loads(read.read()))["domains"]
  os.system("clear")
  print(manuhome)
  for num , mail in enumerate(read):
    print("{BBlack}[ {BGreen}{rxvxrsx} {BBlack}] {BWhite}".format(rxvxrsx=num+1,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite)+mail["email"])
  print(f"\n{BBlack}[{BYellow} 0. {BBlack}]{BYellow} BACK MAIN MANU {BBlack}[ {BGreen}../{BBlack} ]")  
  in__=int(input(f"\n{BBlack}>>>> {BWhite}"))
  if num+1 >= in__ and in__ != 0:
    
    index=(in__-1)
    historymail=read[index]
    number=(int((len(historymail["email"]))))-(int(historymail["digit"]))
    number=(int(historymail["digit"]))
    emailmail=(historymail["email"])[:(int(historymail["digit"]))]
    domainn=(historymail["email"])[((int(historymail["digit"]))+1):]
    jsonrxvxrsx={
	"name":emailmail,
	"token":(historymail["token"]),
	"domain":domainn
}
    login=(json.loads(rp(url,json=jsonrxvxrsx,headers=header).text))["email"]
    
    with open("core/domain.txt","w",encoding="utf-8") as currend:
      currend.write(login)
      currend.close()
  
    if login == historymail["email"]:
      logop(f"{BBlack}[{BGreen} !{BBlack} ]{BGreen} EMAIL SUCCESSFULLY ADDED {BBlack}[{BGreen} !{BBlack} ]")
      inboxchkdef()
    else:
      logop("{BBlack}[{BRed} !{BBlack} ] {BGreen}YOUR EMAIL{BWhites} : {log}".format(log=login,BBlack=BBlack,BRed=BRed,BYellow=BYellow,BGreen=BGreen,BWhite=BWhite))
      exit()
  elif  in__==0:
    #break
    main2()

def makedic(mail,token,digit):
  dic="\n{\"email\":\""+mail+"\",\"token\":\""+token+"\",\"digit\":\""+digit+"\"}"
  return dic
def randomemail():
  randomtype=random.randint(10,15)
  randomemai_l={
	"min_name_length":randomtype,
	"max_name_length":randomtype
}
  newdomain="https://api.internal.temp-mail.io/api/v3/email/new"
  randomemail=(json.loads((rp(newdomain,json=randomemai_l)).text))
  randommail=randomemail["email"]
  mailtoken=randomemail["token"]
  with open("all_domain.json","r+",encoding="utf-8") as alldr:
      randomtypestr=str(randomtype)
      filesdata=alldr.read()
      domall=int(len(filesdata))-2
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(randommail,mailtoken,randomtypestr)+']}'
      alldr.close()
     
  with open("all_domain.json","w",encoding="utf-8") as alldr:
      alldr.write(str(addingmail))
      alldr.close()
  with open("core/domain.txt","w",encoding="utf-8") as currend:
      currend.write(randommail)
      currend.close()
  logop(f"\n{BBlack}[{BGreen} !{BBlack} ] {BGreen}SUCCESSFULLY CREATE A NEW EMAIL {BBlack}[{BGreen} !{BBlack} ]")
  logop("{BBlack}[{BGreen} !{BBlack} ]{BGreen} CREATED EMAIL {BBlack}:{BWhite} {newemail}".format(newemail=randommail,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))    
  inboxchkdef()
  
  

def filchk(rxvxrsx):
  return os.path.exists(rxvxrsx)
  
  
def inboxchkdef():
  os.system("clear")
  
  with open("core/mailchk.rxvxrsx","w",encoding="utf-8") as faka:
    faka.write(" ")
    faka.close()
  with open('core/rxvxrsxcount.rxvxrsx','w',encoding="utf-8") as rxvxrsxcount:
    rxvxrsxcount.write("0")
    rxvxrsxcount.close()
  with open("core/domain.txt","r",encoding="utf-8") as currentemail:
    currentemail=currentemail.read()
    
  currentemail=currentemail
  inboxchk="https://api.internal.temp-mail.io/api/v3/email/{crmail}/messages".format(crmail=currentemail)
  inboxlogo(currentemail)    

  while True:
    try:
      with open("core/mailchk.rxvxrsx","r",encoding="utf-8") as rxvxrsxchk:  
        defaultbox=rxvxrsxchk.read()
        rxvxrsxchk.close()
      time.sleep(0.01)
      inboxget1=  rg(inboxchk,headers=header)
      inboxget=json.loads((inboxget1).text)
      x=str(defaultbox)==str(inboxget)
      if str(defaultbox)==str(inboxget):
        pass
      else:
        if inboxget == []:
          pass
        elif inboxget1.status_code==400:
          inboxget["message"]
          if inboxget["message"]=="Email not found":
            os.system("clear;")
            print("{BBlack}[{BRed} !{BBlack} ] {BYellow}YOUR MAIL IS EXPIRED {BBlack}[{BRed} !{BBlack} ]".format(BBlack=BBlack,BRed=BRed,BYellow=BYellow))
            time.sleep(0.01)
            main2()
            break
          else:
            exit(inboxget["message"])
        else:
          with open("core/mailchk.rxvxrsx","w",encoding="utf-8") as rxvxrsxchk:
            
            inboxget=json.loads((inboxget1).text)
            rxvxrsxchk.write(str(inboxget))
         
          for filse,emailtext in enumerate(inboxget):
            if emailtext==[]:
              pass
            else:
        
              if int(open('core/rxvxrsxcount.rxvxrsx','r',encoding="utf-8").read()) <filse+1:
                
                with open('core/rxvxrsxcount.rxvxrsx','w',encoding="utf-8") as rxvxrsxcount:
                  
                  rxvxrsxcount.write(str(filse+1))
                  rxvxrsxcount.close()
                
                logop(f"{BBlack}----------{BYellow} INBOX {BBlack}-----------\n")
                logop("{BBlack}>>> {BGreen}EMAIL : {BWhite}{filse}\n".format(filse=(1+filse), BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
                if 'T' in emailtext["created_at"]:
                  timecr=emailtext["created_at"].replace("T","rxvxrsx")
                  rxvxrsxtime=timecr.split("rxvxrsx")
                 
                else:
                  timecr=emailtext["created_at"]
                for num,i in enumerate(rxvxrsxtime):
                  if num==0:
                    date=i
                  elif num == 1:
                    timecr=i.split(":")
                    for num,timeing in enumerate(timecr):
                      if num==0:
                        hour=int(timeing)
                        hour=hour+6 
                        hour=str(hour)
                      elif num==1:
                        minit=timeing
                      elif  num==2:
                        second=timeing[:2]
                    print("{BBlack}>>> {BGreen}DATE {BBlack}:{BWhite} {time}".format(time=date+', '+hour+":"+minit+':'+second,BBlack=BBlack,BYellow=BYellow,BGreen=BGreen,BWhite=BWhite))  
                if "<" in emailtext['from']:
                  fromf_ck=emailtext['from']
                  f_cky=fromf_ck.replace(" <"," • ")
                  f_cky=f_cky.replace(">", "")
                  if '"' in f_cky:
                    f_cky=f_cky.replace('"','')
                  else:
                    pass
                else:
                  f_cky=emailtext['from']
                print("{BBlack}>>> {BGreen}FROM {BBlack}:{BWhite} {From}\n".format(From=f_cky,BGreen=BGreen,BBlack=BBlack,BYellow=BYellow,BWhite=BWhite))
                
                print("{BBlack}>>> {BGreen}TO{BBlack} :{BWhite} {To}".format(To=emailtext["to"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
                if str(emailtext["cc"])== "None":
                  pass
                else:
                  print("{BBlack}>>> {BGreen}CC {BBlack}: {BRed}{cc}".format(cc=emailtext["cc"],BBlack=BBlack,BGreen=BGreen,BRed=BRed,BWhite=BWhite))
                print("{BBlack}>>> {BGreen}SUBJECT{BBlack} :{BWhite} {subject}" .format(subject=emailtext["subject"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
                print("\n{BBlack}>>> {BGreen}BODY : {BWhite}{body}".format(body=emailtext["body_text"],BBlack=BBlack,BWhite=BWhite,BGreen=BGreen))
                
                if emailtext["attachments"] == []:
                  pass
                else:
                  for num,ia in enumerate(emailtext["attachments"]):
                    print("\n{BBlack}>>>{BGreen} ATTACHMENT NO. {BBlack}:{BYellow} {ia}\n".format(ia=num+1,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow))
                    print(f"{BBlack}>>>{BGreen} VIEW ATTACHMENT {BBlack}:{BYellow} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?preview=1\n")
                    print(f"{BBlack}>>>{BGreen} DOWNLOAD ATTACHMENT{BBlack} :{BYellow} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?download=1\n")
                    print(f"{BBlack}>>>{BGreen} ATTACHMENT NAME {BBlack}:{BYellow}"+(str(ia["name"]))+"\n")
                    if 1048576<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1048576)
                      sizeofia=mathsize[:4]
                      print(f"{BBlack}>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(sizeofia)+f"{BBlue} M.B.\n")
                    elif 1048576>=int(ia["size"]) and 1024<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1024)
                      sizeofia=mathsize[:4]
                      print(f"{BBlack}>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(sizeofia)+f"{BBlue} K.B.\n")
                    
                    else:
                      print(f"{BBlack}>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(ia["size"])+f"{BBlue} BYTES\n")
                      
              else:
                pass
    except Exception as rxvxrsx:
      exit(rxvxrsx)
    except  KeyboardInterrupt:
      main2()
      break
def more():
  logo="""
  {BBlack}[{BGreen} 1{BBlue}.{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
  {BBlack}[{BGreen} 2{BBlue}.{BBlack} ]{BGreen} Create New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
  {BBlack}[{BWhite} 3{BBlue}.{BBlack} ]{BWhite} See All Email {BBlack}[{BCyan} You Created {BBlack}]
  {BBlack}[{BWhite} 4{BBlue}.{BBlack} ]{BWhite} View Current Email {BBlack}[ {BCyan}All Emails {BBlack}]
  {BBlack}[{BWhite} 5{BBlue}.{BBlack} ]{BWhite} Email History {BBlack}[ {BCyan}You Can Login {BBlack}]
  {BBlack}[{BPurple} 6{BBlue}.{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
  {BBlack}[{BRed} 0{BBlue}.{BBlack} ]{BRed} Exit{BBlack}
  """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
  try:
    while True:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{BBlack}  ~~~>>>{BWhite} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin =="3":
        seemail()
        break
      elif manuin =="4":
        viewmail()
        break
      elif manuin=="5":
        historylog()
        break
      elif manuin=="6":
        rxvxrsxgit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("[ ! ] INVALID SELECTION [ ! ]")
        time.sleep(0.01)
  except KeyboardInterrupt:
    x_X=input(f"\n\n{BYellow} BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BBlue} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()      
def more2():
  logo="""
  {BBlack}[{BGreen} 1{BBlue}.{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
  {BBlack}[{BGreen} 2{BBlue}.{BBlack} ]{BGreen} Create New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
  {BBlack}[{BYellow} 3{BBlue}.{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
  {BBlack}[{BWhite} 4{BBlue}.{BBlack} ]{BWhite} See All Email {BBlack}[{BCyan} You Created {BBlack}]
  {BBlack}[{BWhite} 5{BBlue}.{BBlack} ]{BWhite} View Current Email {BBlack}[ {BCyan}All Emails {BBlack}]
  {BBlack}[{BWhite} 6{BBlue}.{BBlack} ]{BWhite} Email History {BBlack}[ {BCyan}You Can Login {BBlack}]
  {BBlack}[{BPurple} 7{BBlue}.{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
  {BBlack}[{BRed} 0{BBlue}.{BBlack} ]{BRed} Exit{BBlack}
  """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
  try:
    
    while True:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{BBlack}  ~~~>>>{BWhite} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin=="3":
        inboxchkdef()
        break
      elif manuin =="4":
        seemail()
        break
      elif manuin =="5":
        viewmail()
        break
      elif manuin=="6":
        historylog()
        break
      elif manuin=="7":
        rxvxrsxgit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("[ ! ] INVALID SELECTION [ ! ]")
        time.sleep(0.01)   
  except KeyboardInterrupt:
    x_X=input(f"\n\n{BYellow} BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BBlue} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()      
def main2():
  try:
    logo="""
    {BBlack}[{BGreen} 1{BBlue}.{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
    {BBlack}[{BGreen} 2{BBlue}.{BBlack} ]{BGreen} Create New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
    {BBlack}[{BYellow} 3{BBlue}.{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
    {BBlack}[{BYellow} 4{BBlue}.{BBlack} ]{BYellow} More Features {BBlack}[ {BCyan}... {BBlack}]
    {BBlack}[{BPurple} 5{BBlue}.{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
    {BBlack}[{BRed} 0{BBlue}.{BBlack} ]{BRed} Exit{BBlack}
    """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
    while True:
      
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{BBlack}    ~~~>>>{BWhite} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin=="3":
        inboxchkdef()
        break
      elif manuin=="4":
        more2()
        break
      elif manuin =="5":
        rxvxrsxgit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("{BBlack}[{BRed} !{BBlack} ]{BRed} INVALID SELECTION {BBlack}[{BRed} !{BBlack} ]".format(BBlack=BBlack,BRed=BRed))
        time.sleep(0.01)
  except KeyboardInterrupt:
    x_X=input(f"\n\n{BYellow} BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BBlue} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()    
def main():
  try:
    logo="""
    {BBlack}[{BGreen} 1{BBlue}.{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
    {BBlack}[{BGreen} 2{BBlue}.{BBlack} ]{BGreen} Create New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
    {BBlack}[{BYellow} 3{BBlue}.{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
    {BBlack}[{BYellow} 4{BBlue}.{BBlack} ]{BYellow} More Features {BBlack}[ {BCyan}... {BBlack}]
    {BBlack}[{BPurple} 5{BBlue}.{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
    {BBlack}[{BRed} 0{BBlue}.{BBlack} ]{BRed} Exit{BBlack}
    """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
    while True:
      if filchk("core/domain.txt"):
        inboxchkdef()
        break
      else:
        os.system("clear")
        print(manuhome)
        print(logo)
        manuin=input(f"{BBlack}  ~~~>>>{BWhite} ")
        if manuin=="1":
          randomemail()
          break
        elif manuin=="2":
          coustomnewdomains()
          break
        elif manuin=="3":
          more()
          break
        elif manuin=="4":
          rxvxrsxgit()
          break
        elif manuin=="0":
          ext()
        else:
          print("{BBlack}[{BRed} !{BBlack} ]{BRed} Invalid Selection {BBlack}[{BRed} !{BBlack} ]".format(BBlack=BBlack,BRed=BRed))
          time.sleep(0.01)
        
  except KeyboardInterrupt:
    x_X=input(f"\n\n{BYellow} Back main menu or type {BRed}n{BYellow} To exit {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BBlue} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()
        
 
def __init__():
  try:
    os.system("clear")
    print(loginpromt)
    x=json.loads(rg("https://raw.githubusercontent.com/rxvxrsx/CTM-API/main/api/ctm-api.json",headers=headergit).text)
    if x["condition"] == "on":
      if x["product"]=="CTM":
        if x["code"]=="CYFER":
          if x["version"]==currenteversion:
            if x["api"] == "running":
              main()
        else:
          exit("[ ! ] API DOWN [ ! ]")
      else:
      	os.system("bash core/up_ctm.sh")
    else:
      exit("[ ! ] TOOL IS OFF [ ! ]")
  except Exception as mm:
    exit(mm)

__init__()
