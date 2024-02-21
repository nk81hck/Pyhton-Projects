import os 

def isBinod(filename):
    with open(filename, "r") as f:
        filecount = f.read()
    # Detect all forms of Binod like BInod.
    if "binod" in filecount.lower():
        return(True)
    else:
        return(False)
if __name__ == "__main__":
    # Listing the contents of this folder.
    dir_contents = os.listdir()
    
    nBinod = 0
    # For each text file, run isBinod for them
    for item in dir_contents:
        if item .endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)      #A flag in Python acts as a signal to the program to determine whether or not the program as a whole or a specific section of the program should run. In other words, you can set the flag to True and the program will run continuously until any type of event makes it False.
            if(flag):
                print(f"!!!! Binod found in {item}*****")
                nBinod = +1
            else:
                print(f"the Binod is not found in {item}")
    print("@@@ Binod Detector summary****")
    print(f"{nBinod} files found with Binod hidden into them")

    