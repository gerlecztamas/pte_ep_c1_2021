python = "pythonban programozok"
print("a python szó 1. karaktere: ",python[0])
print("a python szó utolsó karaktere: ",python[5])
print("a python szó utolsó karaktere: ",python[-1])
print("a python szó utolsó karaktere: ",python[len(python)-1])

print("A python változóm 5ször egymás után: ",python*5)

str2="hallgató"
str3="Hiába a hegynyi anyag, a hallgató gyorsan halad "
print(str2 in str3)
print(python in str3)
print(python not in str3)
print(str3[0:3])
print(python + str2 + str3)
print(python, str2, str3, sep=" alma ")
str4="HALLGATÓ"
print(str4 in str3)
print(str4>str2)
