class label:
    def __init__(self,canvas):
        self.canvas=canvas

    def new(self,name):
        with open('./gui/labels/'+name+'.label','r') as f:
            print(123)