from Covers.title import covers_title
from Covers.start import start

class cover:
    def __init__(self,canvas):
        self.title=covers_title(canvas)
        self.start=start(canvas)

    def Loading(self,root,time):
        self.title.loading(root,time)