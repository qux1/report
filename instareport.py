from requests import post,get
from rich.console import Console
import requests,os,re,uuid
import time
from colorist import Color
from colorist import red
from rich.text import Text
from datetime import datetime

#this bot made only for ban community and if you get any problem with version contact me in telegram i will give you a new version of this bot and this bot made by ZRO and this is a gift from me to all enjoy your day guys ❤🫶🏼(Disclaimer : I do not tolerate any harm caused by the misuse of the tool for malicious purposes.)

# Set the expiration date (YYYY, MM, DD)
expiration_date = datetime(2025, 12, 31)  # Example: November 4, 2024

# Check if the current date is past the expiration date
if datetime.now() > expiration_date:
    print("\033[1;32mTool Disabled \033[0m")
    exit()

# Continue with the rest of your tool's functionality
print("Welcome to the tool! You can use it.")

uid=str(uuid.uuid4())
console=Console()

def header():
    os.system("cls" if os.name=='nt' else "clear");console.print(f"""
    
███████╗  ██████╗░  ░█████╗░
╚════██║  ██╔══██╗  ██╔══██╗
░░███╔═╝  ██████╔╝  ██║░░██║
██╔══╝░░  ██╔══██╗  ██║░░██║
███████╗  ██║░░██║  ╚█████╔╝
╚══════╝  ╚═╝░░╚═╝  ░╚════╝░



█ █▀▄▀█ █▀█ █▀▀ █▀█ █▀ █▀█ █▄░█ ▄▀█ ▀█▀ █ █▀█ █▄░█
█ █░▀░█ █▀▀ ██▄ █▀▄ ▄█ █▄█ █░▀█ █▀█ ░█░ █ █▄█ █░▀█




█▀█ █▀▀ █▀█ █▀█ █▀█ ▀█▀   ▀█▀ █▀█ █▀█ █░░
█▀▄ ██▄ █▀▀ █▄█ █▀▄ ░█░   ░█░ █▄█ █▄█ █▄▄


""",style='bold red',justify='center')


# Define ANSI color codes for styling
class TextColor:
    HEADER = '\033[95m'  # Magenta
    OKBLUE = '\033[94m'  # Blue
    OKCYAN = '\033[96m'  # Cyan
    OKGREEN = '\033[92m' # Green
    WARNING = '\033[93m' # Yellow
    FAIL = '\033[91m'    # Red
    ENDC = '\033[0m'     # End of color
    
    
def Report_Instagram(target_id, sessionid, csrftoken):
    header()
    
    print(f"{TextColor.HEADER}Choose Report Type{TextColor.ENDC}")
    report_options = [
        "1 - Spam",
        "2 - Self",
        "3 - Drugs",
        "4 - Nudity",
        "5 - Violence",
        "6 - Hate",
        "7 - Bullying",
        "8 - Impersonation"
    ]
    
    for option in report_options:
        print(f"  {TextColor.FAIL}{option}{TextColor.ENDC}")

    while True:
        try:
            reportType = int(input(f"{TextColor.OKGREEN}Choose: {TextColor.ENDC} "))
            if reportType in range(1, 9):
                print(f"{TextColor.OKGREEN}You selected: {reportType}{TextColor.ENDC}")
                break
            else:
                print(f"{TextColor.FAIL}Invalid input. Please choose a number between 1 and 8.{TextColor.ENDC}")
        except ValueError:
            print(f"{TextColor.FAIL}Invalid input. Please enter a valid number.{TextColor.ENDC}")

# Example call to the function (Replace with actual session info)
# Report_Instagram('some_target_id', 'your_session_id', 'your_csrf_token')

    while 1:
        try:
            r3 = post(
                "https://i.instagram.com/users/" + target_id + "/flag/",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
                    "Host": "i.instagram.com",
                    'cookie': f"sessionid={sessionid}",
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                },
                data=f'source_name=&reason_id={reportType}&frx_context=',
                allow_redirects=False
            )         
            
            if r3.status_code==429:
                console.print(f"- Account Flagged [ {r3.status_code} ] ");exit()
            elif r3.status_code==500:
                console.print(f"- Target Not Found with status code [ {r3.status_code} ] ");exit()
            else:
                console.print(f"Reportd Done [bold green]successfully[/bold green]") 
                time.sleep(10)				
        except requests.exceptions.TooManyRedirects:
            console.print(f"Reportd Done [bold green]successfully[/bold green]")#;exit()
            time.sleep(10)
        except Exception as e:
            console.print(f"- Report Failed with status code [ {r3.status_code} ] ");exit()

def starter():
    console.print(Text("Welcome to the Login System!", style="bold underline"))
    
    user = input("\033[1;32mEnter Your Username : \033[0m")
    if user=="":console.print("[!] You must write The user");exit()
    pess = input("\033[1;32m Enter Your Password : \033[0m")
    if pess=="":console.print("[!] You must write The password");exit()
    r1=post('https://i.instagram.com/api/v1/accounts/login/',headers={'User-Agent': 'Instagram 114.0.0.38.120 Android (30/3.0; 216dpi; 1080x2340; huawei/google; Nexus 6P; angler; angler; en_US)',"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US","X-IG-Capabilities": "3brTvw==","X-IG-Connection-Type": "WIFI","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Host': 'i.instagram.com'},data={'_uuid': uid,'password': pess,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_count': '0'},allow_redirects=True)
    if 'logged_in_user' in r1.text:
        console.print("Logged in [bold green]successfully[/bold green] ")
        sessionid=r1.cookies['sessionid']
        csrftoken=r1.cookies['csrftoken']
        target=input(f"\033[1;36m Target : \033[0m ") #The username Must Be Entered Manually Not Copy & Paste/n t.me/O_H_3

        r2=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 TweakPY_vv1ck (TweakPY_vv1ck)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % target})
        if 'No users found' in r2.text:
            adv_search=get(f'https://www.instagram.com/{target}',headers={'Host': 'www.instagram.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Cookie': f'csrftoken={csrftoken}','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers'})
            try:
                target_id=re.findall('"profile_id":"(.*?)"',adv_search.text)[0]
                Report_Instagram(target_id,sessionid,csrftoken)
            except IndexError:
                try:
                    target_id=re.findall('"page_id":"profilePage_(.*?)"',adv_search.text)[0]
                    Report_Instagram(target_id,sessionid,csrftoken)
                except IndexError:
                    try:
                        adv_search2=get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={target}',headers={'Host': 'www.instagram.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','X-CSRFToken': csrftoken,'X-IG-App-ID': '936619743392459','X-ASBD-ID': '198387','X-IG-WWW-Claim': 'hmac.AR3KPEPoXkWYhwtoCUKyUHK80GsE1g2PJI1uPtDlCyo4PHKn','X-Requested-With': 'XMLHttpRequest','Alt-Used': 'www.instagram.com','Connection': 'keep-alive','Referer': f'https://www.instagram.com/{target}/','Cookie':  f'sessionid={sessionid}','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','TE': 'trailers'})
                        target_id=adv_search2.json()['data']['user']['id']
                        Report_Instagram(target_id,sessionid,csrftoken)
                    except KeyError:
                        console.print('\n- [bold red]Failed[/bold red] to get target username, Try entering the Target ID manually .\n')
                        target_id=input('- Enter The Target ID : ')
                        Report_Instagram(target_id,sessionid,csrftoken)
        elif '"spam":true' in r2.text:
            console.print("- Try again Later !");exit()
        else:
            try:
                target_id=str(r2.json()['user_id'])
                Report_Instagram(target_id,sessionid,csrftoken)
            except KeyError:
                console.print('- General [bold red]Error[/bold red] ...');exit() 
#AMMAR99
    elif 'ip_block' in r1.text:
        console.print("- You Have [bold red]banned[/bold red] from Instagram ( [bold red]ip block[/bold red] ) !");exit()
    elif 'The password you entered is incorrect' in r1.text:
        console.print("- Please check Your Password !");exit()
    elif "Please check your username and try again." in r1.text:
        console.print("- username Not Found !");exit()
    elif 'two_factor_required' in r1.text:
        console.print("- [bold orange3]Two Factor[/bold orange3] ! ...");exit()
    elif 'challenge_required' in r1.text:
        console.print("- [bold orange3]Secure[/bold orange3] Account ! ...");exit()
    elif 'inactive user' in r1.text:
        console.print('- This user is [bold red]banned[/bold red] from Instagram ...');exit()
    elif "We're working on it and we'll get it fixed as soon as we can." in r1.text:
        console.print("- Try again in a minute !");exit()
    elif 'Please wait a few minutes before you try again' in r1.text:
        console.print("- Try again in a minute !");exit()
    elif 'Bad request' in r1.text:
        console.print("- [bold red]Error[/bold red] in instagram, try again in 15 minutes ...");exit()
    elif 'Invalid Parameters' in r1.text:
        console.print("- [bold red]Error[/bold red] Please Reinstall The Tool From The original Source ... ");exit()
    else:
        console.print('- General [bold red]Error[/bold red] ...');exit()    


#AMMAR99
header();starter()
