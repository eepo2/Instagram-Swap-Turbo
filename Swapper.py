import os
try:
    import requests, random, time, string, hashlib,hmac,sys,uuid,json,os,discord,ctypes,threading,stdiomask
    from user_agent import *
    import stdiomask
    from discord import Webhook, RequestsWebhookAdapter
    from colorama import Fore , init
    from threading import Lock
except:
    os.system("pip install discord")
    os.system("pip install stdiomask")
    os.system("pip install colorama")
    os.system("pip install user_agent")
    os.system("pip install requests")
    import requests, random, time, string, hashlib,hmac,sys,uuid,json,os,discord,ctypes,threading,stdiomask
    from user_agent import *
    import stdiomask
    from discord import Webhook, RequestsWebhookAdapter
    from colorama import Fore , init
    from threading import Lock
if sys.version_info.major == 3:
    import urllib.parse


class Clear:
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{blue}
                                                          
                                                          
  .--.--.    ,--,                    ____                 
 /  /    '.,--.'|    ,--,          ,'  , `.               
|  :  /`. /|  | :  ,--.'|       ,-+-,.' _ |               
;  |  |--` :  : '  |  |,     ,-+-. ;   , ||               
|  :  ;_   |  ' |  `--'_    ,--.'|'   |  ||,---.          
 \  \    `.'  | |  ,' ,'|  |   |  ,', |  |/     \         
  `----.   |  | :  '  | |  |   | /  | |--/    /  |        
  __ \  \  '  : |__|  | :  |   : |  | , .    ' / |        
 /  /`--'  |  | '.''  : |__|   : |  |/  '   ;   /|        
'--'.     /;  :    |  | '.'|   | |`-'   '   |  / |        
  `--'---' |  ,   /;  :    |   ;/       |   :    |        
            ---`-' |  ,   /'---'         \   \  /         
                    ---`-'                `----'   

        ~~ free swapper 
                  by joshua 
                        (@ulzi) ~~       
                                                          
    {reset}\n""")
    



class Start:
    def __init__(self,m):
        for i in range(count):
            t = threading.Thread(target=m.start)
            t.daemon=True
            threads.append(t)
            t.start()
        for i in threads:i.join()
        m.stop()


class Swapper:
    def __init__(self, username, password):
        self.r = requests.session()
        self.uuid = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.isloggedin = False
        self.claimed = False
        self.proxy = False
        self.erorr,self.attempts,self.method = 0,0,1
        self.headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US","X-IG-Capabilities": "3brTvw==","X-IG-Connection-Type": "WIFI","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Host': 'i.instagram.com','Connection': 'keep-alive'}
        self.useragent = 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
        self.IG_SIG_KEY = '109513c04303341a7daf27bb41b268e633b30dcc65a3fe14503f743176113869'
        
    def sprint(self,*a, **b):
        with lock:
            print(*a, **b)

    def signature(self, data):
        body = (hmac.new(self.IG_SIG_KEY.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()+ "."+ urllib.parse.quote(data))
        signature = "signed_body={body}&ig_sig_key_version=4"
        return signature.format(body=body)

    def generateDeviceId(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def generateUUID(self, type):
        generated_uuid = str(uuid.uuid4())
        if (type):return generated_uuid
        else:return generated_uuid.replace('-', '')

    def setProxy(self):
        if useproxies == "y":
            try:
                proxy = random.choice(self.proxies)
                proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy}
                self.r.proxies.update(proxies);return True
            except:return False

    def checkFiles(self):
        try:
            with open(f'proxies.txt', 'r') as f:self.proxies=f.read().splitlines() 
            self.proxies = [i for i in self.proxies if i]
            random.choice(self.proxies)
            return True
        except Exception as e:
            with open(f'proxies.txt', 'a') as f:f.write("ip:port\n")
            input(f'\n[{red}!{reset}] {l}No proxy list found! Please place your proxies in proxies.txt then press enter!{END}')
            return False 

    def disc(self):
        try:
            webhook = Webhook.from_url(self.webhook, adapter=RequestsWebhookAdapter())
            e = discord.Embed(title=f"{self.webtitle}",  url=f"https://instagram.com/{self.target}", color=discord.Color.random())
            e.add_field(name=f"**User**: **{self.target}**", value="-")
            e.add_field(name=f"**Attempts**: **{self.attempts}**", value="-")
            e.set_thumbnail(url=self.webthumb)
            webhook.send(username="Slimy Sniper",avatar_url=self.webpfp,embed=e)
        except Exception as e:
            pass
    
    def options(self):
        json = self.Json
        MyPATH = json['challenge']['api_path']
        self.url_api = 'https://i.instagram.com/api/v1' + MyPATH
        Secure = self.r.get(self.url_api,headers=self.headers)
        text = Secure.text
        self.mode = []
        if 'step_data' in text:
            if ('phone_number') in Secure.json()['step_data']:
                ema = Secure.json()['step_data']['phone_number']
                self.mode.append('[0] Phone: {}'.format(ema))
            if ('email') in Secure.json()['step_data']:
                ema = Secure.json()['step_data']['email']
                self.mode.append('[1] Email: {}'.format(ema))
            if len(self.mode) > 0:
                return True
        return False

    
    def sendcode(self, myMode):
        SecureData = {'choice': myMode,'_uuid': self.uuid,'_uid': self.uuid,'_csrftoken': 'missing'}
        Send_Mode = self.r.post(self.url_api, headers=self.headers, data=SecureData).json()
        if myMode == 0:
            try:self.pasw = Send_Mode['step_data']['contact_point'];return True
            except:return False
        try:self.pasw = Send_Mode['step_data']['contact_point'];return True
        except:return False

    
    def entercode(self, myCode):
        CodeData = {'security_code': myCode,'_uuid': self.uuid,'_uid': self.uuid,'_csrftoken': 'missing'}
        Send_Code = self.r.post(self.url_api, headers=self.headers, data=CodeData)
        if 'logged_in_user' in Send_Code.text:
            loginJson = Send_Code.json()
            self.isloggedin = True
            self.username_id = loginJson["logged_in_user"]["pk"]
            self.token = self.r.cookies["csrftoken"]
            self.sessionidd = self.r.cookies["sessionid"]
            return True
        else:
            print(f'{red}[ERROR]{reset} Failed code!')
            time.sleep(2)
            return False


    
    def SendRequest(self,url, data=None, headers=None):
        if headers == None:
            self.r.headers.update({'Connection': 'close','Accept': '*/*','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie2': '$Version=1','Accept-Language': 'en-US','User-Agent': self.useragent})
        else:self.r.headers.update(headers)
        if data == None:
            while True:
                try:api = self.r.get(url);break
                except: pass
        else:
            while True:
                try:api = self.r.post(url, data=data, cookies=self.r.cookies.get_dict());break
                except:pass
        self.Code = api.status_code
        self.Text = api.text
        try:self.Json = json.loads(api.text)
        except:self.Json = {}
        if api.status_code == 200:
            return True
        else:return False
        

    def login(self):
        try:
            m =hashlib.md5();m.update(self.username.encode('utf-8') + self.password.encode('utf-8'));device_id = self.generateDeviceId(m.hexdigest());self.r.headers.update({'Connection': 'close','Accept': '*/*','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie2': '$Version=1','Accept-Language': 'en-US','User-Agent': self.useragent});response = requests.get('https://www.instagram.com')
            try:csrf = response.cookies['csrftoken']
            except:letters = string.ascii_lowercase;csrf = ''.join(random.choice(letters) for i in range(8))
            self.r.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid=' + self.generateUUID(False));data = {'phone_id': self.generateUUID(True),'_csrftoken': csrf,'username': self.username,'guid': self.generateUUID(True),'device_id': device_id,'password': self.password,'login_attempt_count': '0'}
            while True:
                try:login = self.r.post('https://b.i.instagram.com/api/v1/accounts/login/', self.signature(json.dumps(data)));break
                except Exception as e:
                    print(e)
            self.Text = login.text
            try:self.Json = json.loads(login.text)
            except:self.Json = {}
            if 'logged_in_user' in login.text:self.sessionid = self.r.cookies["sessionid"];self.token = self.r.cookies["csrftoken"];self.username_id = self.r.cookies['ds_user_id'];self.isloggedin=True;return True
            else:return False
        except Exception as e:print(e)

    def getProfileData(self):
        return self.SendRequest("https://i.instagram.com/api/v1/accounts/current_user/?edit=true")

    def parseData(self):
        try:settings = open('settings.txt','r').read().splitlines()
        except FileNotFoundError:
            print(f'\n[{red}!{reset}] Set your settings in settings.txt!')
            with open("settings.txt",'a') as f:f.write("""[Name: slime]\n[Bio: sniped by @ulzi]\n[Webhook: ]\n[WebhookTitle: new claim]\n[WebhookPFP: https://i5.tagstat.com/p1/p/YZamH7Dm8hVTyN-tD-HkY3PfBe0G9BXQ3AbEal36pKKY6WbTwgoWlSf5lV4xN7Ua.png]\n[WebhookThumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Edit_4x_rifle_scope.jpg/1200px-Edit_4x_rifle_scope.jpg]\n""")
        try:
            self.req_get_info = self.Json
            self.first_name = self.req_get_info["user"]["full_name"]
            try:self.first_name = settings[0].split("[Name: ")[1].replace("]",'')
            except:self.first_name = self.req_get_info["user"]["full_name"]
            try:self.bio=settings[1].split("[Bio: ")[1].replace("]",'')
            except:self.bio = 'sniped by @ulzi'
            try:self.webhook=settings[2].split("[Webhook: ")[1].replace("]",'')
            except:self.webhook = ''
            try:self.webtitle=settings[3].split("[WebhookTitle: ")[1].replace("]",'')
            except:self.webtitle = 'New Claim!'
            try:self.webpfp=settings[4].split("[WebhookPFP: ")[1].replace("]",'')
            except:self.webpfp = ''
            try:self.webthumb=settings[5].split("[WebhookThumbnail: ")[1].replace("]",'')
            except:self.webthumb = ''
            try:self.email = self.req_get_info["user"]["email"]
            except:letters = string.ascii_lowercase + '0123456789';self.email = ''.join(random.choice(letters) for i in range(20)) + '@gmail.com'
            try:self.phone = self.req_get_info["user"]["phone_number"]
            except:self.phone = ''
            return True
        except Exception as e:print(e);return False

    def editProfile(self,username):
        self.setProxy()
        data = {'_uuid': self.uuid,'_uid': self.username_id,'_csrftoken': self.token,'external_url': "https://discord.gg/unbans",'phone_number': self.phone,'username': username,'full_name': self.first_name,'biography': self.bio,'email': self.email,'gender': 3}
        return self.SendRequest('https://i.instagram.com/api/v1/accounts/edit_profile/', self.signature(json.dumps(data)))

    def editUsername(self,username):
        self.setProxy()
        data = {'username':username}
        return self.SendRequest('https://i.instagram.com/api/v1/accounts/edit_profile/', data)

    def editWebPost(self,username):
        self.setProxy()
        webhead = {'HOST':'www.instagram.com',  'KeepAlive':'True', 'user-agent':generate_user_agent(), 'Cookie':f"sessionid={self.sessionid}", 'Accept':'*/*', 'ContentType':'application/x-www-form-urlencoded', 'X-Requested-With':'XMLHttpRequest', 'X-IG-App-ID':'936619743392459', 'X-Instagram-AJAX':'missing', 'X-CSRFToken':'missing', 'Accept-Language':'en-US,en;q=0.9'}
        data={"first_name": '', "email": self.email, "username": username, "phone_number": self.phone, "biography": self.bio, "external_url": "https://discord.gg/unbans", "chaining_enabled": "on"}
        return self.SendRequest('https://i.instagram.com/api/v1/accounts/edit_profile/', data=data,headers=webhead)

    def stop(self):
        check = self.r.get(f"https://www.instagram.com/{self.target}/?__a=1")
        if check.status_code != 404 and self.claimed:
            print(f'\n[{green}+{reset}] Successfully Swapped >> @{self.target} | Method #{self.method}')
            self.disc()
            ctypes.windll.user32.MessageBoxW(0, f'Successfully Swapped : @{self.target} | Attempts: {self.attempts}', 'Ulzi Swapper', 0)
            input(f"\n{red}[+] Press ENTER to exit....")
            exit(0)
        print(f'\n[{red}!{reset}] Spam Blocked : @{self.target}')
        ctypes.windll.user32.MessageBoxW(0, f'Rate Limit Reached! : @{self.target}', 'Slimy Swapper', 0)
        input(f"\n{red}[+] Press ENTER to exit....")
        exit(0)

    def start(self):
        target = self.target
        while not self.claimed and "challenge_required" not in self.Text:
            while True:
                if self.claimed:break
                self.editProfile(target)
                self.sprint(f'\r{l}[{yellow}{self.method}{reset}] Attempts : {self.attempts}{END}', end='',flush=True)
                if self.Code == 200:self.claimed = True;return
                elif self.Code == 429:break
                elif self.Code==400:self.attempts+=1
            self.method = 2    
            while True:
                if self.claimed:break
                self.editUsername(target)
                self.sprint(f'\r{l}[{yellow}{self.method}{reset}] Attempts : {self.attempts}{END}', end='',flush=True)
                if self.Code == 200:self.claimed = True;return
                elif self.Code == 429:break
                elif 'confirmed phone number.' in self.Text:break
                elif self.Code==400:self.attempts+=1
            self.method = 3
            while True:
                if self.claimed:break
                self.editWebPost(target)
                self.sprint(f'\r{l}[{yellow}{self.method}{reset}] Attempts : {self.attempts}{END}', end='',flush=True)
                Text = self.Text
                if 'https://www.instagram.com/accounts/login/?hl=' in Text:return
                if self.Code == 200 and '"status": "ok"' in Text:self.claimed=True;return
                elif self.Code == 429 or "Try again later" in Text:return
                elif "feedback_required" in self.Text or "spam" in Text:return
                elif self.attempts >149:return
                elif self.Code==400:self.attempts+=1

    def errorHandle(self):
        if 'The password you entered is incorrect' in self.Text:
            print(f'\n{red}[ERROR]{reset} Incorrect password!\n')
            time.sleep(3)
        elif 'Please check your username and try again.' in self.Text:
            print(f'\n{red}[ERROR]{reset} Incorrect username!\n')
            time.sleep(3)
        elif 'Invalid Parameters' in self.Text:
            print(f'\n{red}[ERROR]{reset} Insufficient data passed!\n')
            time.sleep(3)
        elif "Please wait a few minutes before you try again." in self.Text:
            print(f'\n{red}[ERROR]{reset} Ratelimited on login! Please try again later.\n')
            time.sleep(3)
        elif 'api_path' in self.Text:
            if not self.isloggedin:
                print(f'\n{red}[!]{reset} Challenge code required!\n')
                time.sleep(3)
                if self.options():
                    for i in self.mode:
                        print(i)
                    choice = int(input(f"\n{magenta}[+]{reset} Choose One: "))
                    if self.sendcode(choice):
                        code = input(f"\n{magenta}[+]{reset} Enter your 6 digit code: ")
                        return self.entercode(code)
            else:
                print(f'\n{red}[ERROR]{reset} Your Account Is Challenge Locked!\n')
                self.isloggedin = False
        elif 'login_required' in self.Text:
                self.isloggedin = False;self.loggedout=True
                print(f'\n{red}[ERROR]{reset} Logged out!!\n')
                time.sleep(4)
        else:print("Error: " + self.Text)
        return False

    
            

if __name__ == "__main__":
    lock = Lock()
    init(autoreset=True)
    magenta = Fore.LIGHTMAGENTA_EX
    green = Fore.LIGHTGREEN_EX
    blue = Fore.CYAN
    red = Fore.LIGHTRED_EX
    reset = Fore.RESET
    yellow = Fore.YELLOW
    magenta = Fore.LIGHTMAGENTA_EX
    l = Fore.WHITE
    reset = Fore.RESET
    END = '\033[0m'
    threads = []
    m = Swapper('','')
    while not m.isloggedin:
        Clear().clear()
        usr = input(f"{yellow}[+]{reset} {l}Enter Your Username:{END} ")
        pas = stdiomask.getpass(f"{yellow}[+]{reset} Enter Your Password: ")
        m = Swapper(usr,pas)
        if not m.login():
            if not m.errorHandle():continue
        if not m.getProfileData():m.errorHandle();time.sleep(4);continue
        if not m.parseData():m.errorHandle();time.sleep(4)
    print(f"{green}[SUCCESS]{reset} Logged Into User >> {usr}")
    m.target = input(f"{magenta}[+]{reset} {l}Enter Target Username:{END} ")
    count = int(input(f"{magenta}[+]{reset} {l}Enter Amount of Threads:{END} "))
    useproxies = input(f"{magenta}[+]{reset} {l}Use HTTP Proxies? (Y/N):{END} ").lower()
    if useproxies == 'y':m.checkFiles()
    ctypes.windll.user32.MessageBoxW(0, f'Slatt! Are You ready!??', 'Slimy Swapper', 0)
    Start(m)
