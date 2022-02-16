import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  mdate = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(mdate))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
