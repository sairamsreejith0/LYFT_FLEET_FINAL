from tyres import Tyre
class Carrigan(Tyre):
    def __init__(self,arr):
        self.arr=arr
    def needs_service(self):
        c=0
        for i in self.arr:
            if i>=0.9:
                c+=1
        if c>0:
            return True
        else:
            return False             