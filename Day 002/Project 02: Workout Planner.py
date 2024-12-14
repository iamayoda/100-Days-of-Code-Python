print("Welcome to my Workout Planner!")
total_reps = int(input("How many total reps are you planning to do? "))
rest_percentage = int(input("What percentage of the reps will you take as a rest? (e.g., 10, 20, 30) "))
team_members = int(input("How many team members will join you? "))

# Calculate reps and rest per person
reps_with_rest = total_reps * (1 + rest_percentage / 100)
reps_per_person = round(reps_with_rest / team_members, 2)

print(f"Each person should complete approximately {reps_per_person} reps.")
