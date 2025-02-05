import shutil
#-copyfile
#-copy
#-copy2
str=r"C:\Users\user\Desktop\workSpace"
source=f"{str}/source.txt"
destination=f"{str}/destinationFlie.txt"
shutil.copyfile(source,destination)