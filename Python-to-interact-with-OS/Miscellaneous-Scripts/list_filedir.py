import os

dir = "/home/ahmed/googleCourse"

for name in os.listdir():
  fullname = os.path.join(dir,name)
  if os.path.isdir(fullname):
    print('{} is a directory.'.format(fullname))
  else:
    print('{} is a file.'.format(fullname))
