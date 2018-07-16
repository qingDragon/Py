import re
s = "2+5+6*-3/5-3/2*5"
res = re.search(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)', s).group()
print(res)
