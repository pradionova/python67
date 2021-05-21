math = 0
physics = 0
russian = 0
f = open('C:/Users/Polina/Downloads/dataset_3363_4.txt', 'r')
file_content = f.read()
file_content_lines = file_content.split('\n')
for line in file_content_lines:
    line_split = line.split(';')
    average = (int(line_split[1]) + int(line_split[2]) + int(line_split[3])) / 3
    math += int(line_split[1])
    physics += int(line_split[2])
    russian += int(line_split[3])
    print(average)
math_average = math / len(file_content_lines)
physics_average = physics / len(file_content_lines)
russian_average = russian / len(file_content_lines)
print(math_average, physics_average, russian_average)