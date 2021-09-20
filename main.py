from tkinter import *
from Covers.covers_main import *
import time

class main(Canvas):
    def __init__(self,width=1000,height=700):
        self.root=Tk()
        self.root.title('shoot-the-evemy')
        super(main,self).__init__(self.root,width=width,height=height,bg='#ffaaff')
        self.pack()

        self.bind('Motion',)

        time.sleep(1)
        self.cover=cover(self)
        self.cover.Loading(self.root,time)

        self.root.mainloop()

    def mot(self,event):
        pass
if __name__=='__main__':
    main()