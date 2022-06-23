from PIL import Image
from pathlib import Path

skirtsFoldername = "skirts"

def main():
	folderPath = Path(skirtsFoldername)

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

	eating = [["84@250", "85@400", "86@401", "87@250", "88@250", "87@250", "88@250", "87@250", "0@250"]]

	drinking = [["90@250", "91@150", "92@250", "93@200", "92@250", "93@200", "92@250", "93@200", "91@250", "90@50"]]

	# Hardcoded static indices
	horse = [["107","106","113"]]

	sitting = [["107","117", "113"]]

	standing = [["0","6","12"]]

	# Get all images in skirts folder
	filelist= [file for file in folderPath.glob('**/*') if file.is_file()]

	for file in filelist:
		originalImage = Image.open(Path(file))

		finalImage = Image.new(mode="RGBA",size=(12*16,12000))

		# Save all of the walking sprites row by row
		nextRowNum = saveAllSpriteRows(0, walking, originalImage, finalImage)

		# Save all of the running sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, running, originalImage, finalImage)

		# Save all of the heavy tool sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, heavyTool, originalImage, finalImage)

		# Save all of the heavy tool sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, heavyToolPressed, originalImage, finalImage)

		# Save all of the heavy tool sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, meleeWeapon, originalImage, finalImage)

		# Save all of the heavy tool sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, watering, originalImage, finalImage)

		# Save all of the harvesting sprites row by row
		nextRowNum = saveAllSpriteRows(nextRowNum, harvesting, originalImage, finalImage)

		# Save all of the eating sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, eating, originalImage, finalImage)

		# Save all of the drinking sprites
		nextRowNum = saveAllSpriteRows(nextRowNum, drinking, originalImage, finalImage)

		finalImage = finalImage.crop((0,0,12*16,nextRowNum*32))

		finalImage.save("finalImage.png")

def saveAllSpriteRows(initialRowNum, listName, originalImage, finalImage):
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