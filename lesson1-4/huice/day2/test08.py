from collections import OrderedDict

dict_ee = {2341: 'zhangsan', 3102: 'lisi', 3258: 'tiantian', 7540: 'liuze', 7541:'mayun'}
dict_new = sorted(dict_ee.items())
print(dict_ee)
print(dict_new)
print(OrderedDict(dict_new))

dict_order = OrderedDict([[2341,'zhangsan'],[3102,'lisi'],[3258,'tiantian'],[7540,'liuze'],[7541,'mayun']])
# for key, value in dict_order.items():
#     print 'key:%d value:%s' % (key, value)

print(dict_order)