def calculate_net_salary():
    try:
        # Accept basic salary input
        basic_pay = float(input("Enter the Basic Salary: "))

        # Calculate HRA and DA
        hra = 0.20 * basic_pay
        da = 0.10 * basic_pay

        # Calculate Gross Salary (Total Salary)
        gross_salary = basic_pay + hra + da

        # Calculate Tax (5% of total salary)
        tax = 0.05 * gross_salary

        # Calculate Net Salary
        net_salary = gross_salary - tax

        # Display results
        print("\n--- Salary Breakdown ---")
        print(f"Basic Pay:    {basic_pay:,.2f}")
        print(f"HRA (20%):    {hra:,.2f}")
        print(f"DA (10%):     {da:,.2f}")
        print(f"Gross Salary: {gross_salary:,.2f}")
        print(f"Tax (5%):     {tax:,.2f}")
        print("------------------------")
        print(f"Net Salary:   {net_salary:,.2f}")

    except ValueError:
        print("Error: Please enter a valid numerical value for the salary.")

# Run the program
calculate_net_salary()