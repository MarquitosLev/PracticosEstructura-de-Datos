
def comprobar_num(N):
    NValidos = ("(0345) 154", "+5493454", "3454")
    return N.startswith(NValidos, 0, len(N))

N1 = "(0345) 154123456" 
N2 = "+5493454123456" 
N3 = "3454123456" 
N4 = "+54011123456" 
N5 = "34564123456" 

print(comprobar_num(N1))
print(comprobar_num(N2))
print(comprobar_num(N3))
print(comprobar_num(N4))
print(comprobar_num(N5))
