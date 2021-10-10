class label:
    def __init__(self,canvas):
        self.canvas=canvas
        self.labels=[]

    def new(self,name):
        with open('./gui/labels/'+name+'.label','r') as f:
            self.text=''
            for text in f:
                self.text+=text.strip()
            self.text=self.text.split(',')
            self.labels.append(self.canvas.create_text(self.text[1],self.text[2],font=('Arial',self.text[4]),text=self.text[0],fill=self.text[3]))