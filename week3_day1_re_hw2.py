# Regex project
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

# Hint: use with open() and readlines()
import re
with open("regex-test.txt") as file:
    data = file.read()
search = re.search(r"(^[A-Z])[\w]*\s[A-Z][\w]* ?[A-Z]?[\w]*$", data)
expression = r"(^[A-Z])[\w]*\s[A-Z][\w]* ?[A-Z]?[\w]*$"
answer = ""
open_file = open ("regex-test.txt")
for line in open_file.readlines():
    if (re.search(expression, line.lstrip("ï»¿"))):
        answer = answer+line.lstrip("ï»¿")
    else: answer = answer + "None\n"
print (answer)
open_file.close()