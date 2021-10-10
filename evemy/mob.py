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
            self.items.append({'item':self.canvas.create_image(320,240,image=self.image)})