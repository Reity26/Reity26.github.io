import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector  

#title of the page
def login_screen():
    global root,un,pw,bg
    root=Tk()
   
    root.geometry("700x700+0+0")
    root.title('Telephone directory')
    bg=PhotoImage(file="C:\\Users\\Reity\\OneDrive\\Desktop\\telephone directory login.png")
    labelx = Label(root,image = bg)
    labelx.place(x=0,y=0)
    heading=Label(root,text='Sign In',fg='white', bg='black', font=('roman',24,'bold'))
    heading.place(x=340,y=10)
    un=Entry(root,width=30)
    un.place(x=280,y=125)
    un.insert(0,'Username')
    un.bind('<FocusIn>',on_enter_user)
    un.bind('<FocusOut>',on_leave_user)
    pw=Entry(root,width=30)
    pw.place(x=280,y=185)
    pw.insert(0,'Password')
    pw.bind('<FocusIn>',on_enter_password)
    pw.bind('<FocusOut>',on_leave_password)   
    label1=tk.Label(root,text="username",font=("roman",22),fg="white",height=1,bg="black")
    label1.place(x=140,y=110)
    label2=tk.Label(root,text="password",font=("roman",22),fg="white",height=1,bg="black")
    label2.place(x=140,y=170)
    Button(width=20,pady=7, text='SIGN IN', bg='blue', fg='white', command=signin).place(x=275,y=230)



def on_enter_user(e):
    un.delete(0,'end')
def on_leave_user(e):
    name=un.get()
    if name=='':
        un.insert(0,'Username')

#--------------------------------------------------------------------------------------------

def on_enter_password(e):
   pw.delete(0,'end')
def on_leave_password(e):
    name=pw.get()
    if name=='':
        pw.insert(0,'Password')    


def signin():
    global un,pw
    username=un.get()
    password=pw.get()
    if username=='' or password=='':
        messagebox.showerror("Invalid", "Error")  
    elif username=='reity':
        if password=='rei26*':
            root.destroy()
            homepage()
        else:
            messagebox.showerror("Invalid", "Invalid Password")    
    elif username=='dia':
        if password=='dia17#':
            root.destroy()
            homepage()
        else:    
            messagebox.showerror("Invalid", "Invalid Password")
    elif username=='nishitha':
        if password=='nis01^':
            root.destroy()
            homepage()
        else:
            messagebox.showerror("Invalid", "Invalid password")
    else:
        messagebox.showerror("Error","incorrect user")
        
def homepage():
    global root, root1, bg
    root1=tk.Tk()
    root1.title("Home Page")
    root1.geometry("700x700+0+0")
    img1=PhotoImage(file="C:\\Users\\Reity\\OneDrive\\Desktop\\home.png")
    label1=Label(root1,image=img1)
    label1.place(x=0,y=0)
    btn1=Button(root1,borderwidth=0,text='Inserting Record', font=('roman',20), fg='white', bg='purple',command = record_insert)
    btn1.place(x=50,y=100)
    
    btn3=Button(root1,borderwidth=0,text='Display All Records', font=('roman',20), fg='white', bg="purple",command = record_display)
    btn3.place(x=50, y=200)

    btn4=Button(root1, borderwidth=0,text='Search By Name', font=('roman',20), fg='white', bg='purple',command = search_by_name)
    btn4.place(x=50, y=300)

    btn5=Button(root1,borderwidth=0,text='Search By City', font=('roman', 20), fg='white', bg='purple',command = search_by_city)
    btn5.place(x=50,y=400)

    btn6=Button(root1, borderwidth=0,text='Search By First Letter', font=('roman',20), fg='white', bg='purple',command = search_by_fletter)
    btn6.place(x=50, y=500)

    btn7=Button(root1, borderwidth=0,text='Update', font=('roman',20), fg='white', bg='purple', command = updating)
    btn7.place(x=500, y=100)

    btn8=Button(root1, borderwidth=0,text='Delete', font=('roman',20), fg='white', bg='purple',command = delete)
    btn8.place(x=500, y=200)

    btn9=Button(root1, borderwidth=0,text='About', font=('roman',20), fg='white', bg='purple', command = About)
    btn9.place(x=500, y=300)

    btn10=Button(root1, borderwidth=0,text='Logout', font=('roman',20), fg='white', bg='purple', command = logout)
    btn10.place(x=500,y=400)

    root1.mainloop()

def logout():
    global root1,un,pw,root,bg
    root1.destroy()
    login_screen()

def record_insert():
    global root,root1,root4,root3
    root1.destroy()
    table_insert()
    
def record_display():
    global root,root1,root4,root3
    root1.destroy()
    display()
    
def table_insert():
    global root4,bg
    root4=tk.Tk()
    root4.configure(bg="DarkCyan")
    root4.title("Adding A Record")
    root4.geometry('600x600+0+0')
    bg=PhotoImage(file="C:\\Users\\Reity\\OneDrive\\Desktop\\wp1929946.png")
    label=Label(root4,image=bg)
    label.place(x=0,y=0)
    button1=Button(root4,width=25,bg='purple',text="DIRECTORY TABLE", cursor='hand2', fg='white',command=add_rec)
    button1.place(x=50,y=100)
    button2=Button(root4,width=25,bg='purple', text="ADDRESS TABLE", cursor='hand2',fg='white',command=add_rec1)
    button2.place(x=50,y=200)
    Button(root4, text="GO TO HOMEPAGE", command=hg_i, fg='white',font=("roman", 12), bg='blue', width=18, height=1).place(x=200,y=400)

def hg_i():
    root4.destroy()
    homepage()
#Adding directory1  in the database    
def add_rec():
    global root2
    def create():
        global Dno,Name,PhoneNo,Job,ifi,cur
        con=mysql.connector.connect(host='localhost',user='root',password='reity2612',database='Telephone_directory')
        Dno=e1.get()
        Name=e2.get()
        PhoneNo=e3.get()
        Job=e4.get()
        s=0
        c=0
        if con.is_connected()==False:
            print('Not Connected')
            exit()
        cur=con.cursor()
        cur.execute('SELECT directory_No FROM directory1')
        ifi=[]
        r=cur.fetchall()
        for i in r:
            for j in i:
                ifi.append(j)
        for i in range (len(ifi)):
            if str(Dno)==str(ifi[i]):
                messagebox.showerror(title='ERROR',message='Duplicate Key', parent=root2)
                c=1
        for i in Name:
            if i.isalpha()==False and i!=' ':
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='Name cant have special characters or numbers', parent=root2)
            
        s=0
        for i in Job:
            if i.isalpha()==False and i!=' ':
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='Job cant have numbers or special characters', parent=root2)
                
        s=0
        for i in PhoneNo:
            if i.isnumeric()==False and i!=' ':
                s=1
                c=1
        if s==1:
             messagebox.showerror(title='ERROR',message='Phone number can only have digits', parent=root2)
                

        if len(PhoneNo)!=10:
            messagebox.showerror(title='ERROR',message='Invalid Phone No, Must be 10 digits', parent=root2)
            c=1
            
        for i in Dno:
            if i.isnumeric()==False and i!=' ':
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='directory number can only have digits', parent=root2)
            
        if len(Dno)<3:
            messagebox.showerror(title='ERROR',message='Invalid directory number, atleast be 3 digits', parent=root2)
            c=1
        
        if c!=1: 
            
            cur.execute("CREATE TABLE IF NOT EXISTS directory1(directory_No INT PRIMARY KEY, NAME CHAR(10), PHONE_NO CHAR(10), JOB CHAR(10))")
            query="INSERT INTO directory1 values(%s, %s, %s, %s)"
            values=(Dno, Name, PhoneNo, Job)
            cur.execute(query,values)

            con.commit()
            ifi.append(Dno)
            messagebox.showinfo("Information", "---Record Inserted Successfully---", parent=root2)

     
    global e1, e2, e3, e4
    root2=Toplevel()
    root2.title("directory")
    root2.configure(bg="DarkCyan")
    root2.geometry("500x500+0+0")
    Label(root2, text="DNO").place(x=10,y=10)
    Label(root2, text="NAME").place(x=10, y=60)
    Label(root2, text="PHONE_NO").place(x=10, y=120)
    Label(root2, text="JOB").place(x=10, y=180)
    e1=Entry(root2)
    e1.place(x=200,y=10)
    e2=Entry(root2)
    e2.place(x=200,y=60)
    e3=Entry(root2)
    e3.place(x=200,y=120)
    e4=Entry(root2)
    e4.place(x=200,y=180)
    Button(root2, text="ADD", command=create, bg="red", fg="white",font=("roman",15)).place(x=280,y=320)
    Button(root2, text="BACK", command=deldir, bg="red", fg="white", font=("roman",15)).place(x=150, y=320)
#adding address table in the database           
def add_rec1():
    global root3
    def create1():
        global Aid,House,Area,City,Pincode,Dno
        
        x='INSERT INTO Address VALUES(%s,%s,%s,%s,%s,%s)'
        Aid=e5.get()
        House=e6.get()
        Area=e7.get()
        City =e8.get()
        Pincode=e9.get()
        Dno=e10.get()
        s=0
        c=0
        con=mysql.connector.connect(host='localhost', user='root', password='reity2612',database='Telephone_directory')
        if con.is_connected():
            cur=con.cursor()
            
        for i in Aid:
            if i.isnumeric()==False:
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='AID can only have numbers', parent=root3)
        
        s=0
        for i in House:
            if i.isalnum()==False:
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='HNo cant have special characters', parent=root3)
        s=0
        for i in Area:
            if i.isalpha()==False:
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='Area cant have special characters', parent=root3)
        s=0
        for i in City:
            if i.isalpha()==False:
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='City cant have special characters', parent=root3)
        s=0
        for i in Pincode:
            if i.isnumeric()==False:
                s=1
                c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='Pincode can only have numbers', parent=root3)
        s=0
        for i in Dno:
            if i.isnumeric()==False:
               s=1
               c=1
        if s==1:
            messagebox.showerror(title='ERROR',message='DNo cant have special characters', parent=root3)
            c=1 
        if len(House)<5 or len(House)>5:
            messagebox.showerror(title='ERROR',message='Invalid House_no, has to be 5 digits', parent=root3)
            c=1
        if len(Dno)<3:
            messagebox.showerror(title='ERROR',message='Invalid Dno, atleast be 3 digits', parent=root3)
            c=1
        if len(Pincode)<6 or len(Pincode)>6:
            messagebox.showerror(title='ERROR',message='Invalid Pincode, has to be 6 digits', parent=root3)
            c=1
        if c!=1:
            try:  
                 cur.execute("SELECT * FROM directory1 WHERE directory_No = %s", (Dno,))
                 result = cur.fetchone()

                 if result:
            
                     v = (Aid, str(House), str(Area), str(City), Pincode, Dno)
                     cur.execute(x,v)
                     con.commit()
                     messagebox.showinfo(title='geo', message='Record inserted successfully', parent=root3)
                 else:
                     messagebox.showerror(title='Geo', message='DNO does not exist in the directory table', parent=root3)
                  
            except mysql.connector.Error as e:
                
                messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))

            finally:
                con.close()

    global e5, e6, e7, e8, e9, e10
    root3=Toplevel()
    root3.configure(bg="DarkCyan")
    root3.title("Address")
    root3.geometry("500x500+0+0")
    Label(root3, text="AID").place(x=10,y=10)
    Label(root3, text="HOUSE_NO").place(x=10, y=60)
    Label(root3, text="AREA").place(x=10, y=120)
    Label(root3, text="CITY").place(x=10, y=180)
    Label(root3, text="PINCODE").place(x=10, y=240)
    Label(root3, text="DNO").place(x=10, y=300)
    e5=Entry(root3)
    e5.place(x=200,y=10)
    e6=Entry(root3)
    e6.place(x=200,y=60)
    e7=Entry(root3)
    e7.place(x=200,y=120)
    e8=Entry(root3)
    e8.place(x=200,y=180)
    e9=Entry(root3)
    e9.place(x=200,y=240)
    e10=Entry(root3)
    e10.place(x=200,y=300)
    Button(root3, text="ADD", command=create1,font=("roman",12), bg="red", fg="white").place(x=250,y=400)
    Button(root3, text="BACK", command=deladd,font=("roman",12), bg="red", fg="white").place(x=150,y=400)
    
def display():
    global root5
    con = mysql.connector.connect(host="localhost",user="root",password="reity2612")
    cur=con.cursor()
    root5=tk.Tk()
    root5.geometry('1085x350+0+0')
    root5.configure(bg="indigo")
    cur.execute("use telephone_directory")
    cur.execute('SELECT * FROM ADDRESS')
    r=cur.fetchall()
    if r==[]:
        x='SELECT * FROM directory1'
        cur.execute(x)
        tree=ttk.Treeview(root5,selectmode='browse')
        tree.grid(row=1,column=1,padx=20,pady=20)
        tree['columns']=('Dno','Name','Phone','Job')
        tree['show']='headings'
        tree.column("Dno",width=150,anchor='c')
        tree.column("Name",width=150,anchor='c')
        tree.column("Phone",width=150,anchor='c')
        tree.column("Job",width=150,anchor='c')
        tree.heading("Dno",text='Dno')
        tree.heading("Name",text='Name')
        tree.heading("Phone",text='Phone')
        tree.heading("Job",text='Job')
        r=cur.fetchall()
        
        for i in r:
            tree.insert('','end',text=i[0],values=(i[0],i[1],i[2],i[3]))
    else:
        ifin=[]
        x='SELECT D.directory_no,NAME,PHONE_NO,JOB,House_no,CITY,PINCODE FROM directory1 AS D,ADDRESS AS A WHERE D.directory_no=A.Dno'
        cur.execute(x)
        tree=ttk.Treeview(root5,selectmode='browse')
        tree.grid(row=1,column=1,padx=20,pady=20)
        tree['columns']=('Dno','Name','Phone','Job','House','City','Pincode')
        tree['show']='headings'
        tree.column("Dno",width=150,anchor='c')
        tree.column("Name",width=150,anchor='c')
        tree.column("Phone",width=150,anchor='c')
        tree.column("Job",width=150,anchor='c')
        tree.column("House",width=150,anchor='c')
        tree.column("City",width=150,anchor='c')
        tree.column("Pincode",width=150,anchor='c')
        tree.heading("Dno",text='DNO')
        tree.heading("Name",text='NAME')
        tree.heading("Phone",text='PHONE_NO')
        tree.heading("Job",text='JOB')
        tree.heading("House",text='HOUSE_NO')
        tree.heading("City",text='CITY')
        tree.heading("Pincode",text='PINCODE')
        r=cur.fetchall()
        for i in r:
            ifin.append(i[0])
            tree.insert('','end',text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            
        cur.execute('SELECT * FROM directory1')
        r=cur.fetchall()
        try:
            for i in r:
                if i[0] not in ifin:
                    tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3],'NULL','NULL','NULL'))
        except:
            dfnaoiwd=1
        Button(root5,text='CLOSE',fg='white',bg='red',font=('roman',12),command=disd).place(x=480,y=250)

#searching by name
        
def search_by_name():
    global dname, root7
    root7=Toplevel()
    root7.title('search by name')
    root7.configure(bg="DarkCyan")
    root7.geometry('500x500+0+0')
    dname=Entry(root7,width=30)
    dname.place(x=280,y=167)
    
    Label(root7,text="Enter The Name\nTo Be Searched",font=("roman",18)).place(x=100,y=150)
    Button(root7,text="BACK",font=("roman",18),bg="red",fg="white",command=vig).place(x=200,y=300)
    Button(root7,text="NEXT",font=("roman",18),bg="red",fg="white",command=sbn).place(x=350,y=300)
    
def sbn():
    global dname,root8
    dnname=dname.get()
    con = mysql.connector.connect(host="localhost",user="root",password="reity2612",database="telephone_directory")
    cur=con.cursor()
    
    cur.execute("use telephone_directory")
    q=('SELECT D.Directory_no,NAME,PHONE_NO,JOB,House_NO,CITY FROM DIRECTORY1 D,ADDRESS A WHERE NAME=%s AND D.directory_no=A.Dno')
    v=(dnname,)
    cur.execute(q,v)
    r=cur.fetchall()
    
    if r==[]:
        messagebox.showerror(title='error',message='Name not in table',parent=root7)
    else:
        ifin=[]
        root8=tk.Tk()
        root8.geometry("1000x400+0+0")
        root8.configure(bg="indigo")
        root8.title("searching for a name")
        b=Button(root8,text="BACK",command=sig,bg="red",fg="white",font=("Roman",16)).place(x=250,y=300)
        tree=ttk.Treeview(root8,selectmode='browse')
        tree.grid(row=1,column=1,padx=20,pady=20)
        tree['columns']=('Dno','Name','Phone','Job','House','City')
        tree['show']='headings'
        tree.column("Dno",width=150,anchor='c')
        tree.column("Name",width=150,anchor='c')
        tree.column("Phone",width=150,anchor='c')
        tree.column("Job",width=150,anchor='c')
        tree.column("House",width=150,anchor='c')
        tree.column("City",width=150,anchor='c')
        tree.heading("Dno",text='DNO')
        tree.heading("Name",text='NAME')
        tree.heading("Phone",text='PHONE_NO')
        tree.heading("Job",text='JOB')
        tree.heading("House",text='HOUSE_NO')
        tree.heading("City",text='CITY')
        for i in r:
            ifin.append(i[0])
            tree.insert('','end',text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        try:
            for i in r:
                if i[0] not in ifin:
                    tree.insert('','end',iid=[0],text=i[0],values=(i[0],i[1],i[2],i[3],'NULL','NULL'))
        except:
            dfnaoiwd=1
        root8.mainloop()
              
#searching record by city
        
def search_by_city():        
    global city_name, root9
    root9=Toplevel()
    root9.title('Search by city')
    root9.geometry('500x500+0+0')
    root9.configure(bg="DarkCyan")
    city_name=Entry(root9,width=30)
    city_name.place(x=280,y=215)
    Label(root9,text="Enter The City\nTo Be Searched",font=("roman",18)).place(x=100,y=200)
    Button(root9,text="NEXT",font=("roman",18),bg="red",fg="white",command=sbc).place(x=300,y=350)
    Button(root9,text="BACK",font=("roman",18),bg="red",fg="white",command=clsb).place(x=200,y=350)
def sbc():
    global root10,city_name
    c_name=city_name.get()
    con = mysql.connector.connect(host="localhost",user="root",password="reity2612")
    cur = con.cursor()
    cur.execute("use Telephone_directory")
    query=('SELECT D.Directory_no,NAME,PHONE_NO,JOB,House_NO,CITY FROM DIRECTORY1 D,ADDRESS A WHERE city=%s AND D.directory_no=A.Dno')
    values=(c_name,)
    cur.execute(query,values)
    r=cur.fetchall()
    if r==[]:
        messagebox.showerror("ERROR","City does not exist",parent=root9)
    else:
        ifin=[]
        root10=tk.Tk()
        root10.configure(bg="indigo")
        root10.geometry('1000x400+0+0')
        root10.title('Searching city')
        b=Button(root10,text="BACK",font=("roman",18),bg="red",fg="white",command=close).place(x=250,y=300)
        tree=ttk.Treeview(root10,selectmode='browse')
        tree.grid(row=1,column=1,padx=20,pady=20)
        tree['columns']=('Dno','Name','Phone','Job','House','City')
        tree['show']='headings'
        tree.column("Dno",width=150,anchor='c')
        tree.column("Name",width=150,anchor='c')
        tree.column("Phone",width=150,anchor='c')
        tree.column("Job",width=150,anchor='c')
        tree.column("House",width=150,anchor='c')
        tree.column("City",width=150,anchor='c')
        tree.heading("Dno",text='DNO')
        tree.heading("Name",text='NAME')
        tree.heading("Phone",text='PHONE_NO')
        tree.heading("Job",text='JOB')
        tree.heading("House",text='HOUSE_NO')
        tree.heading("City",text='CITY')
        for i in r:
            ifin.append(i[0])
            tree.insert('','end',text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        try:
            for i in r:
                if i[0] not in ifin:
                    tree.insert('','end',iid=[0],text=i[0],values=(i[0],i[1],i[2],i[3],'NULL','NULL'))
        except:
            dfnaoiwd=1
def search_by_fletter():        
     global f_name,root11
     root11=Toplevel()
     root11.title('Search by first letter of name')
     root11.geometry('500x500+0+0')
     root11.configure(bg="DarkCyan")
     f_name=Entry(root11,width=30)
     f_name.place(x=280,y=215)
     Label(root11,text="Enter first letter \nOf name\nTo be searched",font=("roman",18)).place(x=50,y=200)
     Button(root11,text="NEXT",font=("roman",12),bg="red",fg="white",command=sbfl).place(x=300,y=300)
     Button(root11, text="BACK", command=back, fg='white', bg='red', font=("roman", 12)).place(x=200,y=300)
     
def sbfl():
    global root12,f_name
    fname=f_name.get()
    con = mysql.connector.connect(host="localhost",user="root",password="reity2612")
    cur = con.cursor()
    cur.execute("use Telephone_directory")
    query=('SELECT D.Directory_no,NAME,PHONE_NO,JOB,House_NO,CITY FROM DIRECTORY1 D,ADDRESS A WHERE name like %s AND D.directory_no=A.Dno')
    values=(fname+ "%",)
    cur.execute(query, values)
    
    r=cur.fetchall()
    
    if r==[]:
        messagebox.showerror("ERROR","Name does not exist",parent=root11)
    else:
        ifin=[]
        root12=tk.Tk()
        root12.configure(bg="indigo")
        root12.geometry('900x500+0+0')
        root12.title('searching first letter')
        b=Button(root12,text="BACK",font=("roman",12),bg="red",fg="white",command=fircl).place(x=250,y=300)
        tree=ttk.Treeview(root12,selectmode='browse')
        tree.grid(row=1,column=1,padx=20,pady=20)
        tree['columns']=('Dno','Name','Phone','Job','House','City')
        tree['show']='headings'
        tree.column("Dno",width=150,anchor='c')
        tree.column("Name",width=150,anchor='c')
        tree.column("Phone",width=150,anchor='c')
        tree.column("Job",width=150,anchor='c')
        tree.column("House",width=150,anchor='c')
        tree.column("City",width=150,anchor='c')
        tree.heading("Dno",text='DNO')
        tree.heading("Name",text='NAME')
        tree.heading("Phone",text='PHONE_NO')
        tree.heading("Job",text='JOB')
        tree.heading("House",text='HOUSE_NO')
        tree.heading("City",text='CITY')
        for i in r:
            ifin.append(i[0])
            tree.insert('','end',text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        try:
            for i in r:
                if i[0] not in ifin:
                    tree.insert('','end',iid=[0],text=i[0],values=(i[0],i[1],i[2],i[3],'NULL','NULL'))
        except:
            dfnaoiwd=1
        
    
def delete():
    global root13
    def dell():
        ID=E.get()
        con=mysql.connector.connect(host='localhost',user='root',password='reity2612',database='Telephone_directory')
        cur=con.cursor()
        che=0
        saf=0
        for i in ID:
            if i.isnumeric()==False:
                saf=1
        if saf==1:
            messagebox.showerror(title='ERROR',message='Dno can only have numbers', parent=root13)
            che=1
        elif len(ID)>5:
            messagebox.showerror(title='ERROR',message='Invalid Dno must be 5 or less digits', parent=root13)
            che=1
        cur.execute('SELECT directory_No FROM directory1')
        ifin=[]
        r=cur.fetchall()
        for i in r:
            for j in i:
                ifin.append(j)
        saf=1
        for i in range(len(ifin)):
            if ID==str(ifin[i]):
                saf=0
                break
        if saf==1:
            messagebox.showerror(title='Error',message='Dno not in table', parent=root13)
            che=1
        elif che==0:
            try:
                query="delete from directory1 where directory_No=%s"
                values=(ID,)
                cur.execute(query,values)
                con.commit()
                messagebox.showinfo("Information","Record deleted successfully", parent=root13)
            except Exception as a:
                    print(a)
                    con.rollback()
                    con.close()
    root13=Toplevel()
    root13.title("Delete")
    root13.configure(bg="DarkCyan")
    root13.geometry("500x500+0+0")
    global E
    Label(root13,text="Enter Dno:",font=24).place(x=100,y=120)
    E=Entry(root13,width=30)
    E.place(x=220,y=125)
    Button(root13,text="BACK",command=led,bg='red',fg='white',font=("roman",16)).place(x=150,y=180)
    Button(root13,text="DELETE",command=dell,height=1,width=10,bg='red',fg='white',font=("roman",16)).place(x=230,y=180)
    root13.mainloop()
def About():
    global root23
    f=open('about.txt','w')
    che=0
    root23=Tk()
    root23.title("About")
    root23.configure(bg="DarkCyan")
    root23.geometry("900x210+0+0")
    f.write('Geo is a telecommunication service company which provides telecommunication services to its customers. \nIt uses a structured query language to store vast amount of records of its customers.\n It uses GUI and visually rich application called Geo Enterprises which aids in accessing these tables.\n Geo enterprises connects to 2 tables,\n namely "Directories" and "Address" which store personal and postal address of the customers respectively.\n Using this app, an employee can add, delete, update or search using constraints.\n This app helps in easily manipulating and using data and is efficient in mangement of immense amount of data within seconds.')
    f.close()
    f=open('about.txt','r')
    s=f.read()
    Label(root23,text=s,font=('roman',12),bg='lavender').pack()
    Button(root23,text='CLOSE',bg='red',font=("roman",13),width=17,fg="white",command=A_des).place(x=380, y=170)
    f.close()

def A_des():
    global root23
    root23.destroy()


def updating():
    global e1,e2,e4,root24
    
    def pps():
        
        cn=e1.get()
        cv=e2.get()
        nv=e4.get()
        Dno=e4.get()
        Name=e4.get()
        PhoneNo=e4.get()
        Job=e4.get()
        House=e4.get()
        Area=e4.get()
        City=e4.get()
        Pincode=e4.get()
        s=0
        c=0
        con=mysql.connector.connect(host='localhost',user='root',password='reity2612')
        if con.is_connected():
            cur=con.cursor()
            cur.execute("use telephone_directory")
            query=("select * from directory1 where directory_No=%s")
            values=(cv,)
            cur.execute(query,values)
            record=cur.fetchall()
            if record==[]:
                messagebox.showerror("Error","Dno does not exist", parent=root24)
            else:
                if cn=="dno":
                    for i in Dno:
                        if i.isnumeric()==False and i!=' ':
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='directory number can only have digits', parent=root24)
            
                    if len(Dno)<3:
                        messagebox.showerror(title='ERROR',message='Invalid directory number, atleast be 3 digits', parent=root24)
                        c=1
        
                    if c!=1:
                        try:
                            query_directory = "UPDATE directory11 SET directory1_No=%s WHERE directory_No=%s"
                            values_directory = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory, values_directory)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                elif cn=="name":
                    for i in Name:
                        if i.isalpha()==False and i!=' ':
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='Name cant have special characters or numbers', parent=root24)
            
                    s=0
                    if c!=1:
                        try:
                            query_directory = "UPDATE directory1 SET NAME=%s WHERE directory_No=%s"
                            values_directory = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory, values_directory)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                        
                elif cn=="phone number":
                    for i in PhoneNo:
                        if i.isnumeric()==False and i!=' ':
                            s=1
                            c=1
                    if s==1:
                         messagebox.showerror(title='ERROR',message='Phone number can only have digits', parent=root24)
                

                    if len(PhoneNo)!=10:
                        messagebox.showerror(title='ERROR',message='Invalid Phone No, Must be 10 digits', parent=root24)
                        c=1
                    if c!=1:
                        try:
                            query_directory = "UPDATE directory1 SET PHONE_NO=%s WHERE directory_No=%s"
                            values_directory = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory, values_directory)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                    
                elif cn=="job":
                    for i in Job:
                        if i.isalpha()==False and i!=' ':
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='Job cant have numbers or special characters', parent=root24)
                    
                        s=0
                    if c!=1:
                        try:
                            query_directory1 = "UPDATE directory1 SET JOB=%s WHERE directory_No=%s"
                            values_directory1 = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory1, values_directory1)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                    
                elif cn=="houseno":
                    for i in House:
                        if i.isalnum()==False:
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='HNo cant have special characters', parent=root24)
                        s=0
                    if len(House)<5 or len(House)>5:
                        messagebox.showerror(title='ERROR',message='Invalid House_no, has to be 5 digits', parent=root24)
                        c=1
                    if c!=1:
                        try:
                            query_directory1 = "UPDATE Address SET HOUSE_NO=%s WHERE Dno=%s"
                            values_directory1 = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory1, values_directory1)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                    
                elif cn=="area":
                    for i in Area:
                        if i.isalpha()==False:
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='Area cant have special characters or digits', parent=root24)
                        s=0
                    if c!=1:
                        try:
                            query_directory1 = "UPDATE Address SET AREA=%s WHERE Dno=%s"
                            values_directory1 = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory1, values_directory1)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                                       
                elif cn=="city":
                    for i in City:
                        if i.isalpha()==False:
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='City cant have special characters or digits', parent=root24)
                        s=0
                    if c!=1:
                        try:
                            query_directory1 = "UPDATE Address SET CITY=%s WHERE Dno=%s"
                            values_directory1 = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory1, values_directory1)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()
                elif cn=="pincode":
                    for i in Pincode:
                        if i.isnumeric()==False:
                            s=1
                            c=1
                    if s==1:
                        messagebox.showerror(title='ERROR',message='Pincode can only have numbers', parent=root24)
                        s=0
                    if len(Pincode)<6 or len(Pincode)>6:
                        messagebox.showerror(title='ERROR',message='Invalid Pincode, has to be 6 digits', parent=root24)
                        c=1
                    if c!=1:
                    
                        try:
                            query_directory1 = "UPDATE Address SET PINCODE=%s WHERE Dno=%s"
                            values_directory1 = (nv, cv)
                            with con.cursor() as cur:
                                 cur.execute(query_directory1, values_directory1)
                            con.commit()
                            messagebox.showinfo("INFO","Value modified successfully",parent=root24)
                        except mysql.connector.Error as e:
                            messagebox.showerror(title='Error', message='MySQL Connector Error: {}'.format(e))
                        finally:
                            con.close()        
                    
                else:
                    messagebox.showinfo("ERROR","The specified column does not exist",parent=root24)    
    root24=Toplevel()
    root24.geometry("500x500+0+0")
    root24.configure(bg="DarkCyan")
    root24.title("Update")
    label1=Label(root24,text="Enter column name\n to be modified",fg="black",font=("roman",16)).place(x=50,y=150)
    label2=Label(root24,text="Enter current\ndirectory no",fg="black",font=("roman",16)).place(x=50,y=230)
    label3=Label(root24,text="Enter new value\n of the column",fg="black",font=("roman",16)).place(x=50,y=300)
    Button(root24,text="UPDATE",bg="red",fg="white",command=pps,font=("ROMAN",16)).place(x=330,y=380)
    Button(root24,text="BACK",command=update_des,height=1,width=10,bg='red',fg='white',font=("roman",16)).place(x=180,y=380)
    e1=Entry(root24)
    e1.place(x=250,y=165)
    e2=Entry(root24)
    e2.place(x=250,y=240)
    e4=Entry(root24)
    e4.place(x=250,y=315)
    
def update_des():
    global root24
    root24.destroy()
def clsb():
    global root9
    root9.destroy()
def vig():
    global root7
    root7.destroy()
def sig():
    global root8
    root8.destroy()
def led():
    global root13
    root13.destroy()
def deldir():
    global root2
    root2.destroy()
def deladd():
    global root3
    root3.destroy()
def disd():
    global root5
    root5.destroy()
    homepage()
def disa():
    global root6
    root6.destroy()
def fircl():
    global root12
    root12.destroy()
def back():
    global root11
    root11.destroy()
def close():
    global root10
    root10.destroy()

    
login_screen()
dname=''
f_name=''
city_name=''


