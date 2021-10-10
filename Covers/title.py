class covers_title:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=canvas.create_text(500,1000,text='Shoot-the-evemy',font=('Arial',50),fill='#ffffff')
    
    def loading(self,root,time):
        for i in range(90):
            self.canvas.move(self.item,0,-10)
            root.update()
            time.sleep(0.01)

    def loop(self):
        self.canvas.delete(self.item)
        self.item=self.canvas.create_text(500,1000,text='Shoot-the-evemy',font=('Arial',50),fill='#ffffff')

    def delete(self):
        self.canvas.delete(self.item)