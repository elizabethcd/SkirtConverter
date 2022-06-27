import json
import argparse
from PIL import Image
from pathlib import Path

skirtsFoldername = "input"
shiftRight = True

# Disgusting game code hacks
featureYOffsetPerFrame = [1, 2, 2, 0, 5, 6, 1, 2, 2, 1,
        0, 2, 0, 1, 1, 0, 2, 2, 3, 3,
        2, 2, 1, 1, 0, 0, 2, 2, 4, 4,
        0, 0, 1, 2, 1, 1, 1, 1, 0, 0,
        1, 1, 1, 0, 0, -2, -1, 1, 1, 0,
        -1, -2, -1, -1, 5, 4, 0, 0, 3, 2,
        -1, 0, 4, 2, 0, 0, 2, 1, 0, -1,
        1, -2, 0, 0, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 1, -1, -1, -1, -1, 1,
        1, 0, 0, 0, 0, 4, 1, 0, 1, 2,
        1, 0, 1, 0, 1, 2, -3, -4, -1, 0,
        0, 2, 1, -4, -1, 0, 0, -3, 0, 0,
        -1, 0, 0, 2, 1, 1]

featureXOffsetPerFrame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, -1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, -1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, -1, -1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 0, -1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, -1, 0, 0,
        0, 0, 0, 0, 0, 0]

def main():
	# Create the parser
	parser = argparse.ArgumentParser()
	# Add an argument
	parser.add_argument('--rightHalf', type=bool, required=False, help="Whether to grab the right side sprites (female farmer base)",default=True)
	# Parse the argument
	args = parser.parse_args()
	shiftRight = args.rightHalf

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

	fishCatching = [["74", "57", "84"],
					["72", "57", "84"],
					["76", "57", "84"]]

	milking = [["54@400", "55@400", "54@400", "55@400"],
			   ["58@400", "59@400", "58@400", "59@400"],
			   ["62@400", "63@400", "62@400", "63@400"]]

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
		print("Processing " + str(file))
		originalImage = Image.open(Path(file))

		pantsAnimations = [[],[],[],[]]
		pantsIdle = [[],[],[],[]]

		finalImage = Image.new(mode="RGBA",size=(4096, 96))

		# Save all of the standing sprites row by row
		nextColNum = saveAllSpriteRows(0, standing, originalImage, finalImage, pantsIdle, "default")

		# Save all of the sitting sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, sitting, originalImage, finalImage, pantsIdle, "IsSitting")

		# Save all of the horseback riding sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, horse, originalImage, finalImage, pantsAnimations, "RidingHorse")

		# Save all of the horseback riding sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, horse, originalImage, finalImage, pantsIdle, "RidingHorse")

		# Save all of the slingshot sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, slingshot, originalImage, finalImage, pantsIdle, "IsUsingSlingshot")

		# Save all of the walking sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, walking, originalImage, finalImage, pantsAnimations, "isWalking")

		# Save all of the running sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, running, originalImage, finalImage, pantsAnimations, "isRunning")

		# Save all of the heavy tool sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, heavyTool, originalImage, finalImage, pantsIdle, "IsUsingHeavyTool")

		# Save all of the heavy tool pressed sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, heavyToolPressed, originalImage, finalImage, pantsIdle, "toolCharge")
		# TODO: Deal with this!!!

		# Save all of the scythe sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, meleeWeapon, originalImage, finalImage, pantsIdle, "IsUsingScythe")

		# Save all of the melee weapon sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, meleeWeapon, originalImage, finalImage, pantsIdle, "IsUsingMeleeWeapon")

		# Save all of the watering sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, watering, originalImage, finalImage, pantsIdle, "IsWatering")

		# Save all of the harvesting sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, harvesting, originalImage, finalImage, pantsIdle, "IsHarvesting")

		# Save all of the casting sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, casting, originalImage, finalImage, pantsIdle, "IsCasting")

		# Save all of the fishing sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, fishing, originalImage, finalImage, pantsIdle, "IsFishing")

		# Save all of the reeling sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, reeling, originalImage, finalImage, pantsIdle, "IsReeling")

		# Save all of the fish catching sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, fishCatching, originalImage, finalImage, pantsIdle, "IsPullingFishOutOfWater")

		# Save all of the milking sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, milking, originalImage, finalImage, pantsIdle, "IsUsingMilkPail")

		# Save all of the shearing sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, shearing, originalImage, finalImage, pantsIdle, "IsUsingShears")

		# Save all of the bathing suit sprites row by row
		nextColNum = saveAllSpriteRows(nextColNum, bathingSuit, originalImage, finalImage, pantsAnimations, "IsInBathingSuit")

		# Save all of the eating sprites
		nextColNum = saveAllSpriteRows(nextColNum, eating, originalImage, finalImage, pantsIdle, "IsEating")

		# Save all of the drinking sprites
		nextColNum = saveAllSpriteRows(nextColNum, drinking, originalImage, finalImage, pantsIdle, "IsDrinking")

		# Save all of the panning sprites
		nextColNum = saveAllSpriteRows(nextColNum, panning, originalImage, finalImage, pantsIdle, "IsUsingPan")

		# Save all of the passing out sprites
		nextColNum = saveAllSpriteRows(nextColNum, passOut, originalImage, finalImage, pantsIdle, "IsPassingOut")

		# Save all of the nausea sprites
		nextColNum = saveAllSpriteRows(nextColNum, nausea, originalImage, finalImage, pantsIdle, "IsSick")

		# Crop final image to the used portion
		finalImage = finalImage.crop((0,0,nextColNum*16,3*32))

		# Make folder for this pants
		thisPantsFolder = outputFolder.joinpath(file.stem)
		thisPantsFolder.mkdir(exist_ok=True)

		# Save final image to output folder
		finalImage.save(thisPantsFolder.joinpath("pants.png"))
		pantsData = makePantsModels(pantsIdle, pantsAnimations, file.stem)

		# Save pants json to output folder
		
		with thisPantsFolder.joinpath("pants.json").open("w") as write_file:
			json.dump(pantsData, write_file, indent=4)

def addFrameInfo(pantsAnimations, direction, frameNum, condition, initialColNum):
	if condition == "default":
		pantsAnimations[direction].append({
			"Frame": frameNum,
			"EndWhenFarmerFrameUpdates": True,
		},)
	elif condition == "toolCharge":
		chargeNum = frameNum - initialColNum
		addFrameInfoToolCharging(pantsAnimations, direction, frameNum, chargeNum)
	elif condition != "":
		pantsAnimations[direction].append({
			"Frame": frameNum,
			"EndWhenFarmerFrameUpdates": True,
			"Conditions": [
				{
				"Name": condition,
				"Value": True
				}
			]
		},)

def addFrameInfoToolCharging(pantsAnimations, direction, frameNum, chargeNum):
	if chargeNum == 1:
		pantsAnimations[direction].append({
				"Frame": frameNum,
				"EndWhenFarmerFrameUpdates": True,
				"Conditions": [
					{
					"Name": "ToolChargeLevel",
					"Operator": "EqualTo",
					"Value": 1
					}
				]
			},)
	elif chargeNum == 2:
		pantsAnimations[direction].append({
				"Frame": frameNum,
				"EndWhenFarmerFrameUpdates": True,
				"Conditions": [
					{
					"Name": "ToolChargeLevel",
					"Operator": "GreaterThan",
					"Value": 1
					}
				]
			},)

def saveAllSpriteRows(initialColNum, listName, originalImage, finalImage, pantsAnimations, condition):
	rowNum = 0
	for direction in listName:
		colNum = initialColNum
		for frame in direction:
			# Add the frames in this direction to the spritesheet
			frameNum = int(frame.split("@")[0])
			xLoc = frameNum % 6
			yLoc = frameNum // 6
			# Swap to right half if needed
			if shiftRight:
				xLoc = xLoc + 6
			frameImage = originalImage.crop((xLoc*16, yLoc*32, (xLoc+1)*16, (yLoc+1)*32))
			finalImage.paste(frameImage,(colNum*16-featureXOffsetPerFrame[frameNum],rowNum*32-featureYOffsetPerFrame[frameNum]))

			# Add the frames in this direction to the animations list
			addFrameInfo(pantsAnimations, rowNum, colNum, condition, initialColNum)
			# Add left pants as well if we're adding right pants
			if rowNum == 1:
				addFrameInfo(pantsAnimations, 3, colNum, condition, initialColNum)

			# Increment the column number
			colNum = colNum + 1
		rowNum = rowNum + 1
	return colNum

def makePantsModels(pantsIdle, pantsAnimations, pantsName):
	pantsData = {}
	pantsData["Name"] = pantsName

	frontPants = {}
	frontPants["StartingPosition"] = {"X": 0, "Y": 0}
	frontPants["BodyPosition"] = {"X": 0, "Y": 0}
	frontPants["PantsSize"] = {"Width": 16, "Length": 32}
	frontPants["HideWhileSwimming"] = True
	frontPants["HideWhileWearingBathingSuit"] = True
	frontPants["DisableGrayscale"] = True
	frontPants["IdleAnimation"] = pantsIdle[0]
	frontPants["MovementAnimation"] = pantsAnimations[0]
	pantsData["FrontPants"] = frontPants

	rightPants = {}
	rightPants["StartingPosition"] = {"X": 0, "Y": 32}
	rightPants["BodyPosition"] = {"X": 0, "Y": 1}
	rightPants["PantsSize"] = {"Width": 16, "Length": 32}
	rightPants["HideWhileSwimming"] = True
	rightPants["HideWhileWearingBathingSuit"] = True
	rightPants["DisableGrayscale"] = True
	rightPants["IdleAnimation"] = pantsIdle[1]
	rightPants["MovementAnimation"] = pantsAnimations[1]
	pantsData["RightPants"] = rightPants

	backPants = {}
	backPants["StartingPosition"] = {"X": 0, "Y": 64}
	backPants["BodyPosition"] = {"X": 0, "Y": 0}
	backPants["PantsSize"] = {"Width": 16, "Length": 32}
	backPants["HideWhileSwimming"] = True
	backPants["HideWhileWearingBathingSuit"] = True
	backPants["DisableGrayscale"] = True
	backPants["IdleAnimation"] = pantsIdle[2]
	backPants["MovementAnimation"] = pantsAnimations[2]
	pantsData["BackPants"] = backPants

	leftPants = {}
	leftPants["StartingPosition"] = {"X": 0, "Y": 32}
	leftPants["BodyPosition"] = {"X": 0, "Y": 0}
	leftPants["PantsSize"] = {"Width": 16, "Length": 32}
	leftPants["Flipped"] = True
	leftPants["HideWhileSwimming"] = True
	leftPants["HideWhileWearingBathingSuit"] = True
	leftPants["DisableGrayscale"] = True
	leftPants["IdleAnimation"] = pantsIdle[3]
	leftPants["MovementAnimation"] = pantsAnimations[3]
	pantsData["LeftPants"] = leftPants

	return pantsData

# Call the main function
main()