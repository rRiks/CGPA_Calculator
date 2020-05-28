from tkinter import *
from tkinter import messagebox as ms
import sqlite3



with sqlite3.connect('quit.db') as db:
	c= db.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password NOT NULL);')
	db.commit()
	db.close()
	class main:
		def __init__(self,master):
			self.master =master
			self.username = StringVar()
			self.password = StringVar()
			self.n_username =StringVar()
			self.n_password = StringVar()
			self.widgets()
			
		def login(self):
			with sqlite3.connect('quit.db') as db:
				c= db.cursor()
			find_user =('SELECT FROM user WHERE username = ? and password =?')
			c.execute(find_user,[(self.username.get()),(self.password.get())])
			if result ==c.fetchall():
				ms.showerror('Error!','Username already taken Try another.')
			else:
				ms.showinfo('success!','Account Created')
				self.log()
			insert = 'INSERT INTO user(username,password) VALUES(?,?)'
			c.execute(insert,[(self.n_username.get()),(self.n_username.get())])
			db.commit()
			
		def login(self):
			with sqlite3.connect('quit.db') as db:
				c=db.cursor()
				find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
				c.execute(find_user,[(self.username.get()),(self.password.get())])
				result = c.fetchall()
				if result:
					self.logf.pack_forget()
					self.head['text'] = '\n Logged In'
					self.head['pady'] = 150
				else:
					ms.showerror('Username Not Found.')
		def new_user(self):
			with sqlite3.connect('quit.db') as db:
				c=db.cursor()
				
			find_user =('SELECT username FROM user WHERE username =?')
			c.execute(find_user,[(self.n_username.get())])
			if c.fetchall():
				ms.showerror('Username taken Try different one.')
			else:
				ms.showinfo('Account created Successfully.')
				self.log()
			insert = 'INSERT INTO user (username,password) VALUES (?,?)'
			c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
			db.commit()
		def log(self):
			self.username.set('')
			self.password.set('')
			self.crf.pack_forget()
			self.head['text'] = 'LOGIN'
			self.logf.pack()
		def cr(self):
			self.n_username.set('')
			self.n_password.set('')
			self.logf.pack_forget()
			self.head['text'] = 'Create Account'
			self.crf.pack()
			
		def widgets(self):
			self.head =Label(self.master,text ='LOGIN',pady= 10)
			self.head.pack()
			self.logf =Frame(self.master ,padx =10,pady=10)
			Label(self.logf,text='Username',pady =5,padx =5).grid(sticky =W)
			Entry(self.logf,textvariable= self.username,bd=5).grid(row =0,column=1)
			Label(self.logf,text='password',pady =5,padx=5).grid(sticky=W)
			Entry(self.logf,textvariable = self.password,bd=5).grid(row = 1,column =1)
			Button(self.logf,text ='Login',bd =3,padx =5,command=self.login).grid()
			Button(self.logf,text='Create Account',bd =3,padx=5,pady=5,command=self.cr).grid(row=2,column=1)
			self.logf.pack()
			
			self.crf =Frame(self.master,padx=10,pady=10)
			Label(self.crf,text='Enter new Username  ',pady=5,padx=5).grid(sticky=W)
			Entry(self.crf,textvariable=self.n_username,bd=5).grid(row=0,column=1)
			Label(self.crf,text='Enter new Password',pady=5,padx=5).grid(sticky=W)
			Entry(self.crf,textvariable =self.n_password,bd =5,show='*').grid(row=1,column=1)
			Button(self.crf,text='Create Account',bd=3,padx=5,pady=5,command=self.new_user).grid()
			Button(self.crf,text='Login into existing account',bd =3,padx=5,pady=5,command=self.log).grid(row=2,column=1)
	
	if __name__ == '__main__' :
		root =Tk()
		root.title('Login Form')
		root.geometry('400x350+300+300')
		main(root)
		root.mainloop()