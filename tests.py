from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
print("Results:")

result1 = run_python_file("calculator", "main.py")
print(result1)
print("----------------------------------------------")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(result2)
print("----------------------------------------------")
result3 = run_python_file("calculator", "tests.py")
print(result3)
print("----------------------------------------------")
result4 = run_python_file("calculator", "../main.py")
print(result4)
print("----------------------------------------------")
result5 = run_python_file("calculator", "nonexistent.py")
print(result5)
print("----------------------------------------------")

# result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result1)
# print("----------------------------------------------")
# result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result2)
# print("----------------------------------------------")
# result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result3)
# print("----------------------------------------------")

# result1 = get_file_content("calculator", "main.py")
# print(result1)
# print("----------------------------------------------")
# result2 = get_file_content("calculator", "pkg/calculator.py")
# print(result2)
# print("----------------------------------------------")
# result3 = get_file_content("calculator", "/bin/cat")
# print(result3)
# print("----------------------------------------------")
# result4 = get_file_content("calculator", "pkg/does_not_exist.py")
# print(result4)
# print("----------------------------------------------")

# result1 = get_files_info("calculator", ".")
# print(result1)
# print("----------------------------------------------")
# result2 = get_files_info("calculator", "pkg")
# print(result2)
# print("----------------------------------------------")
# result3 = get_files_info("calculator", "/bin")
# print(result3)
# print("----------------------------------------------")
# result4 = get_files_info("calculator", "../")
# print(result4)