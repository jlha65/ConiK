import re

string = "x^2+y^2=1"
if re.match(r'\s*x\s*\^\s*2\s*\+\s*y\s*\^\s*2\s*\=\s*([0-9]+(\.[0-9]+)?\s*)\s*', string):
    print("matched")
else:
    print("nel paps")