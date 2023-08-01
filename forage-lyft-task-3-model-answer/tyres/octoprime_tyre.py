from tyres import Tyre
class Octoprime(Tyre):
    def __init__(self,arr):
        self.arr=arr
    def needs_service(self):
        if sum(self.arr)>=3:
            return True
        else:
            return False