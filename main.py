from tkinter import *

window = Tk()
window.minsize(350, 450)
window.title("Secret Notes")

myTitle = Label(window, text="Enter Your Title", font=('arial', 15, "normal"))
myTitle.pack()

titleEntry = Entry(window, width=30)
titleEntry.pack()

secret_label = Label(window, text="Enter Your Secret", font=('arial', 15, "normal"))
secret_label.pack()

myText = Text(height=15, width=30)
myText.pack()

masterKey = Label(window, text="Enter master key", font=('arial', 15, "normal"))
masterKey.pack()

keyEntry = Entry(window, width=30)
keyEntry.pack()


def creating_text_file():
    save_file = open("Accounts.txt", "w")
    title = titleEntry.get()
    save_file.write(title)
    save_file.write("\n")
    secret_File = myText.get(1.0, END)
    save_file.write(secret_File)
    save_file.write("\n")
    save_file.close()

encryptButton = Button(text="Save & Encrypt", command= creating_text_file)
encryptButton.pack()

decryptButton = Button(text="Decrypt")
decryptButton.pack()

window.mainloop()
