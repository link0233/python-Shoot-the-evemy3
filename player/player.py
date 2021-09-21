class player:
    def __init__(self,canvas):
        self.canvas=canvas

    def start(self,item):
        self.item=self.canvas.create_image(500,640,image=item)