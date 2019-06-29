reciept = []
item = ""
while item != "done":
	item = input ("item name or enter done when finished: ") 
	if item =="done":
		break
	price= float(input ("enter price: "))
	quantity = int(input("enter quantity:"))
	items = { 
	"item:" :item,
	"price" : price,
	"quantity" : quantity,
	}

	reciept.append(items)


	for items in reciept:
		print (items)
