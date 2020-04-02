from tkinter import*
import tkinter.messagebox
import tkinter.messagebox as tmb;
from tkinter import ttk
import random
import time
import datetime





def main():
      a=Tk()
      app=Window1(a)
      a.geometry("14000x50000")

      

      


class Window1:
      
    def __init__(self,master):
          
        self.master=master
        self.master.title("STUDENT GRADE PREDICTION")
        self.master.geometry("6000x6000")
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master,bg="blue",width=9000,height=40000)
        self.frame.pack()
        self.master.title("WELCOME TO MY PROJECT")
        self.lb1Title=Label(self.frame,text="STUDENT GRADE PREDICTION",font=('arial',10,'bold'),bg="powder blue",fg="black")
        self.lb1Title.grid(row=0,column=0,columnspan=5,pady=40)
        self.L1 = Label(self.frame, text = "Enter Term Id", height =2,fg="black")
        self.L1.grid(row=1,column=2)
        self.E1 = Entry (self.frame, bd = 4)
        self.E1.grid(row=1,column=3)
        self.L1 = Label(self.frame, text = "Enter your Branch", height = 2,fg="black")
        self.L1.grid(row=2,column=2)
        self.E1 = Entry (self.frame, bd = 4)
        self.E1.grid(row=2,column=3)
        self.btnLogin=Button(self.frame,text="SUBMIT",width=15,command=self.new_window)
        self.btnLogin.grid(row=3,column=3)
        self.btnLogin=Button(self.frame,text="CANCEL",width=15,command=self.new8_window)
        self.btnLogin.grid(row=3,column=4)
            
            
            
    def new_window(self):
       self.newWindow=Toplevel(self.master)
       self.app=Window2(self.newWindow)
    def new8_window(self):
          tmb.showinfo(title="cancel",message="sure you want to cancel")
          self.L1 = Label(self.frame, text = "", height =2,fg="blue")
          self.L1.grid(row=1,column=2)
          self.E1 = Entry (self.frame, bd = 5)
          self.E1.grid(row=1,column=3)
          self.L1 = Label(self.frame, text = "", height = 2,fg="blue")
          self.L1.grid(row=2,column=2)
          self.E1 = Entry (self.frame, bd = 5)
          self.E1.grid(row=2,column=3)
       
     
class Window2:
    def __init__(self,master):
            self.master=master
            self.master.title("Welcome to my project")
            self.master.geometry('600x600')
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.label=Label(self.frame,text="Welcome",fg="blue")
            self.label.grid(row=0,column=0)
            self.label=Label(self.frame,text="Choose your Desired Classification Algo",fg="blue")
            self.label.grid(row=0,column=0)
            self.button=Button(self.frame,text="SUPPORT VECTOR MACHINE",width=40,command=self.new4_window,bg="orange")
            self.button.grid(row=1,column=0)
            self.button=Button(self.frame,text="DECISION TREE",width=40,command=self.new3_window,bg="orange")
            self.button.grid(row=2,column=0)
            self.button=Button(self.frame,text="K-NEAREST ALGORITHM",width=40,command=self.new2_window,bg="orange")
            self.button.grid(row=3,column=0)
            self.button=Button(self.frame,text="RANDOM FOREST",width=40,command=self.new1_window,bg="orange")
            self.button.grid(row=4,column=0)
            self.button=Button(self.frame,text="LOGISTIC REGRESSION",width=40,command=self.new1_window,bg="orange")
            self.button.grid(row=5,column=0)
            self.button=Button(self.frame,text="NAIVE BAYES",width=40,command=self.new1_window,bg="orange")
            self.button.grid(row=6,column=0)
            self.frame=Frame(self.master,bg="blue")
            self.frame.pack()
            

    def new1_window(self):
         self.new1Window=Toplevel(self.master)
         self.app=Window3(self.new1Window)
    def new2_window(self):
         self.new2Window=Toplevel(self.master)
         self.app=Window4(self.new2Window)
    def new3_window(self):
         self.new3Window=Toplevel(self.master)
         self.app=Window5(self.new3Window)
    def new4_window(self):
          self.new4Window=Toplevel(self.master)
          self.app=Window6(self.new4Window)
    


class Window3:
      
      def __init__(self,master):
            self.master=master
            self.master.title("Welcome to my project")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Enter academic details!!!",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA3(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your Attendance in %", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new112_window)
            self.btnLogin.grid(row=7,column=3)


      def new112_window(self):
                  
            self.new555Window=Toplevel(self.master)
            self.app=Window678(self.new555Window)
            
class Window678:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Keep working hard your grade is E",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)     
       
            

class Window4:

      def __init__(self,master):
            self.master=master
            self.master.title("Welcome to my project")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Enter academic details!!!",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA3(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100)( marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your Attendance in %", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new111_window)
            self.btnLogin.grid(row=7,column=3)

            
      def new111_window(self):
                  
            self.new56Window=Toplevel(self.master)
            self.app=Window67(self.new56Window)
            
class Window67:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="You can do better keep doing hard work your grade is B+ ",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)               
            
            


class Window5:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry('500x500+0+0')
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Enter academic details!!!",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA3(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your Attendance in %", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new78_window)
            self.btnLogin.grid(row=7,column=3)


            


      def new78_window(self):
                  
            self.new87Window=Toplevel(self.master)
            self.app=Window78(self.new87Window)

                  
class Window78:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="you can do better Keep working hard your grade is B+",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)                  
       
       
            
            
         
         


class Window6:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Choose your Kernel!!!",font=('arial',10,'bold'),bg="yellow",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40,sticky=E)
            
            self.btnLogin=Button(self.frame,text="POLYNOMIAL",width=17,bg="orange",command=self.new7_window)
            self.btnLogin.grid(row=1,column=3,sticky=NW)
            self.btnLogin=Button(self.frame,text="LINEAR",width=17,bg="orange",command=self.new786_window)
            self.btnLogin.grid(row=2,column=3,sticky=NW)
            self.btnLogin=Button(self.frame,text="RBF",width=17,bg="orange",command=self.new790_window)
            self.btnLogin.grid(row=3,column=3,sticky=NW)


      def new7_window(self):
                  
            self.new5Window=Toplevel(self.master)
            self.app=Window7(self.new5Window)
      def new786_window(self):
                  
            self.new590Window=Toplevel(self.master)
            self.app=Window386(self.new590Window)
      def new790_window(self):
                  
            self.new555Window=Toplevel(self.master)
            self.app=Window387(self.new555Window)



                  
class Window7:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Enter your Academic detail!!!",font=('arial',10,'bold'),bg="yellow",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40,sticky=E)
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your attendance in %", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new999_window)
            self.btnLogin.grid(row=7,column=3)

      def new999_window(self):
                  
            self.new33Window=Toplevel(self.master)
            self.app=Window71(self.new33Window)

class Window71:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Keep working hard your grade is E",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)

class Window386:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="Enter your Academic detail!!!",font=('arial',10,'bold'),bg="yellow",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40,sticky=E)
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA3(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your Attendance in % marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new9991_window)
            self.btnLogin.grid(row=7,column=3)
      def new9991_window(self):
                  
            self.new34Window=Toplevel(self.master)
            self.app=Window72(self.new34Window)
class Window72:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="It is good Keep working hard your grade is B+",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)

                    

class Window387:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.L1 = Label(self.frame, text = "Enter your CA1(50) marks", height =2,fg="blue",bg="orange")
            self.L1.grid(row=1,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=1,column=3)
        
            self.L1 = Label(self.frame, text = "Enter your CA2(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=2,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=2,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA3(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=3,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=3,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA4(50) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=4,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=4,column=3)
            self.L1 = Label(self.frame, text = "Enter your CA(100) marks", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=5,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=5,column=3)
            self.L1 = Label(self.frame, text = "Enter your Attendance in %", height = 2,fg="blue",bg="orange")
            self.L1.grid(row=6,column=2)
            self.E1 = Entry (self.frame, bd = 5)
            self.E1.grid(row=6,column=3)
            self.E1.grid(row=6,column=3)
            self.btnLogin=Button(self.frame,text="SUBMIT",width=17,bg="orange",command=self.new9992_window)
            self.btnLogin.grid(row=7,column=3)
            #self.lb1Title=Label(self.frame,text="Keep working hard ypur grade is E",font=('arial',10,'bold'),bg="orange",fg="black")
            #self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)
      def new9992_window(self):
                  
            self.new35Window=Toplevel(self.master)
            self.app=Window73(self.new35Window)
class Window73:

      def __init__(self,master):
            self.master=master
            self.master.title("ATM 2.0")
            self.master.geometry("600x600")
            self.master.config(bg="cadet blue")
            self.frame=Frame(self.master,bg="powder blue")
            self.frame.pack()
            self.lb1Title=Label(self.frame,text="It is  nice Keep working hard ypur grade is B+",font=('arial',10,'bold'),bg="orange",fg="black")
            self.lb1Title.grid(row=0,column=0,columnspan=2,pady=40)

       
       
            


                  


      
main()
