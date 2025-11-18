monitorCost = int(input("Enter the monitor cost: "))
systemCost = int(input("Enter the system unit cost: "))
keyboardCost = int(input("Enter the keyboard cost: "))
mouseCost = int(input("Enter the mouse cost: "))

totalCost = monitorCost + systemCost + keyboardCost + mouseCost
print("The cost of three computers is", totalCost*3)
numberOfComputers = int(input("Enter the number of computers: "))
print("The total cost of all computers is", totalCost * numberOfComputers)