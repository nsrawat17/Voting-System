import tkinter as tk
from tkinter import messagebox
# import library for voice
import pyttsx3

class VotingSystem:
    def __init__(self,root):
        self.root=root
        # create title
        self.root.title("VOTING SYSTEM")

# intialize pyttsx3
        self.engine=pyttsx3.init()


        self.BJP = 0
        self.CONGRESS=0
        self.AAP=0

# create a headline for greeting
        self.label=tk.Label(root,text="Thankyou for Coming to the polling  station")
        self.label.pack(pady=10)

# create a button for BJP
        self.btn_BJP=tk.Button(root,text="Press for vote for BJP ",command=self.vote_BJP)
        self.btn_BJP.pack(pady=7)

# create a buttton for congress
        self.btn_CONGRESS=tk.Button(root,text="Press for vote for CONGRESS ",command=self.vote_CONGRESS)
        # pady and pack use add some common space vertical and horizontal
        self.btn_CONGRESS.pack(pady=7)
# create a button for AAP
        self.btn_AAP=tk.Button(root,text="Press for vote for APP ",command=self.vote_AAP)
        self.btn_AAP.pack(pady=10)
# create a button for result
        self.btn_results = tk.Button(root, text="Show Results", command=self.voting_result)
        self.btn_results.pack(pady=10)

# define function for BJP
    def vote_BJP(self):
        self.BJP +=1
        self.speak("JAi  Shree Ram")
        messagebox.showinfo("vote","You vote for BJP")
# define function for congress
    def vote_CONGRESS(self):
        self.CONGRESS +=1
        self.speak("Appka Sath hamare Sath")
        messagebox.showinfo("vote","You vote for Congress")
# define function for AAP
    def vote_AAP(self):
        self.AAP +=1
        self.speak(" Sub kuch free free")
        messagebox.showinfo("vote","You vote for AAP")
# define function for Results
    def voting_result(self):
        results = (
            f"Result \n"
            f"BJP : {self.BJP}  votes \n"
            f"CONGRESS : {self.CONGRESS}  votes \n"
            f"AAP : {self.AAP}  votes \n"
        )
        messagebox.showinfo("Results",results)

    def speak(self , text ):
        self.engine.say(text)
        self.engine.runAndWait()


root=tk.Tk()
voting_system=VotingSystem(root)
root.mainloop()




