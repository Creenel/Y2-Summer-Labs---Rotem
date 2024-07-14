temperatures = []
import random
for i in range(7):
	temperatures.append(random.randint(26,41))
days_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
good_days_count = 0
for i in range(7):
	if temperatures[i] % 2 == 0:
		print(temperatures[i])
		good_days_count+=1
highest_temp = 0
lowest_temp = 99
highest_temp_day = "Sunday"
lowest_temp_day = "Sunday"
for i in range(7):
	if temperatures[i] > highest_temp:
		highest_temp = temperatures[i]
		highest_temp_day = days_of_the_week[i]
	if temperatures[i] < lowest_temp:
		lowest_temp = temperatures[i]
		lowest_temp_day = days_of_the_week[i]
temps_total = 0
for i in range(7):
	temps_total += temperatures[i]
temps_avg = temps_total / 7
above_avg = []
for i in range(7):
	if temperatures[i] > temps_avg:
		above_avg.append(temperatures[i])
for i in range(7):
	print("Day: " + str(days_of_the_week[i]) + " Temp: " + str(temperatures[i]))
print("There are " + str(good_days_count) + " good days for Shelly!")
print("Hottest day: " + highest_temp_day + " Temp: " + str(highest_temp) + " Coldest day: " + lowest_temp_day + " Temp: " + str(lowest_temp))
print("Average temp: " + str(temps_avg))
print("Days hotter than average: " + str(above_avg))