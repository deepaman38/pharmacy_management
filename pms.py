from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from tkinter import StringVar

class PharmacyManagementSystem:
    # Constructor
     def __init__(self,root):  # root is the name of the main window
        self.root = root
        self.root.title("Beyond Medicine,Caring for You")
        # Width and height of the window
        self.root.geometry("1600x1000+0+0")
#========================= add medicine variables=============================
        self.ref_var=StringVar()
        self.addmed_var=StringVar()
#================================================================================
        heading = Label(self.root,text="BeyondMeds",bd=15,relief=RIDGE,
                         bg='#b3b3ff',fg='#00cea5',font=("arial",50,"bold"),
                         padx=2,pady=4)
        heading.pack(side=TOP,fill="x")
        #==========================================================================================================
        #r stand raw string and use for interpret the image in correct manner
        img1= Image.open ("logos.jpg") #(r"C:\Users\Tegpal\pharma_project\logos.jpg") 
        img1 = img1.resize((80, 80), Image.LANCZOS)
        #this command ImageTk used to convert the PIL image object into a format that Tkinter can work with.
        self.photoimg1=ImageTk.PhotoImage(img1)
        imgpanel=Label(self.root,image=self.photoimg1,borderwidth=0)
        imgpanel.place(x=80,y=20) #place to set the logo from x axis and y axis
        
    
#===============================DATA FRAME==============================================================================
        #This is a frame where we can make add medicine and medicine finding frames.
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20 )
        DataFrame.place(x=0,y=120,width=1280,height=400)
        #=====================Left dataframe====================================
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="MEDICINE INFORMATION",bg="white",fg='#00cea5',
                                 font=("arial",18,"bold"))
        DataFrameLeft.place(x=0,y=3,width=850,height=350)
        #=======================Right dataframe===================================
        DataFrameright=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Add Medicine",bg="white",fg='#00cea5',
                                 font=("arial",18,"bold"))
        DataFrameright.place(x=790,y=3,width=430,height=350)
        #===========================Butoon dataframe Bottom=============================
        ButtonFrame=Frame(self.root,bd=7,relief=RIDGE,padx=20,bg='#b3b3ff' )
        ButtonFrame.place(x=0,y=480,width=1280,height=55)
       #=============================Main Button window================================
        add_button = Button(ButtonFrame,text="ADD",font=("arial",14,"bold"),width=12,bg="#f9ffe3",fg="#00cea5")
        add_button.grid(row=0,column=0)
        #==============================================update========================
        update_button = Button(ButtonFrame,text="UPDATE",font=("arial",14,"bold"),width=12,bg="#f9ffe3",fg="#00cea5")
        update_button.grid(row=0,column=1, padx=10)
        #===================================delete========================================
        delete_button = Button(ButtonFrame,text="DELETE",font=("arial",14,"bold"),width=12,bg="#f9ffe3",fg="#00cea5")
        delete_button.grid(row=0,column=2, padx=10)
        # reset_button = Button(ButtonFrame,text="RESET",font=("arial",14,"bold"),width=12,bg="#f9ffe3",fg="#e25822")
        # reset_button.grid(row=0,column=3, padx=15)
        # quit_button = Button(ButtonFrame,text="EXIT",font=("arial",14,"bold"),width=12,bg="#f9ffe3",fg="#e25822")
        # quit_button.grid(row=0,column=4, padx=15)

       #===========================searchby=========================================================
        search_label=Label(ButtonFrame,text="Search By",font=("arial",14,"bold"),padx=2,width=10,bg="#b3b3ff",fg="#00cea5")
        search_label.grid(row=0,column=5,sticky=W)
        #===================combo box=======================
        search_combo = ttk.Combobox(ButtonFrame,width=10,font=("arial",14),state="read only")
        search_combo["values"]=('Ref no.',
                                'Medicine name',
                                'Lot no.'
                                )
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        #============================
        txt_search=Entry(ButtonFrame,width=12,bd=3,relief=RIDGE,font=("arial",14,"bold"),)
        txt_search.grid(row=0,column=7,padx=10)
        #=================search button
        search_button=Button(ButtonFrame,text="Search",font=("arial",14,"bold"),width=10,bg="#f9ffe3",fg="#00cea5")
        search_button.grid(row=0,column=8,padx=10)
        show_button=Button(ButtonFrame,text="Show all",font=("arial",14,"bold"),width=10,bg="#f9ffe3",fg="#00cea5")
        show_button.grid(row=0,column=9)

        #=======================label,entry and combo===========================================
        ref_label=Label(DataFrameLeft,text="Reference No",font=("arial",10,"bold"),padx=2,bg='white')
        ref_label.grid(row=0,column=0,sticky=W,pady=10)
        conn = mysql.connector.connect(host="localhost", 
                                        username="root", 
                                         password="Test@123",
                                         database="pmsdata")
        my_cursor = conn.cursor()
        my_cursor.execute("select ref from pharma")
        ref_row = my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataFrameLeft,width=27,font=("arial",10),state="read only")
        ref_combo["values"]= ref_row                         
        ref_combo.grid(row=0,column=1,padx=2,pady=5)
        ref_combo.current(0)
        #=============================
        comp_label=Label(DataFrameLeft,text="Company Name",font=("arial",10,"bold"),bg='white')
        comp_label.grid(row=1,column=0,sticky=W,pady=5)
        comp_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        comp_comp.grid(row=1,column=1,pady=5,padx=2,sticky=EW)
        #=======================================
        TOM_label=Label(DataFrameLeft,text="Medicine Type",font=("arial",10,"bold"),bg='white')
        TOM_label.grid(row=2,column=0,sticky=W)
        TOM_combo = ttk.Combobox(DataFrameLeft,width=26,font=("arial",10),state="read only")
        TOM_combo["value"]=('a',
                                'b')
        TOM_combo.grid(row=2,column=1,padx=2,pady=5,sticky=EW)
        TOM_combo.current(0)
        #=================================
        Medname_label=Label(DataFrameLeft,text="Medicine Name",font=("arial",10,"bold"),bg='white')
        Medname_label.grid(row=3,column=0,sticky=W)
        conn = mysql.connector.connect(host="localhost", 
                                        username="root", 
                                         password="Test@123",
                                         database="pmsdata")
        my_cursor = conn.cursor()
        my_cursor.execute("select medname from pharma")
        med_row = my_cursor.fetchall()
        Medname_combo = ttk.Combobox(DataFrameLeft,width=27,font=("arial",10),state="read only")
        Medname_combo["value"]=med_row
                                
        Medname_combo.grid(row=3,column=1,padx=2,pady=5,sticky=EW)
        Medname_combo.current(0)
        #=====================================
        Lot_label=Label(DataFrameLeft,text="Lot No.",font=("arial",10,"bold"),bg='white')
        Lot_label.grid(row=4,column=0,sticky=W)
        Lot_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        Lot_comp.grid(row=4,column=1,padx=2,pady=5,sticky=EW)

        Issdate_label=Label(DataFrameLeft,text="Issue Date:",font=("arial",10,"bold"),bg='white')
        Issdate_label.grid(row=5,column=0,sticky=W)
        Issdate_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        Issdate_comp.grid(row=5,column=1,padx=2,pady=5,sticky=EW)

        Exp_label=Label(DataFrameLeft,text="Exp. Date:",font=("arial",10,"bold"),bg='white')
        Exp_label.grid(row=6,column=0,sticky=W)
        Exp_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        Exp_comp.grid(row=6,column=1,sticky=EW,padx=2,pady=5)

        uses_label=Label(DataFrameLeft,text="Uses:",font=("arial",10,"bold"),bg='white')
        uses_label.grid(row=7,column=0,sticky=W)
        uses_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        uses_comp.grid(row=7,column=1,sticky=EW,padx=2,pady=5)

        side_label=Label(DataFrameLeft,text="Side Effect",font=("arial",10,"bold"),bg='white')
        side_label.grid(row=8,column=0,sticky=W)
        side_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        side_comp.grid(row=8,column=1,sticky=EW,padx=2,pady=5)

        pqt_label=Label(DataFrameLeft,text="Product QT.",font=("arial",10,"bold"),bg='white',padx=20,pady=6,width=20)
        pqt_label.grid(row=0,column=2,sticky=W)
        pqt_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        pqt_comp.grid(row=0,column=3,sticky=EW)

        dos_label=Label(DataFrameLeft,text="Dosage",font=("arial",10,"bold"),bg='white',pady=6,padx=20,width=20)
        dos_label.grid(row=1,column=2,sticky=W)
        dos_comp=Entry(DataFrameLeft,width=29,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        dos_comp.grid(row=1,column=3,sticky=EW)

        #======================image=================================
        img3= Image.open(r"C:\Users\Tegpal\pharma_project\lab2.jpg") 
        img3 = img3.resize((370,200), Image.LANCZOS)
        #this command ImageTk used to convert the PIL image object into a format that Tkinter can work with.
        self.photoimg3=ImageTk.PhotoImage(img3)
        imgpanel=Label(self.root,image=self.photoimg3,borderwidth=5)
        #place to set the logo from x axis and y axis
        imgpanel.place(x=450,y=270)
        #=====================label right=======================================
        DataFrameright=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Dep.",bg="white",fg='#00cea5',
                                  font=("arial",18,"bold"))
        DataFrameright.place(x=790,y=3,width=430,height=350)
        #====================================================================================
        img4= Image.open(r"C:\Users\Tegpal\pharma_project\med.jpg") 
        img4 = img4.resize((200,100), Image.LANCZOS)
        #this command ImageTk used to convert the PIL image object into a format that Tkinter can work with.
        self.photoimg4=ImageTk.PhotoImage(img4)
        imgpanel=Label(self.root,image=self.photoimg4,borderwidth=2)
        #place to set the logo from x axis and y axis
        imgpanel.place(x=840,y=180)
        #=========================================================================================
        img5= Image.open(r"C:\Users\Tegpal\pharma_project\injection.jpg") 
        img5 = img5.resize((200,100), Image.LANCZOS)
        #this command ImageTk used to convert the PIL image object into a format that Tkinter can work with.
        self.photoimg5=ImageTk.PhotoImage(img5)
        imgpanel=Label(self.root,image=self.photoimg5,borderwidth=2)
        #place to set the logo from x axis and y axis
        imgpanel.place(x=1040,y=180)
        #=================right label=======================================================================
        ref_label=Label(DataFrameright,text="Reference No:",font=("arial",10,"bold"),padx=2,bg='white')
        ref_label.place(x=0,y=140)        
        ref_entry=Entry(DataFrameright,textvariable=self.ref_var,width=15,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        ref_entry.place(x=105,y=140)

        med_label=Label(DataFrameright,text="Medicine Name",font=("arial",10,"bold"),padx=2,bg='white')
        med_label.place(x=0,y=180)        
        med_entry=Entry(DataFrameright,textvariable=self.addmed_var,width=15,relief=RIDGE,font=("arial",10,"bold"),bd=2)
        med_entry.place(x=105,y=180)
        #===================================side frame============================================================
        side_frame=Frame(DataFrameright,bd=2,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=210,width=220,height=100)

        sc_x=Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill="x")
        sc_y=Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill="y")
        #===================Treeview to make a table======================================
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        #xview and yview is for adjust the vertical and horizontal view of the table.
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        self.medicine_table.heading("ref", text="Ref No.")
        self.medicine_table.heading("medname", text="Medicine Name")
        self.medicine_table["show"]="headings"
        
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        self.datafecth_med()
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        
        
            
        #===========================right frame button==============================================================
        down_frame=Frame(DataFrameright,bd=4,bg="#b3b3ff")
        down_frame.place(x=250,y=110,width=135,height=180)
        add_buton= Button(down_frame,text="ADD",command=self.medicineadd_database,font=("arial",12,"bold"),width=12,fg="#00cea5")
        add_buton.grid(row=0,column=0,pady=3)
        up_buton= Button(down_frame,command=self.updateMed,text="UPDATE",font=("arial",12,"bold"),width=12,fg="#00cea5")
        up_buton.grid(row=1,column=0,pady=3)
        del_buton= Button(down_frame,command=self.del_database,text="DELETE",font=("arial",12,"bold"),width=12,fg="#00cea5")
        del_buton.grid(row=2,column=0,pady=3)
        cle_buton= Button(down_frame,text="CLEAR",font=("arial",12,"bold"),width=12,fg="#00cea5")
        cle_buton.grid(row=3,column=0,pady=4)
        #==================================Frame details ================================================================
        frame_details=Frame(self.root,bd=7,relief=RIDGE,bg="white")
        frame_details.place(x=0,y=527,width=1280,height=140)
        #=========================scrollbar=====================================
        x_scrollbar=ttk.Scrollbar(frame_details,orient=HORIZONTAL)
        x_scrollbar.pack(side=BOTTOM,fill=X)
        y_scrollbar=ttk.Scrollbar(frame_details,orient=VERTICAL)
        y_scrollbar.pack(side=RIGHT,fill=Y)
        #==================================connection=============================
     def medicineadd_database(self):
        
        conn = mysql.connector.connect(host="localhost", 
                                        username="root", 
                                        password="Test@123",
                                        database="pmsdata")
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO pharma(ref,medname) VALUES (%s, %s)", 
                          (self.ref_var.get(), self.addmed_var.get())
                          )
        conn.commit()
        #self.datafecth_med()
        # self.Medget_cursor()
        #self.del_database()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")
    #===============================fetching the data to show in table==========================================
     def datafecth_med(self):
        conn = mysql.connector.connect(host="localhost", 
                                         username="root", 
                                         password="Test@123",
                                         database="pmsdata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
         #=======fetching all the data to show in table===============
        rows=my_cursor.fetchall()
        if len(rows)!=0:
        #=================medicine table to delete children data=============================
                self.medicine_table.delete(*self.medicine_table.get_children())
                for i in rows:
        #=============inseting the data in table======================
                        self.medicine_table.insert("",END,values=i)
                conn.commit()
        conn.close()
#=============================Medicine get cursor==========================================
     def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        if not cursor_row:
            return
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        if not row:
            return
        self.ref_var.set(row[0])
        self.addmed_var.set(row[1])
        print("Selected:", row)
#====================================update===============================================================
     def updateMed(self):
        if self.ref_var.get()=="" or self.addmed_var.get()=="":
                messagebox.showerror("Error","All fields are required")
        else:
                conn = mysql.connector.connect(host="localhost", 
                                          username="root", 
                                          password="Test@123",                                         
                                          database="pmsdata")
                my_cursor = conn.cursor()
                my_cursor.execute("update pharma set medname=%s where ref=%s",(
                                                                        self.addmed_var.get(),
                                                                        self.ref_var.get()
                                                                        ))
                conn.commit()
                self.datafecth_med()
                conn.close()
                messagebox.showinfo("Success","Medicine has been successfully updated.")
      
     def del_database(self):
        
        conn = mysql.connector.connect(host="localhost", 
                                          username="root", 
                                          password="Test@123",                                         
                                          database="pmsdata")
        my_cursor = conn.cursor()
        sql="delete from pharma where ref=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val               
                           ) 
        conn.commit()
        self.datafecth_med()
        conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()  # To keep the window open
     


