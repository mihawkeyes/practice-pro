from  tkinter import * 
class LoginPage():

    __balance=30000;
    
    def __init__(self):
        
        def Login():
            # print(self.usr_name)
            # print(self.password)
            if str(self.usr_name.get()) == 'Ruthvik' and str(self.password.get()) == '1234':
                # print(self.usr_name)
                # print(self.password)
                for a in self.login_page_widget:
                    a.grid_remove()
                # self.Main
            elif str(self.usr_name.get()) != '' and str(self.password.get()) != '':
                self.lb_warning = Label(window, bg="green", fg="red", font=(
                    "warning", 15, "bold"), text="invalid cerdetials!!!")
                self.lb_warning.grid_configure(row=2, column=1)


        self.lb_username = Label(window, bg="green", fg="black", font=(
            "roboto", 15, "bold"), text="User Name :")
        self.lb_password = Label(window,bg="green", fg="black", font=(
            "roboto", 15, "bold"),text="Password :")
        self.usr_name= StringVar()
        self.name_entry = Entry(window, fg="blue", borderwidth=3,
                        textvariable=self.usr_name)
        self.password = StringVar()
        self.password_entry = Entry(window, fg="blue", borderwidth=3,
                            textvariable=self.password)
        self.log_in_bt = Button(window, bg="blue", fg="white", highlightbackground="lightblue",
                                text="login", width=10, height=3, activebackground="red")

        self.login_page_widget = [self.lb_username,self.lb_password,self.name_entry,self.password_entry,self.log_in_bt]

        
        self.log_in_bt.configure(command=Login())
        self.lb_username.grid(row=0,column=0)
        self.lb_password.grid(row=1,column=0)
        self.name_entry.grid(row=0,column=1)
        self.password_entry.grid(row=1, column=1)
        self.log_in_bt.grid(row=2,column=0)

        window.mainloop()
    
    # # def MainMenu(self):
    # #     window
    #     self.acc_detail_bt = button(window,)
        

window = Tk(className="banking app")
window.configure(bg="green")
bank=LoginPage()

# class Banking():

#     def __init__(self):
#         self.window=Tk(className="banking app")
#         self.window = 
#         self.Login()
#         self.window.mainloop()

#     def Login(self):
        
#         self.lb_username = Label(self.window, bg="green", fg="black", font=(
#             "roboto", 15, "bold"), text="User Name :")
#         self.lb_password = Label(self.window,bg="green", fg="black", font=(
#             "roboto", 15, "bold"),text="Password :")
#         self.usr_name= StringVar()
#         self.name_entry = Entry(self.window, fg="blue", borderwidth=3,
#                         textvariable=self.usr_name)
#         self.password = StringVar()
#         self.password_entry = Entry(self.window, fg="blue", borderwidth=3,
#                             textvariable=self.password)
#         self.log_in_bt = Button(self.window, bg="blue", fg="white", highlightbackground="lightblue",
#                                 text="login", width=10, height=3, activebackground="red")

#         # self.login_page_widget = [self.lb_username,self.lb_password,self.name_entry,self.password_entry,self.log_in_bt]

        
#         # self.log_in_bt.configure(command=self.Login_bt(self.window))
#         self.lb_username.grid(row=0,column=0)
#         self.lb_password.grid(row=1,column=0)
#         self.name_entry.grid(row=0,column=1)
#         self.password_entry.grid(row=1, column=1)
#         self.log_in_bt.grid(row=2,column=0)
#         self.window.mainloop()
#     # def Login(self,window):
#     # # print(self.usr_name)
#     # # print(self.password)
#     #     if str(self.usr_name.get())=='Ruthvik' and  str(self.password.get())=='1234':
#     #         # print(self.usr_name)
#     #         # print(self.password)
#     #         for a in self.login_page_widget:
#     #             a.grid_remove()
#     #         # self.Main
#     #     elif  str(self.usr_name.get())!='' and  str(self.password.get())!='':
#     #         self.lb_warning = Label(window, bg="green", fg="red", font=(
#     #             "warning", 15, "bold"), text="invalid cerdetials!!!")
#     #         self.lb_warning.grid_configure(row=2, column=1)

# bank=Banking()
