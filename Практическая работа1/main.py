from tasks.task1 import *
from tasks.task7 import *
from tasks.task15 import *
from tasks.task25 import *
from tasks.task33 import *
from tasks.task41 import *
from tasks.task45 import *
from tasks.task46 import *

print("ЗАДАНИЕ1")
task1()
print()

print("ЗАДАНИЕ7")
task7("Исходная строка")
print()

print("ЗАДАНИЕ15")
task15([1, 3, 5, 7, 9], 5)
print()

print("ЗАДАНИЕ25")
my_dict = {'key1': 'value1', 'key2': 'value2'}
task25(my_dict, 'key1')
task25(my_dict, 'value1')
task25(my_dict, 'key')
print()

print("ЗАДАНИЕ33")
task33()
print()

print("ЗАДАНИЕ41")
task41("Text Document.txt", "Новая строка")
print()

print("ЗАДАНИЕ45")
task45([1, 2, 3, "apple", "banana", 3.14])
print()

print("ЗАДАНИЕ46")
data = {
    "age": 28,
    "is_active": True,
    "skills": ["Python", "C#", "SQL"],
    "address": {
        "city": "Москва",
        "zip": "101000"
    }
}
task46(data)