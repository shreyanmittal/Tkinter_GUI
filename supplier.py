from ast import excepthandler
from pkgutil import get_data
from tkinter import*
import tkinter
from tkinter import ttk,messagebox
import sqlite3

from PIL import*

class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1200x500+220+130')
        self.root.title("Medicine dashboard")
        self.root.config(bg="white")
        self.root.focus_force()

        #==============================================
        #=============All Variables============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_desc=StringVar()
        

        #================options===============
        lbl_search=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white",fg="black")
        lbl_search.place(x=700,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow",fg="black").place(x=800,y=80,width=150)

        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",10),bg="blue",cursor="hand2",fg="black").place(x=980,y=79,width=100,height=28)

        #============================title============================
        title=Label(self.root,text="Supplier details",font=("bold",20),bg="dark blue",fg="white").place(x=50,y=10,width=1100,height=40)


        #========================content======================


        #=================row1================
        lbl_supplier_invoice=Label(self.root,text="Invoice ID",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=80)
        

        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=180,y=80,width=180)
        
        #============search===========
          
        #txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=200,y=10)

        #btn_search=Button(self.root,text="Search",font=("goudy old style",10),bg="blue",cursor="hand2").place(x=0,y=0,width=100,height=20)
        
        


        #=================row2================
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=180,y=120)
        


        #==============================row3==============================
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=180,y=160)

        #===============================row4===============================
        
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white",fg="black").place(x=50,y=200)
        txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=180,y=200,width=470,height=120)
        

        #===================button=======================

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",10),bg="#2196f3",fg="black",cursor="hand2").place(x=50,y=370,width=150,height=35)
        btn_update=Button(self.root,text="UPDATE",command=self.update,font=("goudy old style",10),bg="#2196f3",fg="black",cursor="hand2").place(x=200,y=370,width=150,height=35)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",10),bg="#2196f3",fg="black",cursor="hand2").place(x=350,y=370,width=150,height=35)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("goudy old style",10),bg="#2196f3",fg="black",cursor="hand2").place(x=490,y=370,width=150,height=35)


        #======================Supplier Details==========================

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=700,y=120,height=350,width=380)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(sup_frame,columns=("invoice","Name","contact"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("Name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        #self.supplierTable.heading("description",text="Description")
        
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("Name",width=90)
        self.supplierTable.column("contact",width=90)
        #self.supplierTable.column("description",width=90)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#===============================add===============

    def add(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("ERROR","INVOICE MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("ERROR","This invoice is already assigned",parent=self.root)
                    
                else:
                    cur.execute("Insert into supplier(invoice,Name,contact)values(?,?,?)",(
                                                          self.var_sup_invoice.get(),
                                                          self.var_name.get(),
                                                          self.var_contact.get(),))
                                                          #self.var_desc.get('1.0',END),))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added",parent=self.root)
                    self.show()
                    


        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)


    def show(self):
         con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
         cur=con.cursor()

         try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children(),)
            for row in rows:
                self.supplierTable.insert('',END,values=row)

         except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    def get_data(self,ev):
         f=self.supplierTable.focus()
         content=(self.supplierTable.item(f))
         row=content['values']
         #print(row)
         self.var_sup_invoice.set(row[0])
         self.var_name.set(row[1])
         self.var_contact.set(row[2])
         '''
         self.var_desc.delete('1.0',END)
         self.var_desc.insert(END,row[3])

         '''

    


    #====================================================update=======================================
    def update(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try: 
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("ERROR","Invoice MUST BE REQUIRED",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","INVALID invoice",parent=self.root)
                    
                else:
                    cur.execute("Update supplier set Name=?,contact=? where invoice=?",(
                                                         
                                                          self.var_name.get(),
                                                          self.var_contact.get(),
                                                          #self.var_desc.get(),
                                                          self.var_sup_invoice.get(), ))
                    con.commit()
                    messagebox.showinfo("Update Success","supplier added",parent=self.root)
                    self.clear()
                    

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

#================================delete=========================
    def delete(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()
        try:
              if self.var_sup_invoice.get()=="":
                    messagebox.showerror("ERROR","INVOICE MUST BE REQUIRED",parent=self.root)
              else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("ERROR","INVALID INVOICE",parent=self.root)
                    
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                             cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                             con.commit()
                             messagebox.showinfo("Delete","Supplier deleted",parent=self.root)
                             self.clear()

        except Exception as ex:
                messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

     

          
            
#==================================clear======================
    def clear(self):
             self.var_sup_invoice.set("")
             self.var_name.set("")
             self.var_contact.set("")
             #self.var_desc.delete()
             self.var_searchtxt.set("")
             self.show()
    
#===========================search===================================
    def search(self):
        con=sqlite3.connect(database=r'LOGIN_SYSTEM.db')
        cur=con.cursor()

        try:
            '''
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","select search by option",parent=self.root)
             '''
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice should be required",parent=self.root)
            else:

                cur.execute("select * from supplier where invoice=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)

                
                else:
                    messagebox.showerror("Error","NO record found",parent=self.root)
               

            
            

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO : {str(ex)}",parent=self.root)

    

           

            



if __name__=="__main__":
        root = tkinter.Tk()
        obj = supplierclass(root)
        root.mainloop()