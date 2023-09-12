# importing
import tkinter as tk
from tkinter import IntVar
from tkinter import messagebox
from tkinter import PhotoImage

# start project

class baytara(tk.Tk):
#window     
      def __init__(self):

            self.window= tk.Tk()
            self.window.title("Baytara😸🐶")
            self.window.geometry("500x400")
            self.window.configure(bg='orange2')
            self.window.rowconfigure(0,minsize=800, weight=1)
            #self.image =PhotoImage(file="C:\Users\marya\OneDrive\Pictures\Saved Pictures\baytara.jpg")
            #self.image_label =tk.Label(self,image=self.image)
            #self.image_label.pack()
      


            
            self.project_name= tk.Label(self.window,text='''
                                          welcome to
                                          BAYTARA🐶😸
                                ''' ,bg="orange2",fg="cornsilk" ,width=50,height=2,font=("Arial",18))
            self.project_name.pack(padx=20,pady=20)
            self.hello_text = tk.Label(text="where your animal is safe in our hands 🐻🤝🏼!",
                                 bg="orange2",fg="black",width=40,height=2,font=("Arial",16))
            self.hello_text.pack()
            self.Q1= tk.Label(text="what animal do you want to ask about?",
                              bg="orange2",fg="black",width=50,height=2,font=('arial',14))
            self.Q1.pack()
#Button_state           
            self.Button_state=tk.IntVar()
            self.Buttonframe =tk.Frame(self.window,bg="orange2")
            self.Buttonframe.columnconfigure(0,weight=1)
            self.Buttonframe.columnconfigure(1,weight=1)
            self.Buttonframe.columnconfigure(2,weight=1)
            self.Buttonframe.pack(fill=("x"))


            self.animal_cat = tk.Button(self.Buttonframe,text="cat",width=3,height=2,bg="cornsilk2",command=self.animal_name)
            self.animal_cat.grid(row=0,column=0,sticky=tk.W+tk.E,padx=20,pady=20) 

            self.animal_dog = tk.Button(self.Buttonframe,text="dog",width=3,height=2,bg="cornsilk2",command=self.animal_name)
            self.animal_dog.grid(row=0,column=1,sticky=tk.W+tk.E,padx=20,pady=20) 

            self.animal_bird =tk.Button(self.Buttonframe,text="bird",width=3,height=2,bg="cornsilk2",command=self.animal_name)
            self.animal_bird.grid(row=0,column=2,sticky=tk.W+tk.E,padx=20,pady=20) 
# information from the user  
            
            self.hello_label= tk.Label(self.window,text='''great! we can help you 
                 but first we will take some information about your pet💕 ''',width=50,height=2,bg="orange2")
            self.hello_label.pack()
            
            self.window.mainloop()
      def animal_name(self):
            if self.Button_state.get():
                
                print(self.hello_label.config(text='''great! we can help you 
                 but first we will take some information about your pet💕 '''))  
                
            else:
                messagebox.showinfo(title="massage",message="try harder")
             
            
baytara()                
