import datetime
import pywhatkit as kit
import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkcalendar import DateEntry
import qrcode
from PIL import Image,ImageTk

def main():
    UserDashboard()


class UserDashboard():

    itemlist = []
    total_bill = 0
    total = 0
    userName = ""
    usertype = ""


    def __init__(self):

# ------------------Area for creating window -----------------------------------------#
        self.master = tkinter.Tk()
        self.master.title("Electricity Billing Management System")
        self.master.geometry("1800x950+20+20")
        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window -------------------END----------------------#

# ---Area for creating Tab and widget named notebook that manages a collection of windows/displays----------------------------------------#
        self.notebook = tkinter.ttk.Notebook(self.master)
        self.settingTab = tkinter.LabelFrame(self.notebook)
        self.billingTab = tkinter.LabelFrame(self.notebook)
        self.logoutTab = tkinter.LabelFrame(self.notebook)

        self.notebook.add(self.settingTab, text="Setting")
        self.notebook.add(self.billingTab, text="Billing")
        self.notebook.add(self.logoutTab, text="Logout")
        self.notebook.pack(expand=True, fill="both")

# Inside Setting Tab --------------------------Start-----------------------------------------#

        self.toggle_settingTab_frame = tkinter.LabelFrame(self.settingTab, bg="#158aff")
        self.toggle_settingTab_frame.place(x=0, y=0, height=950, width=288)

# add Menu items in toggle frame------------------Start --------------------

# Dashboard background image ----------Start-----------------------------------------------#

        self.backimage = Image.open("images/background02.jpg")
        self.backimage = self.backimage.resize((1500, 910), Image.BOX)
        self.bakcgroundPhotoImage = ImageTk.PhotoImage(self.backimage)

        self.backgroundlabel = tkinter.Label(self.settingTab, image=self.bakcgroundPhotoImage)
        self.backgroundlabel.place(x=286, y=0)

# Dashboard background image ----------End-----------------------------------------------#
        self.addNewCustomer_Btn = tkinter.Button(self.toggle_settingTab_frame, text="Customer Registration",
                                             font=("bookman old style", 15),
                                             anchor="w", width=21, height=1, bg="#158aff", fg="white",
                                             command=self.addnewcustomerForm)

        self.addNewCustomer_Btn.grid(row=0, column=0)

        self.meterInfo_btn = tkinter.Button(self.toggle_settingTab_frame, text="Meter Information",
                                            font=("bookman old style", 15),
                                            anchor="w", width=21, height=1, bg="#158aff", fg="white",
                                            command=self.meterinfoForm)
        self.meterInfo_btn.grid(row=1, column=0)

        self.services_btn = tkinter.Button(self.toggle_settingTab_frame, text="Service Charges",
                                           font=("bookman old style", 15),
                                           anchor="w", width=21, height=1, bg="#158aff", fg="white",
                                           command=self.servicechargesForm)
        self.services_btn.grid(row=2, column=0)

# Area for user Login Details ----------Start-----------------------------------------------#

        self.userimage = Image.open("images/electricitybillpay.png")
        self.userimage = self.userimage.resize((248, 250), Image.BOX)
        self.userPhotoImage = ImageTk.PhotoImage(self.userimage)

        self.userLogin(self.toggle_settingTab_frame, self.userPhotoImage)

# Area for user Login Details ----------End-----------------------------------------------#

# Inside Setting Tab --------------------------End----------------------------------------------------------#

# Inside Billing Tab ------------------------------------------Start-----------------------------------------#

        self.toggle_subBillingTab_frame = tkinter.LabelFrame(self.billingTab, bg="#158aff")
        self.toggle_subBillingTab_frame.place(x=0, y=0, height=950, width=288)

# add toggle menu items

        self.billDetails_btn = tkinter.Button(self.toggle_subBillingTab_frame, text="Billing Details",
                                             font=("bookman old style", 15),
                                             anchor="w", width=21, height=1, bg="#158aff", fg="white", command=self.billingForm)
        self.billDetails_btn.grid(row=0, column=0)

        self.calculatebill_btn = tkinter.Button(self.toggle_subBillingTab_frame, text="Calculate Bill",
                                              font=("bookman old style", 15),
                                              anchor="w", width=21, height=1, bg="#158aff", fg="white", command=self.calculatebillForm)
        self.calculatebill_btn.grid(row=1, column=0)

# Area for user Login Details ----------Start-----------------------------------------------#

        self.userLogin(self.toggle_subBillingTab_frame, self.userPhotoImage)

# Area for user Login Details ----------End-----------------------------------------------#

# Inside Billing Tab ------------------------------------------End-----------------------------------------#

# Inside Logout Tab ------------------------Start----------------------------------------------------------#

        self.subLogoutTabFrame = tkinter.LabelFrame(self.logoutTab, bg="#158aff")
        self.subLogoutTabFrame.place(x=0, y=0, height=950, width=288)

        # add toggle menu items

        self.Logout_btn = tkinter.Button(self.subLogoutTabFrame, text="Log out",
                                              font=("bookman old style", 15),
                                              anchor="w", width=21, height=1, bg="#158aff", fg="white", command=self.logout)
        self.Logout_btn.grid(row=0, column=0)

        self.support_btn = tkinter.Button(self.subLogoutTabFrame, text="Support", font=("bookman old style", 15),
                                           anchor="w", width=21, height=1, bg="#158aff", fg="white")
        self.support_btn.grid(row=3, column=0)

        self.feedback_btn = tkinter.Button(self.subLogoutTabFrame, text="Feedback", font=("bookman old style", 15),
                                            anchor="w", width=21, height=1, bg="#158aff", fg="white")
        self.feedback_btn.grid(row=4, column=0)

# Area for user Login Details ----------Start-----------------------------------------------#

        self.userLogin(self.subLogoutTabFrame, self.userPhotoImage)

# Area for user Login Details ----------End-----------------------------------------------#

# Inside Logout Tab ------------------------End----------------------------------------------------------#

#----------------------------------setting tab all functions --------------------Start---------------------------------
        self.master.mainloop()
#----------------------------------------------- Area for add new customer -------------------------#
    def addnewcustomerForm(self):

        self.AddNewCustomerframe = tkinter.LabelFrame(self.settingTab, bg="#EDF5F4")
        self.AddNewCustomerframe.place(x=288, y=0, height=950, width=650)

        self.TitleAddCustomer_Label = tkinter.Label(self.AddNewCustomerframe, text="Customer Registration:", font=("bookman old style", 20, "underline","bold"))
        self.TitleAddCustomer_Label.place(x=20, y=20)

        self.CustomerName_Label = tkinter.Label(self.AddNewCustomerframe, text="Customer Name: ", font=("bookman old style", 15))
        self.CustomerName_Label.place(x=20, y=90)

        self.CustomerNameEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.CustomerNameEntry.place(x=250, y=90)
        self.CustomerNameEntry.focus_set()
        # self.FirstNameEntry.bind("<Return>", self.on_enter_firstName)

        self.PhoneNoLabel = tkinter.Label(self.AddNewCustomerframe, text="Phone No: ", font=("bookman old style", 15))
        self.PhoneNoLabel.place(x=20, y=130)

        self.PhoneNoEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.PhoneNoEntry.place(x=250, y=130)
        # self.PhoneNoEntry.bind("<Return>", self.on_enter_phoneno)

        self.EmaiIdLabel = tkinter.Label(self.AddNewCustomerframe, text="Email Id: ", font=("bookman old style", 15))
        self.EmaiIdLabel.place(x=20, y=170)

        self.EmailIDEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.EmailIDEntry.place(x=250, y=170)

        self.address_Label = tkinter.Label(self.AddNewCustomerframe, text="Address: ", font=("bookman old style", 15))
        self.address_Label.place(x=20, y=210)

        self.addressEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.addressEntry.place(x=250, y=210)

        self.city_Label = tkinter.Label(self.AddNewCustomerframe, text="City: ", font=("bookman old style", 15))
        self.city_Label.place(x=20, y=250)

        self.cityEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.cityEntry.place(x=250, y=250)

        self.state_Label = tkinter.Label(self.AddNewCustomerframe, text="State: ", font=("bookman old style", 15))
        self.state_Label.place(x=20, y=290)

        self.stateEntry = tkinter.Entry(self.AddNewCustomerframe, width=29, font=("bookman old style", 15))
        self.stateEntry.place(x=250, y=290)

        self.addcanceltbnimage = Image.open("icon/cancel13.png")
        self.addcanceltbnimage = self.addcanceltbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddcancelbtnimage = ImageTk.PhotoImage(self.addcanceltbnimage)

        self.cancelbtn = tkinter.Button(self.AddNewCustomerframe, text="Cancel", width=168,height=30,font=("bookman old style", 15),
                                        command=self.resetAddNewCustomerForm, bg="#FF7575", fg="white",
                                         image=self.imagePhotoaddcancelbtnimage, compound=tkinter.RIGHT)
        self.cancelbtn.place(x=250, y=330)

        self.addmovetbnimage = Image.open("icon/move1.png")
        self.addmovetbnimage = self.addmovetbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddmovebtnimage = ImageTk.PhotoImage(self.addmovetbnimage)

        self.movetbtn = tkinter.Button(self.AddNewCustomerframe, text="Move",width=168, height=30,
                                       font=("bookman old style", 15), bg="#FFFF99",
                                       command=self.movetometerinfoForm, image=self.imagePhotoaddmovebtnimage, compound=tkinter.RIGHT)
        self.movetbtn.place(x=427, y=330)

# ----------------------- Customer details- ------------------------------------------------------------------

# New frame for list of customers
        self.AllCustomerframe = tkinter.LabelFrame(self.settingTab, bg="#EDF5F4")
        self.AllCustomerframe.place(x=937, y=0, height=1000, width=849)

        self.CustomerDetailsTextArea = tkinter.Text(self.AllCustomerframe, width=90, height=44)
        self.CustomerDetailsTextArea.grid(row=0, column=0)

# ----------------------- Customer details- ---end---------------------------------------------------------------

# -------------- all functions ----------------------

    def resetAddNewCustomerForm(self):

        self.CustomerNameEntry.delete(0,tkinter.END)
        self.PhoneNoEntry.delete(0,tkinter.END)
        self.EmailIDEntry.delete(0,tkinter.END)
        self.addressEntry.delete(0,tkinter.END)
        self.cityEntry.delete(0,tkinter.END)
        self.stateEntry.delete(0,tkinter.END)
        self.CustomerNameEntry.focus_set()

    def movetometerinfoForm(self):

        self.CustomerDetailsTextArea.delete("1.0", tkinter.END)
        self.itemlist.clear()

        # after_count_space S1, s2, s3 and so on

        s1 = " " * 10
        s2 = " " * 5
        s3 = " " * 7
        s4 = " " * 3
        s5 = " " * 3
        s6 = " " * 10
        s7 = " " * 9

        ItemHead = "." * 30 + "New Customer Details" + "." * 30 + "\n\n"

        self.itemlist.append(ItemHead)

        data = (
                f" Customer Name:         {s2}| {self.CustomerNameEntry.get()}\n"
                f" Phone No:            {s3}| {self.PhoneNoEntry.get()}\n"
                f" Email ID:                {s4}| {self.EmailIDEntry.get()}\n"
                f" Address:                 {s5}| {self.addressEntry.get()}\n"
                f" City:             {s6}| {self.cityEntry.get()}\n"
                f" State:             {s7}| {self.stateEntry.get()}\n"
                f"\n")

        self.itemlist.append(data)

        self.CustomerDetailsTextArea.delete("1.0", tkinter.END)
        for item in self.itemlist:
            self.CustomerDetailsTextArea.insert(tkinter.END, str(item))

        self.meterinfoForm()

# -----------------------------------------End Add new customer -----------------------------------------------------------

# ------------------------------Meter information --------------------------------------------------------------------------

    def meterinfoForm(self):
        self.meterinfoframe = tkinter.LabelFrame(self.settingTab, bg="#EDF5F4")
        self.meterinfoframe.place(x=288, y=0, height=950, width=650)

        self.TitleAddMeterinfo_Label = tkinter.Label(self.meterinfoframe, text="Meter Registration:", font=("bookman old style", 20, "underline","bold"))
        self.TitleAddMeterinfo_Label.place(x=20, y=20)

        self.meter_no_Label = tkinter.Label(self.meterinfoframe, text="Meter No: ", font=("bookman old style", 15))
        self.meter_no_Label.place(x=20, y=90)

        self.meternoEntry = tkinter.Entry(self.meterinfoframe, width=29, font=("bookman old style", 15))
        self.meternoEntry.place(x=250, y=90)
        self.meternoEntry.focus_set()

        self.meterlocation_Label = tkinter.Label(self.meterinfoframe, text="Meter Location: ", font=("bookman old style", 15))
        self.meterlocation_Label.place(x=20, y=130)

        self.meterLocationEntry = tkinter.Entry(self.meterinfoframe, width=29, font=("bookman old style", 15))
        self.meterLocationEntry.place(x=250, y=130)

        self.meterTypeLabel = tkinter.Label(self.meterinfoframe, text="Meter Type: ", font=("bookman old style", 15))
        self.meterTypeLabel.place(x=20, y=170)

        self.meterTypeEntry = tkinter.Entry(self.meterinfoframe, width=29, font=("bookman old style", 15))
        self.meterTypeEntry.place(x=250, y=170)

        self.phaseCodeLabel = tkinter.Label(self.meterinfoframe, text="Phase Code: ", font=("bookman old style", 15))
        self.phaseCodeLabel.place(x=20, y=210)

        self.phaseCodeEntry = tkinter.Entry(self.meterinfoframe, width=29, font=("bookman old style", 15))
        self.phaseCodeEntry.place(x=250, y=210)

        self.billType_Label = tkinter.Label(self.meterinfoframe, text="Bill Type: ", font=("bookman old style", 15))
        self.billType_Label.place(x=20, y=250)

        self.billTypeEntry = tkinter.Entry(self.meterinfoframe, width=29, font=("bookman old style", 15))
        self.billTypeEntry.place(x=250, y=250)
        # self.addressEntry.bind("<Return>", self.on_enter_address)

        self.dateLabel = tkinter.Label(self.meterinfoframe, text="Date: ", font=("bookman old style", 15))
        self.dateLabel.place(x=20, y=290)

        self.dateEntry = DateEntry(self.meterinfoframe, selectmode="day", date_pattern="dd/mm/yyyy", sticky="w",
                                   font=("bookman old style", 15))
        self.dateEntry.configure(width=27)
        self.dateEntry.place(x=250, y=290)

        self.addcanceltbnimage = Image.open("icon/cancel13.png")
        self.addcanceltbnimage = self.addcanceltbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddcancelbtnimage = ImageTk.PhotoImage(self.addcanceltbnimage)

        self.cancelbtn = tkinter.Button(self.meterinfoframe, text="Cancel", width=168,height=30,font=("bookman old style", 15),
                                        command=self.resetMeterInfoForm, bg="#FF7575", fg="white",
                                         image=self.imagePhotoaddcancelbtnimage, compound=tkinter.RIGHT)
        self.cancelbtn.place(x=250, y=330)

        self.addmovetbnimage = Image.open("icon/move1.png")
        self.addmovetbnimage = self.addmovetbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddmovebtnimage = ImageTk.PhotoImage(self.addmovetbnimage)

        self.movetowardsSChbtn = tkinter.Button(self.meterinfoframe, text="Move",width=168, height=30,
                                                font=("bookman old style", 15), bg="#FFFF99",
                                                command=self.movetowardsserviceChargeForm, image=self.imagePhotoaddmovebtnimage, compound=tkinter.RIGHT)
        self.movetowardsSChbtn.place(x=427, y=330)



# -------------- all functions ----------------------

    def resetMeterInfoForm(self):
        self.meternoEntry.delete(0,tkinter.END)
        self.meterLocationEntry.delete(0,tkinter.END)
        self.meterTypeEntry.delete(0,tkinter.END)
        self.phaseCodeEntry.delete(0,tkinter.END)
        self.billTypeEntry.delete(0,tkinter.END)
        self.dateEntry.set_date(date=datetime.date.today())
        self.meternoEntry.focus_set()

    def movetowardsserviceChargeForm(self):

        #self.CustomerDetailsTextArea.delete("1.0", tkinter.END)

        # after_count_space S1, s2, s3 and so on

        s1 = " " * 10
        s2 = " " * 9
        s3 = " " * 3
        s4 = " " * 2
        s5 = " " * 2
        s6 = " " * 7
        s7 = " " * 12



        data = (
            f" Meter No:          {s2}| {self.meternoEntry.get()}\n"
            f" Meter Location:          {s3}| {self.meterLocationEntry.get()}\n"
            f" Meter Type:               {s4}| {self.meterTypeEntry.get()}\n"
            f" Phase Code:               {s5}| {self.phaseCodeEntry.get()}\n"
            f" Bill Type:           {s6}| {self.billTypeEntry.get()}\n"
            f" Date:           {s7}| {self.dateEntry.get()}\n"
            f"\n")

        self.itemlist.append(data)

        self.CustomerDetailsTextArea.delete("1.0", tkinter.END)
        for item in self.itemlist:
            self.CustomerDetailsTextArea.insert(tkinter.END, str(item))


        self.servicechargesForm()


# --------------------------------------Meter Information End --------------------------------------------------------------

# ---------------------------------------Service Charges ----------------------------------------------------------------
    def servicechargesForm(self):

        self.totalLabel_var = tkinter.StringVar()


        self.serviceChargesframe = tkinter.LabelFrame(self.settingTab, bg="#EDF5F4")
        self.serviceChargesframe.place(x=288, y=0, height=950, width=650)

        self.TitleServiceChargesinfo_Label = tkinter.Label(self.serviceChargesframe, text="Service Charges:",
                                                     font=("bookman old style", 20, "underline","bold"))
        self.TitleServiceChargesinfo_Label.place(x=20, y=20)

        self.meterFileChargeLabel = tkinter.Label(self.serviceChargesframe, text="Meter File Charge: ", font=("bookman old style", 15))
        self.meterFileChargeLabel.place(x=20, y=90)

        self.meterFileChargeEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))

        self.meterFileChargeEntry.place(x=280, y=90)
        self.meterFileChargeEntry.focus_set()

        self.meterFileChargeEntry.bind("<FocusOut>", self.updateLabelafter)


        self.meterChargeLabel = tkinter.Label(self.serviceChargesframe, text="Meter Charge: ",
                                                 font=("bookman old style", 15))
        self.meterChargeLabel.place(x=20, y=130)

        self.meterChargeEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))

        self.meterChargeEntry.place(x=280, y=130)

        self.meterChargeEntry.bind("<FocusOut>", self.updateLabelafter)


        self.connectionChargeLabel = tkinter.Label(self.serviceChargesframe, text="Connection Charge: ", font=("bookman old style", 15))
        self.connectionChargeLabel.place(x=20, y=170)

        self.connectionChargeEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))

        self.connectionChargeEntry.place(x=280, y=170)

        self.connectionChargeEntry.bind("<FocusOut>", self.updateLabelafter)


        self.labourChargeLabel = tkinter.Label(self.serviceChargesframe, text="Labour Charge: ", font=("bookman old style", 15))
        self.labourChargeLabel.place(x=20, y=210)

        self.labourChargeEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))
        self.labourChargeEntry.place(x=280, y=210)
        self.labourChargeEntry.bind("<FocusOut>", self.updateLabelafter)


        self.totalLabel = tkinter.Label(self.serviceChargesframe, text="Rs. ",
                                                  font=("bookman old style", 15), textvariable=self.totalLabel_var)
        self.totalLabel.place(x=280, y=250)

        self.advanceDepositeLabel = tkinter.Label(self.serviceChargesframe, text="Advance Deposite: ", font=("bookman old style", 15))
        self.advanceDepositeLabel.place(x=20, y=290)


        self.advanceDepositeEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))
        self.advanceDepositeEntry.place(x=280, y=290)
        self.advanceDepositeEntry.bind("<FocusOut>", self.updateLabelafter)

        self.balanceLabel = tkinter.Label(self.serviceChargesframe, text="Balance: ", font=("bookman old style", 15))
        self.balanceLabel.place(x=20, y=330)

        self.balanceEntry = tkinter.Entry(self.serviceChargesframe, width=26, font=("bookman old style", 15))

        self.balanceEntry.place(x=280, y=330)
        # self.cityEntry.bind("<Return>", self.on_enter_city)

        # self.stateEntry.bind("<Return>", self.on_enter_state)

        self.addcanceltbnimage = Image.open("icon/cancel13.png")
        self.addcanceltbnimage = self.addcanceltbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddcancelbtnimage = ImageTk.PhotoImage(self.addcanceltbnimage)

        self.cancelbtn = tkinter.Button(self.serviceChargesframe, text="Cancel", width=153, height=30, bg="#FF7575",
                                        font=("bookman old style", 15), command=self.resetserviceChargeForm, fg="white",
                                        image=self.imagePhotoaddcancelbtnimage, compound=tkinter.RIGHT)
        self.cancelbtn.place(x=280, y=370)

        self.addsubmitbnimage = Image.open("icon/save1.png")
        self.addsubmitbnimage = self.addsubmitbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddsubmitbtnimage = ImageTk.PhotoImage(self.addsubmitbnimage)

        self.submitbtn = tkinter.Button(self.serviceChargesframe, text="Submit", width=153, height=30, bg="#ceffcf",
                                        font=("bookman old style", 15), command=self.movetowardsubmit, image=self.imagePhotoaddsubmitbtnimage, compound=tkinter.RIGHT)
        self.submitbtn.place(x=442, y=370)

# -------------- all functions ----------------------

    def resetserviceChargeForm(self):
        self.meterFileChargeEntry.configure(state=tkinter.NORMAL)
        self.meterChargeEntry.configure(state=tkinter.NORMAL)
        self.connectionChargeEntry.configure(state=tkinter.NORMAL)
        self.labourChargeEntry.configure(state=tkinter.NORMAL)

        self.advanceDepositeEntry.configure(state=tkinter.NORMAL)
        self.balanceEntry.configure(state=tkinter.NORMAL)

        self.meterFileChargeEntry.delete(0,tkinter.END)
        self.meterChargeEntry.delete(0,tkinter.END)
        self.connectionChargeEntry.delete(0,tkinter.END)
        self.labourChargeEntry.delete(0,tkinter.END)
        self.totalLabel_var.set("Rs. ")
        self.advanceDepositeEntry.delete(0,tkinter.END)
        self.balanceEntry.delete(0,tkinter.END)
        self.total = 0

        self.meterFileChargeEntry.focus_set()


    def updateLabelafter(self,event):

            if self.meterFileChargeEntry.get() == "":
                self.total += 0

            else:

                self.total += int(self.meterFileChargeEntry.get())
                self.meterFileChargeEntry.configure(state=tkinter.DISABLED)

            if self.meterChargeEntry.get() == "":
                self.total += 0

            else:

                self.total -= int(self.meterFileChargeEntry.get())
                self.total += int(self.meterChargeEntry.get())
                self.meterChargeEntry.configure(state=tkinter.DISABLED)

            if self.connectionChargeEntry.get() == "":
                self.total += 0

            else:
                self.total -= int(self.meterChargeEntry.get())
                self.total += int(self.connectionChargeEntry.get())
                self.connectionChargeEntry.configure(state=tkinter.DISABLED)


            if self.labourChargeEntry.get() == "":
                self.total += 0

            else:
                self.total -= int(self.connectionChargeEntry.get())
                self.total += int(self.labourChargeEntry.get())
                self.labourChargeEntry.configure(state=tkinter.DISABLED)

            if self.advanceDepositeEntry.get() == "":
                self.total += 0

            else:

                a = self.total
                a -= int(self.labourChargeEntry.get())
                a -= int(self.advanceDepositeEntry.get())
                self.total -= int(self.labourChargeEntry.get())
                self.balanceEntry.insert(0,str(a))
                self.advanceDepositeEntry.configure(state=tkinter.DISABLED)


            self.totalLabel_var.set("Rs. "+str(self.total))
            #print(self.total)


 

    def movetowardsubmit(self):

        # self.CustomerDetailsTextArea.delete("1.0", tkinter.END)

        # after_count_space S1, s2, s3 and so on

        s1 = " " * 10
        s2 = " " * 5
        s3 = " " * 7
        s4 = " " * 3
        s5 = " " * 10
        s6 = " " * 15

        data = (
            f" Meter File Charge:     {s2}| Rs. {self.meterFileChargeEntry.get()}\n"
            f" Meter Charge:        {s3}| Rs. {self.meterChargeEntry.get()}\n"
            f" New Connection Charge:   {s4}| Rs. {self.connectionChargeEntry.get()}\n"
            f" Labour Charge:    {s5}| Rs. {self.labourChargeEntry.get()}\n"
            f" Advance Deposite: {s5}| Rs. {self.advanceDepositeEntry.get()}\n"
            f" Balance Amount:   {s5}| Rs. {self.balanceEntry.get()}\n"
            f"\n")

        self.itemlist.append(data)

        self.CustomerDetailsTextArea.delete("1.0", tkinter.END)
        for item in self.itemlist:
            self.CustomerDetailsTextArea.insert(tkinter.END, str(item))

        self.submitfromServiceChargeForm()

    def submitfromServiceChargeForm(self):

    # data from customer form -------------------------

        u1 = self.CustomerNameEntry.get().lower()
        u2 = self.PhoneNoEntry.get().lower()
        u3 = self.EmailIDEntry.get().lower()
        u4 = self.addressEntry.get().lower()
        u5 = self.cityEntry.get().lower()
        u6 = self.stateEntry.get().lower()

# data from meter info form -------------

        u7 = self.meternoEntry.get().lower()
        u8 = self.meterLocationEntry.get().lower()
        u9 = self.meterTypeEntry.get().lower()
        u10 = self.phaseCodeEntry.get().lower()
        u11 = self.billTypeEntry.get().lower()
        u12 = self.dateEntry.get()

# data from service charge form ------------------------------

        u13 = self.meterFileChargeEntry.get().lower()
        u14 = self.meterChargeEntry.get().lower()
        u15 = self.connectionChargeEntry.get().lower()
        u16 = self.labourChargeEntry.get().lower()
        u17 = self.advanceDepositeEntry.get().lower()
        u18 = self.balanceEntry.get().lower()

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()


            q = f"insert into customer (name, meter_no, phone_no, email_id, address, city, state) values ('{u1}','{u7}','{u2}', '{u3}', '{u4}', '{u5}', '{u6}');"

            q1 = f"insert into meter_info (meter_no, meter_location, meter_type, phase_code, bill_type, date) values ('{u7}','{u8}','{u9}', '{u10}', '{u11}', '{u12}');"

            q2 = f"insert into service_charge (meter_no, meter_file_charge, meter_charge, conn_charge, labour_charge, advance_deposite, balance) values ('{u7}','{u13}','{u14}', '{u15}', '{u16}', '{u17}', '{u18}');"

            self.mycursor.execute(q)
            self.myconnect.commit()

            self.mycursor.execute(q1)
            self.myconnect.commit()

            self.mycursor.execute(q2)
            self.myconnect.commit()

            s1 = "*" * 30

            a = f"{s1} Data Submit Successfully {s1}\n"
            self.itemlist.append(a)

            self.CustomerDetailsTextArea.delete("1.0", tkinter.END)
            for item in self.itemlist:
                self.CustomerDetailsTextArea.insert(tkinter.END, str(item))

            tkinter.messagebox.showinfo("Success", "Data saved successfully")

            self.resetserviceChargeForm()

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()

# --------------------------------------Service Charges End ----------------------------------------------------------


# ------------------------------billing Tab Area----------------------------------------------------

    def billingForm(self):

            self.subBillingTab_frame = tkinter.LabelFrame(self.billingTab, bg="#EDF5F4")
            self.subBillingTab_frame.place(x=288, y=0, height=950, width=650)

            self.TitlefindCustomer_Label = tkinter.Label(self.subBillingTab_frame, text="Find Customer Bill Details:",
                                                    font=("bookman old style", 20, "underline","bold"))
            self.TitlefindCustomer_Label.place(x=20, y=20)

            self.findcustomerbillingframe = tkinter.LabelFrame(self.subBillingTab_frame, bg="#EDF5F4")
            self.findcustomerbillingframe.place(x=20, y=70, height=120, width=600)

            self.billingMeterno_Label = tkinter.Label(self.findcustomerbillingframe, text="Meter No: ",
                                                      font=("bookman old style", 15))
            self.billingMeterno_Label.place(x=20, y=20)

            self.paybillMeternoEntry = tkinter.Entry(self.findcustomerbillingframe, width=26, font=("bookman old style", 15))
            self.paybillMeternoEntry.place(x=250, y=20)
            self.paybillMeternoEntry.focus_set()
            self.paybillMeternoEntry.bind("<Return>", self.on_enter_paybillmeternoEntry)


            self.addfindbtnimage = Image.open("icon/find2.jpg")
            self.addfindbtnimage = self.addfindbtnimage.resize((26, 26), Image.BOX)
            self.imagePhotoaddfindbtnimage = ImageTk.PhotoImage(self.addfindbtnimage)

            self.findcustomerbtn = tkinter.Button(self.findcustomerbillingframe, text="Find", width=114, height=30,
                                          font=("bookman old style", 15), command=self.findbilling, bg="#acfeff",
                                          image=self.imagePhotoaddfindbtnimage, compound=tkinter.LEFT)
            self.findcustomerbtn.place(x=250, y=60)
            self.findcustomerbtn.bind("<Return>", self.on_enterFindBtn)

            self.Titlepaybill_Label = tkinter.Label(self.subBillingTab_frame, text="Pay Bill:",
                                                     font=("bookman old style", 20, "underline","bold"))
            self.Titlepaybill_Label.place(x=20, y=280)

            self.paybillframe = tkinter.LabelFrame(self.subBillingTab_frame, bg="#EDF5F4")
            self.paybillframe.place(x=20, y=330, height=160, width=600)

            self.selectMonthLabel = tkinter.Label(self.paybillframe, text="Month: ",
                                               font=("bookman old style", 15))
            self.selectMonthLabel.place(x=20, y=20)

            self.selectmonthCombobox = tkinter.ttk.Combobox(self.paybillframe,
                                                              values=["", "January", "February", "March", "April",
                                                                      "May",
                                                                      "June", "July", "August", "September", "August",
                                                                      "September", "October", "November", "December"],
                                                              width=20, font=("bookman old style", 15))

            self.selectmonthCombobox.configure(width=24)
            self.selectmonthCombobox.place(x=250, y=20)
            self.selectmonthCombobox.bind("<Return>", self.on_enter_selectmonthCombobox)

            self.billamountLabel = tkinter.Label(self.paybillframe, text="Bill Amount Rs: ",
                                               font=("bookman old style", 15))
            self.billamountLabel.place(x=20, y=60)

            self.billamountEntry = tkinter.Entry(self.paybillframe, width=26, font=("bookman old style", 15))
            self.billamountEntry.place(x=250, y=60)
            self.billamountEntry.bind("<Return>", self.on_enter_billamountEntry)


            self.addpaybtnimage = Image.open("icon/rupee2.jpg")
            self.addpaybtnimage = self.addpaybtnimage.resize((26, 26), Image.BOX)
            self.imagePhotoaddpaybtnimage = ImageTk.PhotoImage(self.addpaybtnimage)

            self.paybtn = tkinter.Button(self.paybillframe, text="Pay", width=125, height=30,
                                         font=("bookman old style", 15), command=self.payment, bg="#ceffcf",
                                         image=self.imagePhotoaddpaybtnimage, compound=tkinter.RIGHT)
            self.paybtn.place(x=250, y=100)
            self.paybtn.bind("<Return>", self.on_enter_paymentBtn)


            self.Titlebillsend_Label = tkinter.Label(self.subBillingTab_frame, text="Send Information to Customer:",
                                                     font=("bookman old style", 20, "underline", "bold"))
            self.Titlebillsend_Label.place(x=20, y=600)

            self.sendbillframe = tkinter.LabelFrame(self.subBillingTab_frame, bg="#EDF5F4")
            self.sendbillframe.place(x=20, y=650, height=200, width=600)

            self.wbno_Label = tkinter.Label(self.sendbillframe, text="WhatsApp No: ",
                                            font=("bookman old style", 15))
            self.wbno_Label.place(x=20, y=20)

            self.wbnoEntry = tkinter.Entry(self.sendbillframe, width=26, font=("bookman old style", 15))
            self.wbnoEntry.place(x=235, y=20)
            self.wbnoEntry.bind("<Return>", self.on_enter_wbnoEntry)

            self.selectMonthLabel = tkinter.Label(self.sendbillframe, text="Month: ",
                                                  font=("bookman old style", 15))
            self.selectMonthLabel.place(x=20, y=60)

            self.selectmonthwbCombobox = tkinter.ttk.Combobox(self.sendbillframe,
                                                            values=["", "January", "February", "March", "April",
                                                                    "May",
                                                                    "June", "July", "August", "September", "August",
                                                                    "September", "October", "November", "December"],
                                                            width=20, font=("bookman old style", 15))

            self.selectmonthwbCombobox.configure(width=24)
            self.selectmonthwbCombobox.place(x=235, y=60)
            self.selectmonthwbCombobox.bind("<Return>", self.on_entermonthcombobox)

            self.billamountLabel = tkinter.Label(self.sendbillframe, text="Bill Amount Rs: ",
                                                 font=("bookman old style", 15))
            self.billamountLabel.place(x=20, y=100)

            self.billamountwbEntry1 = tkinter.Entry(self.sendbillframe, width=26, font=("bookman old style", 15))
            self.billamountwbEntry1.place(x=235, y=100)
            self.billamountwbEntry1.bind("<Return>",self.on_enter_billamountEntry1)

            self.addshowbtnimage = Image.open("icon/send.png")
            self.addshowbtnimage = self.addshowbtnimage.resize((40, 40), Image.BOX)
            self.imagePhotoaddshowbtnimage = ImageTk.PhotoImage(self.addshowbtnimage)

            self.sendbtn = tkinter.Button(self.sendbillframe, text="Send", width=113, height=30, bg="#FFB733",
                                          font=("bookman old style", 15), command=self.sendmessage,
                                          image=self.imagePhotoaddshowbtnimage, compound=tkinter.RIGHT)
            self.sendbtn.place(x=235, y=140)
            self.sendbtn.bind("<Return>", self.on_enterSendBtn)



# ----------------------- Billing details- ------------------------------------------------------------------

            # New frame for list of customers
            self.subBillingDetailsframe = tkinter.LabelFrame(self.billingTab, bg="#EDF5F4")
            self.subBillingDetailsframe.place(x=937, y=0, height=1000, width=849)

            self.BillingDetailsTextArea = tkinter.Text(self.subBillingDetailsframe, width=90, height=44)
            self.BillingDetailsTextArea.grid(row=0, column=0)

    def calculatebillForm(self):
        self.subCalTab_frame = tkinter.LabelFrame(self.billingTab, bg="#EDF5F4")
        self.subCalTab_frame.place(x=288, y=0, height=950, width=650)

        self.TitlCal_Label = tkinter.Label(self.subCalTab_frame, text="Calculate Bill:",
                                                font=("bookman old style", 20, "underline","bold"))
        self.TitlCal_Label.place(x=20, y=20)

        self.calMeterno_Label = tkinter.Label(self.subCalTab_frame, text="Meter No: ",
                                                  font=("bookman old style", 15))
        self.calMeterno_Label.place(x=20, y=90)

        self.calMeternoEntry = tkinter.Entry(self.subCalTab_frame, width=29, font=("bookman old style", 15))
        self.calMeternoEntry.place(x=250, y=90)
        self.calMeternoEntry.focus_set()
        self.calMeternoEntry.bind("<Return>", self.on_enter_calmeternoentry)

        self.addfindcalbtnimage = Image.open("icon/find2.jpg")
        self.addfindcalbtnimage = self.addfindcalbtnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddfindcalbtnimage = ImageTk.PhotoImage(self.addfindcalbtnimage)


        self.findcustomerbtn1 = tkinter.Button(self.subCalTab_frame, text="Find", width=114, height=30, bg="#acfeff",
                                      font=("bookman old style", 15), command = self.findcustomer,
                                      image=self.imagePhotoaddfindcalbtnimage, compound=tkinter.LEFT)
        self.findcustomerbtn1.place(x=250, y=130)
        self.findcustomerbtn1.bind("<Return>", self.on_enter_findcustomer)

        self.monthLabel = tkinter.Label(self.subCalTab_frame, text="Month: ",
                                        font=("bookman old style", 15))
        self.monthLabel.place(x=20, y=180)

        self.calmonthCombobox = tkinter.ttk.Combobox(self.subCalTab_frame,
                                                  values=["", "January", "February", "March", "April", "May",
                                                          "June", "July", "August", "September", "August",
                                                          "September", "October", "November", "December"],
                                                  width=20, font=("bookman old style", 15))

        self.calmonthCombobox.configure(width=27)
        self.calmonthCombobox.place(x=250, y=180)
        self.calmonthCombobox.bind("<Return>", self.on_enter_calmonthcombobox)


        self.calunitconsumedLabel = tkinter.Label(self.subCalTab_frame, text="Units Consumed: ",
                                        font=("bookman old style", 15))
        self.calunitconsumedLabel.place(x=20, y=220)

        self.calunitconsumedEntry = tkinter.Entry(self.subCalTab_frame, width=29, font=("bookman old style", 15))
        self.calunitconsumedEntry.place(x=250, y=220)
        self.calunitconsumedEntry.bind('<Return>', self.on_enter_calunitconsumedEntry)

        self.addcanceltbnimage = Image.open("icon/cancel13.png")
        self.addcanceltbnimage = self.addcanceltbnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddcancelbtnimage = ImageTk.PhotoImage(self.addcanceltbnimage)

        self.calcancelbtn = tkinter.Button(self.subCalTab_frame, text="Cancel", width=168, height=30,
                                        font=("bookman old style", 15), bg="#FF7575", fg="white",
                                         image=self.imagePhotoaddcancelbtnimage,
                                        compound=tkinter.RIGHT)
        self.calcancelbtn.place(x=250, y=260)

        self.addcalbtnimage = Image.open("icon/calculate.png")
        self.addcalbtnimage = self.addcalbtnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddcalbtnimage = ImageTk.PhotoImage(self.addcalbtnimage)

        self.calculatebtn = tkinter.Button(self.subCalTab_frame, text="Calculate", width=168, height=30,
                                     font=("bookman old style", 15), command=self.calculateBill, bg="#ceffcf",
                                           image=self.imagePhotoaddcalbtnimage, compound=tkinter.RIGHT)

        self.calculatebtn.place(x=428, y=260)
        self.calculatebtn.bind("<Return>", self.on_enter_calculatebtn)

        self.addgeneratebtnimage = Image.open("icon/generate.jpg")
        self.addgeneratebtnimage = self.addgeneratebtnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddgeneratebtnimage = ImageTk.PhotoImage(self.addgeneratebtnimage)

        self.generatebtn = tkinter.Button(self.subCalTab_frame, text="Generate Bill", width=345, height=30,
                                          font=("bookman old style", 15), command=self.generatebill, bg="#be9aff",
                                          image=self.imagePhotoaddgeneratebtnimage, compound=tkinter.RIGHT)
        self.generatebtn.place(x=250, y=300)

# ---------------All function -------------------------------------#

# ------------------------Find Tab all function ------------------------------------------------------
    def findCustomerForm(self):
        self.FindCustomerframe = tkinter.LabelFrame(self.findTab, bg="#EDF5F4")
        self.FindCustomerframe.place(x=237, y=0, height=720, width=514)

        self.TitleFindCustomer_Labe = tkinter.Label(self.FindCustomerframe, text="_____Find Customer Details____",
                                                    font=("bookman old style", 20, "bold"))
        self.TitleFindCustomer_Labe.place(x=20, y=20)

        self.findCustomerframe = tkinter.LabelFrame(self.FindCustomerframe, bg="#EDF5F4")
        self.findCustomerframe.place(x=20, y=70, height=200, width=455)

        self.FindMeterNumber_Labe = tkinter.Label(self.findCustomerframe, text="Meter No: ",
                                                  font=("bookman old style", 15))
        self.FindMeterNumber_Labe.place(x=20, y=20)

        self.FindMeterNumberEntry = tkinter.Entry(self.findCustomerframe, width=20, font=("bookman old style", 15))
        self.FindMeterNumberEntry.place(x=180, y=20)

        self.or_Labe = tkinter.Label(self.findCustomerframe, text="_" * 19 + "OR" + "_" * 19,
                                     font=("bookman old style", 15))
        self.or_Labe.place(x=20, y=60)

        self.FindPhoneNoLabel = tkinter.Label(self.findCustomerframe, text="Phone No: ", font=("bookman old style", 15))
        self.FindPhoneNoLabel.place(x=20, y=100)

        self.FindPhoneNoEntry = tkinter.Entry(self.findCustomerframe, width=20, font=("bookman old style", 15))
        self.FindPhoneNoEntry.place(x=180, y=100)

        self.addfindbtnimage = Image.open("icon/find2.jpg")
        self.addfindbtnimage = self.addfindbtnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddfindbtnimage = ImageTk.PhotoImage(self.addfindbtnimage)

        self.findbtn = tkinter.Button(self.findCustomerframe, text="Find", width=114, height=30,
                                            font=("bookman old style", 15),
                                      image=self.imagePhotoaddfindbtnimage, compound=tkinter.LEFT)
        self.findbtn.place(x=180, y=140)

        self.addshowbtnimage = Image.open("icon/show.png")
        self.addshowbtnimage = self.addshowbtnimage.resize((26, 26), Image.BOX)
        self.imagePhotoaddshowbtnimage = ImageTk.PhotoImage(self.addshowbtnimage)

        self.showPreviousRecordtbtn = tkinter.Button(self.findCustomerframe, text="Show", width=113, height=30,
                                                     font=("bookman old style", 15),
                                                     image=self.imagePhotoaddshowbtnimage, compound=tkinter.RIGHT)
        self.showPreviousRecordtbtn.place(x=305, y=140)

# ----------------------- All Customer details- ------------------------------------------------------------------

# New frame for list of customers
        self.FindAllCustomerDetailsFrame = tkinter.LabelFrame(self.findTab, bg="#EDF5F4")
        self.FindAllCustomerDetailsFrame.place(x=751, y=0, height=750, width=740)

        self.FindCustomerDetailsTextArea = tkinter.Text(self.FindAllCustomerDetailsFrame, width=90, height=44)
        self.FindCustomerDetailsTextArea.grid(row=0, column=0)

# ----------------------- Customer details- ---end---------------------------------------------------------------

#----------- all functions ------------------------

    def on_enter_paybillmeternoEntry(self, event):
        self.findcustomerbtn.focus_set()


    def on_enterFindBtn(self,event):
        self.findbilling()

    def on_enter_selectmonthCombobox(self,event):
        self.billamountEntry.focus_set()

    def on_enter_billamountEntry(self,event):
        self.paybtn.focus_set()

    def on_enter_paymentBtn(self, event):
        self.payment()

    def on_enter_wbnoEntry(self, event):
        self.selectmonthwbCombobox.focus_set()

    def on_entermonthcombobox(self, event):
        self.billamountwbEntry1.focus_set()

    def on_enter_billamountEntry1(self, event):
        self.sendbtn.focus_set()

    def on_enterSendBtn(self, event):
        self.sendmessage()

    def on_enter_calmeternoentry(self, event):
        self.findcustomerbtn1.focus_set()

    def on_enter_findcustomer(self, event):
        self.findcustomer()

    def on_enter_calmonthcombobox(self, event):
        self.calunitconsumedEntry.focus_set()

    def on_enter_calunitconsumedEntry(self, event):
        self.calculatebtn.focus_set()

    def on_enter_calculatebtn(self, event):
        self.calculateBill()



    def findbilling(self):
        meter_No = self.paybillMeternoEntry.get().lower()

        self.itemlist.clear()
        #print(len(self.itemlist))

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"select * from customer where meter_no = '{meter_No}';"

            self.mycursor.execute(q)
            row = self.mycursor.fetchall()

            if len(row) == 0:
                tkinter.messagebox.showerror("Error", "No record Found")

            else:
                name = row[0]

                self.BillingDetailsTextArea.delete("1.0", tkinter.END)

                # after_count_space S1, s2, s3 and so on

                s1 = " " * 10
                s2 = " " * 5
                s3 = " " * 7
                s4 = " " * 3
                s5 = " " * 10
                s6 = " " * 15

                ItemHead = "." * 30 + "Customer Details" + "." * 30 + "\n\n"

                self.itemlist.append(ItemHead)

                data = (f" Meter No: {s1}| {name[1]}\n"
                        f" Customer Name: {s2}| {name[0].capitalize()}\n"
                        f" Phone No:    {s3}| {name[2]}\n"
                        f" Email ID:        {s4}| {name[3]}\n"
                        f" City:     {s5}| {name[5].capitalize()}\n"
                        f"  {s6}\n")

                self.itemlist.append(data)

# fetch data from bill table and show all details about billing -------------------------------#

                q1 = f"select * from bill where meter_no = '{meter_No}';"

                self.mycursor.execute(q1)
                row1 = self.mycursor.fetchall()

                count = 0

                s1 = " " * 13
                s2 = " " * 5
                s3 = " " * 5
                s4 = " " * 5
                s5 = " " * 4
                s6 = "*" * 40

                while count < len(row1):
                    name1 = row1[count]
                    data = (
                        f"{s6}\n"
                        f" Month: {s1}| {name1[1].capitalize()}\n"
                        f" Unit Consumed: {s2}| {name1[2]}\n"
                        f" Total Bill:    {s3}| Rs. {name1[3]}\n"
                        f" Status:        {s4}| {name1[4].capitalize()}\n"
                        f"{s6}\n"
                    )

                    self.itemlist.append(data)
                    count += 1

                self.BillingDetailsTextArea.delete("1.0", tkinter.END)
                for item in self.itemlist:
                    self.BillingDetailsTextArea.insert(tkinter.END, str(item))

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()



    def findcustomer(self):
        meter_No = self.calMeternoEntry.get().lower()

        self.itemlist.clear()

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"select * from customer where meter_no = '{meter_No}';"

            self.mycursor.execute(q)
            row = self.mycursor.fetchall()

            if len(row) == 0:
                    tkinter.messagebox.showerror("Error", "No record Found")

            else:
                name = row[0]

                self.BillingDetailsTextArea.delete("1.0", tkinter.END)

                # after_count_space S1, s2, s3 and so on

                s1 = " " * 10
                s2 = " " * 5
                s3 = " " * 7
                s4 = " " * 3
                s5 = " " * 10
                s6 = " " * 15

                ItemHead = "."*30+"Customer Details"+"."*30+"\n\n"

                self.itemlist.append(ItemHead)

                data = (f" Meter No: {s1}| {name[1]}\n"
                        f" Customer Name: {s2}| {name[0].capitalize()}\n"
                        f" Phone No:    {s3}| {name[2]}\n"
                        f" Email ID:        {s4}| {name[3]}\n"
                        f" City:     {s5}| {name[5].capitalize()}\n"
                        f"  {s6}\n")

                self.itemlist.append(data)

                # fetch data from bill table and show all details about billing

                self.BillingDetailsTextArea.delete("1.0", tkinter.END)
                for item in self.itemlist:
                    self.BillingDetailsTextArea.insert(tkinter.END, str(item))

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()


    def calculateBill(self):
        a = self.calmonthCombobox.get()
        b = int(self.calunitconsumedEntry.get())

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"select * from tax;"

            self.mycursor.execute(q)
            row = self.mycursor.fetchall()

            name = row[0]

            s1 = " " * 14
            s2 = " " * 5
            s3 = " " * 5
            s4 = " " * 7
            s5 = " " * 4
            s6 = " " * 7
            s7 = ""
            s8 = " " * 11
            s9 = " " * 8
            s10 = "*" * 40

            tc = b*int(name[0])
            mr = (int(name[1])*tc)/100
            sc = (int(name[2]) * tc) / 100
            st = (int(name[3]) * tc) / 100
            sbc = (int(name[4]) * tc) / 100
            ft = (int(name[5]) * tc) / 100
            self.total_bill = mr+sc+st+sbc+ft

            data = (f" Year: {s1}| {a}\n"
                    f" Unit Consumed: {s2}| {b}\n"
                    f" Cost per Unit: {s3}| Rs. {name[0]}\n"
                    f" Meter Rent : {s4}| Rs. {mr}\n"
                    f" Service Charge: {s5}| Rs. {sc}\n"
                    f" Service tax: {s6}| Rs. {st}\n"
                    f" Swachh Bharat Cess: {s7}| Rs. {sbc}\n"
                    f" Fix Tax: {s8}| Rs. {ft}\n"
                    f" {s10}\n"
                    f" Total bill: {s9}| Rs. {self.total_bill}\n"
                    f" {s10}\n"
                    )

            self.itemlist.append(data)

            self.BillingDetailsTextArea.delete("1.0", tkinter.END)
            for item in self.itemlist:
                self.BillingDetailsTextArea.insert(tkinter.END, str(item))

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()


    def generatebill(self):
        itemlist1 = []
        size = len(self.itemlist)
        itemlist1.append(self.itemlist[0])
        itemlist1.append(self.itemlist[1])
        itemlist1.append(self.itemlist[size-1])
        s1 = "*"*30

        a = f"{s1} Bill Generated {s1}\n"
        itemlist1.append(a)
        self.itemlist = itemlist1[:]


        self.BillingDetailsTextArea.delete("1.0", tkinter.END)
        for item in self.itemlist:
            self.BillingDetailsTextArea.insert(tkinter.END, str(item))

        u1 = self.calMeternoEntry.get().lower()
        u2 = self.calmonthCombobox.get().lower()
        u3 = self.calunitconsumedEntry.get().lower()
        u4 = str(self.total_bill)
        u5 = "pending"

        try:

            import Conn

            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"insert into bill (meter_no, month, units, total_bill, status) values ('{u1}','{u2}','{u3}', '{u4}', '{u5}');"

            self.mycursor.execute(q)
            self.myconnect.commit()

            tkinter.messagebox.showinfo("Success", "Data saved successfully")

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()

    def sendmessage(self):
        # set target phone number

        try:
            phone_no = "+91"+self.wbnoEntry.get()
            dt = datetime.datetime.now()
            time = dt.time()
            tt = str(time)

            hh = int(tt[0:2])
            mm = int(tt[3:5])
            mm += 1

            month = self.selectmonthwbCombobox.get().capitalize()
            amt = self.billamountwbEntry.get()

            #set message content
            message = f"*This message is from Electricity Billing Management System*\n\nInformed you to pay *{month}* month bill amount Rs. *{amt}* pay your electricity bill before due date to avoid late payment charges"
            kit.sendwhats_image(phone_no,"icon/logo.jpg",message)
            #kit.sendwhatmsg(phone_no,message,hh,mm,15,True, 2)
            tkinter.messagebox.showinfo("Message","Message send successfully")

        except Exception as e:
            print(str(e))




    def payment(self):

        self.amt = self.billamountEntry.get()

        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data('Pay amount Rs. '+self.amt)
        self.qr.make(fit=True)

        self.img = self.qr.make_image(fill_color="red", back_color="white")

        self.qrcodeimage_window = tkinter.Toplevel(self.master)
        self.qrcodeimage_window.title("QRCode for payment")
        self.qrcodeimage_window.geometry("500x750+965+90")
        self.qrcodeimage_window.resizable(False,False)

        #load image
        self.img = self.img.resize((400, 400), Image.BOX)
        self.photo1 = ImageTk.PhotoImage(self.img)

        #display the image in the label
        self.qrcode_frame = tkinter.LabelFrame(self.qrcodeimage_window)
        self.qrcode_frame.place(x=20, y=20)
        self.qrcode_frame.configure(height=650, width=450)
        self.qrcode_label = tkinter.Label(self.qrcode_frame,
                                     image=self.photo1,compound=tkinter.LEFT)
        self.qrcode_label.place(x=20, y=20)

        self.amountLabel = tkinter.Label(self.qrcode_frame, text="Scan This QR code and\nPay Rs: "+self.amt,
                                         font=("bookman old style", 20, "bold"), fg="blue")
        self.amountLabel.place(x=40, y=450)

        self.addpaybtnimage = Image.open("icon/paid.png")
        self.addpaybtnimage = self.addpaybtnimage.resize((60, 60), Image.BOX)
        self.imagePhotoaddpaybtnimage = ImageTk.PhotoImage(self.addpaybtnimage)

        self.qrpaybtn = tkinter.Button(self.qrcodeimage_window, text="Click to Paid", width=300,
                                       image=self.imagePhotoaddpaybtnimage,compound=tkinter.LEFT,
                                       font=("bookman old style", 20, "bold"), command=self.paymentdone, fg="#884EA0", background="#F4D03F"
                                       )
        self.qrpaybtn.place(x=100, y=575)
    def paymentdone(self):
        u1 = self.paybillMeternoEntry.get()
        u2 = self.selectmonthCombobox.get()

        try:

            import Conn

            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"update bill set status = 'paid' where meter_no = '{u1}'and month = '{u2}';"

            self.mycursor.execute(q)
            self.myconnect.commit()

            self.qrcodeimage_window.destroy()

            tkinter.messagebox.showinfo("Success", "Paid successfully")
            self.selectmonthCombobox.current(0)
            self.billamountEntry.delete(0,tkinter.END)

            self.billingForm()
            self.paybillMeternoEntry.focus_set()

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()

#--------------------------Logout tab all functions -------------------------------------------------------

    def logout(self):
        self.master.destroy()

        import LoginForm
        LoginForm.main()

    def userLogin(self, frame, photoimage):

        currentTime = datetime.datetime.now().strftime('%I:%M %p')

        self.userDetailsframe = tkinter.LabelFrame(frame, bg="#3791ff")
        self.userDetailsframe.place(x=10, y=500, height=405, width=267)

        self.userImageLabel = tkinter.Label(self.userDetailsframe, image=photoimage,
                                            anchor="w", bg="#3791ff")
        self.userImageLabel.place(x=5, y=5)

        self.userNameLabel = tkinter.Label(self.userDetailsframe, text="" + self.userName.capitalize(), fg="#9b0000",
                                           font=("bookman old style", 15, "underline"), bg="#3791ff")
        self.userNameLabel.place(x=5, y=270)

        self.userTypeLabel = tkinter.Label(self.userDetailsframe, text="User Type: " + self.usertype.capitalize(),
                                           fg="#9b0000", font=("bookman old style", 15), bg="#3791ff")
        self.userTypeLabel.place(x=5, y=310)

        self.loginTimeLabel = tkinter.Label(self.userDetailsframe, text="Login at: " + str(currentTime),
                                            fg="#9b0000", font=("bookman old style", 15), bg="#3791ff")
        self.loginTimeLabel.place(x=5, y=350)

# ------------------------On Close -----------------------------------------------
    def on_close(self, event):
        self.master.quit()



if __name__=="__main__":
    main()