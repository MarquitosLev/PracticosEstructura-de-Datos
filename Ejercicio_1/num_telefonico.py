import re

#Ni idea que hice aca kpos
patron = "([\\(\\]0345|345[\\)\\])\s([0-9]{16})" 
print("Patron: ",patron)
print(re.findall(patron, "(0345) 154682374"))