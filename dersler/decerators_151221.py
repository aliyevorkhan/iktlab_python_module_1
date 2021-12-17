# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       print("lc_func: ", func)
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper

# decorator function to split words
def splitter_decorator(function):
   def hhhh():
       func = function()
       print("sp: ", func)
       string_split = func.split()
       return string_split[0], string_split[-1]
   return hhhh

def reverse_decorator(function):
    def wrapper():
        a, b = function()
        return b, a
    return wrapper

@reverse_decorator
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
s = hello()   # output => [ 'hello' , 'world' ]
print(s)

# def splitter(s):
#     return s.split()

# def lowercaser(s):
#     return s.lower()

# def hello():
#     return "Hello World"

# s = hello()
# print(s)
# s = lowercaser(s)
# print(s)
# s = splitter(s)
# print(s)