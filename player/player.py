from player.si import si

class player:
    def __init__(self,canvas):
        self.canvas=canvas
        self.si=si(canvas)
        self.time=0
        self.sit=100
        with open('./gui/labels/player_sit.label','w') as f:
            f.write('剩餘子彈:'+str(self.sit)+',100,50,White,15')

    def start(self,item,root,time):
        self.item=self.canvas.create_image(500,800,image=item)
        for t in range(60):
            self.canvas.move(self.item,0,-5)
            root.update()
            time.sleep(0.01)

    def loop(self,x,button1):
        self.time+=1
        self.xy=self.canvas.coords(self.item)
        #射擊
        if self.time>10 and button1==1 and self.sit>0:
            self.si.step(self.xy[0],self.xy[1]-20)
            self.time=0
            self.sit-=1

        with open('./gui/labels/player_sit.label','w') as f:
            f.write('剩餘子彈:'+str(self.sit)+',100,50,White,15')
        self.si.loop()

        if abs(x-self.xy[0])>5:
            if self.xy[0]>x:
                self.canvas.move(self.item,-5,0)
            else:
                self.canvas.move(self.item,5,0)