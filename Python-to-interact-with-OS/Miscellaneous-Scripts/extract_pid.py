import re

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None:
    return ""
  return result

log = "July 31 mycomputer bad_process [12345] : ERROR"
print(extract_pid(log))

log = "99 elephants in a [cage]"
print(extract_pid(log))
