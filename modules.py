# #modules are set of functions or class that are used to import from other module
# #math module
# #datetime module
# #os module
# #random module
# #calender module
# import datetime
# import calendar 

# # sqr=mh.sqrt(20)
# # print(sqr)
# print(calendar.isleap(2019))

import os
from datetime import datetime

# print('current working directory is',os.getcwd())

# os.makedirs('workmodules.py/subdic.py')

# print(os.listdir())
# os.removedirs('workmodules.py')
# os.rename('workmodules.py/subdic.py','note.txt')
# print(os.stat('note.txt'))
print(os.stat('note.txt').st_size)
t=(os.stat('note.txt').st_mtime)
print(datetime.fromtimestamp(t))

