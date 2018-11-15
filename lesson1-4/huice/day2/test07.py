dict_ee = {2341: 'zhangsan', 3102: 'lisi', 3258: 'tiantian', 7540: 'liuze', 7541:'mayun'}
dict_ee2 = {2341: 'zhangsan', 3102: 'lisi', 3258: 'tiantian', 7540: 'liuze', 7541:'mayun'}

# ee = dict_ee.pop(7541)
# print ee
# print dict_ee

# print cmp(dict_ee, dict_ee2)
# print dict_ee == dict_ee2
# print len(dict_ee), len(dict_ee2)
#
#
# dic_key = dict_ee.keys()
# print type(dic_key)
# print dic_key
#
# dic_value = dict_ee.values()
# print type(dic_value)
# print dic_value
#
# for key in dict_ee.keys():
#     print key
#
# for value in dict_ee.values():
#     print value
#
# dict_items = dict_ee.items()
# for item in dict_items:
#     print 'key:'+str(item[0])+', vlaue:'+item[1]
#
#
# dict_ee2.clear()
# print dict_ee2
# print len(dict_ee2)
#
# dict_ee3 = dict_ee.copy()
# print id(dict_ee)
# print id(dict_ee3)
# print dict_ee3 == dict_ee


student_id = [1, 2, 3, 4, 5, 4, 1]
student_name = 'name'

dict_ee4 = dict.fromkeys(student_id)
print(dict_ee4)

# dict_ee4 = dict.fromkeys(student_id, student_name)
# print dict_ee4

print(dict_ee[7541])
# print dict_ee[7542]
print(dict_ee.get(7542, 'name'))

print(dict_ee)
print(dict_ee4)
dict_ee.update(dict_ee4)
print(dict_ee)

dict_ee.update({1:'zhangyi', 2:'zhanger', 3:'zhangsan'})
print(dict_ee)


# for
for key, value in list(dict_ee.items()):
    print('key:%d value:%s' %(key, value))


# switch
list_id = [2341, 3102, 3258, 7540, 7541]
list_name = ['zhangsan', 'lisi', 'tiantian', 'liuze', 'mayun']
dic_new = dict(list(zip(list_id, list_name)))
print(dic_new)
print(dict([[2341,'zhangsan'],[3102,'lisi'],[3258,'tiantian'],[7540,'liuze'],[7541,'mayun']]))


# ==keys
print(list(dict_ee))
print(tuple(dict_ee))
print(str(dict_ee))

