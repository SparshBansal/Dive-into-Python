import os

# use it to get the current working directory
print os.getcwd()

# use it to change the current working directory
# Note -- Linux style paths have been used here on Windows Machine
os.chdir('C:/Users/SPARSH/Desktop')
print os.getcwd()

# OS module also provides a path module
# On windows a backslash is added and on linux a forward slash is added
newPath = os.path.join('C:/Users/SPARSH/Desktop','image.jpg')
print newPath

print os.path.expanduser('~')

# os.path.split can be used to find the filename and dirname
# It returns a tuple

(dirname , filename) = os.path.split(newPath)
print dirname
print filename

# os.path.splitext splits a filename into the shortname and the extension
# Also returns a tuple
(shortname , extension) = os.path.splitext(filename)
print shortname
print extension


# GLOB module to get contents of directories programmatically
import glob
import time
import humansize

# glob method matches the given wildcard against the filename and returns
# the matched list
print glob.glob('*.jpg')

os.chdir('C:/Users/SPARSH')

# We can specify wildcards for filenames/dirnames in subdirectories
print glob.glob('C:/Users/SPARSH/WebstormProjects/*')

# Access file metadata -- Don't need to open the file, just the filenames
# is required
os.chdir('C:/Users/SPARSH/Desktop')
metadata = os.stat('image.jpg')

print metadata.st_mtime
print time.localtime(metadata.st_mtime)
print humansize.approximateSize(metadata.st_size)

# print the absolute path from the root
print os.path.realpath('image.jpg')

# Comprehensions in a list

# mapping a list to another by applying a function to each element of the list
a_list = [2,4,5,6]

a_new_list = [2*element for element in a_list]

print a_new_list

# Applying Comprehensions to glob lists
print [os.path.realpath(element) for element in glob.glob('*')]

# We can also apply filters to shorten lists by appending if statements at the
# end of the comprehension
print [f for f in glob.glob('*') if os.stat(f).st_size > 3000]

# We can also make complex statements in the Comprehensions
print [(humansize.approximateSize(os.stat(filename).st_size) , filename) for filename in glob.glob('*')]


# Comprehensions in a dictionary

# Creating a dictionary using Comprehensions
meta_dict = {f : os.stat(f) for f in glob.glob('*')}

print meta_dict
print meta_dict.keys()

# Include if clause to filter the dictionary
refined_dict = {f : os.stat(f) for f in glob.glob('*') if os.stat(f).st_size > 3000}
print refined_dict

# Another example
new_dict = {os.path.splitext(filename)[0] : humansize.approximateSize(meta.st_size) for filename,meta in meta_dict.items()}
print new_dict

# reverse key value pairs in a dictionary
reverse_dict = {value : key for key,value in new_dict.items()}
print reverse_dict


# Comprehensions in sets

# Almost same as comprehensions in dictionaries
filename_set = {f for f in meta_dict.keys()}
print filename_set
