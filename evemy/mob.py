from random import randint

class mob:
    def __init__(self,canvas,PhotoImage):
        self.canvas=canvas
        self.items=[]
        self.PhotoImage=PhotoImage
        
    def df(self,mob):
        with open('./evemy/evemys/'+mob+'.mob','r') as f:
            self.text=''
            for test in f:
                self.text+=test.strip()
            self.text=self.text.split(',')
            print(self.text)
            self.image=self.PhotoImage(file='./evemy/evemy_image/'+self.text[0]+'.png')
            self.items.append({'item':self.canvas.create_image(randint(50,600),0,image=self.image),
                'move':[self.text[1],self.text[2]],
                'shoot':self.text[3],
                'big':self.text[4],
                'df':self.text[5]
            })

    def loop(self):
        for item in self.items:
            self.random=randint(1,int(item['move'][0]))#move
            if self.random==1:
                self.canvas.move(item['item'],item['move'][1],0)