# import re

# pattern = '.*ma*n'
# test_string = 'woman'
# result = re.match(pattern, test_string)
# print(result)
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	

# import re

# #Replace all white-space characters with the digit "9":

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)


import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)
print(match)
print(match.start())
print(match.end())
if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  
