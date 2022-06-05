class Chain:
    def __init__(self,value) :
        self.value = value
    def __repr__(self):
        return repr(self.value)
    def __call__(self,value):
        if type(self.value) == str:
            value = Chain(self.value +' '+ value)
            return value
        else:
            value = Chain(self.value + value)
            return value
    def __lt__(self, other_object):
        return self.value < other_object.value

    def __eq__(self, other_object):
        return self.value == other_object
        