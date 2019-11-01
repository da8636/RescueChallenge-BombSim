def printgrid(city):
	print("\n".join([' '.join(a) for a in city]))

	# for i in range(width):
	# 	for k in range(height):
	# 		if k == height-1:
	# 			print(city[i][k])
	# 		else:
	# 			print(city[i][k]+" ", end = '')
	#
def bombplant(bombwidth, bombheight):
	city[bombwidth][bombheight] = "O"
	print("Bomb planted")
	printgrid(city)


def explode(power, width, height):
	for l in range(power):
		for i in range(width):
			for k in range(height):
				if city[i][k] == "O":
					city[i-(l+1)][k-(l+1)] = "x"
					city[i-(l+1)][k] = "x"
					city[i-(l+1)][k+(l+1)] = "x"

					city[i][k-(l+1)] = "x"
					city[i][k+(l+1)] = "x"

					city[i+(l+1)][k-(l+1)] = "x"
					city[i+(l+1)][k] = "x"
					city[i+(l+1)][k+(l+1)] = "x"
		print("Bomb Exploded")
		printgrid(city)

	print("Rubble...")
	printgrid(city)


# city = []
# for i in range(height):
# 	for k in range(width):
# 		city[i][k] = []

width = 10
height = 10
city = [list("-"*width) for i in range(height)]
#city = [["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-","-"], ["-","-","-","-","-","-","-","-","-","-"]]
printgrid(city)

bombplant(5, 7)

explode(3, 10, 10)
