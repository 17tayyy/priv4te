# 🛡️ Priv4te Ransomware

**⚠️ Disclaimer: This project is for educational and research purposes only. Do not use it for illegal activities. The author is not responsible for any misuse of this code.**

## 📌 About
This repository contains a **ransomware simulation script** designed for **educational purposes**. The objective is to demonstrate how ransomware works and how security professionals can analyze and mitigate such threats.

## 🚀 Features
- Generates an encryption key and encrypts user files.
- Sends notifications via Telegram (requires API setup).
- Modifies system wallpaper with a simulated ransom note.
- Disables Task Manager to mimic real-world ransomware behavior.

## 🛠️ Usage
**Do not run this script on a system with real data.** If used in a controlled environment (like a virtual machine), proceed with caution.

1. Clone the repository:

  ```sh
  git clone https://github.com/17tayyy/priv4te
  cd priv4te
  ```

2. Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

3. Run the script:
  ```sh
  python priv4te.py
  ```

## ✅ TODO

  -  AES-256 instead of Fernet.
  -  Antivirus evasion.
  -  Database priority (.sql, .mdb, .db).
  -  Data exfiltration
  -  Self-propagation on local networks (infecting other PCs).
