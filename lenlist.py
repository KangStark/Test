A=[{'a':1,'b':2,'c':3},{'a':4,'c':5}]
print len(A)

class test(object):
    def __init__(self):
        self._params=None
    
    def add_query_param(self, k, v):
        self._params[k] = v

    def set_DataDisks(self, DataDisks): 
	for i in range(len(DataDisks)):
	    if DataDisks[i].get('a') is not None:
		self.add_query_param('DataDisk.' + str(i + 1) + '.a' , DataDisks[i].get('a'))
	    if DataDisks[i].get('b') is not None:
		self.add_query_param('DataDisk.' + str(i + 1) + '.b' , DataDisks[i].get('b'))
	    if DataDisks[i].get('c') is not None:
		self.add_query_param('DataDisk.' + str(i + 1) + '.c' , DataDisks[i].get('c'))
	    if DataDisks[i].get('d') is not None:
		self.add_query_param('DataDisk.' + str(i + 1) + '.d' , DataDisks[i].get('d'))

t1 = test()
t1.set_DataDisks(A)
print A
