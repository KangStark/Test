class A(object):
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class B(A):
    def __init__(self, param3):
        
        super(B,self).__init__('param1', 'param2')
        self.param3 = param3
       
a= B('param3')
print a.param1
print a.param2
print a.param3
