# Opening the input file
fileOpening = open("./input4.txt", "r")
fileElements = fileOpening.readlines()

# print(fileElements)     # ['13\n', 'ABCD will departure for Mymensingh at 00:30\n', 'DhumketuExpress will departure for Chittagong at 02:30\n', 'SubornoExpress will departure for Chittagong at 14:30\n', 'ABC will departure for Dhaka at 17:30\n', 'ShonarBangla will departure for Dhaka at 12:30\n', 'SubornoExpress will departure for Rajshahi at 14:30\n', 'ABCD will departure for Chittagong at 01:00\n', 'SubornoExpress will departure for Dhaka at 11:30\n', 'ABC will departure for Barisal at 03:00\n', 'PadmaExpress will departure for Chittagong at 20:30\n', 'ABC will departure for Khulna at 03:00\n', 'ABCE will departure for Sylhet at 23:05\n', 'PadmaExpress will departure for Dhaka at 19:30']

N = int(fileElements[0])

trains = fileElements[1::]

# adding the line break to the last element of trains list
trains[-1] = trains[-1] + "\n"

# print(trains)

# print("before sorting", trains)

# using Bubble Sort.
for i in range(N):
    for j in range(N-1):
        trainName1 = trains[j].split(" ")[0]
        trainName2 = trains[j+1].split(" ")[0]
        if trainName1 == trainName2:
            if trains[j].split(" ")[-1] < trains[j+1].split(" ")[-1]:
                temp = trains[j]
                trains[j] = trains[j+1]
                trains[j+1] = temp
        elif trainName1 > trainName2:
            temp = trains[j]
            trains[j] = trains[j+1]
            trains[j+1] = temp

# print("after sorting", trains)

# Generating the Output file.
outputFileCreating = open("output4.txt", "a")
for i in trains:
    outputFileCreating.writelines(i)

outputFileCreating.close()
