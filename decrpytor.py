import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    try:
        cipher = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted_content = file.read()
        decrypted_content = cipher.decrypt(encrypted_content)

        original_name = file_path.replace(".enc", "")
        with open(original_name, "wb") as file:
            file.write(decrypted_content)
        os.remove(file_path)
    except Exception as e:
        pass

def decrypt_directory(directory, key):
    decrypted_files = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".enc"):
                decrypt_file(os.path.join(root, file), key)
                decrypted_files += 1

    if decrypted_files > 0:
        messagebox.showinfo("Decryption Complete", f"Successfully decrypted {decrypted_files} files.")
    else:
        messagebox.showwarning("No Encrypted Files", "No encrypted files were found in the selected directory.")

def start_decryption():
    key_input = entry_key.get().encode()
    key_hash = hashlib.sha256(key_input).hexdigest()

    try:
        with open("encryption.key", "r") as key_file:
            stored_hash = key_file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found.")
        return

    if key_hash != stored_hash:
        messagebox.showerror("Incorrect Key", "The entered key is invalid.")
        return

    directory = filedialog.askdirectory(title="Select the folder to decrypt")
    if directory:
        messagebox.showinfo("Starting Decryption", "The decryption process has started. Please wait...")
        root.update()
        decrypt_directory(directory, key_input)

def show_decryption_gui():
    global entry_key, root
    root = tk.Tk()
    root.title("File Decryptor")
    root.geometry("500x250")
    root.configure(bg="#1e1e1e")

    title_label = tk.Label(root, text="🔓 File Decryptor", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
    title_label.pack(pady=(10, 5))

    info_label = tk.Label(root, text="Enter the decryption key:\nThen select the folder you want to decrypt.\nDuring decryption, the program may appear unresponsive.", 
                          font=("Arial", 12), fg="lightgray", bg="#1e1e1e", wraplength=450)
    info_label.pack()

    entry_key = tk.Entry(root, width=40, show="*", font=("Arial", 12))
    entry_key.pack(pady=10)

    button_decrypt = tk.Button(root, text="🔑 Decrypt Files", font=("Arial", 12, "bold"),
                               fg="white", bg="#ff4500", activebackground="#cc3700",
                               command=start_decryption, width=25, height=2)
    button_decrypt.pack(pady=15)

    root.mainloop()

if __name__ == '__main__':
    show_decryption_gui()
