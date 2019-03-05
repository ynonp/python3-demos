import glob
import os.path
import collections
all_files_with_extensions = glob.glob('*.*')

extensions = [
    os.path.splitext(fname)[1]
    for fname in all_files_with_extensions
]

counter = collections.Counter(extensions)
print(counter)