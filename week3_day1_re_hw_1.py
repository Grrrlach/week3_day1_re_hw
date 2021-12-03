import re

# with open("names.txt") as file:
#     data = file.read()
    
#     names = re.search(r"(^[A-Z]+[\w]*, [A-Z][\w-]+)|(@[\w]*\s)", data)
#     new_list = (names).findall(data)
#     print(new_list)
answer = ""
open_file = open ("names.txt")
lines = []
answer = "===================\nFull Name / Twitter\n===================\n\n"
for line in open_file.readlines():
    # print ("line: ", line)
    if (re.search(r"(^[A-Z]+[\w]*, [A-Z][\w-]+)", line.lstrip("ï»¿"))) and (re.search(r"(@[\w]*$)", line.lstrip("ï»¿"))):
        # answer = answer+line.lstrip("ï»¿")
        lines.append(line)
# print ("your lines are: ", lines)
print ("the answer is: ", answer)
for line in lines:
    prog = re.compile(r"@[\w]*$")
    first_name = line.split(",", 1)[1].lstrip().split("\t", 1)[0]
    last_name = line.split(",", 1)[0].lstrip()
    # print("the line is: ",line)
    twitter = prog.match(line)
    answer = answer + first_name +" " + last_name + " / 'regex101 says this matches a handle'\n"
print(answer)


# # print (answer)
# # print(answer.split(",", 1))
# split_answer = answer.split("\n")
# for line in split_answer:
#     last_name = line.split(",", 1)[0].lstrip()
#     # print (last_name)
#     if line.strip():
#         first_name = line.split(",", 1)[1].lstrip().split("'\'", 1)
#     # print (first_name)
#     # print (first_name)
#     # print (first_name.split(" "))
# open_file.close()