f = open("文件", "r")

f_new = open("文件.bak", "w")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等georgel享受")
        f_new.write(line)
    else:
        f_new.write(line)

f.close()
f_new.close()

