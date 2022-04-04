from ast import excepthandler
from pkgutil import get_data
from tkinter import*
import tkinter
from tkinter import ttk,messagebox
import sqlite3

from PIL import*

class medicineclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x500+220+130")
        self.root.title("Medicine dashboard")
        self.root.config(bg="white")
        self.root.focus_force()

        #==============================================
        #=============All Variables============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_med_id=StringVar()
        self.var_med_name=StringVar()
        self.var_med_company=StringVar()
        self.var_med_type=StringVar()
        self.var_med_price=StringVar()
        self.var_med_quantity=StringVar()
   
        self.var_med_mandate=StringVar()
        self.var_med_expdate=StringVar()



        #=======================search frame==========================
        SearchFrame=LabelFrame(self.root,text="Search Medicine",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white",fg="black")
        SearchFrame.place(x=250,y=20,width=600,height=70)

 


        #================options===============
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values= ("Select","Name","Type","Company","Reference ID"),state="readonly",justify=CENTER)
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow",fg="black").place(x=200,y=10)

        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",10),bg="blue",fg="black",cursor="hand2").place(x=350,y=10,width=150,height=20)

        #============================title============================
        title=Label(self.root,text="Medicine details",font=("goudy old style",18),bg="dark blue",fg="white").place(x=50,y=100,width=1000)


        #========================content======================

        #=================row1================
        lbl_med_id=Label(self.root,text="Reference ID",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=150)
        lbl_med_type=Label(self.root,text="Type",font=("goudy old style",15),bg="white",fg="black").place(x=450,y=150)
        lbl_med_company=Label(self.root,text="Company",font=("goudy old style",15),bg="white",fg="black").place(x=750,y=150)


        txt_med_id=Entry(self.root,textvariable=self.var_med_id,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=170,y=150,width=180)
        #txt_med_type=Entry(self.root,textvariable=self.var_med_type,font=("goudy old style",15),bg="white").place(x=510,y=150,width=180)
        cmb_type=ttk.Combobox(self.root,textvariable=self.var_med_type,values= ("INJECTION","SYRUP","DROPS","TABLETS","OTHERS"),state="readonly",justify=CENTER)
        cmb_type.place(x=510,y=150,width=180)
        cmb_type.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow",fg="black").place(x=200,y=10)

        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",10),bg="blue",cursor="hand2").place(x=350,y=10,width=150,height=20)
        txt_med_company=Entry(self.root,textvariable=self.var_med_company,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=850,y=150,width=180)



        #=================row2================
        lbl_med_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=250)
        lbl_med_quantity=Label(self.root,text="Quantity",font=("goudy old style",15),bg="white",fg="black").place(x=450,y=250)
        lbl_med_price=Label(self.root,text="Price",font=("goudy old style",15),bg="white",fg="black").place(x=790,y=250)


        txt_med_name=Entry(self.root,textvariable=self.var_med_name,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=110,y=250)
        txt_med_quantity=Entry(self.root,textvariable=self.var_med_quantity,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=540,y=250)
        txt_med_price=Entry(self.root,textvariable=self.var_med_price,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=850,y=250)


        #==============================row3==============================
        lbl_med_mandate=Label(self.root,text="Manufacturing Date",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=350)
        lbl_med_expdat=Label(self.root,text="Expiry Date",font=("goudy old style",15),bg="white",fg="black").place(x=450,y=350)
      

        txt_med_mandate=Entry(self.root,textvariable=self.var_med_mandate,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=220,y=350)
        txt_med_expdate=Entry(self.root,textvariable=self.var_med_expdate,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=550,y=350)

        #===================button=======================

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",10,"bold"),bg="gray",fg="black",cursor="hand2").place(x=50,y=400,width=150,heigh=30)
        btn_update=Button(self.root,text="UPDATE",command=self.update,font=("goudy old style",10,"bold"),bg="gray",fg="black",cursor="hand2").place(x=200,y=400,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",10,"bold"),bg="gray",fg="black",cursor="hand2").place(x=350,y=400,width=150,height=30)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("goudy old style",10,"bold"),bg="gray",fg="black",cursor="hand2").place(x=500,y=400,width=150,height=30)


        #======================Medicine Details==========================

        med_frame=Frame(self.root,bd=3,relief=RIDGE)
        med_frame.place(x=0,y=430,relwidth=1,height=150)

        scrolly=Scrollbar(med_frame,orient=VERTICAL)
        scrollx=Scrollbar(med_frame,orient=HORIZONTAL)

        self.Medtable=ttk.Treeview(med_frame,columns=("Medicine_ID","Name","Company","Type","Price","Quantity","Manufacturing_Date","Expiry_Date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Medtable.xview)
        scrolly.config(command=self.Medtable.yview)
        self.Medtable.heading("Medicine_ID",text="Medicine_ID")
        self.Medtable.heading("Name",text="Name")
        self.Medtable.heading("Company",text="Company")
        self.Medtable.heading("Type",text="Type")
        self.Medtable.heading("Price",text="Price")
        self.Medtable.heading("Quantity",text="Quantity")
        self.Medtable.heading("Manufacturing_Date",text="Manufacturing_Date")
        self.Medtable.heading("Expiry_Date",text="Expiry_Date")
        
        self.Medtable["show"]="headings"

        self.Medtable.column("Medicine_ID",width=90)
        
        self.Medtable.column("Name",width=90)
        self.Medtable.column("Company",width=90)
        self.Medtable.column("Type",width=90)
        self.Medtable.column("Price",width=90)
        self.Medtable.column("Quantity",width=90)
        self.Medtable.column("Manufacturing_Date",width=90)
        self.Medtable.column("Expiry_Date",width=90)
        self.Medtable.pack(fill=BOTH,expand=1)
        self.Medtable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#========================================================================add===============

    def add(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_med_id.get()=="":
                messagebox.showerror("ERROR","MED ID MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from medicine where Medicine_ID=?",(self.var_med_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","This ID is already assigned",parent=self.root)
                    
                else:
                    cur.execute("Insert into medicine(Medicine_ID,Name,Company,Type,Price,Quantity,Manufacturing_Date,Expiry_Date)values(?,?,?,?,?,?,?,?)",(
                                                          self.var_med_id.get(),
                                                          self.var_med_name.get(),
                                                          self.var_med_company.get(),
                                                          self.var_med_type.get(),
                                                          self.var_med_price.get(),
                                                          self.var_med_quantity.get(),
                                                          self.var_med_mandate.get(),
                                                          self.var_med_expdate.get(),
                                                          


                    ))
                    con.commit()
                    messagebox.showinfo("Success","Medicine added",parent=self.root)
                    self.show()
                    


        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)


    def show(self):
         con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
         cur=con.cursor()

         try:
            cur.execute("select * from medicine")
            rows=cur.fetchall()
            self.Medtable.delete(*self.Medtable.get_children())
            for row in rows:
                self.Medtable.insert('',END,values=row)

         except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    def get_data(self,ev):
         f=self.Medtable.focus()
         content=(self.Medtable.item(f))
         row=content['values']
         #print(row)
         self.var_med_id.set(row[0])
         self.var_med_name.set(row[1])
         self.var_med_company.set(row[2])
         self.var_med_type.set(row[3])
         self.var_med_price.set(row[4])
         self.var_med_quantity.set(row[5])
         self.var_med_mandate.set(row[6])
         self.var_med_expdate.set(row[7])



    


    #====================================================update=======================================
    def update(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_med_id.get()=="":
                messagebox.showerror("ERROR","MED ID MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from medicine where Medicine_ID=?",(self.var_med_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","INVALID MED ID",parent=self.root)
                    
                else:
                    cur.execute("Update medicine set Name=?,Company=?,Type=?,Price=?,Quantity=?,Manufacturing_Date=?,Expiry_Date=? where Medicine_ID=?",(
                                                         
                                                          self.var_med_name.get(),
                                                          self.var_med_company.get(),
                                                          self.var_med_type.get(),
                                                          self.var_med_price.get(),
                                                          self.var_med_quantity.get(),
                                                          self.var_med_mandate.get(),
                                                          self.var_med_expdate.get(),
                                                          self.var_med_id.get(),
                                                          


                    ))
                    con.commit()
                    messagebox.showinfo("Update Success","Medicine added",parent=self.root)
                    self.clear()
                    

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

#================================delete=========================
    def delete(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
              if self.var_med_id.get()=="":
                    messagebox.showerror("ERROR","MED ID MUST BE REQUIRED",parent=self.root)
              else:
                    cur.execute("Select * from medicine where Medicine_ID=?",(self.var_med_id.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("ERROR","INVALID MED ID",parent=self.root)
                    
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                             cur.execute("delete from medicine where Medicine_ID=?",(self.var_med_id.get(),))
                             con.commit()
                             messagebox.showinfo("Delete","Medicine deleted",parent=self.root)
                             self.show()

        except Exception as ex:
                messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

     

          
            
#==================================clear======================
    def clear(self):
             self.var_med_id.set("")
             self.var_med_name.set("")
             self.var_med_company.set("")
             self.var_med_type.set("")
             self.var_med_price.set("")
             self.var_med_quantity.set("")
             self.var_med_mandate.set("")
             self.var_med_expdate.set("")
             self.var_searchtxt.set("")
             self.var_searchby.set("Select")  
             self.show()
    
#===========================search===================================
    def search(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()

        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input should be required",parent=self.root)
            else:

                cur.execute("select * from medicine where "+self.var_searchby.get()+" LIKE '%" +self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Medtable.delete(*self.Medtable.get_children())
                    for row in rows:
                         self.Medtable.insert('',END,values=row)

                
                else:
                    messagebox.showerror("Error","NO record found",parent=self.root)
               

            
            

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    

           





if __name__=="__main__":
        root = tkinter.Tk()
        obj = medicineclass(root)
        root.mainloop()