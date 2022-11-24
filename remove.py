import os
from fnmatch import fnmatch

root = 'D:/rich 7 days'
pattern = "*.htaccess"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            try:
                os.remove(os.path.join(path, name))
            except:
                print("Something went wrong")