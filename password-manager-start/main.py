import json
from tkinter import *  # imports all classes and constants not like methods message box
from tkinter import messagebox
from random import randint,choice
# to add text to the clipboard
import pyperclip
import _json

#---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   nr_letters = randint(8, 10)
   nr_symbols = randint(2, 4)
   nr_numbers = randint(2, 4)

   password_list = []

   password1=[choice(letters) for char in range(nr_letters)]
   password2=[choice(symbols) for char in range(nr_symbols)]
   password3=[choice(numbers) for char in range(nr_numbers)]
   password_list=password1+password3+password2
   #print(password_list)
   password=''.join(password_list)
  #print(f"Your password is: {password}")
   e3.insert(0,password)
   # now you can paste the generated password anywhere you want using ctrl+V
   pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# ---------------------------- UI SETUP ---------------------------------#
window=Tk()
window.title('Password_manager')
window.config(padx=100,pady=50)
window.minsize(width=500 ,height=450)
pic=PhotoImage(file='logo.png')
canvas=Canvas(width=200, height=200)
canvas.create_image(100,100,image=pic)
canvas.grid(row=1, column=1 , rowspan=10)
l1=Label(text='Website:').grid(row=11,column=0)
e1=Entry(width=30)
e1.grid(row=11,column=1)
e1.focus()
l2=Label(text='Email/Username')
l2.grid(row=12,column=0)
e2=Entry(width=40)
e2.grid(row=12,column=1,columnspan=2)
e2.insert(0,"vg2024@srmist.edu.in")
l3=Label(text="Password")
l3.grid(row=13, column=0)
e3=Entry(width=23)
e3.grid(row=13,column=1)

def add_data():
    website=e1.get()
    username=e2.get()
    password=e3.get()
    new_data={
        website:{
            'username/mail':username,
            'password':password
        }
    }
    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title='oops',message="you haven't entered some of the fields")

    else:
       #is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered:\n username/mail:{username}\n password:{password}")
       #if is_ok:
       try:
            with open('data.json' , mode='r') as f:
           #reading old data
                data=json.load(f)
           #updating old data with new data
                data.update(new_data)
         # write the updated data to the file
       except FileNotFoundError:
             with open('data.json' , mode='w') as f:
                json.dump(new_data,f , indent=4)
       else:
             with open('data.json' , mode='w') as f:
                json.dump(data,f , indent=4)
       e1.delete(0,END)
       e3.delete(0,END)
def serach_web():
    web=e1.get()
    try:
        with open('data.json') as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='error' , message='no data file found')
    else:
        if web in data:
            user=data[web]['username/mail']
            passw=data[web]['password']
            messagebox.showinfo(title='found', message=f'username/mail : {user}\npassword={passw}')
        else:
            messagebox.showinfo(title='not found' , message= 'sorry, there is no file match found')
b1=Button(text='Generate password',highlightthickness=0 , command=password_generator)
b1.grid(row=13,column=2)
b2=Button(text='ADD',width=34,highlightthickness=0 , command=add_data)
b2.grid(row=14,column=1,columnspan=2)
b3=Button(text='Search',command=serach_web)
b3.grid(row=11, column=2)

window.mainloop()


