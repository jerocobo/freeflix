from Tkinter import *
import freeFlix
import os


class MyDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.canvas = Canvas( self.top, width=300, height=450 )
        self.bgimage = PhotoImage(file = os.getcwd() + "/doggy3.gif")
        # self.bgimage.pack()
        # print os.getcwd() + "1.gif"
        self.controlFrame = Frame(self.top)
        self.controlFrame.pack(side=RIGHT, padx=2, pady=2, fill=Y)

        self.canvas.create_image(250,200,image = self.bgimage )
        self.canvas.pack( expand=YES, fill=BOTH )
        self.choice = "Movie"
        self.movie = Button(self.controlFrame, text= "Movie",highlightbackground= "red", command = self.choose_movie)
        self.movie.configure(bg = "red")
        self.movie.pack()
        self.tv = Button(self.controlFrame, text= "TV", command = self.choose_tv, bg = 'green')
        self.tv.grid(row=0, column=0)
        self.tv.pack()

        # self.choice = StringVar(top)
        # self.choice.set("Movie") # default value

        # w = OptionMenu(top, self.choice, "Movie", "TV")
        # w.pack()

       

        Label(self.controlFrame, text="Name").pack()

        self.e = Entry(self.controlFrame)
        self.e.pack(padx=5)

        self.season = Label(self.controlFrame, text="Season")
        self.episode = Label(self.controlFrame, text="Episode")
        #season.pack()
        self.e1 = Entry(self.controlFrame)
        self.e2 = Entry(self.controlFrame)
        #self.e1.pack(padx=5)


        self.b = Button(self.controlFrame, text="OK", command=self.ok)
        self.b.pack(pady=5)
    def choose_movie(self):
        self.choice = "movie" 
        self.movie.configure(highlightbackground= "red")
        self.tv.configure(highlightbackground= "white")
        self.season.pack_forget()
        self.episode.pack_forget()
        self.e1.pack_forget()
        self.e2.pack_forget()


    def choose_tv(self):
        self.choice = "TV"
        self.tv.configure(highlightbackground= "red")
        self.movie.configure(highlightbackground= "white")
        self.b.pack_forget()
        self.season.pack()

        self.e1.pack(padx=5)
        self.episode.pack()
        self.e2.pack()
        self.b.pack(pady=5)
 

    def ok(self):
 
        print self.e.get() 
        if self.choice == "TV":
            print self.e1.get(), self.e2.get()
            freeFlix.finder(["tv"]+self.e.get().split()+ [self.e1.get(),self.e2.get() ])
        else:
            freeFlix.finder(self.e.get().split() )

        self.top.destroy()  


root = Tk()
root.title("freeFlix")
root.withdraw()

d = MyDialog(root)
root.update()


root.wait_window(d.top)