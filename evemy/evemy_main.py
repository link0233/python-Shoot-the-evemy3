from evemy.mob import mob

class evemy_main:
    def __init__(self,canvas,Photo):
        self.mob=mob(canvas,Photo)
    
    def level1(self):
        self.mob.df('mob1')