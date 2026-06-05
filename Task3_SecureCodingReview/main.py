filename = input("Enter Python file name: ")

file = open(filename, "r")
code = file.read()

print("\nSecurity Review Report")

if "eval(" in code:
    print("Warning: eval() found")

if "exec(" in code:
    print("Warning: exec() found")

if "password =" in code:
    print("Warning: Hardcoded password found")

if "SELECT" in code and "+" in code:
    print("Warning: Possible SQL Injection")

print("Review Completed")