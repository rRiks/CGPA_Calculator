from tkinter import *
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('signup_db.db') as db:
	c= db.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password NOT NULL);')
	db.commit()
	#db.close()

with sqlite3.connect('student_db.db') as db2:
	d=db2.cursor()
	d.execute('CREATE TABLE IF NOT EXISTS user(name TEXT,branch TEXT,regd_no INTEGER NOT NULL PRIMARY KEY);')
	db2.commit()
	#db2.close()

	class main:
		def __init__(self,master):
			self.master =master
			self.username = StringVar()
			self.password = StringVar()
			self.n_username =StringVar()
			self.n_password = StringVar()
			self.name = StringVar()
			self.branch = StringVar()
			self.regd_no = StringVar()
			self.n_name = StringVar()
			self.n_branch = StringVar()
			self.n_regd_no = StringVar()
			self.widgets()
			
		def login(self):
			with sqlite3.connect('signup_db.db') as db:
				c= db.cursor()
			find_user =('SELECT * FROM user WHERE username = ? and password =?')
			c.execute(find_user,[(self.username.get()),(self.password.get())])
			result =c.fetchall()
			if result :
				ms.showerror('Error!','Username already taken Try another.')
			else:
				ms.showinfo('success!','Account Created')
				self.log()
			insert = 'INSERT INTO user(username,password) VALUES(?,?)'
			c.execute(insert,[(self.n_username.get()),(self.n_username.get())])
			db.commit()
			#db.close()


			
		def login(self):
			with sqlite3.connect('signup_db.db') as db:
				c=db.cursor()
				find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
				c.execute(find_user,[(self.username.get()),(self.password.get())])
				result = c.fetchall()
				if result:
					self.logf.pack_forget()
					self.log2()
				else:
					ms.showerror('Username Not Found.')

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
		def submit(self):
			with sqlite3.connect('student_db.db') as db:
				c=db.cursor()
				find_user =('SELECT * FROM user WHERE name = ? and branch =? and regd_no =?')
				c.execute(find_user,[(self.name.get()),(self.branch.get()),(self.regd_no.get())])
				result = c.fetchall()
				if result :
					ms.showerror('Error!','Student already exists.')
				else:
					ms.showinfo('success!','Student added')
					self.log()
				c.execute(INSERT ,[(self.n_name.get()),(self.n_name.get()),(self.n_regd_no.get())])
				db.commit()
		def submit(self):
			with sqlite3.connect('student_db.db') as db:
				db=db.cursor()
				find_user = ('SELECT regd_no FROM user WHERE regd_no =?')
			c.execute(find_user,[(self.regd_no.get())])
			result = c.fetchall()
			if result:
				self.logf.pack_forget()
				self.head['text'] = '\n this is the file'
				self.head['pady'] = 150
			else:
				ms.showerror(''' Data doesn't exists ''')
		def new_student(self):
			with sqlite3.connect('student_db.db') as db:
				c=db.cursor()
				find_user =('SELECT regd_no FROM user WHERE regd_no =?')
				c.execute(find_user,[(self.regd_no.get())])
			if c.fetchall():
				ms.showerror('Student data already exists.')
			else:
				ms.showinfo('New student added Successfully.')
				self.log()
			insert = 'INSERT INTO user(name,branch,regd_no) VALUES (?,?,?)'
			c.execute(insert,[(self.n_name.get()),(self.n_branch.get()),(self.n_regd_no.get())])
			db.commit()
			self.log2()
		def log2(self):
			self.name.set('')
			self.branch.set('')
			self.regd_no.set('')
			self.cr2f.pack_forget()
			self.head['text'] = 'Update Existing Data'
			self.log2f.pack()
		def cr2(self):
			self.n_name.set('')
			self.n_branch.set('')
			self.regd_no.set('')
			self.log2f.pack_forget()
			self.head['text'] = 'Add New Data'
			self.cr2f.pack()
		def new_user(self):
			with sqlite3.connect('signup_db.db') as db:
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
		def widgets(self):
			self.head =Label(self.master,text ='LOGIN',pady= 10)
			self.head.pack()
			self.logf =Frame(self.master ,padx =10,pady=10)
			Label(self.logf,text='Username',pady =5,padx =5).grid(sticky =W)
			Entry(self.logf,textvariable= self.username,bg='white',fg='black',bd=5).grid(row =0,column=1)
			Label(self.logf,text='password',pady =5,padx=5).grid(sticky=W)
			Entry(self.logf,textvariable = self.password,show='*',bg='white',fg='black',bd=5).grid(row = 1,column =1)
			Button(self.logf,text ='Login',bg='blue',fg='black',bd =3,padx =5,command=self.login).grid(row=2,column=1)
			Button(self.logf,text='Create Account',bg='green',fg='black',bd =3,padx=5,pady=5,command=self.cr).grid(row=3,column=1)
			self.logf.pack()
			
			self.crf =Frame(self.master,padx=10,pady=10)
			Label(self.crf,text='Enter new Username  ',pady=5,padx=5).grid(sticky=W)
			Entry(self.crf,textvariable=self.n_username,bd=5).grid(row=0,column=1)
			Label(self.crf,text='Enter new Password',pady=5,padx=5).grid(sticky=W)
			Entry(self.crf,textvariable =self.n_password,bd =5,show='*').grid(row=1,column=1)
			Button(self.crf,text='Create Account',bd=3,padx=5,pady=5,command=self.validateLogin).grid()
			Button(self.crf,text='Login into existing account',bd =3,padx=5,pady=5,command=self.log).grid(row=2,column=1)


			self.log2f =Frame(self.master ,padx =10,pady=10)
			Label(self.log2f,text='Registration No',pady =5,padx=5).grid(sticky=W)
			Entry(self.log2f,textvariable = self.regd_no,bd=5).grid(row = 0,column =1)
			Button(self.log2f,text='Add New Student',bd=3,padx=5,pady=5,command=self.cr2).grid()
			Button(self.log2f,text='UPDATE',bd=3,padx=5,pady=5,command=self.submit).grid(row =1,column=1)
			#self.log2f.pack()
			self.cr2f =Frame(self.master,padx=10,pady=10)
			Label(self.cr2f,text='Enter new name  ',pady=5,padx=5).grid(sticky=W)
			Entry(self.cr2f,textvariable=self.n_name,bd=5).grid(row=0,column=1)
			Label(self.cr2f,text='Enter new branch',pady=5,padx=5).grid(sticky=W)
			Entry(self.cr2f,textvariable =self.n_branch,bd =5).grid(row=1,column=1)
			Label(self.cr2f,text='Enter new Regd. No',pady=5,padx=5).grid(sticky=W)
			Entry(self.cr2f,textvariable =self.n_regd_no,bd =5).grid(row=2,column=1)
			Button(self.cr2f,text='Add new student data',bd=3,padx=5,pady=5,command=self.validateSubmit).grid()
			Button(self.cr2f,text='Update existing student data',bd =3,padx=5,pady=5,command=self.log2).grid(row=3,column=1)

		def validateLogin(self):
			if self.n_username.get() == '':
				ms.showinfo('Information','Please enter some valid Username.')
			elif len(self.n_username.get()) <4:
				ms.showinfo('Information','Username must be of 4 characters.')

			elif self.n_password.get() == '':
				ms.showinfo('Information','Please enter some valid password.')
			elif len(self.n_password.get()) !=8 :
				ms.showinfo('Information','Password must be of 8 characters.')
			else:
				self.new_user()
		def validateSubmit(self):
			if self.n_name.get() == '':
				ms.showinfo('Information','Please enter some valid Name.')
			elif self.n_branch.get() == '':
				ms.showinfo('Information','Please enter some valid Branch.')
			elif self.n_regd_no.get() == '':
				ms.showinfo('Information','Please enter some valid Registration Number.')
			elif len(self.n_regd_no.get()) !=10 :
				ms.showinfo('Information','Please enter some valid Registration Number.')
			else:
				self.new_student()



	if __name__ == '__main__' :
		root =Tk()
		root.title('Login Form')
		root.geometry('400x350+300+300')
		main(root)
		root.mainloop()