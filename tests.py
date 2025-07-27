from functions.get_files_info import get_files_info
print("Results:")

result1 = get_files_info("calculator", ".")
print(result1)
print("----------------------------------------------")
result2 = get_files_info("calculator", "pkg")
print(result2)
print("----------------------------------------------")
result3 = get_files_info("calculator", "/bin")
print(result3)
print("----------------------------------------------")
result4 = get_files_info("calculator", "../")
print(result4)