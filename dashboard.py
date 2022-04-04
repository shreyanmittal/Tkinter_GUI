from tkinter import*
import tkinter
from PIL import*
from category import categoryclass
from medicine import*
from tkinter import*
from supplier import*
from product import*
from sales import*

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Pharmacy dashboard")
        self.root.config(bg="white")
        #================title========================
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Pharmacy Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",padx="20").place(x=0,y=0,relwidth=1,height=100)

        #======logout button=====
        btn_logout=Button(self.root,text="Logout",font=("timesa new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1300,y=25)


        #====left menu========
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=445)
        self.icon_side=PhotoImage(file="images/logo1.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("timesa new roman",20,"bold"),bg="green",fg="white").pack(side=TOP,fill=X)

        btn_medicine=Button(LeftMenu,text="Medicine",command=self.medicine,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_medicine=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)


        btn_medicine=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_medicine=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_medicine=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        btn_medicine=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",fg="black",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        #=====contents=====

        self.lbl_employee=Label(self.root,text="Total Medicines\n [0]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=120,height=150,width=350)
        self.lblsupplier=Label(self.root,text="Total Suppliers\n [0]",bd=5,relief=RIDGE,bg="red",fg="white",font=("goudy old style",20,"bold")).place(x=850,y=120,height=150,width=350)
        self.lbl_category=Label(self.root,text="Total Category\n [0]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=400,height=150,width=350)
        self.lbl_dosage=Label(self.root,text="Dosage\n [0]",bd=5,relief=RIDGE,bg="green",fg="white",font=("goudy old style",20,"bold")).place(x=850,y=400,height=150,width=350)


        #=======footer========
        lbl_footer=Label(self.root,text="Pharmacy management system By G5",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        #=============================================================================================

    def medicine(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=medicineclass(self.new_wim)
    
    def dosage(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=dosageclass(self.new_wim)

    def supplier(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_wim)

    
    def category(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_wim)

    def product(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=productclass(self.new_wim)
    
    def sales(self):
        self.new_wim=Toplevel(self.root)
        self.new_obj=salesclass(self.new_wim)





if __name__=="__main__":
        root = tkinter.Tk()
        obj = IMS(root)
        root.mainloop() 