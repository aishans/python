skills= ["python", "c++", "javascript", "juggling" ,"running", "eating"]
cv ={}
name = input ("please enter name")
cv["name"] = name,
age = int(input ("please enter age"))
cv["age"]= age,
experience  = input ("please enter years of experience")
cv["experience"] = experience,
cv["skills"]= []
print ("1." + skills[0] + "2." + skills[1] + "3." + skills[2] + "4." + skills[3], "5." + skills[4] + "6." + skills[5])
skills1 = input ("choose a skill from the list above: ") #skills[0], skills[1], skills[2], skills[3], skills[4], skills[5]) 
skills2 = input ("choose another skill from above: ")#, skills[0], skills[1], skills[2], skills[3], skills[4], skills[5]) 
cv["skill 1"]= skills1
cv["skill 2"] = skills2
skill7= input ("add a skill of your own: ")
skills.append (skill7)
if (age <= 40 and age >= 25):
	if (experience <3):
		print ("you have been accepted, "+ name)
else :
	print ("sorry you were not qualified ")



