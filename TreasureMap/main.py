row1 = ["⬜️","⬜️","⬜️"] # really row 0
row2 = ["⬜️","⬜️","⬜️"] # really row 1
row3 = ["⬜️","⬜️","⬜️"] # really row 2
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#example answer would be 23 for the bottom middle

pos1 = int(position[0]) - 1 # -1 to start index at 0
pos2 = int(position[1]) - 1 # -1 to start index at 0
# print("Row: " + str(pos1))
# print("Col: " + str(pos2))
map[pos2][pos1] = " X"
# print(map[pos1][pos2])
selection = map[pos1][pos2]

# print(selection)

print(f"{row1}\n{row2}\n{row3}")