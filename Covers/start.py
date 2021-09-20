class start:
    def __init__(self,canvas):
        self.item={
            'bg':canvas.create_rectangle(-200,225,0,275,fill='White'),
            'text':canvas.create_text(1100,250,text='start',fill='#000000',font=('Arial',20))
        }
        self.canvas=canvas

    def Loading(self,root,time):
        for i in range(60):
            self.canvas.move(self.item['bg'],10,0)
            self.canvas.move(self.item['text'],-10,0)
            root.update()
            time.sleep(0.01)