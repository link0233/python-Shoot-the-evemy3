from gui.label import label

class gui_main:
    def __init__(self,canvas):
        self.canvas=canvas
        self.label=label(canvas)

    def start(self):
        self.label.new('aaaa')