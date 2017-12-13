from tkinter import *
import tkinter.messagebox
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def view_com():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_com():
    list1.delete(0,END)
    for row in backend.search(tit_t.get(),aut_t.get(),ye_t.get(),ui_t.get()):
        list1.insert(END,row)

def add_com():
    backend.insert(tit_t.get(),aut_t.get(),ye_t.get(),ui_t.get())
    list1.delete(0,END)
    list1.insert(END,(tit_t.get(),aut_t.get(),ye_t.get(),ui_t.get()))

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_com()

def del_com():
    backend.delete(selected_tuple[0])
    view_com()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_com():
    backend.update(selected_tuple[0],tit_t.get(),aut_t.get(),ye_t.get(),ui_t.get())
    view_com()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)


window=Tk()

window.wm_title("BOOK")
tkinter.messagebox.showinfo('bookstore', 'you are entering bookstore ')

ans = tkinter.messagebox.askquestion('surity', 'do you want to open')
if ans == 'yes':
    l1=Label(window,text="Title")
    l1.grid(row=0,column=0)

    l2=Label(window,text="Author")
    l2.grid(row=0,column=2)

    l3=Label(window,text="Year")
    l3.grid(row=1,column=0)

    l4=Label(window,text="UID")
    l4.grid(row=1,column=2)

    tit_t=StringVar()
    aut_t=StringVar()
    ye_t=StringVar()
    ui_t=StringVar()
    def testVal(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isdigit():
                return False
        return True

    def testVal1(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isalnum():
                return False
        return True

    e1=Entry(window,textvariable=tit_t)
    #e1['validatecommand']=(e1.register(testVal1),'%P','%i','%d')
    e1.grid(row=0,column=1)

    e2=Entry(window,textvariable=aut_t)
    #e2['validatecommand']=(e2.register(testVal1),'%P','%i','%d')
    e2.grid(row=0,column=3)

    e3=Entry(window,textvariable=ye_t, validate="key")
    e3['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e3.grid(row=1,column=1)

    e4=Entry(window,textvariable=ui_t,validate="key")
    e4['validatecommand'] = (e4.register(testVal),'%P','%i','%d')
    e4.grid(row=1,column=3)


    list1= Listbox(window,height=7,width=35)
    list1.grid(row=2,column=0,rowspan=6,columnspan=2)

    sb1=Scrollbar(window)
    sb1.grid(row=2,column=2,rowspan=6)

    sb2=Scrollbar(window,orient=HORIZONTAL)
    sb2.grid(row=7,column=0,columnspan=2)

    list1.configure(yscrollcommand=sb1.set,xscrollcommand=sb2.set)
    sb1.configure(command=list1.yview)
    sb2.configure(command=list1.xview)

    list1.bind('<<ListboxSelect>>',get_selected_row)

    b1=Button(window,text="view all",width=15,command=view_com)
    b1.grid(row=2,column=3)


    b2=Button(window,text="search",width=15,command=search_com)
    b2.grid(row=3,column=3)


    b3=Button(window,text="add",width=15,command=add_com)
    b3.grid(row=4,column=3)


    b4=Button(window,text="update",width=15,command=update_com)
    b4.grid(row=5,column=3)


    b5=Button(window,text="delete",width=15,command=del_com)
    b5.grid(row=6,column=3)

    b6=Button(window,text="close",width=15,command=window.destroy)
    b6.grid(row=7,column=3)
else :
    window.destroy()
window.mainloop()

"""Here's the solution you're looking for:

def testVal(inStr,i,acttyp):
    ind=int(i)
    if acttyp == '1': #insert
        if not inStr[ind].isalpha():
            return False
    return True
Heres some other things which might be useful:

.isdigit() tests if a string is an integer
.isalpha() tests if a string contains only letters
.isalnum() tests if a string contains only letters and numbers
.isupper() tests for uppercase
.islower() tests for lowercase
 """
