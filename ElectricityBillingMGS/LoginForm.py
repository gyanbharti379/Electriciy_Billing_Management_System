import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
from os.path import getsize

from PIL import Image, ImageTk

def main():
    Login()


class Login:
    def __init__(self):

# ------------------Area for creating window -----------------------------------------#

        self.master = tkinter.Tk()
        self.master.title("Electricity Billing Management System")
        self.master.geometry("460x680+550+30")
        self.master.config(bg="#FEFDFE")
        img = Image.open("icon/iconwin.png")
        ImageLabel = ImageTk.PhotoImage(img)
        self.master.iconphoto(True, ImageLabel)
        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window -----------------END------------------------#

# --------------Creating Login Form ------------------------------Start-----------------------#

        self.frame = tkinter.Frame(self.master)
        self.frame.place(x=8, y=220)

 # image on top ----------------------------------------
        imgLabel = Image.open("icon/login_image.jpeg")
        imgLabel = imgLabel.resize((430, 200), Image.BOX)
        self.imageLabel = ImageTk.PhotoImage(imgLabel)

        self.ImageonLabel = tkinter.Label(self.master, image=self.imageLabel)
        self.ImageonLabel.place(x=10, y=20)

# First Frame -----------------------------------------------------------------#
        self.First_Frame = tkinter.LabelFrame(self.frame)
        self.First_Frame.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        self.UserTypeLabel = tkinter.Label(self.First_Frame, text="User Type: ", font=("bookman old style", 15))
        self.UserTypeLabel.grid(row=0, column=0, sticky="e")

        self.UserName_label = tkinter.Label(self.First_Frame, text="User Name: ", font=("bookman old style", 15))
        self.UserName_label.grid(row=1, column=0, sticky="e")

        self.Password_Label = tkinter.Label(self.First_Frame, text="Password: ", font=("bookman old style", 15))
        self.Password_Label.grid(row=2, column=0, sticky="e")

        self.UserTypeComboBox = tkinter.ttk.Combobox(self.First_Frame, values=["Select", "Admin", "User"], width=21,
                                                     font=("bookman old style", 15))
        self.UserTypeComboBox.current(0)
        self.UserTypeComboBox.grid(row=0, column=1, sticky="w")
        self.UserTypeComboBox.focus_set()
        self.UserTypeComboBox.bind('<Return>', self.on_enter)

        self.UserNameEntry = tkinter.Entry(self.First_Frame, width=23, font=("bookman old style", 15))
        self.UserNameEntry.grid(row=1, column=1, sticky="w")

        self.UserNameEntry.bind('<Return>', self.on_enter1)

        self.PasswordEntry = tkinter.Entry(self.First_Frame, width=23, show="*", font=("bookman old style", 15))
        self.PasswordEntry.grid(row=2, column=1, sticky="w")
        self.PasswordEntry.bind('<Return>', self.on_enter2)

        self.addforgetimage = Image.open("icon/forgetpassword.png")
        self.addforgetimage = self.addforgetimage.resize((25, 25), Image.BOX)
        self.imagePhotoaddforgetlabelimage = ImageTk.PhotoImage(self.addforgetimage)

        self.forget_Label = tkinter.Label(self.First_Frame, text="Forget Password?", cursor="hand2",
                                          image=self.imagePhotoaddforgetlabelimage, compound=tkinter.LEFT,
                                          font=("bookman old style", 10), fg="#9E0B04"
                                          )
        self.forget_Label.grid(row=3, column=1, sticky="e")
        self.forget_Label.bind("<Button-1>", self.forgetidandpassword)

# Image on Button --------------------------------------------

        self.addloginbtnimage = Image.open("icon/login.png")
        self.addloginbtnimage = self.addloginbtnimage.resize((35, 35), Image.BOX)
        self.imagePhotoaddloginbtnimage = ImageTk.PhotoImage(self.addloginbtnimage)

        self.Signin_Button = tkinter.Button(self.First_Frame,
                                            text="Sign In", bg="#33B805",
                                            width=10, font=("bookman old style", 15), image=self.imagePhotoaddloginbtnimage,
                                            compound=tkinter.LEFT,
                                            command=self.checkEntryValidation,
                                            )
        self.Signin_Button.grid(row=4, column=1, sticky="news")
        self.Signin_Button.bind("<Return>", self.on_enterSignInBtn)

        self.or_Label = tkinter.Label(self.First_Frame, text=" ---------------- OR -------------",font=("bookman old style", 15), fg='#1F7302')
        self.or_Label.grid(row=5, column=1, sticky="w")

        img3 = Image.open("images/social_advt.jpg")
        img3 = img3.resize((280, 60), Image.BOX)
        self.advt_logo = ImageTk.PhotoImage(img3)

        self.logoLabel = tkinter.Label(self.First_Frame, image=self.advt_logo)
        self.logoLabel.grid(row=6, column=1, sticky="n")

        self.CreateAccountLabel = tkinter.Label(self.First_Frame, text="Don't have an account? ",
                                                font=("bookman old style", 10))
        self.CreateAccountLabel.grid(row=7, column=1, stick="w")

        self.CreateAccountLabel1 = tkinter.Label(self.First_Frame, fg="blue",text="Create New One",font=("bookman old style", 10),
                                                 cursor="hand2")
        self.CreateAccountLabel1.bind("<Button-1>",self.register)
        self.CreateAccountLabel1.grid(row=7, column=1, stick="e")

        for widget in self.First_Frame.winfo_children():
            widget.grid(padx=4, pady=4)

        self.master.mainloop()

# --------------Creating Login Form ------------------------------ End -----------------------#

    def on_enter(self, event):
        self.UserNameEntry.focus_set()

    def on_enter1(self, event):
        self.PasswordEntry.focus_set()

    def on_enter2(self, event):
        self.Signin_Button.focus_set()

    def on_close(self, event):
        self.master.quit()

    def on_enterSignInBtn(self, event):
        self.checkEntryValidation()

    def checkEntryValidation(self):
        if self.UserTypeComboBox.get() == "Select":
            tkinter.messagebox.showerror("Error", "Please select User Type")
            self.UserTypeComboBox.focus_set()

        elif self.UserNameEntry.get() == "":
            tkinter.messagebox.showerror("Error", "Please fill Login Id")
            self.UserNameEntry.focus_set()

        elif self.PasswordEntry.get() == "":
            tkinter.messagebox.showerror("Error", "Please fill Password")
            self.PasswordEntry.focus_set()
        else:
            self.check_User_Authentication()

    def check_User_Authentication(self):

        ut = self.UserTypeComboBox.get().lower()
        us = self.UserNameEntry.get().lower()
        pp = self.PasswordEntry.get().lower()

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()

            q = f"SELECT * FROM login where utype = '{ut}' and uname= '{us}' and pass= '{pp}';"

            self.mycursor.execute(q)
            row = self.mycursor.fetchone()

            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.resetallfields()

            else:

                self.master.destroy()
                import UserDashboard
                UserDashboard.UserDashboard.userName =row[2]
                UserDashboard.UserDashboard.usertype = row[4]
                UserDashboard.main()
                self.resetallfields()

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()

    def register(self,event):

        try:
            self.master.destroy()
            import SignUP
            SignUP.main()

        except Exception as e:
             print(str(e))

    def forgetidandpassword(self,event):

        try:
            self.master.destroy()
            import ForgetPassword
            ForgetPassword.main()

        except Exception as e:
            print(str(e))



    def resetallfields(self):
        self.UserTypeComboBox.current(0)
        self.UserNameEntry.delete(0, tkinter.END)
        self.PasswordEntry.delete(0, tkinter.END)
        self.UserTypeComboBox.focus_set()



if __name__ == "__main__":
    main()
