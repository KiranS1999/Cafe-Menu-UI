file = open("Mini project\Week 1\hello.txt", "r")
contents = file.read()
print(contents)


file = open("Mini project\Week 1\hello.txt", "r")
lines = file.readlines()
for line in lines:
    line = line.strip()
    print(line)