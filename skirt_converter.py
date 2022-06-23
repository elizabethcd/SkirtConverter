from PIL import Image
from pathlib import Path

skirtsFoldername = "input"

def main():
	folderPath = Path(skirtsFoldername)

	# Hardcoded static indices
	standing = [["0"],["6"],["12"]]
	sitting = [["107"],["117"],["113"]]
	horse = [["107"],["106"],["113"]]
	fishing = [["70"],["91"],["44"]]
	reeling = [["66"],["48"],["36"]]
	slingshot = [["42"],["43"],["44"]]

	# Hardcoded animation indices
	walking = [["0@200", "1@200", "0@200", "2@200"],
			   ["6@200", "7@200", "6@200", "8@200"],
			   ["12@200", "13@200", "12@200", "14@200"]]

	running = [["0@90", "1@60", "18@120", "1@60", "0@90", "2@60", "19@120", "2@60"],
			   ["6@90", "21@140", "17@100", "6@90", "20@140", "11@100"],
			   ["12@90", "13@60", "22@120", "13@60", "12@90", "14@60", "23@120", "14@60"]]

	heavyTool = [["66@150", "67@40", "68@40", "69@170", "70@75"],
				 ["48@100", "49@40", "50@40", "51@220", "52@75"],
				 ["36@100", "37@40", "38@40", "63@220", "62@75"]]

	heavyToolPressed =[["66@600", "74@600", "75"],
					   ["48@600", "72@600", "73"],
					   ["36@600", "76@600", "77"]]

	meleeWeapon = [["24@55", "25@45", "26@25", "27@25", "28@25", "29"],
				   ["30@55", "31@45", "32@25", "33@25", "34@25", "35"],
				   ["36@55", "37@45", "38@25", "39@25", "40@25", "41"]]

	watering = [["54@75", "55@100", "25@500"],
				["58@75", "59@100", "45@500"],
				["62@75", "63@100", "46@500"]]

	harvesting = [["54@100", "55@100", "56@100", "57@100"],
				  ["58@100", "59@100", "60@100", "61@10"],
				  ["62@100", "63@100", "64@100", "65@100"]]

	casting = [["66@100", "67@40", "68@40", "69@80", "70@200"],
			   ["48@100", "49@40", "50@40", "51@80", "52@200"],
			   ["76@100", "38@40", "63@40", "62@80", "63@200"]]

	milking = [["54@400", "55@400", "54@400", "55@400"],
			   ["58@400", "59@400", "58@400", "59@400"],
			   ["56@400", "57@400", "56@400", "57@400"]]

	shearing = [["78@400", "79@400", "78@400", "79@400"],
			    ["80@400", "81@400", "80@400", "81@400"],
			    ["82@400", "83@400", "82@400", "83@40"]]

	bathingSuit = [["108@200", "109@200", "108@200", "110@200"],
				   ["114@200", "115@200", "114@200", "116@200"],
				   ["120@200", "121@200", "120@200", "122@200"]]

	eating = [["84@250", "85@400", "86@401", "87@250", "88@250", "87@250", "88@250", "87@250", "0@250"]]
	drinking = [["90@250", "91@150", "92@250", "93@200", "92@250", "93@200", "92@250", "93@200", "91@250", "90@50"]]
	panning = [["123@150", "124@150", "123@150", "125@150", "123@150", "124@150", "123@150", "125@150", "123@150", "124@150", "123@150", "125@150", "123@150", "124@150", "123@500"]]
	passOut = [["16@1000", "0@500", "16@1000", "4@200", "5@6000"]]
	nausea = [["104@350", "105@350", "104@350", "105@350", "104@350", "105@350", "104@350", "105@350"]]

	# Get all images in skirts folder
	filelist = folderPath.glob("*.png")

	# Prepare the output location
	outputFolder = Path("output")
	outputFolder.mkdir(exist_ok=True)
	for file in filelist:
		print(file)
		originalImage = Image.open(Path(file))

		pantsAnimations = []

		finalImage = Image.new(mode="RGBA",size=(12*16,12000))

		# Save all of the standing sprites row by row
		nextRowNum = saveAllSpriteRows(0, standing, originalImage, finalImage, pantsAnimations, "")

		# Save all of the sitting sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, sitting, originalImage, finalImage, pantsAnimations, "IsSitting")

		# Save all of the horseback riding sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, horse, originalImage, finalImage, pantsAnimations, "RidingHorse")

		# Save all of the slingshot sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, slingshot, originalImage, finalImage, pantsAnimations, "IsUsingSlingshot")

		# Save all of the walking sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, walking, originalImage, finalImage, pantsAnimations, "isWalking")

		# Save all of the running sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, running, originalImage, finalImage, pantsAnimations, "isRunning")

		# Save all of the heavy tool sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, heavyTool, originalImage, finalImage, pantsAnimations, "IsUsingHeavyTool")

		# Save all of the heavy tool pressed sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, heavyToolPressed, originalImage, finalImage, pantsAnimations, "")

		# Save all of the scythe sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, meleeWeapon, originalImage, finalImage, pantsAnimations, "IsUsingScythe")

		# Save all of the melee weapon sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, meleeWeapon, originalImage, finalImage, pantsAnimations, "IsUsingMeleeWeapon")

		# Save all of the watering sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, watering, originalImage, finalImage, pantsAnimations, "")

		# Save all of the harvesting sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, harvesting, originalImage, finalImage, pantsAnimations, "IsHarvesting")

		# Save all of the casting sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, casting, originalImage, finalImage, pantsAnimations, "IsCasting")

		# Save all of the fishing sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, fishing, originalImage, finalImage, pantsAnimations, "IsFishing")

		# Save all of the reeling sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, reeling, originalImage, finalImage, pantsAnimations, "IsReeling")

		# Save all of the milking sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, milking, originalImage, finalImage, pantsAnimations, "IsUsingMilkPail")

		# Save all of the shearing sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, shearing, originalImage, finalImage, pantsAnimations, "IsUsingShears")

		# Save all of the bathing suit sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, bathingSuit, originalImage, finalImage, pantsAnimations, "IsInBathingSuit")

		# Save all of the eating sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, eating, originalImage, finalImage, pantsAnimations, "IsEating")

		# Save all of the drinking sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, drinking, originalImage, finalImage, pantsAnimations, "IsDrinking")

		# Save all of the panning sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, panning, originalImage, finalImage, pantsAnimations, "IsUsingPan")

		# Save all of the passing out sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, passOut, originalImage, finalImage, pantsAnimations, "")

		# Save all of the nausea sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, nausea, originalImage, finalImage, pantsAnimations, "")

		finalImage = finalImage.crop((0,0,12*16,nextRowNum*32))

		finalImage.save(outputFolder.joinpath(file.name))

def saveAllSpriteRows(initialRowNum, listName, originalImage, finalImage, pantsAnimations, condition):
	rowNum = initialRowNum

	for direction in listName:
		colNum = 0
		for frame in direction:
			frameNum = int(frame.split("@")[0])
			xLoc = frameNum % 6
			yLoc = frameNum // 6
			# print("x = " + str(xLoc) + " y = " + str(yLoc))
			frameImage = originalImage.crop((xLoc*16, yLoc*32, (xLoc+1)*16, (yLoc+1)*32))
			finalImage.paste(frameImage,(colNum*16,rowNum*32))
			colNum = colNum + 1
		rowNum = rowNum + 1
	return rowNum

# Call the main function
main()