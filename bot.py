import requests
from eth_account import Account
from colorama import init, Fore, Style
import time
from fake_useragent import UserAgent

init(autoreset=True)

ua = UserAgent()
# jangan di maling bang 
def print_banner():
    banner = f"""
    {Fore.YELLOW}==========================================
    |                                        |
    |  {Fore.GREEN}WELCOME TO AIRPUMP.AI AUTO REFERRAL{Fore.YELLOW}   |
    |          @AirdropFamilyIDN             |
    {Fore.YELLOW}==========================================
    """
    print(banner)

def register(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBE4cLaS8quuc59LYuS2aW898K1dB-b82w"
    payload = {
        "returnSecureToken": True,
        "email": email,
        "password": password,
        "clientType": "CLIENT_TYPE_WEB"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        #"Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "Origin": "https://refer.aipump.ai",
        "User-Agent": ua.chrome,
        "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["idToken"]
    else:
        print("Failed to register")
        return None

def set_username(idToken, username):
    url = "https://europe-west1-aipump-420d2.cloudfunctions.net/users/set-username"
    payload = {
        "username": username
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": idToken,
        "Accept": "*/*",
        #"Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "Origin": "https://refer.aipump.ai",
        "User-Agent": ua.chrome,
        "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Username set successfully")
    else:
        print("Failed to set username")

def add_wallet(idToken, wallet):
    url = "https://europe-west1-aipump-420d2.cloudfunctions.net/users/add-wallet"
    payload = {
        "wallet": wallet
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": idToken,
        "Accept": "*/*",
        #"Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "Origin": "https://refer.aipump.ai",
        "User-Agent": ua.chrome,
        "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Wallet added successfully")
    else:
        print("Failed to add wallet")

def paste_kode_reff(idToken, referredBy):
    url = "https://europe-west1-aipump-420d2.cloudfunctions.net/users/set-referred-by"
    payload = {
        "referredBy": referredBy
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": idToken,
        "Accept": "*/*",
        #"Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
        "Origin": "https://refer.aipump.ai",
        "User-Agent": ua.chrome,
        "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Referral code set successfully")
    else:
        print("Failed to set referral code")

def get_random_username():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()
        username = data['results'][0]['login']['username']
        return username
    else:
        print("Failed to get random username")
        return None

print_banner()
password = "Dewareff123@"

referredBy = input("Masukkan kode referral contoh: sadamganteng : ")

jumlah_iterasi = int(input("Mau berapa Reff Bosku? : "))

for i in range(jumlah_iterasi):
    print(f"\nProses Referral {i+1}/{jumlah_iterasi}")
    username = get_random_username()
    if username:
        email = f"{username}@gmail.com"
        idToken = register(email, password)
        if idToken:
            set_username(idToken, username)
            acct = Account.create()
            wallet = acct.address
            add_wallet(idToken, wallet)
            paste_kode_reff(idToken, referredBy)

            acct = Account.create()
            wallet = acct.address
            private_key = acct._private_key.hex()[2:]

            with open("akun.txt", "a") as file:
                file.write(f"Address: {wallet}\n")
                file.write(f"Privatekey: {private_key}\n")
    
    time.sleep(5)