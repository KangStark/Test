# coding=utf-8

# test_str = 'jkjsfjk/fajoifjs/{ififi}/fsflslf'
# tt  = ['ififi', 'hahaha']
#
# print test_str.count("{%s}"%tt[0])
# test_str=test_str.replace("{%s}"%tt[0],'hahaha')
# print test_str

# a=[{'a':1,'b':2},{'e':5,'f':6}]
# print a[0]['a']
# b=[]
# b=a.append({'c':3,'d':4})
# print b
# b=[{}]
# print b.append({})
# print len(b)


class test(object):
    def __init__(self):
        self._payload = {'others0': 'other_params0','others1': 'other_params1'}

    def add_body_param(self, k, v):
        self._payload[k] = v

    def get_members(self):
        return self.get_body_param().get('members')

    def get_body_param(self):
        return self._payload


    def set_members(self, members):
        if members != []:
            self.add_body_param('members', members)
        if self.get_members() is None:
            self.add_body_param('members', members)
        if members == []:
            self._payload['members'].append({})

    def add_member_param(self, k, v):
        self._payload['members'][len(self.get_members())-1][k] = v

    def add_member_id(self, ID):
        self.add_member_param('id', ID)

    def add_member_port(self, port):
        self.add_member_param('port', port)

t = test()
# 依次添加
t.set_members([])
t.add_member_id('test_id')
t.add_member_port('test_port')
print t._payload

t.set_members([])
t.add_member_id('test_id2')
t.add_member_port('test_port2')
print t._payload

# 批量添加
t.set_members([{'id':'test_id1','port':'test_port1'},
               {'id':'test_id2','port':'test_port2'},
               {'id':'test_id3','port':'test_port3'}])
print t._payload

t.set_members([])
t.add_member_id('test_id2')
t.add_member_port('test_port2')
print t._payload
