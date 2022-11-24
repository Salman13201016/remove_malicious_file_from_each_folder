import os
from fnmatch import fnmatch

root = 'your directory'
pattern = "*.htaccess" #specific File Pattern

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            try:
                os.remove(os.path.join(path, name))
            except:
                print("Something went wrong")
