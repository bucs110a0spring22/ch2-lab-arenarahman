
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, type(cost_per_class))
print("cost_per_class:", cost_per_class, "Smiling Bubbles")

#Part B
import random
my_favorite_candies = ["milkyways", "gummy bears", "kitkat", "twix", "jolly ranchers"]
random.choice(my_favorite_candies)
result = random.choice(my_favorite_candies)
print(result)