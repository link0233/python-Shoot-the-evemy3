from Covers.title import covers_title

class cover:
    def __init__(self,canvas):
        self.title=covers_title(canvas)

    def Loading(self,root,time):
        self.title.loading(root,time)