from Covers.title import covers_title
from Covers.start import start

class cover:
    def __init__(self,canvas):
        self.title=covers_title(canvas)
        self.start=start(canvas)
        self.delete=0

    def Loading(self,root,time):
        self.title.loading(root,time)
        self.start.Loading(root,time)

    def loop(self,eventx,eventy,button1):
        self.start.loop(eventx,eventy)
        if abs(eventx-500)<100 and abs(eventy-250)<25 and button1==1:
            self.start.delete()
            self.title.delete()
            self.delete=1
        elif self.delete==1:
            self.start.delete()
            self.title.delete()