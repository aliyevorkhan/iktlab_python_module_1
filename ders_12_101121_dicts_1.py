thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "hybrid": False,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(len(thisdict))

thisdict["modify_year"] = 2000
print(thisdict)
print(len(thisdict))

#accessing
#pint(thisdict["year"])
print(thisdict.get("year", 1999))
print(thisdict)

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

thisdict["hybrid"] = True
print(thisdict)

