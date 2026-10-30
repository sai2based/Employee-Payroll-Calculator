filePath = "C:/Users/asaiy/OneDrive/Desktop/Py/employeeDatabase.csv"
import csv

while True:
    searchedID = None

    
    try:
        searchedID = int(input("Enter an employee ID: "))
    except ValueError:
        print("Employee not found.")  
        continue

    if searchedID is not None:
        found = False
        with_open = True

    with open(filePath, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            try:

                if int(row[2]) == int(searchedID):
                    found = True

                    while True:
                        try:
                            hoursWorked = float(input(f"How many hours has {row[0]} {row[1]} worked? "))

                            if hoursWorked > 80 or hoursWorked < 0:
                                print("Invalid entry.")
                                continue
                        
                            break
                        except ValueError:
                            print("Invalid entry. ")


                    hourlyRate = float(row[3])
                    
                    if hoursWorked <= 40:
                        grossPay = hoursWorked * hourlyRate

                    else:
                        regularPay = 40 * hourlyRate
                        overtimeHours = hoursWorked - 40
                        overtimePay = overtimeHours * (hourlyRate * 1.5)
                        grossPay = regularPay + overtimePay

                    fedTax = 0.12
                    stateTax = 0.0295

                    deductions = (grossPay * fedTax) + (grossPay * stateTax)
                    netPay = grossPay - deductions

                    print(f"\nGross Pay: ${grossPay:.2f}")
                    print(f"Total Taxes Deducted: ${deductions:.2f}")
                    print(f"Take-Home Pay: ${netPay:.2f}")

                    break

            except ValueError:
                pass

    if not found:
        print("Employee not found.")
        continue
    
    run_again = input("\nCalculate next payroll? (y/n): ").strip().lower()

    if run_again != 'y' and run_again != 'yes':
        print("Exiting payroll system. Goodbye!")
        break
        exit()
