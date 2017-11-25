# An emt which gets all the tweets from the user and analyses the emotion it
from tkinter import *
import tkinter.ttk
import os
import Scrape1 as SC    #Web scrapper code

log='Logout.txt'
no_logout='NoLogout.txt'

creds="Signup.txt"
movie_file='Movies.txt'
songs_file='Songs.txt'
sports_file='Sports.txt'
food_file='Food.txt'
contacts_file='Contacts.txt'
def create_widgets_in_zero_frame():
    
     def FSSignup():
      with open(creds, 'w') as f: 
        import Web_scrape_Twitter as WST
        f.write(nameE.get()) 
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close()
      call_first_frame_on_top()
     global pwordE 
     global nameE
     global roots
     intruction = Label(zero_frame, text='Enter new Credidentials\n',bg='#B7EEE6')
     intruction.config(font=("Ariel", 22)) 
     intruction.grid(row=0, column=0, sticky=E) 
 
     nameL = Label(zero_frame, text='New Username(Twitter id): ',bg='#B7EEE6') 
     pwordL = Label(zero_frame, text='New Password: ',bg='#B7EEE6')
     nameL.config(font=("Ariel", 15))
     pwordL.config(font=("Ariel", 15)) 
     nameL.grid(row=1, column=0, sticky=W) 
     pwordL.grid(row=3, column=0, sticky=W) 
 
     nameE = Entry(zero_frame) 
     pwordE = Entry(zero_frame, show='*') 
     nameE.config(font=("Ariel", 15))
     pwordE.config(font=("Ariel", 15))
     nameE.grid(row=2, column=0,sticky=W) 
     pwordE.grid(row=4, column=0,sticky=W) 
 
     signupButton = Button(zero_frame, text='Signup',bg='#D1DDDB', command=FSSignup) 
     signupButton.config(font=("Ariel", 15))
     signupButton.grid(columnspan=2, sticky=W,pady=10)
    
     

def create_widgets_in_first_frame():
    
   
    def check():
     if os.path.isfile(no_logout):
      call_third_frame_on_top()
    
   
    def CheckLogin():
     f=open('NoLogout.txt','a')
     
     with open(creds) as f:
        data = f.readlines()                         
        uname = data[0].rstrip()                               
        pword = data[1].rstrip()                           
        
     if os.path.isfile(movie_file and songs_file and contacts_file and food_file and sports_file) and (nameEL.get() == uname and pwordEL.get() == pword):                                             #Takes you the main window if user has entered all the data
        pwordEL.delete(0,END)
        a=Label(first_frame,text="Either your password or your id \n is wrong",fg='#B7EEE6',bg='#B7EEE6')
        a.config(font=("Ariel", 15))
        a.grid(row=1)
        call_third_frame_on_top()
     elif nameEL.get() == uname and pwordEL.get() == pword: #Takes you the window where user has to enter all the data of his choice
        pwordEL.delete(0,END)
        a=Label(first_frame,text="Either your password or your id \n is wrong",fg='#B7EEE6',bg='#B7EEE6')
        a.config(font=("Ariel", 15))
        a.grid(row=1)
        
        call_second_frame_on_top()
       
     else:
        
          a=Label(first_frame,text="Either your password or your id \n is wrong",fg='#F70909',bg='#B7EEE6')
          a.config(font=("Ariel", 15))
          a.grid(row=1)
        
        
    # Create the label for the frame
    intruction = Label(first_frame, text='Login\n',bg='#B7EEE6',width=20)
    intruction.config(font=("Ariel", 22))
    intruction.grid(sticky=E) 
 
    nameL = Label(first_frame, text='Username(Twitter id): ',bg='#B7EEE6') 
    pwordL = Label(first_frame, text='Password: ',bg='#B7EEE6') 
    nameL.config(font=("Ariel", 15))
    pwordL.config(font=("Ariel", 15))
    nameL.grid(row=2, sticky=W)
    pwordL	.grid(row=4, sticky=W)
 
    nameEL = Entry(first_frame,width=25) 
    pwordEL = Entry(first_frame, show='*',width=25)
    nameEL.config(font=("Ariel", 15))
    pwordEL.config(font=("Ariel", 15))
    nameEL.grid(row=3, sticky=W)
    pwordEL.grid(row=5,sticky=W)
 
    loginB = Button(first_frame, text='Login',bg='#D1DDDB',command=CheckLogin,width=8,height=1) 
    loginB.config(font=("Ariel",15))
    loginB.grid(columnspan=2, sticky=W,pady=10)
    
    
def create_widgets_in_second_frame():
    def clear():                                          # Clears all the entered data in the various text box
     text1.delete('0.0',END)
     text2.delete('0.0',END)
     text3.delete('0.0',END)
     text4.delete('0.0',END)
     text5.delete('0.0',END)
    def Del():                                           # Delete all the entered data from files 
     os.remove(movie_file)
     os.remove(songs_file)
     os.remove(sports_file)
     os.remove(food_file)
     os.remove(contacts_file)
   
    def save():                                          # Saves all the data entered to a file
        text10 = text1.get("1.0",'end-1c')
        with open("Movies.txt", "a") as outf:
            outf.write(text10)
        text20 = text2.get("1.0",'end-1c')
        with open("Songs.txt", "a") as outf:
            outf.write(text20)
        text30= text3.get("1.0",'end-1c')
        with open("Sports.txt", "a") as outf:
            outf.write(text30)
        text40 = text4.get("1.0",'end-1c')
        with open("Food.txt", "a") as outf:
            outf.write(text40)
        text50 = text5.get("1.0",'end-1c')
        with open("Contacts.txt", "a") as outf:
            outf.write(text50)
        call_third_frame_on_top()
    first_window_label = Label(second_frame, text='Enter the data',bg='#B7EEE6',width=45)
    first_window_label.config(font=('Ariel',12))
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the button for the frame
    movie_button = tkinter.Button(second_frame, text = "Movies")
    movie_button.config(font=('Ariel',12))
    movie_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))

    text1=Text(master=second_frame,height=6,width=42)
    text1.grid(row=2,column=0)

    song_button = tkinter.Button(second_frame, text = "Songs")
    song_button.config(font=('Ariel',12))
    song_button.grid(column=0, row=3, pady=10, sticky=(tkinter.N))

    text2=Text(master=second_frame,height=6,width=42)
    text2.grid(row=4,column=0)

    food_button = tkinter.Button(second_frame, text = "Food")
    food_button.config(font=('Ariel',12))
    food_button.grid(column=0, row=5, pady=10, sticky=(tkinter.N))
    
    text3=Text(master=second_frame,height=6,width=42)
    text3.grid(row=6,column=0)

    sport_button = tkinter.Button(second_frame, text = "Sports")
    sport_button.config(font=('Ariel',12))
    sport_button.grid(column=0, row=7, pady=10, sticky=(tkinter.N))

    text4=Text(master=second_frame,height=6,width=42)
    text4.grid(row=8,column=0)

    Contact_button = tkinter.Button(second_frame, text = "Frequent Contacts")
    Contact_button.config(font=('Ariel',12))
    Contact_button.grid(column=0, row=9, pady=10, sticky=(tkinter.N))
 
    text5=Text(master=second_frame,height=6,width=42)
    text5.grid(row=10,column=0)

    Clear_button = tkinter.Button(second_frame, text = "Clear All", command=clear)
    Clear_button.config(font=('Ariel',12))
    Clear_button.grid(column=0, row=11, pady=10, sticky=(tkinter.W))

    Delete_button = tkinter.Button(second_frame, text = "Delete All entries(From file)", command = Del)
    Delete_button.config(font=('Ariel',12))
    Delete_button.grid(column=0, row=11, pady=10, sticky=(tkinter.E))
    
    Save_button = tkinter.Button(second_frame, text = "Save", command =save )
    Save_button.config(font=('Ariel',12))
    Save_button.grid(column=0 ,row=1, pady=10, sticky=(tkinter.E))

def create_widgets_in_third_frame():
        def past():
         tex.delete('0.0',END)
         import files
         for i in range(len(files.Max_tweet)):
          tex.insert(END,files.Max_tweet[i])
          tex.see(END)
          tex.insert(END,',')
          tex.see(END)
          tex.insert(END,'\n') 
          tex.see(END)
        def call():
          call_fourth_frame_on_top() 
        def edit():                          # Enables you to edit your choices
         call_second_frame_on_top()
        def week():                          # Analyse your tweets and classifies them into class which the tweets falls
         
         tex.delete('0.0',END)
         a=['depressed','sad']
         c=0
         import files
         call_fourth_frame_on_top()      
         
	 
         for i in  range(len(files.classified_list)):
           tex.insert(END,files.classified_list[i])
           tex.see(END)
           tex.insert(END,'\n') 
           tex.see(END) 
         suggestion_button = Button(third_frame, text="Suggestion",bg='#D1DDDB',fg='black', command=call,width=12)
         suggestion_button.config(font=('Ariel',12))
         suggestion_button.pack(pady=10) 
         
         root_window.configure(background='red')
        def Del():                                 # Delete the user account removes all the files from system related to the user account
         os.remove(creds)
         os.remove(no_logout)
         os.remove(movie_file)
         os.remove(songs_file)
         os.remove(contacts_file)
         os.remove(sports_file)
         call_zero_frame_on_top()
        def tweet():                                     # Returns all the tweets
          tex.delete('0.0',END)
          import code
          import files
          #print(files.final_tweets)
          for i in range(len(files.final_tweets)):
           tex.insert(END,files.final_tweets[i])
           tex.see(END)
           tex.insert(END,'\n')
           tex.see(END)
        def clear_text():                                #Clears the content of the text box in main window
          tex.delete('0.0',END)
        def get():                                       # Returns only those tweets which are tweeted within a span of 24hrs.     
          clear_text()
          import Web_scrape_Twitter as WST               # Program which returns the tweet which are tweeted within a span of 24hrs.
          d=WST.d
          tweet=WST.tweet
          if d>0:
           for i in range(0,d):
            
             
             tex.insert(END, tweet[i])
             tex.see(END)
             tex.insert(END, '\n')
             tex.see(END)
          else:
           s=["You haven't tweeted anything in the past 24 Hours"]
           tex.insert(END,s[0])
           tex.see(END)
        def logout():                                    #Takes you back to the login window 
         
         
         os.remove(no_logout) 
         c=1
         a=0
         with open('Logout.txt',"a") as f:
          f.write(str(c))
         with open('Logout.txt','r') as f:
          first_line=f.readline()
         for i in range(len(first_line)):
          a=a+int(first_line[i])
         with open('Logout.txt','w') as f:                # Logout.txt file keeps a track of how many times user has logged out
          f.write(str(a))
         call_first_frame_on_top()

        tex =Text(master=third_frame)	
        vsb =Scrollbar(third_frame, orient="vertical",bg='#6A6868', command=tex.yview)
        tex.configure(yscrollcommand=vsb.set)
        vsb.pack(side=RIGHT,fill='y')
        
        
        vsb.pack(side=RIGHT,fill='y')
        
        tex.pack(side=RIGHT,fill='both',expand=True)
        
 
        tweet_button = Button(third_frame, text='Get recent tweets',bg='#D1DDDB',fg='black',command=get)
        tweet_button.config(font=('Ariel',12))
        tweet_button.pack(pady=10)
        
        Week_button = Button(third_frame, text="Weekly Analysis",bg='#D1DDDB',fg='black', command=week)
        Week_button.config(font=('Ariel',12)) 
        Week_button.pack(pady=10)           
        
        Past_button = Button(third_frame, text="Past History",bg='#D1DDDB',fg='black', command=tweet)
        Past_button.config(font=('Ariel',12))
        Past_button.pack(pady=10)
      
        clear_button = Button(third_frame, text="Clear",bg='#D1DDDB',fg='black', command=clear_text)
        clear_button.config(font=('Ariel',12))
        clear_button.pack(pady=10)

 
        edit_button = Button(third_frame, text="Edit",bg='#D1DDDB',fg='black', command=edit)
        edit_button.config(font=('Ariel',12))
        edit_button.pack(pady=10)
        
        
        logout_button = Button(third_frame, text="Logout",bg='#D1DDDB',fg='black', command=logout)
        logout_button.config(font=('Ariel',12))
        logout_button.pack(pady=10)
        
        Delete_button = Button(third_frame, text="Delete Account",bg='#D1DDDB',fg='black', command=Del)
        Delete_button.config(font=('Ariel',12))
        Delete_button.pack(pady=10)
def create_widgets_in_fourth_frame():
        def movie():                                      # Returns the movies entered by user from the file Movies.txt 
         def back():
          root.destroy()
          
         with open('Movies.txt','r') as f:
          a = [line.strip() for line in f]
         print(a[0])
         file_name=a[0]+".txt"
         with open(file_name,'r') as f:
          contents = [line.strip() for line in f]
         
         root=Tk()
         root.title("Movies")
         text1 =Text(master=root,height=6,width=32)
         vsb =Scrollbar(root, orient="vertical",bg='#6A6868', command=text1.yview)
         text1.configure(yscrollcommand=vsb.set)
         vsb.pack(side=RIGHT,fill='y')
         text1.pack()
         b=Button(root,text='Back',bg='#D1DDDB',command=back)
         b.config(font=('Ariel',12))
         b.pack()
         root.configure(bg='#B7EEE6')
         for i in range(len(contents)):
           contents[i]=contents[i]+'\n'
           text1.insert(END, contents[i])
           text1.see(END)
         root.mainloop()
        def song():                                     #Returns the songs entered by user from the file Songs.txt
         def back():
          root.destroy()
         with open('Songs.txt','r') as f:         
          contents = [line.strip() for line in f]
         root=Tk()
         root.title("Songs")
         text1 =Text(master=root,height=6,width=32)
         vsb =Scrollbar(root, orient="vertical",bg='#6A6868', command=text1.yview)
         text1.configure(yscrollcommand=vsb.set)
         vsb.pack(side=RIGHT,fill='y')
         text1.pack()
         b=Button(root,text='Back',bg='#D1DDDB',command=back)
         b.config(font=('Ariel',12))
         b.pack()
         root.configure(bg='#B7EEE6')
         for i in range(len(contents)):
           contents[i]=contents[i]+'\n'
           text1.insert(END, contents[i])
           text1.see(END)
         root.mainloop()
        def sport():                                     #Returns the songs entered by user from the file Sports.txt
        
         def back():
          root.destroy()
          
         with open('Sports.txt','r') as f:
          contents = [line.strip() for line in f]
         root=Tk()
         root.title("Sports")
         text1 =Text(master=root,height=6,width=32)
         vsb =Scrollbar(root, orient="vertical",bg='#6A6868', command=text1.yview)
         text1.configure(yscrollcommand=vsb.set)
         vsb.pack(side=RIGHT,fill='y')
         text1.pack()
         b=Button(root,text='Back',bg='#D1DDDB',command=back)
         b.config(font=('Ariel',12))
         b.pack()
         root.configure(bg='#B7EEE6')
         for i in range(len(contents)):
           contents[i]=contents[i]+'\n'
           text1.insert(END, contents[i])
           text1.see(END)
         root.mainloop()
        def food():                                       #Returns the songs entered by user from the file food.txt
         def back():
          root.destroy()
         
         with open('Food.txt','r') as f:
          contents = [line.strip() for line in f]
         root=Tk()
         root.title("Food")
         text1 =Text(master=root,height=6,width=32)
         vsb =Scrollbar(root, orient="vertical",bg='#6A6868', command=text1.yview)
         text1.configure(yscrollcommand=vsb.set)
         vsb.pack(side=RIGHT,fill='y')
         text1.pack()
         b=Button(root,text='Back',bg='#D1DDDB',command=back)
         b.config(font=('Ariel',12))
         b.pack()
         root.configure(bg='#B7EEE6')
        def contacts():                                    #Returns the songs entered by user from the file Contacts.txt
         def back():
          root.destroy()
         with open('Contacts.txt','r') as f:
          contents = [line.strip() for line in f]
         root=Tk()
         root.title("Contacts")
         text1 =Text(master=root,height=6,width=32)
         vsb =Scrollbar(root, orient="vertical",bg='#6A6868', command=text1.yview)
         text1.configure(yscrollcommand=vsb.set)
         vsb.pack(side=RIGHT,fill='y')
         text1.pack()
         b=Button(root,text='Back',bg='#D1DDDB',command=back)
         b.config(font=('Ariel',12))
         b.pack()
         root.configure(bg='#B7EEE6')
         for i in range(len(contents)):
           contents[i]=contents[i]+'\n'
           text1.insert(END, contents[i])
           text1.see(END)
         root.mainloop()
        label=Label(fourth_frame,text='Take a look at what you liked previously',bg='#B7EEE6',width=60)
        label.config(font=('Ariel',12))
        label.pack()
        movie_button = Button(fourth_frame, text='Movies',bg='#D1DDDB',fg='black',command=movie,width=12)
        movie_button.config(font=('Ariel',12))
        movie_button.pack(pady=10)
        
        song_button = Button(fourth_frame, text="Songs",bg='#D1DDDB',fg='black', command=song,width=12)
        song_button.config(font=('Ariel',12))
        song_button.pack(pady=10)           
        
        food_button = Button(fourth_frame, text="Food",bg='#D1DDDB',fg='black', command=food,width=12)
        food_button.config(font=('Ariel',12))
        food_button.pack(pady=10)
         

        sport_button = Button(fourth_frame, text="Sport",bg='#D1DDDB',fg='black', command=sport,width=12)
        sport_button.config(font=('Ariel',12))
        sport_button.pack(pady=10)

 
        contact_button = Button(fourth_frame, text="Contacts",bg='#D1DDDB',fg='black', command=contacts,width=12)
        contact_button.config(font=('Ariel',12))
        contact_button.pack(pady=10)
        
        
         
        Home_button = Button(fourth_frame, text="Home",bg='#D1DDDB',fg='black', command=call_third_frame_on_top,width=12)
        Home_button.config(font=('Ariel',12))
        Home_button.pack(pady=10)   
     
        
def call_zero_frame_on_top():
    
     first_frame.grid_forget()
     second_frame.grid_forget()
     third_frame.grid_forget()
     fourth_frame.grid_forget()
     zero_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_first_frame_on_top():

    zero_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    fourth_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_second_frame_on_top():
    
    zero_frame.grid_forget()
    first_frame.grid_forget()
    third_frame.grid_forget()
    fourth_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_third_frame_on_top():
    
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    fourth_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_fourth_frame_on_top():
    
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def quit_program():
    root_window.destroy()

# Main program starts here  #


# Create the root GUI window.
root_window =Tk()

# Define window size
window_width = 400
window_heigth = 300


# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions.
#zero_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
zero_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#B7EEE6')
zero_frame['borderwidth'] = 2
zero_frame['relief'] = 'sunken'
zero_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E)) 


first_frame=Frame(root_window, width=300, height=200,bg='#B7EEE6')
first_frame['borderwidth'] = 2
first_frame['relief'] = 'sunken'
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#B7EEE6')
second_frame['borderwidth'] = 2
second_frame['relief'] = 'sunken'
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

third_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#B7EEE6')
third_frame['borderwidth'] = 2
third_frame['relief'] = 'sunken'
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fourth_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#B7EEE6')
fourth_frame['borderwidth'] = 2
fourth_frame['relief'] = 'sunken'
fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# Create all widgets to all frames
create_widgets_in_fourth_frame()
create_widgets_in_third_frame()
create_widgets_in_second_frame()
create_widgets_in_first_frame()
create_widgets_in_zero_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).

if (os.path.isfile(creds) and os.path.isfile(no_logout)):   #Directs to the main window if the user already has a account and not logged out
 
 fourth_frame.grid_forget()
 second_frame.grid_forget()
 first_frame.grid_forget()
 zero_frame.grid_forget()
elif os.path.isfile(creds):                                #Directs to the login window if the user already has a account and logged out
 fourth_frame.grid_forget()
 third_frame.grid_forget()
 second_frame.grid_forget()
 zero_frame.grid_forget()
else:                                                   #Direct to the Signup window if new user
 fourth_frame.grid_forget()
 third_frame.grid_forget()
 second_frame.grid_forget()
 first_frame.grid_forget()
# Start tkinter event - loop
root_window.title('Emotion detection')
root_window.configure(background='#D1DDDB')


root_window.mainloop()
