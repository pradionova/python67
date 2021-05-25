x = 0
y = 0

commandsCol = int(input())
for i in range(0, commandsCol):
    command = input().lower()
    commandSplit = command.split()
    direction = commandSplit[0]
    distance = int(commandSplit[1])
    if direction == 'север':
        y += distance
    elif direction == 'запад':
        x -= distance
    elif direction == 'юг':
        y -= distance
    elif direction == 'восток':
        x += distance

print(x, y)