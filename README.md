# 🛡️ Priv4te Ransomware

**⚠️ Disclaimer: This project is for educational and research purposes only. Do not use it for illegal activities. The author is not responsible for any misuse of this code.**

![Banner](https://github.com/user-attachments/assets/84033b10-c7de-4e92-93f0-813db0a5505a)

![image](https://github.com/user-attachments/assets/84033b10-c7de-4e92-93f0-813db0a5505a)

![image](https://github.com/user-attachments/assets/6b505368-1a38-4a5f-8222-ba6a0f0c5cb4)

## 📌 About
This repository contains a **ransomware simulation script** designed for **educational purposes**. The objective is to demonstrate how ransomware works and how security professionals can analyze and mitigate such threats.

## 🚀 Features
- Generates an encryption key and encrypts user files.
- Sends notifications via Telegram (requires API setup).
- Modifies system wallpaper with a simulated ransom note.
- Disables Task Manager to mimic real-world ransomware behavior.

## 🛠️ Usage
**Do not run this script on a system with real data.** If used in a controlled environment (like a virtual machine), proceed with caution.

### 1️⃣ **Setup a Virtual Environment**
For security reasons, it is recommended to test this script in an **isolated virtual machine**.
- Use **VirtualBox**, **VMware**, or **Hyper-V**.
- Create **snapshots** before running the script to restore the system easily.
- Use **Windows Sandbox** for a quick testing environment.

### 2️⃣ **Disable Antivirus & Windows Defender (for testing purposes)**
Some security software may block execution:
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

### 3️⃣ **Clone the repository**
```sh
git clone https://github.com/17tayyy/priv4te
cd priv4te
```

### 4️⃣ **Install dependencies**
```sh
pip install -r requirements.txt
```

### 5️⃣ **Generate test files** (for encryption testing)
Run the following **PowerShell script** to create dummy files in common user directories:
```powershell
powershell -ExecutionPolicy Bypass -File setup-for-testing.ps1
```
This will generate **test files** in:
- Desktop
- Documents
- Downloads
- Pictures
- External Drives

### 6️⃣ **Run the script**
#### Encrypt files:
```sh
python3 priv4te.py"
```

## ✅ TODO

- Implement a **Decryptor**
- Replace **Fernet** with **AES-256** for stronger encryption
- Improve **Antivirus evasion techniques**
- Target **databases** (`.sql`, `.mdb`, `.db`) as a priority
- Implement **Data exfiltration** techniques
- Self-propagation in **local networks**
