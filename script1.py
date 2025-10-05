

list = [11, 22, 47, 33, 45, 77, 58, 42, 12, 34, 17, 112, 228]
suma = 0
produkt = 1 
for number in list:
    if not number %2:
        suma += number
        produkt *= number
   
    
print (f"suma je {suma}, produkt je {produkt}")
    
