from PIL import Image
from pathlib import Path

skirtsFoldername = "skirts"

def main():
	folderPath = Path(skirtsFoldername)

	# Some hardcoded indices
	walking = [["0@200", "1@200", "0@200", "2@200"],
			   ["6@200", "7@200", "6@200", "8@200"],
			   ["12@200", "13@200", "12@200", "14@200"]]

	running = [["0@90", "1@60", "18@120", "1@60", "0@90", "2@60", "19@120", "2@60"],
			   ["6@90", "21@140", "17@100", "6@90", "20@140", "11@100"],
			   ["12@90", "13@60", "22@120", "13@60", "12@90", "14@60", "23@120", "14@6"]]

	harvesting = [["54@100", "55@100", "56@100", "57@100"],
				  ["58@100", "59@100", "60@100", "61@10"],
				  ["62@100", "63@100", "64@100", "65@100"]]

	eating = [["84@250", "85@400", "86@401", "87@250", "88@250", "87@250", "88@250", "87@250", "0@250"]]

	drinking = [["90@250", "91@150", "92@250", "93@200", "92@250", "93@200", "92@250", "93@200", "91@250", "90@50"]]

	# Get all images in skirts folder
	filelist= [file for file in folderPath.glob('**/*') if file.is_file()]

	for file in filelist:
		originalImage = Image.open(Path(file))

		finalImage = Image.new(mode="RGBA",size=(12*16,12000))

		# Save all of the walking sprites row by row
		saveAllSpriteRows(0, walking, originalImage, finalImage)

		# Save all of the running sprites row by row
		saveAllSpriteRows(3, running, originalImage, finalImage)

		# Save all of the harvesting sprites row by row
		saveAllSpriteRows(6, harvesting, originalImage, finalImage)

		finalImage = finalImage.crop((0,0,12*16,20*32))

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

# Call the main function
main()