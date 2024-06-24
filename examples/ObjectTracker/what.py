import json
file = open('allFolders.txt', 'w')

coor = [f"X: {int(12)} mm",f"Y: {int(2)} mm",f"Z: {int(1)} mm"]

print(coor, coor[0])

file.write(json.dumps(coor))
file.write("PKEASE")

file.close()