you = input("Say something to robot: ")

if you == "":
    robot_brain = "I can't hear you, try again."
elif you == "hello":
    robot_brain = "Hello, I can help you."
else:
    robot_brain = "I fire thank you and you"

print(robot_brain)