class player:
    def __init__(self,canvas):
        self.canvas=canvas

    def start(self,item,root,time):
        self.item=self.canvas.create_image(500,800,image=item)
        for t in range(60):
            self.canvas.move(self.item,0,-5)
            root.update()
            time.sleep(0.01)

    def loop(self,x,y):
        self.xy=self.canvas.coords(self.item)
        if abs(x-self.xy[0])>3:
            if self.xy[0]>x:
                self.canvas.move(self.item,-3,0)
            else:
                self.canvas.move(self.item,3,0)