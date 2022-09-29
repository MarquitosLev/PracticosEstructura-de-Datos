N1 = "(0345) 154123456" 
N2 = "+5493454123456" 
N3 = "3454123456" 
N4 = "+54011123456" 
N5 = "34564123456" 

NValidos = ("(0345) 154", "+5493454", "3454")

Aux = N1.startswith(NValidos, 0, len(N1))
print (Aux)

Aux = N2.startswith(NValidos, 0, len(N2))
print (Aux)

Aux = N3.startswith(NValidos, 0, len(N3))
print (Aux)

Aux = N4.startswith(NValidos, 0, len(N4))
print (Aux)

Aux = N5.startswith(NValidos, 0, len(N5))
print (Aux)
