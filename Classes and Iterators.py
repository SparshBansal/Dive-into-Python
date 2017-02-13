import re
# An iterator in the form of a class
class Fib:
    '''
    Fibonacci Number generator using class
    '''

    def __init__(self , max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    # Define __next__() for Python3 and next() for Python2
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a,self.b= self.b,self.a+self.b
        return fib

# We can create an instance by just calling the class as if it were a function
fib_20 = Fib(20)

for num in fib_20:
    print (num)


def build_match_and_apply_functions(pattern , search , replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search , replace , word)

    return (matches_rule , apply_rule)


# Building an iterator for the plural nouns problems
class LazyRules:

    def __init__(self , filename):
        self.rules_filename = filename
        self.pattern_file = open(filename , 'r')
        self.cache = []

    def __iter__(self):
        self.cache_idx = 0
        return self

    def __next__(self):
        self.cache_idx += 1
        if len(self.cache) >= self.cache_idx:
            return self.cache[self.cache_idx - 1]

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search , replace = line.split(None,3)
        funcs = build_match_and_apply_functions(pattern,search,replace)
        self.cache.append(funcs)
        return funcs

# Instantiate our class
rules = LazyRules('plural4-rules.txt')

def plural(noun):
    for match_rule , apply_rule in rules:
        if match_rule(noun):

            return apply_rule(noun)

# Test it out
print (plural('vacancy' ))
print (plural('daisy' ))
print (plural('noise'))
print (plural('boy' ))
print (plural('watch' ))
