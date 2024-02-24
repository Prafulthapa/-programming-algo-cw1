from tkinter import *
import base64

def DECRYPT():
    password = code.get()

    if password == "1234":
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")

        try:
            base64_bytes = base64.b64decode(encode_message)
            DECRYPTED = base64_bytes.decode("ascii")

            screen1 = Toplevel(screen)
            screen1.title("decryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#28a745")

            Label(screen1, text="DECRYPTED", font="arial", fg="white", bg="#28a745").place(x=10, y=0)
            text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, DECRYPTED)

        except base64.binascii.Error:
            messagebox.showerror("Error", "Invalid Base64 encoded message")

def ENCRYPT():
    password = code.get()

    if password == "1234":
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        ENCRYPTED = base64_bytes.decode("ascii")

        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, ENCRYPTED)

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("475x498")
    screen.title("PacketApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for Encryption and Decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 18", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=10, width=355, height=100)

    Label(text="Enter secret key for Encryption and Decryption", fg="Black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=20, bd=0, font=("arial", 25), show="*").place(x=10, y=195)

    Button(text="ENCRYPT", height="2", width=23, bg="red", fg="white", bd=0, command=ENCRYPT).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="green", fg="white", bd=0, command=DECRYPT).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
