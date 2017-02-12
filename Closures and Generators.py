# Plural nouns examples using regular expressions

import re

# function to pluralize nouns
def plural(noun):
    if re.search(noun , '[sxz]$'):
        return re.sub('$' , 'es' , noun)

    # negation regex matches anything except the mentioned expressions
    elif re.search('[^aeioudkgprt]h$' , noun):
        return re.sub('$' , 'es' , noun)

    elif re.search('[^aeiou]y$' , noun):
        return re.sub('y$' , 'ies' , noun)

    else:
        return noun + 's'

# # Test it out
# print plural('vacancy')
# print plural('daisy')
# print plural('noise')
# print plural('boy')
# print plural('watch')


# Another way of doing the same thing
def match_sxz(noun):
    return re.search('[sxz]$' , noun)

def apply_sxz(noun):
    return re.sub('$' , 'es' , noun)


def match_h(noun):
    return re.search('[^aeioudkpgrt]h$' , noun)

def apply_h(noun):
    return re.sub('$' , 'es' , noun)


def match_y(noun):
    return re.search('[^aeiou]y$' , noun)

def apply_y(noun):
    return re.sub('y$' , 'ies' , noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

# rules = ((match_sxz , apply_sxz),
#          (match_h , apply_h),
#          (match_y , apply_y),
#          (match_default , apply_default))
#
# def plural(noun):
#     for match_rule,apply_rule in rules:
#         if(match_rule(noun)):
#             return apply_rule(noun)
#
#
# # Test it out
# print plural('vacancy')
# print plural('daisy')
# print plural('noise')
# print plural('boy')
# print plural('watch')


# Lets write it in a shorter way by factoring out repetitive parts

def build_match_and_apply_functions(pattern , search , replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search , replace , word)

    return (matches_rule , apply_rule)

# patterns = (('[sxz]$' , '$' , 'es'),
#             ('[^aeioudkpgrt]h$' , '$' , 'es'),
#             ('[^aeiou]y$' , 'y$' , 'ies'),
#             ('$' , '$' , 's'))

# rules = [build_match_and_apply_functions(pattern,search,replace) for pattern,search,replace in patterns]


def plural(noun):
    for match_rule,apply_rule in rules:
        if(match_rule(noun)):
            return apply_rule(noun)

#
# # instead of declaring in the program read from a file instead
# rules = []
#
# with open('plural4-rules.txt' , 'r') as pattern_file:
#     for line in pattern_file :
#         pattern, search , replace = line.split(None , 3)
#         rules.append(build_match_and_apply_functions(pattern , search , replace))

# # Test it out
# print plural('vacancy')
# print plural('daisy')
# print plural('noise')
# print plural('boy')
# print plural('watch')

# Now using generators to do the same
def rules(rules_filename):
    with open(rules_filename , 'r') as pattern_file:
        for line in pattern_file:
            pattern , search , replace  = line.split(None , 3)
            yield build_match_and_apply_functions(pattern , search , replace)


def plural(noun , rules_filename):
    for match_rule , apply_rule in rules(rules_filename):
        if match_rule(noun):

            return apply_rule(noun)

filename = 'plural4-rules.txt'
# Test it out
print plural('vacancy' , filename)
print plural('daisy' , filename)
print plural('noise' ,  filename)
print plural('boy' , filename)
print plural('watch' , filename)

# Building a fibanacci generator
def fib(n):
    a , b = 0,1
    while a <= n:
        yield a
        a , b = b , a+b

fib_20 = fib(20)

for element in fib_20:
    print element
