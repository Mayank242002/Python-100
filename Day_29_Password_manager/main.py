from email import message
from tkinter import *
from tkinter import messagebox
import random


def save():
    website_info=website_entry.get()
    email_info=email_username_entry.get()
    password_info=password_entry.get()  
    final_text=website_info+" | "+email_info+" | "+password_info+"\n"

    if ((len(website_info)==0) | (len(password_info)==0)):
        messagebox.showwarning(title="Opps",message="Please don't leave any fields empty")
   
    else:
         is_ok=messagebox.askokcancel(title=website_info,message=f"These are the details entered:\nEmail:{email_info} \nPassword: {password_info} \nIs it okay to save?")
         if (is_ok):
            file=open("Day_29_Password_manager/data.txt","a")
            file.write(final_text)
            file.close()
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')


def password_generator():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#',"$",'%',"&",'(',')','*','+']

    n_letters=random.randint(8,10)
    n_symbols=random.randint(2,4)
    n_numbers=random.randint(2,4)
    password=[]
    for i in range(n_letters):
        password.append(letters[random.randint(0,len(letters)-1)])
    for i in range(n_symbols):
        choice_index=random.randint(0,len(password)-1)
        password.insert(choice_index,symbols[random.randint(0,len(symbols)-1)])
    for i in range(n_numbers):
        choice=random.randint(0,len(password)-1)
        password.insert(choice,numbers[random.randint(0,len(numbers)-1)])
   
    final="".join(password)
    password_entry.insert(0,final)
   



   

   

window=Tk()
window.title("Password Manager")
window.minsize(width=500,height=500)
window.config(padx=40,pady=40)


canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="Day_29_Password_manager/logo1.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
website_label.config(padx=16,pady=16)

website_entry=Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_username_label=Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)
email_username_label.config(padx=16,pady=16)

email_username_entry=Entry(width=43)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"msngi24july@gmail.com")
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_label.config(padx=14,pady=16)

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

generate_password_button=Button(text="Generate Password",highlightthickness=0,command=password_generator)
generate_password_button.grid(column=2,row=3)

add_button=Button(text="Add",highlightthickness=0,width=38,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()

