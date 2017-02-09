# Regular expressions when searching in a string has to be more flexible
# than simple methods on strings

# Some string methods -- remember strings are immutable sequences

s = "100 NORTH MAIN ROAD"

# replace a substring by another substring
ns = s.replace("ROAD" , "RD.");

# print s
print ns;

# Problem with blind replacement
s = "100 NORTH BROAD ROAD"
ns = s.replace("ROAD" , "RD.")

print ns

# import regular expressions' module
import re

# Now solve the above question with regular expression
ns_regular = re.sub("ROAD$" , "RD." , s)

print ns_regular

# $ matches the expression at the end of the string
# Problem with this approach
another_string = "100 NORTH BROAD"

another_result = re.sub("ROAD$" , "RD." , another_string);
print another_result

# Solution is to word boundaries - we use raw strings here
# Raw String - Strings preceded by r , in raw string nothing is escaped

final_string = "100 BROAD ROAD APT 3"
final_result = re.sub(r"\bROAD\b" , "RD." , final_string);

print final_result

# Roman Numerals examples

# Checking for thousands
# pattern = '^M?M?M?$'
#
# # matches upto 3 M's
# print re.search(pattern , 'M')
# print re.search(pattern , 'MM')
# print re.search(pattern , 'MMM')
# print re.search(pattern , 'XM')
#
# # Append for matching hundreds
# pattern = '^M?M?M?(CM|CD|D?C?C?C?)'
#
# print re.search(pattern , 'MC')
# print re.search(pattern , 'MCC')


# Another easy way of doing this using {i,j} operator
pattern = '^M{0,3}D?C{0,3}$'

# Appending for tens and ones
# Final roman numeral tester
pattern = '^M{0,3}(D?C{0,3}|CD|CM)(XL|XC|L?X{0,3})(IV|IX|V?I{0,3})$'

# Lets match some roman Numerals
# print re.search(pattern, 'MDLV')
# print re.search(pattern, 'MMDCLXVI')
# print re.search(pattern, 'MMMDCCCLXXXVIII')
# print re.search(pattern, 'I')
# print re.search(pattern, 'XXC')

# Verbose regular expressions allows us to put comments and whitespace and
# carriage returns in the regular expression and it ignores them. If we wish
# to match any whitespace or cr we must escape it. Also we need to explicilty
# specify verbose expression constant in re.search()

pattern = '''
^                   # Matches the start of the string
M{0,3}              # Matches 0 to 3 M for thousands place
(CM|CD|D?C{0,3})    # Matches hundreds place with CD and CM being the
                    # exceptions
(XL|XC|L?X{0,3})    # Matches tens place just like hundreds
(IV|IX|V?I{0,3})    # Matches ones place just like tens
$                   # Matches end of string
'''

print re.search(pattern, 'MDLV' , re.VERBOSE)
print re.search(pattern, 'MMDCLXVI' , re.VERBOSE)
print re.search(pattern, 'MMMDCCCLXXXVIII' , re.VERBOSE)
print re.search(pattern, 'I' , re.VERBOSE)
print re.search(pattern, 'XXC' , re.VERBOSE)


# Case Study -- Parsing phone numbers -- Dive into python3

# Phone numbers to accept
#
# 800-555-1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234
#
# Also identify the area code, trunk , number and extension

# \d matches any digit 0-9
# \D matches any character except a digit
phone_pattern = re.compile(r"(\d{3})\D+(\d{3})\D+(\d{4})\D*(\d+)?$")

print phone_pattern.search("800-555-1212").groups()
print phone_pattern.search("800 555 1212 1234").groups()

# Verbose version
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
''', re.VERBOSE)

print phone_pattern.search("800-555-1212").groups()
print phone_pattern.search("800 555 1212 1234").groups()
