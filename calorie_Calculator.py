# calcutlate how much your calorie intake was after your daily run
total_calorie_intake = int(input('Whats your total calorie intake?')) # daily calorie intake

calories_burnt_per_km = 60 # average brunt calories per kilometer( based off simple google search)

kilometers_run = int(input('How many km was your run?')) # kilometers run

daily_calorie_intake_after_run = total_calorie_intake - (kilometers_run * calories_burnt_per_km) # straight forward simple math

print('Your daily calorie intake after running is:')
print(daily_calorie_intake_after_run)
