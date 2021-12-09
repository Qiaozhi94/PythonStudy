import re

m = re.search(r'[1-9]\d{5}', 'BIT 100081, TSU 100084')

if m:
     print(m.group(0))
     print(m.re)
type_match = type(m)
print(type_match)
