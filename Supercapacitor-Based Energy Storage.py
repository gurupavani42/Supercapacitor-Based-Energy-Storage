# Supercapacitor-Based-Energy-Storage
# Supercapacitor Energy Storage Simulation

capacity = 100       # Maximum energy (%)
energy = 0           # Current stored energy (%)

while True:
    print("\n--- SUPERCAPACITOR ENERGY STORAGE ---")
    print("1. Charge")
    print("2. Discharge")
    print("3. Check Energy")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if energy < capacity:
            energy += 10

            if energy > capacity:
                energy = capacity

            print("Supercapacitor charging...")
            print("Stored Energy:", energy, "%")
        else:
            print("Supercapacitor is fully charged!")

    elif choice == "2":
        if energy > 0:
            energy -= 10

            if energy < 0:
                energy = 0

            print("Supercapacitor discharging...")
            print("Stored Energy:", energy, "%")
        else:
            print("Supercapacitor is empty!")

    elif choice == "3":
        print("Current Stored Energy:", energy, "%")

    elif choice == "4":
        print("System stopped.")
        break

    else:
        print("Invalid choice!")
