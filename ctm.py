#rxvxrsx
#coding/bin/python3
#coding=utf-8
from core.headers import *
from core.logo import *
import os
import re
import webbrowser
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
currenteversion="v1.3"
def logop(z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.02)
def rxvxrsxgit():
  try:
    os.system("xdg-open https://github.com/rxvxrsx/")
  except OSError:
      print("xdg-open failed, using webbrowser instead.")
      webbrowser.open("https://github.com/rxvxrsx/")
def ext():
  exit("\n{BBlack}[{BRed} !{BBlack} ] {BGreen}THANKS FOR USING {BBlack}[{BRed} !{BBlack} ]\n".format(BBlack=BBlack,BRed=BRed,BGreen=BGreen))

def viewmail():
  if os.path.exists("core/domain.txt"):
    with open("core/domain.txt","r",encoding="utf-8") as cmmail:
      cmmail = cmmail.read().strip()  # ลบช่องว่างส่วนเกิน
      if cmmail:  # ตรวจสอบว่าไฟล์มีเนื้อหาหรือไม่
         print(f"\n{BBlack}[{BGreen} * {BBlack}]{BGreen} CUREENT_EMAIL{BBlack} :{BWhite} {cmmail}")
      else:
         print(f"\n{BBlack}[{BYellow} !{BBlack} ]{BYellow} NO SAVED EMAILS FOUND.")
  else:
    print(f"\n{BBlack}[{BRed} !{BBlack} ]{BRed} EMAIL FILE NOT FOUND.")

    #print(f"\n{BBlack}>>>>>{BGreen} CUREENT_EMAIL{BBlack} :{BWhite} {cmmail}")

  while True:
    x_X = get_yes_no_input(f"\n{BYellow}BACK MAIN MANU {BBlack}[ {BGreen}y {Color_Reset}/ {BRed}n {BBlack}] {BBlack}:{BWhite} ")
    if x_X == "y":
      main()
    elif x_X == "n":
      ext()

def validate_email_name(email_name):
    # Regular expression to check for valid email name characters (excluding special characters and spaces)
    valid_email_name_pattern = r"^[a-zA-Z0-9]+[a-zA-Z0-9._-]{6,30}$"
    return re.match(valid_email_name_pattern, email_name)
def coustomnewdomains():
  domain=(json.loads(rg("https://api.internal.temp-mail.io/api/v3/domains",headers=header).text))["domains"]
  
  while True:
      email_name = input(f"\n{BBlack}# {BGreen}ENTER EMAIL NAME {BBlack}:{BWhite} ")
      if email_name.strip():  # Check if input is not empty after removing whitespace
          if validate_email_name(email_name):
              break  # Valid email name
          else:
              print(f"\n{BBlack}[{BRed} !{BBlack} ]{BRed} INVALID EMAIL NAME. {BYellow}Please use only {BBlack}[ {BGreen}a-zA-Z0-9_.- {BBlack}] {BBlack}[{BRed} !{BBlack} ]")
              print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} The email name must be between 6 and 30 characters.")  # เพิ่มข้อความแสดงความยาว
              print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} Special characters other than ._- are not allowed.")  # เพิ่มข้อความแสดงอักขระพิเศษ
      else:
          print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} EMAIL BACK MAIN MANU CANNOT BE EMPTY {BBlack}[{BRed} !{BBlack} ]")
  
  for domainsrow,domains in enumerate(domain):
      print(f"{BBlack}\n[{BYellow}",domainsrow+1,f"{BBlack}]{BWhite}",domains["name"],f" {BYellow}!{Color_Reset}")
  
  # กำหนดจำนวนโดเมนทั้งหมด (ตัวอย่าง)
  num_domains = len(domain)

  # รับ input จากผู้ใช้ และตรวจสอบค่า
  while True:
      try:
          ma = int(input(f"\n{BBlack}#{BGreen} SELECT THE DESIRED DOMAIN NUMBER {BBlack}( {BGreen}1 {BBlack}- {BGreen}{num_domains}{BBlack} ) : {BWhite}"))
          if 1 <= ma <= num_domains:
              # ถ้าค่าถูกต้อง ให้ทำการดำเนินการต่อที่นี่
              break  # ออกจาก loop
          else:
              print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} THE ENTERED VALUE IS INVALID. PLEASE SELECT A DOMAIN NUMBER BETWEEN {BGreen}1 {BRed}AND {BGreen}{num_domains}{BBlack}")
      except ValueError:
        print(f"{BBlack}[{BRed} !{BBlack} ]{BRed} PLEASE ENTER NUMBERS ONLY.{BBlack}")

  if domainsrow+1 >= ma:
    inputdomain = ma - 1
    print(f"\n{BBlack}[ {BYellow}# {BBlack}]{BYellow} SELECTED DOMAIN {BBlack}:{BWhite} "+domain[inputdomain]["name"])
    coustom_domain = domain[inputdomain]["name"]
    
    coustom = {
        "name": email_name,
        "domain": coustom_domain
}
    digite=len(email_name)
    newdomain="https://api.internal.temp-mail.io/api/v3/email/new"
    domainr=rp(newdomain,json=coustom,headers=header)
    emailcoustom=email_name+"@"+coustom_domain
    domaincon=(json.loads(domainr.text))["email"]==emailcoustom
    mailtoken=(json.loads(domainr.text))["token"]
    if domaincon:

      logop(f"\n{BBlack}[{BGreen} !{BBlack} ] {BGreen}SUCCESSFULLY CREATE A NEW EMAIL {BBlack}[{BGreen} !{BBlack} ]")
      logop("{BBlack}[{BCyan} *{BBlack} ]{BCyan} CREATED EMAIL {BBlack}:{BWhite} {newemail}".format(newemail=(json.loads(domainr.text))["email"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite,BCyan=BCyan))

    with open("all_domain.json","r+",encoding="utf-8") as alldr:
      filesdata=alldr.read()
      domall=int(len(filesdata))-5
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(emailcoustom,mailtoken,(str(digite)))+'\n\t]\n}'
     
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

  while True:
    x_X = get_yes_no_input(f"\n{BYellow}BACK MAIN MANU {BBlack}[ {BGreen}y {Color_Reset}/ {BRed}n {BBlack}] {BBlack}:{BWhite} ")
    if x_X == "y":
      main()
    elif x_X == "n":
      ext()

def get_yes_no_input(prompt):
  while True:
    answer = input(prompt).lower()
    if answer in ['y', 'n']:
      return answer
    else:
      print(f"{BBlack}[{BCyan} ! {BBlack}]{BCyan} PLEASE ENTER {BGreen}y {BCyan}OR {BRed}n {BCyan}ONLY. {BBlack}[{BYellow} ! {BBlack}]{BYellow}")
      

def get_number_input(prompt, max_choice):
  while True:
        try:
            number = int(input(prompt))
            if 0 <= number <= max_choice:
                return number
            else:
                print(f"{BBlack}[{BCyan} ! {BBlack}]{BCyan} NUMBERS BETWEEN {BGreen}0 {BCyan}AND {BGreen}{max_choice} {BBlack}")
        except ValueError:
            print(f"{BBlack}[{BCyan} ! {BBlack}]{BCyan} PLEASE ENTER NUMBERS ONLY.{BBlack}")

      
def historylog():
  url='https://api.internal.temp-mail.io/api/v3/email/new'
  with open("all_domain.json","r",encoding="utf-8") as read:
    read=(json.loads(read.read()))["domains"]
  os.system("clear")
  print(manuhome)
  for num , mail in enumerate(read):
    print("{BBlack}[ {BGreen}{rxvxrsx} {BBlack}] {BWhite}".format(rxvxrsx=num+1,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite)+mail["email"])
  
  print(f"\n{BBlack}[{BYellow} 0 {BBlack}]{BYellow} BACK MAIN MANU {BBlack}[ {BYellow}../{BBlack} ]") 

    # สมมติว่า len(read) คือจำนวนตัวเลือกที่ต้องการ
  max_choice = len(read)
  num_choices = get_number_input(f"\n{BBlack}[ {BGreen}# {BBlack}]{BGreen} LOGIN {BBlack}( {BGreen}0 {BBlack}- {BGreen}{max_choice} {BBlack}) : {BWhite}", max_choice)
  
  if 0 <= num_choices <= max_choice:
      # ดำเนินการตามค่าที่ได้รับ
      print(f"{BBlack}[{BCyan} ! {BBlack}]{BCyan} YOU HAVE SELECTED EMAIL : {BWhite}{num_choices}{BBlack}")
      # ... (ส่วนที่เหลือของโค้ดที่ใช้ค่า num_choices)
  else:
      print(f"{BBlack}[{BCyan} ! {BBlack}]{BCyan} THERE WAS AN ERROR SELECTING AN OPTION.{BBlack}")

  if num+1 >= num_choices and num_choices != 0:  
    index=(num_choices-1)
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
      logop(f"{BBlack}[{BGreen} !{BBlack} ]{BGreen} EMAIL SUCCESSFULLY ADDED")
      inboxchkdef()
    else:
      logop("{BBlack}[{BRed} !{BBlack} ] {BGreen}YOUR EMAIL{BWhite} : {log}".format(log=login,BBlack=BBlack,BRed=BRed,BYellow=BYellow,BGreen=BGreen,BWhite=BWhite))
      exit()
  elif  num_choices==0:
    #break
    main2()


def makedic(mail,token,digit):
  dic="\n\t\t{\n\t\t\t\"email\": \""+mail+"\",\n\t\t\t\"token\": \""+token+"\",\n\t\t\t\"digit\": \""+digit+"\"\n\t\t}"
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
      domall=int(len(filesdata))-5
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(randommail,mailtoken,randomtypestr)+'\n\t]\n}'
      alldr.close()
      
  with open("all_domain.json","w",encoding="utf-8") as alldr:
      alldr.write(str(addingmail))
      alldr.close()
  with open("core/domain.txt","w",encoding="utf-8") as currend:
      currend.write(randommail)
      currend.close()
  logop(f"\n{BBlack}[{BGreen} !{BBlack} ] {BGreen}SUCCESSFULLY CREATE A NEW EMAIL {BBlack}[{BGreen} !{BBlack} ]")
  logop("{BBlack}[{BGreen} !{BBlack} ]{BCyan} CREATED EMAIL {BBlack}:{BWhite} {newemail}".format(newemail=randommail,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite,BCyan=BCyan))    
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
                logop("{BBlack}>>>>> {BGreen}EMAIL : {BWhite}{filse}\n".format(filse=(1+filse), BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
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
                    print("{BBlack}>>>>> {BGreen}DATE {BBlack}:{BWhite} {time}".format(time=date+', '+hour+":"+minit+':'+second,BBlack=BBlack,BYellow=BYellow,BGreen=BGreen,BWhite=BWhite))  
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
                print("{BBlack}>>>>> {BGreen}FROM {BBlack}:{BWhite} {From}\n".format(From=f_cky,BGreen=BGreen,BBlack=BBlack,BYellow=BYellow,BWhite=BWhite))
                
                print("{BBlack}>>>>> {BGreen}TO{BBlack} :{BWhite} {To}".format(To=emailtext["to"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
                if str(emailtext["cc"])== "None":
                  pass
                else:
                  print("{BBlack}>>>>> {BGreen}CC {BBlack}: {BRed}{cc}".format(cc=emailtext["cc"],BBlack=BBlack,BGreen=BGreen,BRed=BRed,BWhite=BWhite))
                print("{BBlack}>>>>> {BGreen}SUBJECT{BBlack} :{BWhite} {subject}" .format(subject=emailtext["subject"],BBlack=BBlack,BGreen=BGreen,BYellow=BYellow,BWhite=BWhite))
                print("\n{BBlack}>>>>> {BGreen}BODY : {BWhite}{body}".format(body=emailtext["body_text"],BBlack=BBlack,BWhite=BWhite,BGreen=BGreen))
                
                if emailtext["attachments"] == []:
                  pass
                else:
                  for num,ia in enumerate(emailtext["attachments"]):
                    print("\n{BBlack}>>>>>{BGreen} ATTACHMENT NO. {BBlack}:{BYellow} {ia}\n".format(ia=num+1,BBlack=BBlack,BGreen=BGreen,BYellow=BYellow))
                    print(f"{BBlack}>>>>>{BGreen} VIEW ATTACHMENT {BBlack}:{BYellow} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?preview=1\n")
                    print(f"{BBlack}>>>>>{BGreen} DOWNLOAD ATTACHMENT{BBlack} :{BYellow} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?download=1\n")
                    print(f"{BBlack}>>>>>{BGreen} ATTACHMENT NAME {BBlack}:{BYellow}"+(str(ia["name"]))+"\n")
                    if 1048576<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1048576)
                      sizeofia=mathsize[:4]
                      print(f"{BBlack}>>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(sizeofia)+f"{BCyan} MB.\n")
                    elif 1048576>=int(ia["size"]) and 1024<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1024)
                      sizeofia=mathsize[:4]
                      print(f"{BBlack}>>>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(sizeofia)+f"{BCyan} KB.\n")
                    
                    else:
                      print(f"{BBlack}>>>>>{BGreen} ATTACHMENT SIZE {BBlack}:{BYellow} "+str(ia["size"])+f"{BCyan} BYTES.\n")
                      
              else:
                pass
    except Exception as rxvxrsx:
      exit(rxvxrsx)
    except  KeyboardInterrupt:
      main2()
      break
def more():
    logo="""{BBlack}[{BGreen} 1{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
{BBlack}[{BGreen} 2{BBlack} ]{BGreen} Custom New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
{BBlack}[{BWhite} 3{BBlack} ]{BWhite} See All Email {BBlack}[{BCyan} You Created {BBlack}]
{BBlack}[{BWhite} 4{BBlack} ]{BWhite} View Current Email {BBlack}[ {BCyan}Current Email {BBlack}]
{BBlack}[{BWhite} 5{BBlack} ]{BWhite} Email History {BBlack}[ {BCyan}You Can Login {BBlack}]
{BBlack}[{BPurple} 6{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
{BBlack}[{BRed} 0{BBlack} ]{BRed} Exit{BBlack}
""".format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
    try:
      while True:
        os.system("clear")
        print(manuhome)
        print(logo)
        manuin=input(f"{BBlack}[ #{BBlack} ]{BWhite} ")
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
      while True:
          try:
              x_X = get_yes_no_input(f"\n\n{BYellow}BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
              if x_X == "y":
                  main2()
              elif x_X == "n":
                  ext()
          except KeyboardInterrupt:
              print(f"\n{BRed}EXITING PROGRAM...")
              sys.exit(0)  # Exit program cleanly
      
def more2():
  logo="""{BBlack}[{BGreen} 1{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
{BBlack}[{BGreen} 2{BBlack} ]{BGreen} Custom New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
{BBlack}[{BYellow} 3{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
{BBlack}[{BWhite} 4{BBlack} ]{BWhite} See All Email {BBlack}[{BCyan} You Created {BBlack}]
{BBlack}[{BWhite} 5{BBlack} ]{BWhite} View Current Email {BBlack}[ {BCyan}Current Email {BBlack}]
{BBlack}[{BWhite} 6{BBlack} ]{BWhite} Email History {BBlack}[ {BCyan}You Can Login {BBlack}]
{BBlack}[{BPurple} 7{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
{BBlack}[{BRed} 0{BBlack} ]{BRed} Exit{BBlack}
""".format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
  try:
    
    while True:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{BBlack}[ #{BBlack} ]{BWhite} ")
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
        print(f"{BBlack}[ {BRed}! {BBlack}]{BRed} INVALID SELECTION {BBlack}[ {BRed}! {BBlack}]")
        time.sleep(1.0)   
  except KeyboardInterrupt:
    while True:
        try:
            x_X=input(f"\n\n{BYellow}BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
            if x_X == "y":
                main2()
            elif x_X == "n":
                ext()
        except KeyboardInterrupt:
            print(f"\n{BRed}EXITING PROGRAM...")
            sys.exit(0)  # Exit program cleanly 
def main2():
  try:
    logo="""{BBlack}[{BGreen} 1{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
{BBlack}[{BGreen} 2{BBlack} ]{BGreen} Custom New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
{BBlack}[{BYellow} 3{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
{BBlack}[{BYellow} 4{BBlack} ]{BYellow} More Features {BBlack}[ {BCyan}... {BBlack}]
{BBlack}[{BPurple} 5{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
{BBlack}[{BRed} 0{BBlack} ]{BRed} Exit{BBlack}
    """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
    while True:
      
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{BBlack}[ #{BBlack} ]{BWhite} ")
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
    while True:
        try:
            x_X=input(f"\n\n{BYellow}BACK MAIN MANU OR TYPE {BRed}n{BYellow} TO EXIT {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
            if x_X == "y":
                main2()
            elif x_X == "n":
                ext()
        except KeyboardInterrupt:
            print(f"\n{BRed}EXITING PROGRAM...")
            sys.exit(0)  # Exit program cleanly
    
def main():
  try:
    logo="""{BBlack}[{BGreen} 1{BBlack} ]{BGreen} Random New Email{BBlack} [{BCyan} Random {BBlack}] 
{BBlack}[{BGreen} 2{BBlack} ]{BGreen} Custom New Email{BBlack} [{BCyan} Create Your Self {BBlack}]
{BBlack}[{BYellow} 3{BBlack} ]{BYellow} Inbox Check{BBlack} [{BCyan} All Inbox {BBlack}]
{BBlack}[{BYellow} 4{BBlack} ]{BYellow} More Features {BBlack}[ {BCyan}... {BBlack}]
{BBlack}[{BPurple} 5{BBlack} ]{BPurple} Github {BBlack}[{BCyan} rxvxrsx {BBlack}]
{BBlack}[{BRed} 0{BBlack} ]{BRed} Exit{BBlack}
    """.format(Color_Reset=Color_Reset,BBlack=BBlack,BRed=BRed,BGreen=BGreen,BYellow=BYellow,BBlue=BBlue,BPurple=BPurple,BCyan=BCyan,BWhite=BWhite,BIBlack=BIBlack,BIRed=BIRed,BIGreen=BIGreen,BIYellow=BIYellow,BIBlue=BIBlue,BIPurple=BIPurple,BICyan=BICyan,BIWhite=BIWhite)
    while True:
      if filchk("core/domain.txt"):
        inboxchkdef()
        break
      else:
        os.system("clear")
        print(manuhome)
        print(logo)
        manuin=input(f"{BBlack}[ #{BBlack} ]{BWhite} ")
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
        elif manuin=="5":
          rxvxrsxgit()
          break
        elif manuin=="0":
          ext()
        else:
          print("{BBlack}[{BRed} !{BBlack} ]{BRed} INVALID SELECTION {BBlack}[{BRed} !{BBlack} ]".format(BBlack=BBlack,BRed=BRed))
          time.sleep(1.0)
        
  except KeyboardInterrupt:
    x_X=input(f"\n\n{BYellow} Back main menu or type {BRed}n{BYellow} To exit {BBlack}[{BGreen}y{Color_Reset}/{BRed}n{BBlack}] {BBlack}:{BWhite} ")
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
