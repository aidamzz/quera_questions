import traceback
class Chain:
    def __init__(self,value) :
        self.value = value
    def __repr__(self):
        return repr(self.value)
    def __call__(self,value):
        if type(self.value) == str:
            try:
                value = Chain(self.value +' '+ value)
                return value
            except Exception:
                traceback.print_exc()
                print('Exception: invalid operation')
            
        else:
            value = Chain(self.value + value)
            if int(value) == value:
                value = int(value)
            return value
    def __lt__(self, other_object):
        return self.value < other_object.value

    def __eq__(self, other_object):
        return self.value == other_object
        