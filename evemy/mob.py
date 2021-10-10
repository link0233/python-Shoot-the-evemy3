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