from tkinter import *

class main(Canvas):
    def __init__(self,width=1000,height=600):
        self.root=Tk()
        self.root.title('shoot-the-evemy')
        super(main,self).__init__(self.root,width=width,height=height,bg='#ffaaff')
        self.pack()
        self.root.mainloop()
if __name__=='__main__':
    main()