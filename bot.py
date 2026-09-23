import time
import requests

ROOM_ID = "37uqc814uu"

REFRESH_TOKEN = "AMf-vByw8FAmxA_6KlZW4QaAk95y2eAlwQctqs6Xm17WLhbBH18CG-pn8pSGIWytVm--_SxTByiHjfISm_t5EX4ruRO-YyJ2uUYTiAHrUXgvVftoO_RneW8SGignHtpxJPAWqg02GZ1EA3el6wGuyDDQRS3AJd0QYc9FyVyoEW8ok3raFEG7Zf1nSo7DKrtWhFqcxPaIILPsja1jZfqLPIB4QV3my1VXy-eN6SlO1XvBpyLDbAa9HaebR4ZE4YMP-471Gy02G9cqaIzjDEe65hobYXdn1ip5gLslVPtuxujbBub1ud4T7_mmmtDBTNeJykQq-BfDGM6pXAo_n7vXfqGicUKoDVe5wP4R3MwE8qB3HdCSUtRS9-jU6XsAtaZBLy8dqXz4VuHvFJYptOmA7Kxt-G-h7jliRLo9mwh_pVLvTGAdNJPvLf8"
API_KEY = "AIzaSyAz51581sbr0pX9Q5uQwdTnNMA80"

CF_CLEARANCE = "7uXUmoaNU8Dr8A6HRa9uSW7vx3g9Yr30aAqwciv4K70-1790174377-1.2.1.1-0Xit_z3JPvX8Gx.JaWAAo0r0ERieUae_7llwwCTMUPM IIXF09aT.ehelaB0CzsRk30H9ErOGA_0rVAhF0fKualu9vxF27KU_FtLaNdLohfkIIA.Ifu_aLaMiWKVoH.wjZcqoWlzgF_35U20DFF243RBxi dvMbBjdjrNxl3OYFvdk5fG86jJYFbkPel05Dy2xDG1kanvWdUCv8HuseGLnVyXblwyt18D60HHDwTZA9U7xuJLq2.yUXfsWYo0MyiK.4V mF1G1bjy4QIlt7HT4mld09gfbwfD_5KMepOLGH98hzHbMZnG.Jk23hDithKDU.Jofl5Zd37fErkGBrs6v8lbNs.up4aUE14_L.MLuX7PLCSI"

def refresh_access_token(refresh_token):
    url = f"https://securetoken.googleapis.com/v1/token?key={API_KEY}"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            print("🔄 புதிய Access Token வெற்றிகரமாகப் பெறப்பட்டது!")
            return data.get("id_token")
        else:
            print(f"⚠️ Token Refresh செய்ய முடியவில்லை: {response.text}")
            return None
    except Exception as e:
        print(f"Network Error in Refresh: {e}")
        return None

def send_chat_message(token, message):
    url = f"https://api.groic.in/api/v1/room/{ROOM_ID}/chat"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://groic.in",
        "Referer": f"https://groic.in/room/{ROOM_ID}",
        "Authorization": f"Bearer {token}",
        "Cookie": f"cf_clearance={CF_CLEARANCE}"
    }
    try:
        res = requests.post(url, json={"message": message}, headers=headers)
        if res.status_code in [200, 201]:
            print(f"✅ [{ROOM_ID}] மெசேஜ் அனுப்பப்பட்டது: '{message}'")
            return True
        else:
            print(f"⚠️ Status: {res.status_code} - {res.text}")
            return False
    except Exception as e:
        print(f"Chat Error: {e}")
        return False

print("🤖 24/7 Cloud Bot இயக்கப்படுகிறது...")
current_token = None

while True:
    if not current_token:
        current_token = refresh_access_token(REFRESH_TOKEN)
        
    if current_token:
        success = send_chat_message(current_token, "Welcome Bot Active 🚀")
        if not success:
            current_token = None 
    else:
        print("❌ டோக்கன் கிடைக்கவில்லை. 30 நொடிகள் கழித்து மீண்டும் முயற்சிக்கிறது...")
        
    time.sleep(60)
