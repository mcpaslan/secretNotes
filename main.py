from tkinter import *
from tkinter import messagebox
import base64

window = Tk()
window.minsize(350, 450)
window.title("Secret Notes")

title_info_label = Label(window, text="Enter Your Title", font=('arial', 15, "normal"))
title_info_label.pack()

title_entry = Entry(window, width=30)
title_entry.pack()

secret_label = Label(window, text="Enter Your Secret", font=('arial', 15, "normal"))
secret_label.pack()

input_text = Text(height=15, width=30)
input_text.pack()

master_secret = Label(window, text="Enter master key", font=('arial', 15, "normal"))
master_secret.pack()

master_secret_key = Entry(window, width=30)
master_secret_key.pack()

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def creating_text_file():
    title = title_entry.get()
    master_secret = master_secret_key.get()
    message = input_text.get(1.0, END)
    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error",message="Please enter all information.")
    else:
        #encrypt
        message_encrypted = encode(master_secret, message)
        try:
            with open("secret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open ("secret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,END)
            master_secret_key.delete(0,END)
            input_text.delete("1.0",END)

def decrypt_password():
    master_secret = master_secret_key.get()
    message_encrypted = input_text.get(1.0, END)
    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error", message="Please enter encrypted text.")


encrypt_button = Button(text="Save & Encrypt", command= creating_text_file)
encrypt_button.pack()

decrypt_button = Button(text="Decrypt", command=decrypt_password)
decrypt_button.pack()

window.mainloop()