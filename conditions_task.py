print ("1. + ")
print ("2. - ")
print ("3. * ")
print ("4. / ")
operation = int(input ("choose the operation 1, 2, 3, 4 : "))
if (operation >= 1 and operation <=4) :
	print ("choose two numbers: ")
	no1 = int(input())
	no2 = int(input())
	if operation == 1:
		result = no1 + no2
		print ("result = " +str(result) )
	elif operation == 2 :
		 result = no1 - no2
		 print ("result = " +str(result) )
	elif operation == 3 :
		 result = no1 * no2
		 print ("result = " +str(result) )
	elif operation == 4 :
		 result = no1 / no2
		 print ("result = " +str(result) )
else :
	print ("the numbers were invalid")



