from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3


#with sqlite3.connect('student_db.db') as db:
#	db.execute('DROP TABLE user')
with sqlite3.connect('student_db.db') as db:
    c= db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS admin(username TEXT NOT NULL PRIMARY KEY,password NOT NULL);')
    db.commit()

with sqlite3.connect('student_db.db') as db:
    d=db.cursor()
    d.execute('CREATE TABLE IF NOT EXISTS user(Name TEXT,Branch TEXT,Regd_no INTEGER NOT NULL,Semester INTEGER NOT NULL,'
              'CET01,CET02,CET03,CGPA REAL(1,2),GRADE,PRIMARY KEY(Regd_no,Semester));')
    db.commit()

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
            self.sem_c = StringVar()
            self.cet01 = StringVar()
            self.cet02 = StringVar()
            self.cet03 = StringVar()
            self.widgets()

        def login(self):
            with sqlite3.connect('student_db.db') as db:
                c= db.cursor()
            find_user =('SELECT * FROM admin WHERE username = ? and password =?')
            c.execute(find_user,[(self.username.get()),(self.password.get())])
            result =c.fetchall()
            if result :
                ms.showerror('Error!','Username already taken Try another.')
            else:
                ms.showinfo('success!','Account Created')
                self.log()
            insert = 'INSERT INTO admin(username,password) VALUES(?,?)'
            c.execute(insert,[(self.n_username.get()),(self.n_username.get())])
            db.commit()

        def login(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user = ('SELECT * FROM admin WHERE username = ? and password = ?')
                c.execute(find_user,[(self.username.get()),(self.password.get())])
                result = c.fetchall()
                if result:
                    self.logf.pack_forget()
                    self.log2()
                else:
                    ms.showerror('Username Not Found.')

        def addSub(self):
            if int(self.cet01.get()) >= 90:
                grade_point1= 10
            elif int(self.cet01.get()) >= 80 and int(self.cet01.get()) < 90:
                grade_point1= 9
            elif int(self.cet01.get()) >= 70 and int(self.cet01.get()) < 80:
                grade_point1= 8
            elif int(self.cet01.get()) >= 60 and int(self.cet01.get()) < 70:
                grade_point1= 7
            elif int(self.cet01.get()) >= 50 and int(self.cet01.get()) < 60:
                grade_point1= 6
            elif int(self.cet01.get()) >= 20 and int(self.cet01.get()) < 50:
                grade_point1= 5
            elif int(self.cet01.get()) < 20:
                grade_point1= 2
            if int(self.cet02.get()) >= 90:
                grade_point2= 10
            elif int(self.cet02.get()) >= 80 and int(self.cet02.get()) < 90:
                grade_point2= 9
            elif int(self.cet02.get()) >= 70 and int(self.cet02.get()) < 80:
                grade_point2= 8
            elif int(self.cet02.get()) >= 60 and int(self.cet02.get()) < 70:
                grade_point2= 7
            elif int(self.cet02.get()) >= 50 and int(self.cet02.get()) < 60:
                grade_point2= 6
            elif int(self.cet02.get()) >= 20 and int(self.cet02.get()) < 50:
                grade_point2= 5
            elif int(self.cet02.get()) < 20:
                grade_point2= 2
            if int(self.cet03.get()) >= 90:
                grade_point3= 10
            elif int(self.cet03.get()) >= 80 and int(self.cet03.get()) < 90:
                grade_point3= 9
            elif int(self.cet03.get()) >= 70 and int(self.cet03.get()) < 80:
                grade_point3= 8
            elif int(self.cet03.get()) >= 60 and int(self.cet03.get()) < 70:
                grade_point3= 7
            elif int(self.cet03.get()) >= 50 and int(self.cet03.get()) < 60:
                grade_point3= 6
            elif int(self.cet03.get()) >= 20 and int(self.cet03.get()) < 50:
                grade_point3= 5
            elif int(self.cet03.get()) < 20:
                grade_point3= 2

            calculated_cgpa = float(((grade_point1 + grade_point2 + grade_point3)*3)/9)

            if float(calculated_cgpa) >= 9.0:
                dict_grade= 'O'
            elif float(calculated_cgpa) >= 8.0 and float(calculated_cgpa) < 9.0:
                dict_grade= 'E'
            elif float(calculated_cgpa) >= 7.0 and float(calculated_cgpa) < 8.0:
                dict_grade= 'A'
            elif float(calculated_cgpa) >= 6.0 and float(calculated_cgpa) < 7.0:
                dict_grade= 'B'
            elif float(calculated_cgpa) >= 5.0 and float(calculated_cgpa) < 6.0:
                dict_grade= 'C'
            elif float(calculated_cgpa) >= 2.0 and float(calculated_cgpa) < 5.0:
                dict_grade= 'D'
            elif float(calculated_cgpa) < 2.0:
                dict_grade= 'F'
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user1=('SELECT Name,Branch FROM user WHERE Regd_no = ?')
                c.execute(find_user1,[(self.regd_no.get())])
                result1 = c.fetchall()
                nname=result1[0][0]
                bbranch=result1[0][1]
                find_user =('SELECT * FROM user WHERE Regd_no = ? and Semester =?')
                c.execute(find_user,[(self.regd_no.get()),(self.sem_c.get())])
                result = c.fetchall()
                if result:
                    self.log3f.pack_forget()
                    update= '''UPDATE user SET CET01=?,CET02=?,CET03=?,CGPA=?,GRADE=? WHERE Regd_no =? and Semester=?'''
                    c.execute(update ,( (self.cet01.get()),(self.cet02.get()),(self.cet03.get()),calculated_cgpa,dict_grade,(self.regd_no.get()),(self.sem_c.get())))
                    db.commit()
                else:
                    insert = '''INSERT INTO user(CET01,CET02,CET03,Regd_no,Semester,Name,Branch,GRADE,CGPA) VALUES (?,?,?,?,?,?,?,?,?) '''
                    c.execute(insert , ((self.cet01.get()),(self.cet02.get()),(self.cet03.get()),(self.regd_no.get()),(self.sem_c.get()),nname,bbranch,dict_grade,calculated_cgpa))
                    db.commit()
            self.log4()

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

        def log2(self):
            self.regd_no.set('')
            self.sem_c.set('')
            self.cr2f.pack_forget()
            self.head['text'] = 'Update Existing Data'
            self.log2f.pack()

        def cr2(self):
            self.n_name.set('')
            self.n_branch.set('')
            self.regd_no.set('')
            self.sem_c.set('')
            self.log2f.pack_forget()
            self.head['text'] = 'Add New Data'
            self.cr2f.pack()

        def log3(self):
            self.log5f.pack_forget()
            self.regd_no.set(self.regd_no.get())
            self.sem_c.set(self.sem_c.get())
            self.log2f.pack_forget()
            self.cet01.set(self.cet01.get())
            self.cet02.set(self.cet02.get())
            self.cet03.set(self.cet03.get())
            self.log4f.pack_forget()
            self.head['text'] = 'Add New Data'
            self.log3f.pack()

        def log4(self):
            self.head['text'] =''
            self.log3f.pack_forget()
            self.regd_no.set(self.regd_no.get())
            self.sem_c.set(self.sem_c.get())
            self.cet01.set(self.cet01.get())
            self.cet02.set(self.cet02.get())
            self.cet03.set(self.cet03.get())
            self.log4f.pack()

        def log5(self):
            self.head['text']=''
            self.log3f.pack_forget()
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user = ('SELECT * FROM user WHERE Regd_no=?')
                c.execute(find_user,[(self.regd_no.get())])
                rows = c.fetchall()
            self.log5f=Frame(self.master,padx=10,pady=10)
            tv=ttk.Treeview(self.log5f,columns=(1,2,3,4,5,6,7,8,9),show='headings',height='9')
            tv.grid()
            tv.heading(1,text='Name')
            tv.column('1',minwidth=0,width=100,stretch=NO)
            tv.heading(2,text='Branch')
            tv.column('2',minwidth=0,width=50,stretch=NO)
            tv.heading(3,text='Regd No')
            tv.column('3',minwidth=0,width=100,stretch=NO)
            tv.heading(4,text='SEM')
            tv.column('4',minwidth=0,width=50,stretch=NO)
            tv.heading(5,text='CET01')
            tv.column('5',minwidth=0,width=50,stretch=NO)
            tv.heading(6,text='CET02')
            tv.column('6',minwidth=0,width=50,stretch=NO)
            tv.heading(7,text='CET03')
            tv.column('7',minwidth=0,width=50,stretch=NO)
            tv.heading(8,text='CGPA')
            tv.column('8',minwidth=0,width=110,stretch=NO)
            tv.heading(9,text='GRADE')
            tv.column('9',minwidth=0,width=50,stretch=NO)
            Button(self.log5f,text='Go Back',command=self.closelog5).grid()
            Button(self.log5f,text='Close All Windows',command=self.closeAll).grid()
            for i in rows:
                tv.insert('','end',values=i)
                self.log5f.pack()

        def submit(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user =('SELECT * FROM user WHERE Name = ? and Branch =? and Regd_no =? and Semester =?')
                c.execute(find_user,[(self.name.get()),(self.branch.get()),(self.regd_no.get()),(self.sem_c.get())])
                result = c.fetchall()
                if result :
                    ms.showerror('Error!','Student already exists.')
                else:
                    ms.showinfo('success!','Student added')
                c.execute(INSERT ,[(self.n_name.get()),(self.n_name.get()),(self.n_regd_no.get()),(self.sem_c.get())])
                db.commit()
                self.log2()

        def submit(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user = ('SELECT Regd_no FROM user WHERE Regd_no =?')
            c.execute(find_user,[(self.regd_no.get())])
            result = c.fetchall()
            if result:
                self.log3()
            else:
                ms.showerror(''' Data doesn't exists ''')

        def new_student(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user =('SELECT Regd_no FROM user WHERE Regd_no =?')
                c.execute(find_user,[(self.n_regd_no.get())])
            if c.fetchall():
                ms.showerror('Student data already exists.')
            else:
                ms.showinfo('New student added Successfully.')
                insert = 'INSERT INTO user(Name,Branch,Regd_no,Semester) VALUES (?,?,?,?)'
                c.execute(insert,[(self.n_name.get()),(self.n_branch.get()),(self.n_regd_no.get()),(self.sem_c.get())])
                db.commit()
                self.log2()

        def new_user(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
            find_user =('SELECT username FROM admin WHERE username =?')
            c.execute(find_user,[(self.n_username.get())])
            if c.fetchall():
                ms.showerror('Username taken Try different one.')
            else:
                ms.showinfo('Account created Successfully.')
                insert = 'INSERT INTO admin (username,password) VALUES (?,?)'
                c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
                db.commit()
                self.log()

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
            Label(self.log2f,text='Semester Completed',pady =5,padx=5).grid(sticky=W)
            Entry(self.log2f,textvariable = self.sem_c,bd=5).grid(row = 1,column =1)
            Button(self.log2f,text='Add New Student',bd=3,padx=5,pady=5,command=self.cr2).grid()
            Button(self.log2f,text='UPDATE',bd=3,padx=5,pady=5,command=self.validateUpdateData).grid(row =2,column=1)

            self.cr2f =Frame(self.master,padx=10,pady=10)
            Label(self.cr2f,text='Enter new name  ',pady=5,padx=5).grid(sticky=W)
            Entry(self.cr2f,textvariable=self.n_name,bd=5).grid(row=0,column=1)
            Label(self.cr2f,text='Enter new branch',pady=5,padx=5).grid(sticky=W)
            Entry(self.cr2f,textvariable =self.n_branch,bd =5).grid(row=1,column=1)
            Label(self.cr2f,text='Enter new Regd. No',pady=5,padx=5).grid(sticky=W)
            Entry(self.cr2f,textvariable =self.n_regd_no,bd =5).grid(row=2,column=1)
            Label(self.cr2f,text='Semester Completed',pady =5,padx=5).grid(sticky=W)
            Entry(self.cr2f,textvariable = self.sem_c,bd=5).grid(row = 3,column =1)
            Button(self.cr2f,text='Add new student data',bd=3,padx=5,pady=5,command=self.validateSubmit).grid()
            Button(self.cr2f,text='Update existing student data',bd =3,padx=5,pady=5,command=self.log2).grid(row=4,column=1)

            self.log3f =Frame(self.master ,padx =10,pady=10)
            Label(self.log3f,text='   SUBJECT CODE:',pady=20,padx=5).grid(row=2,column=0)
            Label(self.log3f,text='MARKS:',pady=20,padx=5).grid(row=2,column =1)
            Label(self.log3f,text='\t CET 01',pady=5,padx=5).grid(sticky=W)
            Entry(self.log3f,textvariable=self.cet01,bd=5).grid(row=3,column=1)
            Label(self.log3f,text='\t CET 02',pady=5,padx=5).grid(sticky=W)
            Entry(self.log3f,textvariable =self.cet02,bd =5).grid(row=4,column=1)
            Label(self.log3f,text='\t CET 03',pady=5,padx=5).grid(sticky=W)
            Entry(self.log3f,textvariable =self.cet03,bd =5).grid(row=5,column=1)
            Button(self.log3f,text='SUBMIT',command=self.validateMarks,bd=3,padx=5,pady=5).grid(row=6,column=1)
            Button(self.log3f,text='Show Marksheet',command=self.log5).grid(row=7,column=1)

            self.log4f = Frame(self.master,padx=10,pady=10)
            Button(self.log4f,text='CGPA',command=self.calc_CG,bd=3,padx=5,pady=25).grid(row=0,column=0)
            Button(self.log4f,text='GRADE',command=self.grade,bd=3,padx=5,pady=25).grid(row=0,column=1)
            Button(self.log4f,text='ADD NEW',command=self.addNew,bd=3,padx=5,pady=25).grid(row=0,column=2)
            Button(self.log4f,text='CLOSE',command=self.closeAll,bd=3,padx=5,pady=25).grid(row=0,column=3)

            self.log5f = Frame(self.master,padx=10,pady=10)

        def closelog5(self):
            self.log5f.pack_forget()
            self.log3()

        def grade(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user1=('SELECT GRADE FROM user WHERE Regd_no = ? and Semester=?')
                c.execute(find_user1,[(self.regd_no.get()),(self.sem_c.get())])
                result1 = c.fetchall()
                ggrade=result1[0][0]
                ms.showinfo('Current GRADE is ',ggrade)

        def calc_CG(self):
            with sqlite3.connect('student_db.db') as db:
                c=db.cursor()
                find_user1=('SELECT CGPA FROM user WHERE Regd_no = ? and Semester=?')
                c.execute(find_user1,[(self.regd_no.get()),(self.sem_c.get())])
                result1 = c.fetchall()
                ccgpa=result1[0][0]
                ms.showinfo('Your CGPA is ',ccgpa)

        def addNew(self):
            self.cr2()
            self.log4f.pack_forget()

        def closeAll(self):
            root.destroy()

        def validateLogin(self):
            if self.n_username.get() == '':
                ms.showinfo('Information','Please enter some valid Username.')
            elif len(self.n_username.get()) <4:
                ms.showinfo('Information','Username must be of 4 characters.')
            elif self.n_password.get() == '':
                ms.showinfo('Information','Please enter some valid password.')
            elif len(self.n_password.get()) <8 :
                ms.showinfo('Information','Password must be of 8 characters.')
            else:
                self.new_user()

        def validateUpdateData(self):
            if int(self.sem_c.get()) >8 :
                ms.showerror('Information','Please Enter some valid no of semester completed')
            else:
                self.submit()

        def validateSubmit(self):
            if self.n_name.get() == '':
                ms.showinfo('Information','Please enter some valid Name.')
            elif self.n_branch.get() == '':
                ms.showinfo('Information','Please enter some valid Branch.')
            elif self.n_regd_no.get() == '':
                ms.showinfo('Information','Please enter some valid Registration Number.')
            elif len(self.n_regd_no.get()) !=10 :
                ms.showinfo('Information','Please enter some valid Registration Number.')
            elif self.sem_c.get() == '':
                ms.showerror('Information','Please Enter valid no of semester completed.')
            elif self.sem_c.get().isdigit() != True:
                ms.showerror('Information','Please Enter valid no of semester completed.')
            elif int(self.sem_c.get()) >8 :
                ms.showerror('Information','Please Enter some valid no of semester completed')
            elif self.n_regd_no.get().isdigit() != True:
                ms.showinfo('Information','Please enter some valid Registration Number.')
            else:
                self.new_student()

        def validateMarks(self):
            if self.cet01.get() =='':
                ms.showerror('Information','Please Enter valid input for CET01')
            elif self.cet01.get().isdigit() != True :
                ms.showerror('Information','Please Enter valid input for CET01')
            elif int(self.cet01.get()) >100 :
                ms.showerror('Information','Mark should be "0-100 " for CET01')
            elif self.cet02.get() =='':
                ms.showerror('Information','Please Enter valid input for CET02')
            elif self.cet02.get().isdigit() != True :
                ms.showerror('Information','Please Enter valid input for CET02')
            elif int(self.cet02.get()) >100 :
                ms.showerror('Information','Mark should be "0-100 " for CET02')
            elif self.cet03.get() =='':
                ms.showerror('Information','Please Enter valid input for CET03')
            elif self.cet03.get().isdigit() != True :
                ms.showerror('Information','Please Enter valid input for CET03')
            elif int(self.cet03.get()) >100 :
                ms.showerror('Information','Mark should be "0-100 " for CET03')
            else :
                self.addSub()

    if __name__ == '__main__' :
        root =Tk()
        root.title('Login Form')
        #root.geometry('1080x720')
        root.resizable(False,False)
        root.geometry('700x350+300+300')
        main(root)
        root.mainloop()