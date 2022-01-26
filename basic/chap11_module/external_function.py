# list of python modules

import glob
print(glob.glob("*.py"))
# ['built_in_function.py', 'external_function.py', 'fromimportas.py', 'import.py', 'inspect_test.py', 'package_from.py', 'package_test.py', 'test_module.py', '__all__test.py']

import os
print(os.getcwd())
# ./

folder = "simple_dir"

if os.path.exists(folder):
    print("Already")
else:
    os.makedirs(folder)
    print(folder, "done")
    
if os.path.exists(folder):
    os.rmdir(folder)
    print("removed")    

print(os.listdir()) #all files

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# %Y : YYYY / %y : yy / %m : MM / %d : DD / %D : MM/DD/YY

import datetime
print(datetime.date.today())
print(datetime.date.today() + datetime.timedelta(days=100)) #100일 뒤