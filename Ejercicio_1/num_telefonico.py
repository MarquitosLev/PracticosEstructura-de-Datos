#N1 = "(0345) 154123456" 
#N2 = "+5493454123456" 
#N3 = "3454123456" 
#N4 = "+54011123456" 
#N5 = "34564123456" 

Num = input("Ingrese su número de teléfono: ")
NValidos = ("(0345) 154", "+5493454", "3454")
Aux = Num.startswith(NValidos, 0, len(Num))
print (Aux)
