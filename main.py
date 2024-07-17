from tkinter import *
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox
from password_generator import generate_pass
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
   random_pw = generate_pass()
   password_label_textbox.insert(0,random_pw)
   password=password_label_textbox.get()

   password_label_textbox.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    my_file = Path("data.json")

    value_website = website_name_textbox.get()
    value_email = email_username_textbox.get()
    value_pass=password_label_textbox.get()
    new_data={
        value_website.lower():{
            "email":value_email,
            "password":value_pass

        }
    }
    
    if len(value_website) != 0 and len(value_pass) != 0:
        is_ok = messagebox.askokcancel(title="Password Manager", message =f"Do you like to save this data? \n Website: {value_website} \n Email/Username : {value_email} \n Password: {value_pass}")
        if is_ok:
            try:
                with open(my_file,"r") as data_file:
                    #read the data
                    data= json.load(data_file)

                    #update data
                    data.update(new_data)
                    messagebox.showinfo(title="Password Manager", message ="The credentials were successfully saved!")

                #save data    
                with open(my_file, 'w') as data_file:
              
                    json.dump(data,data_file,indent=4)
            except FileNotFoundError:
                messagebox.showinfo(title="Password Manager", message ="File not found! File is created")
                with open(my_file, 'w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            finally:
                website_name_textbox.delete(0, END)
                password_label_textbox.delete(0, END)    
    else:
        messagebox.showinfo(title="Oppps!", message ="Please don't leave any blank fields!")


def find_password():
    website = website_name_textbox.get().lower()
    
    try:
        with open("data.json","r") as data:
            data= json.load(data)
            email=data[website]['email']
            password=data[website]['password']

            messagebox.showinfo(title=website, message =f"Email:{email}\nPassword: {password}")
    except KeyError:
        messagebox.showinfo(title=website, message =f"Credentials for {website} not found")
    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager", message =f"File not Found!")
        save_file()
         
          
        
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=0)

#label
website_name_label = Label(text="Website: ")
website_name_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#entries
website_name_textbox = Entry(width = 53)
website_name_textbox.focus()
website_name_textbox.grid(column=1, row=1, columnspan=2)

email_username_textbox = Entry(width = 53)
email_username_textbox.insert(0,"email@email.com")
email_username_textbox.grid(column=1, row=2, columnspan=2)


password_label_textbox = Entry( width = 53)
password_label_textbox.grid(row=3,column=1,columnspan=2)

# #button
generatepass_button = Button( width = 16, text="Generate Password", command=password_generator)
generatepass_button.grid(row=3, column=2,)

add_button = Button(width = 44, text="Add", command=save_file)
add_button.grid(column=1,row=4,  columnspan=2)

search_button = Button( width = 16, text="Search", command=find_password)
search_button.grid(row=1, column=2,columnspan=3)




window.mainloop()

