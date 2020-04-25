import randomlist
from Folders import create_folders, delete_folders

create_folders()
delete_folders()

print(randomlist.get_random([1, 2, 3, 4]))
print(randomlist.get_random([]))
