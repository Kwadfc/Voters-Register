import tkinter as tk #Module imported for Graphical user interface
from tkinter import ttk
import turtle as t #Module imported to draw Ghana Flag on tkinter canvas
from datetime import date #Module imported to validate age of users

#Password for Registrar is vtRs_20_regstr!$


V={} #Initialize Voter's List as empty dictionary

Vread=open("Voters_Register.txt","r") #Open's text file to read Voter's information
#Loop to append each line in text file as a list in the Voters dictionary, Voter's ID is the key
for i in Vread:
    d=i.split("\t")
    d.remove('\n')
    if len(d)>0:
        V[int(d[0])]=d
    else:
        V={}
Vread.close()

#Function to delete information from entries
def clear_entries():
    ent_first_name.delete(0,tk.END)
    ent_middle_name.delete(0,tk.END)
    ent_last_name.delete(0,tk.END)
    ent_DOB.delete(0,tk.END)
    gnd.set("Please select your Gender")
    var.set("Please Select your region")
    ent_country.delete(0,tk.END)
    ent_vo_id.delete(0,tk.END)

#Function to recieve data from entries and write unto file   
def update_list():
    from datetime import date
    global V
    days = 365.2425
    f_name=ent_first_name.get()
    m_name=ent_middle_name.get()
    l_name=ent_last_name.get()
    DOB=ent_DOB.get()
    gender=gnd.get()
    region=var.get()
    country=ent_country.get()
    card_id=ent_vo_id.get()
    
    Vs=open("Voters_Register.txt","a+") #Open text file to read and write
    #Check age of Voter
    try:
        birthDate=date(int(DOB.split("/")[2]),int(DOB.split("/")[1]),int(DOB.split("/")[0]))    
        age = int((date.today() - birthDate).days / days)
    except IndexError or ValueError:
        tk.messagebox.showwarning("Warning", "Inappropriate date format")
        
    #Conditional statements to ensure form is complete
    if (len(card_id) and len(f_name) and len (m_name)
        and len (l_name) and len(DOB) and len(gender)
        and len(region) and len(country)!=0
        and region!="Please Select your region"
        and gender!="Please select your Gender"):
        
        #Conditional statements to ensure user is an Eligible voter  
        if age>=18 and country=="Ghanaian":
            
            if int(card_id)not in V.keys():
                Vs.write(card_id+'\t' )
                Vs.write(f_name+'\t' )
                Vs.write(m_name+'\t' )
                Vs.write(l_name+'\t' )
                Vs.write(DOB+'\t')
                Vs.write(gender+'\t')
                Vs.write(region+'\t')
                Vs.write(country+'\t'+'\n')
                Vs.close()
                Vread=open("Voters_Register.txt","r")
                tk.messagebox.showinfo("Success!","Form has been submitted succesfully")
                for i in Vread:
                    d=i.split("\t")
                    d.remove('\n')
                    V[int(card_id)]=d
            else:
                tk.messagebox.showerror("Error", "Voters ID already in system")
        else:
            tk.messagebox.showerror("Error", "User is not an eligible voter")
    else:
        tk.messagebox.showerror("Error","Incomplete Registration")


#Funfunction to open voters list
def openlist():
    global window2

    #Creation of 2nd Window, for the list of voters
    window2=tk.Tk() 
    window2.title("Voters_list")

    vtrs_title = tk.Frame(master=window2,relief=tk.SUNKEN, borderwidth=3, height=20)
    vtrs_title.pack(fill=tk.BOTH, expand=False) 

    lbl_title = tk.Label(master=vtrs_title, text="Voters Registration List:")
    lbl_title.pack()



    ttle= ["Voters ID Number",
           "First Name",
           "Middle Name",
           "Last Name",
           "Date of Birth(dd/mm/yyyy)",
           "Gender",
           "Nationality",
           "Region"
           ]
           
    vtrs_row2=tk.Frame(master=window2,relief=tk.SUNKEN, borderwidth=3,height=150)
    vtrs_row2.pack(fill=tk.BOTH,expand=True)

    
    a=0
    for i in ttle:
        vtrs_col=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=3,height=40)
        vtrs_col.grid(column=a,row=0,sticky="new")

        a=a+1

        vtrs_ttle=tk.Label(master=vtrs_col, text=i)
        vtrs_ttle.grid(sticky="nsew")

    Vread=open("Voters_Register.txt","r")
    b=0

    #Creation of frames and Listboxes for Voters list window
    
    vtrs_list0=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list0.grid(column=0,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(0,weight=1)
    vtrs_list0.rowconfigure(0,weight=1)
    vtrs_list0.columnconfigure(0,weight=1)
    listbox0 = tk.Listbox(master=vtrs_list0)
    listbox0.grid(sticky="nsew")

    vtrs_list1=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list1.grid(column=1,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(1,weight=1)
    vtrs_list1.rowconfigure(0,weight=1)
    vtrs_list1.columnconfigure(0,weight=1)
    listbox1 = tk.Listbox(master=vtrs_list1)
    listbox1.grid(sticky="nsew")

    vtrs_list2=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list2.grid(column=2,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(2,weight=1)
    vtrs_list2.rowconfigure(0,weight=1)
    vtrs_list2.columnconfigure(0,weight=1)
    listbox2 = tk.Listbox(master=vtrs_list2)
    listbox2.grid(sticky="nsew")

    vtrs_list3=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list3.grid(column=3,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(3,weight=1)
    vtrs_list3.rowconfigure(0,weight=1)
    vtrs_list3.columnconfigure(0,weight=1)
    listbox3 = tk.Listbox(master=vtrs_list3)
    listbox3.grid(sticky="nsew")

    vtrs_list4=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list4.grid(column=4,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(4,weight=1)
    vtrs_list4.rowconfigure(0,weight=1)
    vtrs_list4.columnconfigure(0,weight=1)
    listbox4 = tk.Listbox(master=vtrs_list4)
    listbox4.grid(sticky="nsew")

    vtrs_list5=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list5.grid(column=5,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(5,weight=1)
    vtrs_list5.rowconfigure(0,weight=1)
    vtrs_list5.columnconfigure(0,weight=1)
    listbox5= tk.Listbox(master=vtrs_list5)
    listbox5.grid(sticky="nsew")

    vtrs_list6=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list6.grid(column=6,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(6,weight=1)
    vtrs_list6.rowconfigure(0,weight=1)
    vtrs_list6.columnconfigure(0,weight=1)
    listbox6= tk.Listbox(master=vtrs_list6)
    listbox6.grid(sticky="nsew")

    vtrs_list7=tk.Frame(master=vtrs_row2,relief=tk.SUNKEN, borderwidth=0.5)
    vtrs_list7.grid(column=7,row=1,sticky="nsew")
    vtrs_row2.rowconfigure(1,weight=1)
    vtrs_row2.columnconfigure(7,weight=1)
    vtrs_list7.rowconfigure(0,weight=1)
    vtrs_list7.columnconfigure(0,weight=1)
    listbox7= tk.Listbox(master=vtrs_list7)
    listbox7.grid(sticky="nsew")

    scrollbar = tk.Scrollbar(vtrs_list7, orient=tk.VERTICAL)
    #Function for scrollbar control
    def yview(*args):
        listbox0.yview(*args)
        listbox1.yview(*args)
        listbox2.yview(*args)
        listbox3.yview(*args)
        listbox4.yview(*args)
        listbox5.yview(*args)
        listbox6.yview(*args)
        listbox7.yview(*args)

    scrollbar.config(command=yview)
    scrollbar.grid(row=0,column=len(ttle),sticky="nse")
    lbox=[listbox0,listbox1,listbox2,listbox3,listbox4,listbox5,listbox6,listbox7]
    
                                    
    for i in range(len(lbox)):                                                      #Loop to append data into listboxes        
        x=0
        
        for key in V:
            lbox[i].insert(x,V[key][i])
            x=x+1
                                                                                    #Function to delete selected user
    def del_user():        
        Vread1=open("Voters_Register.txt","r")                                      #Open file to read
        pos = 0
        for line in Vread1:
                                                                                    # For each line, check if line contains the string            
            if ent_search.get() in line:
                print(pos)
                break
            pos += 1
        Vread1.close()
        try:
            del V[int(ent_search.get())]                                            #Delete ID number stated from Dictionary
            
        except KeyError or ValueError:
            tk.messagebox.showinfo("my message","User not found in Voter's List")
        Vread2 = open("Voters_Register.txt", "r")                                   #Open file to read
        lines = Vread2.readlines()
        Vread2.close()
        del lines[pos]                                                              #Delete line that contains ID number stated from text file
        Vwrite = open("Voters_Register.txt", "w+")                                  #Open file to write
        for line in lines:                                                          #Write remaining files to text file     
            Vwrite.write(line)

        Vwrite.close()
        window2.withdraw()
        openlist()
        
    def reset():
        Vread3 = open("Voters_Register.txt", "r")                                   #Open file to read
        backup_lines = Vread3.readlines()
        Vread3.close()
        Vbackup = open("Voters_Register_backup.txt", "w+")                          #Open back up file to write
        for line in backup_lines:                                                   #Write remaining files to text file     
            Vbackup.write(line)
        Vbackup.close()
        V.clear()                                                                   #Clear Voters Dictionary
        Vs=open("Voters_Register.txt","w")                                          #Open File to write
        window2.withdraw()                                                          #Temporarily close Window
        openlist()                                                                  #Refresh page to display new list
            



    #Frame to search for Users  
    vtrs_search = tk.Frame(master=window2,relief=tk.SUNKEN, borderwidth=3, height=20)
    vtrs_search.pack(fill=tk.BOTH, expand=False)
    btn_delete = tk.Button(master=vtrs_search, text="Delete",command=del_user)
    btn_delete.pack(side=tk.RIGHT, padx=10,pady=10, ipadx=10)

    btn_reset = tk.Button(master=vtrs_search, text="Reset",command=reset)
    btn_reset.pack(side=tk.LEFT, padx=10,pady=10, ipadx=10)
    
    ent_search = tk.Entry(master=vtrs_search)
    ent_search.pack(side=tk.RIGHT,padx=10,pady=10)
    lbl_search = tk.Label(master=vtrs_search, text="Search for Voter's ID")
    lbl_search.pack(side=tk.RIGHT,padx=10,pady=10)
    
    


    window2.mainloop()
        
def confirm2():
    if entry2.get()=="vtRs_20_regstr!$":
        check.withdraw()
        window.deiconify()
        entry2.delete(0,tk.END)
    else:
       tk.messagebox.showerror("error", "Incorrect password, check code")
       
def confirm():

    global response
    global btn_dup
    response=choice.get()
    if response==0:
        login.withdraw()
        window.deiconify()        
        btn_dup.pack_forget()

        return response
    else:
        login.withdraw()
        check.deiconify()
        return response
    
def log_out():
    window.withdraw() or check.withdraw()
    login.deiconify()
    entry2.delete(0,tk.END)
    btn_dup.pack(side=tk.RIGHT,padx=10,pady=10, ipadx=10)




#Creation of 1st Window, for data entry
window = tk.Tk()
window.withdraw()
window.title("Voter's Registration")
##login=tk.Tk()
login = tk.Toplevel(window)
login.geometry("700x300")
login_heading=tk.Frame(master=login,relief=tk.SUNKEN,borderwidth=3,height=3)
login_heading.pack(fill=tk.BOTH,side=tk.LEFT, expand=True,pady=30,padx=(20,10))
lbl_login= tk.Label(master=login_heading, text="Welcome to Ghana's \n\nVoters Registeration form")
lbl_login.config(font=("Courier", 20))
lbl_login.pack(expand=False,side=tk.TOP,pady=10)

question = tk.Label(master=login_heading, text="Please indicate your Status:")
question.config(font=("Courier", 14))
question.pack(anchor=tk.CENTER,expand=True)
choice=tk.IntVar()
choice.set(0)
voter=tk.Radiobutton(login, text="Voter",padx = 20,variable=choice,value=0)
voter.config(font=("Times", 14))
voter.pack(anchor=tk.W, expand=True)
registrar=tk.Radiobutton(login, text="Registrar",padx = 20,variable=choice,value=1)
registrar.config(font=("Times", 14))
registrar.pack(anchor=tk.W,expand=True)
ans = tk.Button (login, text = 'Submit', command = confirm,bg="green",fg="white")
ans.pack (pady=10)
check = tk.Toplevel(window)
check.geometry("700x250")

check.withdraw()
heading=tk.Frame(master=check,height=3)
label2 = tk.Label(heading, text="Enter Registrar's passcode")
label2.config(font=("Courier", 18))
heading.pack(pady=(30,20),anchor=tk.CENTER)
entry2 = tk.Entry(check,show="*",width=30)
button2 = tk.Button(check, text="Verify", command=confirm2,bg="green",fg="white",width=7)
button2.config(font=("Times", 14))
btn_logout1 = tk.Button(master=check, text="Logout", command=log_out)

label2.pack(anchor=tk.CENTER)
entry2.pack(anchor=tk.CENTER)

button2.pack(pady=20,ipadx=10,anchor=tk.CENTER)
btn_logout1.pack(padx=10,pady=(30,5), ipadx=10,anchor=tk.CENTER)


vtrs_top=tk.Frame(master=window,borderwidth=1,height=3)
vtrs_top.pack(fill=tk.BOTH,padx=40)


vtrs_heading=tk.Frame(master=vtrs_top,relief=tk.SUNKEN,borderwidth=3,height=3)
vtrs_heading.pack(fill=tk.BOTH,side=tk.LEFT, expand=True,pady=(20,40))
lbl_heading= tk.Label(master=vtrs_heading, text="Welcome to Ghana's Voters Registeration form")
lbl_heading.config(font=("Courier", 14))
lbl_heading.pack(expand=False,side=tk.TOP)
lbl_warning= tk.Label(master=vtrs_heading, text="Please fill this form honestly and to the best of your knowledge ",height=1)
lbl_warning.pack(expand=False)
lbl_disclaimer= tk.Label(master=vtrs_heading, text="AN INACCURATE REPRESENATION OF YOUR TRUE IDENTITY IS A CRIME! ",fg="red")
lbl_disclaimer.pack(expand=False)
canvas = tk.Canvas(master=vtrs_top,width=151,height=121)
canvas.pack(expand=False,side=tk.LEFT,padx=10,pady=10)

#Ghana Flag
Kwad=t.RawTurtle(canvas)
Kwad.speed(speed="fastest")
Kwad.hideturtle()
x=-76
y=61
color=["red","yellow","green"]
for i in color:
    Kwad.penup()
    Kwad.goto(x,y)
    Kwad.pendown()
    Kwad.fillcolor(i)
    Kwad.begin_fill()
    for i in range(2):
        Kwad.forward(150)
        Kwad.right(90)
        Kwad.forward(40)
        Kwad.right(90)
    Kwad.end_fill()
    y=y-40

Kwad.penup()
Kwad.goto(-16,7)
Kwad.pendown()
Kwad.fillcolor('black')
Kwad.begin_fill()
for i in range(5):
    Kwad.forward(30)
    Kwad.right(144)
Kwad.end_fill()



#Creation of the forms frame and entries
vtrs_form = tk.Frame(master=window,relief=tk.SUNKEN, borderwidth=3)
vtrs_form.pack(fill=tk.BOTH, expand=True)



vtrs_form.grid_columnconfigure(0, weight=1)
vtrs_form.grid_columnconfigure(1, weight=1)
for i in range(9):
    vtrs_form.grid_rowconfigure(i, weight=1)

#Function to validate Voters ID entry
def votID(no,P):
    if len(P)<=10:
        if no.isdigit():
            return True
        elif no ==" ":
            return True
        else:
            return False
    else:
        return False
    
vi=window.register(votID)

lbl_gh_no = tk.Label(master=vtrs_form, text="Voter's ID Number:\n(10 digits)")
ent_vo_id = tk.Entry(master=vtrs_form, width=50)
lbl_gh_no.grid(row=0, column=0, sticky="ew")
ent_vo_id.grid(row=0, column=1,sticky="ew",padx=10,pady=5)
ent_vo_id.config(validate="key",validatecommand=(vi,"%S","%P"))

lbl_first_name = tk.Label(master=vtrs_form, text="First Name:")
ent_first_name = tk.Entry(master=vtrs_form, width=50)
lbl_first_name.grid(row=1, column=0, sticky="ew")
ent_first_name.grid(row=1, column=1,sticky="ew",padx=10,pady=5)

lbl_middle_name = tk.Label(master=vtrs_form, text="Middle Name:")
ent_middle_name = tk.Entry(master=vtrs_form, width=50)
lbl_middle_name.grid(row=2, column=0, sticky="ew")
ent_middle_name.grid(row=2, column=1,sticky="ew",padx=10,pady=5)


lbl_last_name = tk.Label(master=vtrs_form, text="Last Name:")
ent_last_name = tk.Entry(master=vtrs_form, width=50)
lbl_last_name.grid(row=3, column=0, sticky="ew")
ent_last_name.grid(row=3, column=1,sticky="ew",padx=10,pady=5)


#Function to validate Date of Birth entry
def DOB(ent,P):
    if len(P)<=10:
        if ent.isdigit():
            return True
        elif ent == " ":
            return True
        elif "/" in ent:
            return True

        else:
            return False
    else:
        return False
db=window.register(DOB)

lbl_DOB = tk.Label(master=vtrs_form, text="Date of Birth:\n (dd/mm/yyyy)")
ent_DOB = tk.Entry(master=vtrs_form, width=50)
lbl_DOB.grid(row=4, column=0, sticky="ew")
ent_DOB.grid(row=4, column=1,sticky="ew",padx=10,pady=5)
ent_DOB.config(validate="key",validatecommand=(db,"%S","%P"))



lbl_gender = tk.Label(master=vtrs_form, text="Gender:")
lbl_gender.grid(row=5, column=0, sticky="ew")

Options = [
    "Male",
    "Female"
    ]
gnd = tk.StringVar()
gnd.set("Please select your Gender")

opt = tk.OptionMenu(vtrs_form, gnd, *Options)
opt.grid(row=5,column=1,sticky="ew",padx=10,pady=5)

#Function to validate Nationality entry
def cntry(cnt,P):
    if len(P)<=56:
        if cnt.isalpha():
            return True

        elif "-" in cnt:
            return True
        elif cnt == "":
            return True
        else:
            return False
    else:
        return False
ct=window.register(cntry)
lbl_country = tk.Label(master=vtrs_form, text="Nationality:")
ent_country = tk.Entry(master=vtrs_form, width=50)
lbl_country.grid(row=6, column=0, sticky="ew")
ent_country.grid(row=6, column=1,sticky="ew",padx=10,pady=5)
ent_country.config(validate="key",validatecommand=(ct,"%S","%P"))

OptionList = [
"Ahafo",
"Ashanti",
"Brong Ahafo",
"Bono East",
"Central",
"Eastern",
"Greater Accra",
"North East",
"Northern",
"Oti",
"Savannah",
"Upper East",
"Upper West",
"Volta",
"Western",
"Western North"
]

lbl_region = tk.Label(master=vtrs_form, text="Region:")
lbl_region.grid(row=8, column=0, sticky="new")

var = tk.StringVar()


 
opt = ttk.Combobox(vtrs_form,textvariable = var)
opt['values'] =(
"Ahafo",
"Ashanti",
"Brong Ahafo",
"Bono East",
"Central",
"Eastern",
"Greater Accra",
"North East",
"Northern",
"Oti",
"Savannah",
"Upper East",
"Upper West",
"Volta",
"Western",
"Western North"
)

opt.set("Please Select your region")

opt.grid(row=8,column=1,sticky="new",padx=10,pady=5)

##Buttons
frm_buttons = tk.Frame(master=window)
frm_buttons.pack(fill=tk.BOTH,expand=False)

btn_submit = tk.Button(master=frm_buttons, text="Submit",command=lambda:[update_list(),clear_entries()])
btn_submit.pack(side=tk.RIGHT, padx=10,pady=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear_entries)
btn_clear.pack(side=tk.RIGHT,padx=10,pady=10, ipadx=10)


btn_dup = tk.Button(master=frm_buttons, text="Open List", command=openlist)
btn_dup.pack(side=tk.RIGHT,padx=10,pady=10, ipadx=10)

btn_logout = tk.Button(master=frm_buttons, text="Logout", command=log_out)
btn_logout.pack(side=tk.LEFT,padx=10,pady=10, ipadx=10)


# Start the form

window.mainloop()
