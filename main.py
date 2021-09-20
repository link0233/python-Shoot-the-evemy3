from tkinter import *
from Covers.covers_main import *
import time

class main(Canvas):
    def __init__(self,width=1000,height=700):
        self.root=Tk()
        self.root.title('shoot-the-evemy')
        super(main,self).__init__(self.root,width=width,height=height,bg='#ffaaff')
        self.pack()

<<<<<<< HEAD
=======
        self.bind('Motion',)

        time.sleep(1)
>>>>>>> da85b418997537f3b21ee1c81b04494f5f43f1f9
        self.cover=cover(self)
        self.cover.Loading(self.root,time)

        self.bind('<Motion>',self.mot)
        self.x=0
        self.y=0

        while True:
            self.cover.loop(self.x,self.y)
            self.root.update()
            time.sleep(0.01)

        self.root.mainloop()

    def mot(self,event):
<<<<<<< HEAD
        self.x=event.x
        self.y=event.y
=======
        pass
>>>>>>> da85b418997537f3b21ee1c81b04494f5f43f1f9
if __name__=='__main__':
    main()