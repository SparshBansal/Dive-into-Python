# Create a string
s = "this is a string"
print s

# Length of a string
print len(s)

# print a character of a string
print s[2]

# Concatenating strings
print s + ". Also it can be appended."

formatter = "{n}"

# Formatting strings -- using a format() method on strings
print "{0} can be used as placehoder".format(formatter)

# Compound field name we can use compound objects as arguments to
# the format methods
import humansize
suffixes = humansize.SUFFIXES[1000]

print "1000{0[0]} = 1{0[1]}".format(suffixes)

# format specifiers-- : marks the beginning of the format specifier .1
# represents number of places after decimal point and f represents fixed point
# representation
print "{0:.2f}{1}".format(931.232 , "GB")

# Other string operations

# multiline strings
m_string = '''This is a multiline string
It means that this strings has multiple lines
we can use splitlines methods to split this string into lines
'''

print m_string.splitlines()

# Another operation on strings

# Lets try nested comprehensions

query = 'user=pilgrim&database=master&password=PapayaWhip'
m_list = query.split('&')

m_dict = {}

for queryString in m_list:
    m_dict[queryString.split('=')[0]] = queryString.split('=')[1]

print m_dict;

# splicing strings in just like splicing lists
print query[2:18]
