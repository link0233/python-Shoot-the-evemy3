class si:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=[]
        
    def step(self,x,y):
        self.item.append({
            'item':self.canvas.create_rectangle(x-5,y-20,x+5,y,fill='#0000ff'),
            'xy':[x-5,y-20,x+5,y]
        })

    def loop(self):
        self.item_new=[]
        for item in self.item:
            self.canvas.move(item['item'],0,-10)
            item['xy']=self.canvas.coords(item['item'])
            if item['xy'][1]<20:
                self.canvas.delete(item['item'])
            else:
                self.item_new.append(item)
        self.item=self.item_new