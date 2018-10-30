dict1 = {'zhangsan': '2341', 'lisi': '9102', 'tiantian': '3258'}
dict2 = {2341: 'zhangsan', 9102: 'lisi', 3258: 'tiantian'}
dict3 = dict(name='zhangsan', id='lisi')

print(dict3)
print(dict1['lisi'])
print(dict2[9102])

print(id(dict2))
dict2[9102] = 'liuze'
print(dict2)
print(id(dict2))

# dict2[9103] = 'mayun'
# print dict2#
# del dict2[9102]
# print dict2
#
# del dict2
# print dict2
#
print(2341 in dict2)
print('tiantian' in dict2)
#

print(2341 in dict2)
print('tiantian' in dict2)

print(dict2.pop(2341))


print(list(dict2.items()))


#
#
# # ***
# template = '''
#     <html>
#         <head>
#             <title>%(title)s</title>
#         </head>
#             <body>
#                 <h1>%(h1)s</h1>
#                 <p>%(text)s</p>
#             </body>
#     </html>
# '''
# data = {'h1':u'我的主页', 'title':u'笨方法学Python', 'text':u'欢迎来到Python学习小站'}
# print template % data
