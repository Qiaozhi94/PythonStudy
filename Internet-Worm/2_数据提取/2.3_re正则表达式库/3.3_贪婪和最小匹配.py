import re

match = re.search(r'PY.*N', 'PYANBNCNDN')
m = match.group(0)
print(m)    #Re库默认采用贪婪匹配，即输出匹配最长的子串


match = re.search(r'PY.*?N', 'PYANBNCNDN')
m1 = match.group(0)
print(m1)   #最小匹配

