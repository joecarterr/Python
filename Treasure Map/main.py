row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
position = input("Where would you like to put the treasure?: ")
positions = position.split(" ")

horizontal = int(positions[0])
verticle = int(positions[1])

selected_row = map[verticle - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
