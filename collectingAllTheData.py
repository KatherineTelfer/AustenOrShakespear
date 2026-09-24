#collating data

    # 1. import all of the data in a subfolder (e.g. for files in folder)
    # 2. add them to new csv with information on who wrote ite
    # 3. close the csv
    # 4. return output so that you know it works


# Source - https://stackoverflow.com/a/10378012
# Posted by anselm, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-23, License - CC BY-SA 4.0

import os

directory = os.fsencode("trainingData")
shakespeares = {"JuliusCaesar.txt", "Macbeth.txt", "RomeoAndJuliet.txt"}
trainingData = []


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    #print(filename)

    #figure out how to copy all of the data
    with open("trainingData/" + filename, 'r') as file:
        copiedData = file.read().rstrip('\n')
        print(copiedData[0])

        if filename in shakespeares:
            print("shakespeare")
            tempTrainingData = ("0", copiedData)
        else:
            print("austen")
            tempTrainingData = ("1", copiedData)

        trainingData.append(tempTrainingData)
        #print(trainingData[0][1])