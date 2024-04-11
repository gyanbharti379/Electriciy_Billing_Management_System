import tkinter
import tkinter.ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from random import random, randint,randrange


def main():
    RegistrationEntryForm()


class RegistrationEntryForm:

    def __init__(self):

# ------------------------------Area for creating window -------------------------------------------------#

        self.master = tkinter.Tk()
        self.master.geometry("630x515+400+150")
        self.master.title("Electricity Billing Management System")

        # change the icon of window
        img = Image.open("icon/iconwin.png")
        ImageLabel = ImageTk.PhotoImage(img)
        self.master.iconphoto(True, ImageLabel)

        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window -----------------END------------------------#

# -----------------Create From -------------------------------Start ----------------------------#

        self.frame = tkinter.Frame(self.master)
        self.frame.configure(bg="#d3e0c9")
        self.frame.pack()

        self.Title_label = tkinter.Label(self.frame, text="User Registration Form", fg="blue",bg="#d3e0c9",
                                         font=("bookman old style", 20, "underline","bold"))
        self.Title_label.grid(row=0, column=0)

# ---------------First Frame -------------------------
        self.FirstFrame = tkinter.LabelFrame(self.frame, text="User information",font=("bookman old style", 10), bg="#d3e0c9")
        self.FirstFrame.grid(row=1,column=0, sticky="news", padx=20, pady=12)

        self.EmpID_Label = tkinter.Label(self.FirstFrame, text="Employee ID",font=("bookman old style",10), bg="#d3e0c9")
        self.EmpID_Label.grid(row=0, column=0, sticky="w")

        self.FristName_Label = tkinter.Label(self.FirstFrame, text="First Name",font=("bookman old style",10), bg="#d3e0c9")
        self.FristName_Label.grid(row=0,column=1, sticky="w")

        self.LastName_Label = tkinter.Label(self.FirstFrame, text="Last Name",font=("bookman old style",10), bg="#d3e0c9")
        self.LastName_Label.grid(row=0, column=2, sticky="w")

        self.EmpIDEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=22)
        self.EmpIDEntry.grid(row=1, column=0, sticky="w")

        self.FirstNameEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=20)
        self.FirstNameEntry.grid(row=1, column=1, sticky="w")
        self.FirstNameEntry.focus_set()
        self.FirstNameEntry.bind("<Return>", self.on_enter_firstName)

        self.LastNameEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=20)
        self.LastNameEntry.grid(row=1, column=2, sticky="w")
        self.LastNameEntry.bind("<Return>", self.on_enter_lastName)

        self.UserType_Label = tkinter.Label(self.FirstFrame, text="User Type",font=("bookman old style",10), bg="#d3e0c9")
        self.UserType_Label.grid(row=2, column=0, sticky="w")

        self.Password_Label = tkinter.Label(self.FirstFrame, text="Password",font=("bookman old style",10), bg="#d3e0c9")
        self.Password_Label.grid(row=2, column=1, sticky="w")

        self.RePassword_Label = tkinter.Label(self.FirstFrame, text="Re-Password",font=("bookman old style",10), bg="#d3e0c9")
        self.RePassword_Label.grid(row=2, column=2, sticky="w")

        self.UserType_Combobox = tkinter.ttk.Combobox(self.FirstFrame, values=["","Admin","User"],font=("bookman old style",10))
        self.UserType_Combobox.grid(row=3, column=0, sticky="w")
        self.UserType_Combobox.bind("<Return>", self.on_enter_UTypeCombobox)

        self.PasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=20)
        self.PasswordEntry.grid(row=3, column=1, sticky="w")
        self.PasswordEntry.bind('<Return>',self.on_enter_Pass)

        self.RePasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=20)
        self.RePasswordEntry.grid(row=3, column=2, sticky="w")
        self.RePasswordEntry.bind("<Return>", self.on_enter_RePass)

        for widget in self.FirstFrame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

# second frame -------------------------Contact information----------------------#

        self.Contact_InfoFrame = tkinter.LabelFrame(self.frame, text="Contact Information",font=("bookman old style", 10), bg="#d3e0c9")
        self.Contact_InfoFrame.grid(row=2, column=0, sticky="news", padx=20, pady=12)

        self.PhoneNoLabel = tkinter.Label(self.Contact_InfoFrame, text="Phone No",font=("bookman old style",10), bg="#d3e0c9")
        self.PhoneNoLabel.grid(row=0,column=0, sticky="w")

        self.EmaiIdLabel = tkinter.Label(self.Contact_InfoFrame, text="Email Id",font=("bookman old style",10), bg="#d3e0c9")
        self.EmaiIdLabel.grid(row=0, column=1, sticky="w")

        self.dobLabel = tkinter.Label(self.Contact_InfoFrame, text="Date of Birth",font=("bookman old style",10), bg="#d3e0c9")
        self.dobLabel.grid(row=0, column=2, sticky="w")

        self.PhoneNoEntry = tkinter.Entry(self.Contact_InfoFrame, font=("bookman old style",10), width=20)
        self.PhoneNoEntry.grid(row=1, column=0, sticky="w")
        self.PhoneNoEntry.bind("<Return>", self.on_enter_phoneno)

        self.EmailIDEntry = tkinter.Entry(self.Contact_InfoFrame, font=("bookman old style",10), width=20)
        self.EmailIDEntry.grid(row=1, column=1, sticky="w")
        self.EmailIDEntry.bind('<Return>', self.on_enter_email)

        self.dobEntry = DateEntry(self.Contact_InfoFrame, selectmode="day", date_pattern="dd/mm/yyyy", sticky="w",
                                  font=("bookman old style",10), width=20)
        self.dobEntry.grid(row=1, column=2)

        for widget in self.Contact_InfoFrame.winfo_children():
            widget.grid(padx=10, pady=5)

# ----Terms and condition Frame ---------------------------------------------------------------#

        self.AddInformationFrame = tkinter.LabelFrame(self.frame, text="Address Information",font=("bookman old style", 10), bg="#d3e0c9")
        self.AddInformationFrame.grid(row=3, column=0, sticky="news", padx=20, pady=12)

        self.address_Label = tkinter.Label(self.AddInformationFrame, text="Address",font=("bookman old style",10), bg="#d3e0c9")
        self.address_Label.grid(row=0, column=0, sticky="w")

        self.city_Label = tkinter.Label(self.AddInformationFrame, text="City",font=("bookman old style",10), bg="#d3e0c9")
        self.city_Label.grid(row=0, column=1, sticky="w")

        self.state_Label = tkinter.Label(self.AddInformationFrame, text="State",font=("bookman old style",10), bg="#d3e0c9")
        self.state_Label.grid(row=0, column=2, sticky="w")

        self.addressEntry = tkinter.Entry(self.AddInformationFrame, font=("bookman old style",10))
        self.addressEntry.grid(row=1, column=0, sticky="w")
        self.addressEntry.bind("<Return>", self.on_enter_address)

        self.cityEntry = tkinter.Entry(self.AddInformationFrame, font=("bookman old style",10))
        self.cityEntry.grid(row=1, column=1, sticky="w")
        self.cityEntry.bind("<Return>", self.on_enter_city)

        self.stateEntry = tkinter.Entry(self.AddInformationFrame, font=("bookman old style",10))
        self.stateEntry.grid(row=1, column=2, sticky="w")
        self.stateEntry.bind("<Return>", self.on_enter_state)

        for widget in self.AddInformationFrame.winfo_children():
            widget.grid(padx=10, pady=5)

# ----------Button Frame ----------------------------------------------------------------------------------#

        self.ButtonFrame = tkinter.LabelFrame(self.frame, bg="#d3e0c9")
        self.ButtonFrame.grid(row=4, column=0, sticky="news", padx=20, pady=12)

        self.resetButton = tkinter.Button(self.ButtonFrame, text="Reset", width=22,bg="#FF7575", height=1,
                                          font=("bookman old style", 15),command=self.resetallfield)
        self.resetButton.grid(row=0, column=0)

        self.SubmitButton = tkinter.Button(self.ButtonFrame, text="Submit",height=1, width=22,bg="#ceffcf",
                                           font=("bookman old style", 15),command=self.submit_Mouse)
        self.SubmitButton.grid(row=0, column=2)
        self.SubmitButton.bind("<Return>", self.on_enter_submit)

        self.master.mainloop()

# -----------------Create From -------------------------------END ----------------------------#

    # generate employee id with random number
    def on_enter_firstName(self, event):
        empidtext = f"{self.FirstNameEntry.get()}"+f"{randint(1,1000)}"
        self.EmpIDEntry.insert(0, empidtext)
        self.LastNameEntry.focus_set()
        self.EmpIDEntry.config(state=tkinter.DISABLED, fg="black")

    def on_enter_lastName(self, event):
        self.UserType_Combobox.focus_set()

    def on_close(self, event):
        self.master.quit()

    def on_enter_UTypeCombobox(self, event):
        self.PasswordEntry.focus_set()

    def on_enter_Pass(self, event):
        import passwordValidation
        passwordValidation.passValidation.password_passfield_validation(passwordValidation, self.PasswordEntry.get())
        self.RePasswordEntry.focus_set()

    def on_enter_RePass(self, event):
        if self.PasswordEntry.get() == self.RePasswordEntry.get():
            self.PhoneNoEntry.focus_set()
        else:
            tkinter.messagebox.showerror("Error", "Password not match")
            self.RePasswordEntry.focus_set()

    def on_enter_phoneno(self,event):
        self.EmailIDEntry.focus_set()

    def on_enter_email(self,event):
        import emailValidation
        emailValidation.emailValidation.email_textfield_validation(emailValidation,self.EmailIDEntry.get())
        self.dobEntry.focus_set()

    def on_enter_address(self,event):
        self.cityEntry.focus_set()


    def on_enter_city(self,event):
        self.stateEntry.focus_set()

    def on_enter_state(self,event):
        self.SubmitButton.focus_set()

    # reset all fields
    def resetallfield(self):

        self.EmpIDEntry.delete(0,tkinter.END)
        self.FirstNameEntry.delete(0,tkinter.END)
        self.LastNameEntry.delete(0,tkinter.END)
        self.UserType_Combobox.current(0)
        self.PasswordEntry.delete(0,tkinter.END)
        self.PhoneNoEntry.delete(0,tkinter.END)
        self.EmailIDEntry.delete(0,tkinter.END)
        self.addressEntry.delete(0,tkinter.END)
        self.cityEntry.delete(0,tkinter.END)
        self.stateEntry.delete(0,tkinter.END)


    def on_enter_submit(self,event):
        self.submit()

    def submit_Mouse(self):
        self.submit()


    def submit(self):

        u1 = self.EmpIDEntry.get().lower()
        u2 = self.FirstNameEntry.get().lower()
        u3 = self.LastNameEntry.get().lower()
        u4 = self.UserType_Combobox.get().lower()
        u5 = self.PasswordEntry.get()
        u6 = self.PhoneNoEntry.get().lower()
        u7 = self.EmailIDEntry.get().lower()
        u8 = self.dobEntry.get()
        u9 = self.addressEntry.get().lower()
        u10 = self.cityEntry.get().lower()
        u11 = self.stateEntry.get().lower()
        u12 = f"{u2}{u6}" #create user name
        u13 = f"{u2} {u3}"

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"insert into employee (empid, uname, pass, utype, fname, lname, phone_no,dob, email_id, address, city, state) values ('{u1}','{u12}','{u5}', '{u4}', '{u2}', '{u3}', '{u6}', '{u8}', '{u7}', '{u9}', '{u10}','{u11}');"

            self.mycursor.execute(q)
            self.myconnect.commit()

            q = f"insert into login(empid, uname, name, pass, utype) values('{u1}','{u12}','{u13}','{u5}','{u4}');"
            self.mycursor.execute(q)
            self.myconnect.commit()

            tkinter.messagebox.showinfo("Saving . . . ", "Data saved successfully")

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()
            self.resetallfield()



if __name__=="__main__":
    main()