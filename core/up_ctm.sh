##########################################################
# DEV : CYFER
# Github : https://github.com/rxvxrsx
##########################################################

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
BReset='\033[0;00m'

update(){
  echo -e "${BBlack}[ ${BCyan}# ${BBlack}]${BCyan} A UPDATE AVAILABLE"
  sleep 0.1
  echo -e "${BBlack}[ ${BCyan}# ${BBlack}]${BCyan} CTM IS UPDATING"
  sleep 0.1
  echo -e "${BBlack}[ ${BGreen}! ${BBlack}]${BGreen} PLEASE WAIT...\n" 
  rm -rf ctm ;
  apt update ; 
  apt install python3 -y ; 
  apt install git -y ; 
  pip install requests ; 
  cd .. ;
  rm -rf ctm ;
  git clone https://github.com/rxvxrsx/ctm > /dev/null 2>&1 ;
  python ctm.py
  


  echo
  echo -e "${BBlack}[ ${BGreen}! ${BBlack}]${BGreen} NOW YOUR TOOL UPDATED." 
  echo
  echo -e "${BBlack}[ ${BPurple}# ${BBlack}]${BPurple} THANKS FOR UPDATE ME."
  echo
  echo -e "${BBlack}[ ${BYellow}! ${BBlack}]${BYellow} NOW TYPE ${BBlack}[ ${BYellow}! ${BBlack}]"
  echo
  echo -e "${BBlack}[ ${BGreen}* ${BBlack}]${BGreen} python ctm.py ${BBlack}| ${BGreen}python3 ctm.py${BReset}" ;
  sleep 3


}
update
echo
exit


##########################################################
# DEV : CYFER
# Github : https://github.com/rxvxrsx
##########################################################
