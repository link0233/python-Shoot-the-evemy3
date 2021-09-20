class start:
    def __init__(self,canvas):
        self.item={
            'bg':canvas.create_rectangle(400,225,600,275,fill='White'),
            'text':canvas.create_text(500,250,text='start',fill='#000000',font=('Arial',20))
        }