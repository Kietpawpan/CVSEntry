# I modified the code from
# https://www.tutorialspoint.com/python-tkinter-how-to-export-data-from-entry-fields-to-a-csv-file

# Import the required libraries
import os
import csv
import tkinter
from csv import *
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("jTech")
window.geometry("700x450")
main_lst=[]

def Add():
   lst=[caseID.get(), information.get(), result.get(), reason.get()]
   main_lst.append(lst)
   with open("resolution.csv","w", newline="") as file:
      Writer=writer(file)
      Writer.writerow(["Case ID","Information","Result", "Reason"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Notice","Added succesfully")

def Check():
      os.startfile("resolution.csv")

def Clear():
   caseID.delete(0,END)
   information.delete(0,END)
   result.delete(0,END)
   reason.delete(0, END)

# 3 labels, 4 buttons,3 entry fields
label7=Label(window,text="",padx=40,pady=10)
label1=Label(window,text="รหัสคำขอ: ",padx=40,pady=10)
label2=Label(window,text="ข้อมูลที่ขอ: ",padx=40,pady=10)
label3=Label(window,text="ผลการพิจารณา: ",padx=40,pady=10)
label4=Label(window,text="เหตุผล: ",padx=40,pady=10)
label5=Label(window,text="Data Entry")
label6=Label(window,text=u"\u00A9" "MNRE-SLC") # Show copyright symbol


caseID=Entry(window,width=30,borderwidth=3)
information=Entry(window,width=30,borderwidth=3)
result=Entry(window,width=30,borderwidth=3)
reason=Entry(window,width=30, borderwidth=3)

add=Button(window,text="Add",padx=20,pady=10,command=Add)
check=Button(window,text="Check",padx=23,pady=10,command=Check)
clear=Button(window,text="Clear",padx=20,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label7.grid(row=0,column=0)
label1.grid(row=1,column=0)
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)
label4.grid(row=4,column=0)

label5.place(x=500, y=5)
label6.place(x=500, y=22)

caseID.grid(row=1,column=1)
information.grid(row=2,column=1)
result.grid(row=3,column=1)
reason.grid(row=4,column=1)


add.grid(row=5,column=0,columnspan=2)
check.grid(row=5,column=1,columnspan=1)
clear.grid(row=5,column=2,columnspan=1)
Exit.grid(row=5,column=3,columnspan=1)

window.mainloop()