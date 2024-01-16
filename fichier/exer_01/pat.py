from pathlib import Path

a = Path.home() /"Documents" / "bisben.txt"
print(a)

a.touch()

# print(a)

# print (a/"Documents")/


# new_file = a.touch('bisben.py')

# new_way_of_file = a/"Documents"/new_file

# print(new_way_of_file)