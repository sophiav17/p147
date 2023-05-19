from tkinter import*

root = Tk()

root.title("Encrytion With Ascii Code")
root.geometry("400x400")
root.configure(background="pink")

take_input = Entry(root)
take_input.place(relx = 0.5, rely = 0.4,  anchor = CENTER)

display_ascii_label = Label(root, text = "Name in Ascii: ")
display_ascii_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
display_encrypted_string_label = Label(root, text = "Encrypted Name: ")
display_encrypted_string_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def ascii_code() :
    get_input = take_input.get()
    
    for letter in get_input() :
        get_input(ord(letter))
        display_ascii_label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encryted = ascii - 1
        display_encrypted_string_label["text"] += str(chr(encryted))
        
btn = Button(root, text = "Display the Ascii Code and the Encrypted Value", command = ascii_code, bg = "dark blue", fg = "white")
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)        
root.mainloop()