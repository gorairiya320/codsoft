from tkinter import *
import random

def generate_password():
    length = int(length_entry.get())
    password = ""

    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    small_alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char_list = ['@', '#', '$', '&', '*']

    small_int = small_var.get()
    capital_int = capital_var.get()
    special_int = special_var.get()

    if small_int:
        num_list.extend(small_alpha_list)

    if capital_int:
        num_list.extend(cap_alpha_list)

    if special_int:
        num_list.extend(special_char_list)

    for i in range(length):
        random_index = random.randint(0, len(num_list) - 1)
        password += num_list[random_index]

    password_var.set(password) 


root =Tk()
root.title("Password Generator")
root.geometry('380x440')
root.resizable(0,0)

root.configure(background='#728fce')


length_label = Label(root, text="Enter your required length for generate password:",fg='#ffffff',bg='#728fce')
length_label.pack()
length_label.config(font=('verdana',10,'bold'))


length_entry = Entry(root,width=50)
length_entry.pack(pady=(10,20))

# Checkboxes for character types variable
small_var = BooleanVar()
capital_var = BooleanVar()
special_var = BooleanVar()

smallAlpha_check = Checkbutton(root, text="Do you want to include small alphabets", variable=small_var,fg='black',bg='#728fce')
smallAlpha_check.pack(pady=(5,15))
smallAlpha_check.config(font=('verdana',8,'bold'))

capitalAlpha_check = Checkbutton(root, text="Do you want to include capital alphabets", variable=capital_var,fg='black',bg='#728fce')
capitalAlpha_check.pack(pady=(5,15))
capitalAlpha_check.config(font=('verdana',8,'bold'))

specialChar_check = Checkbutton(root, text="Do you want to include special character", variable=special_var,fg='black',bg='#728fce')
specialChar_check.pack(pady=(5,15))
specialChar_check.config(font=('verdana',8,'bold'))


generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=(10,20))

text_label = Label(root, text="The generated password is shown below:",fg='#ffffff',bg='#728fce')
text_label.pack()
text_label.config(font=('verdana',10,'bold'))

# Display generated password
password_var = StringVar()

password_label = Label(root, textvariable=password_var, bg='#728fce', fg='black')
password_label.pack()
password_label.config(font=('verdana',8,'bold'))

root.mainloop()
