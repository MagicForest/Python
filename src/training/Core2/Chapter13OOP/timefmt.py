import time

class TimeFmt(object):
    def __init__(self,val=time.time()):
        self.value = val

    def update(self,new_value=time.time()):
        self.value = new_value

    def display(self,style=""):
        styles = {"MDY":"%m/%d/%y", "MDYY":"%m/%d/%Y", "DMY":"%d/%m/%y",
                  "DMYY":"%d/%m/%Y", "MODYY":"%a %d, %Y"}
        if style in styles:
            return time.strftime(styles[style],time.localtime(self.value))
        else:
            return time.asctime(time.localtime(self.value))
