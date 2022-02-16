import re

def rearrange_name(name):
  # old line: result = re.search(r"^(\w*), (\w*)$", name)
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

#print(rearrange_name("Lovelace, Ada"))
#print(rearrange_name("Ritchie, Dennis"))

