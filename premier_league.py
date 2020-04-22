import matplotlib.pyplot as plt

team = 'Arsenal'

with open("C:/Users/Lidija/Desktop/Gregor/python_course/PyCharm/session_6.1_6.2/season-1819_csv.csv") as infile:
    data = infile.read()

list_of_lines = data.split("\n")


home_goals = []

for row in range(len(list_of_lines) -1):
    if list_of_lines[row].split(",")[3] == team:
        home_goals.append(list_of_lines[row].split(",")[5])

goals_ints = [int(y) for y in home_goals]
index_strs = [str(x) for x in range(1, len(home_goals) +1)]

plt.bar(index_strs, goals_ints, color="r")
plt.suptitle("Goals Away: {} 2018".format(team))
plt.xlabel("Game #")
plt.ylabel("Goals scored")
plt.show()

#pyformat.info

"""plt.plot(index_strs, goals_ints, 'ro')
plt.axis([-1, len(index_strs), 0, max(goals_ints) + 1])
plt.show()"""