class si:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=[]
        
    def step(self,x,y):
        self.item.append({
            'item':self.canvas.create_rectangle(x-5,y-20,x+5,y,fill='#ff0000')
        })