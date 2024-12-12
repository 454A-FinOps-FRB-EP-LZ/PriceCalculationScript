def main():
    print("Select calculation mode:")
    print("1. Non-Dynamic Full Pricing")
    print("2. Dynamic FinOps Pricing")

    model = input("Enter 1 or 2: ").strip()

    if model == "1":
        # Non-dynamic pricing formula:
        # #instances * instance_hourly_pricing * 24 hours * 7 days) = weekly * 4 = monthly * 12 = yearly

        instances = float(input("Enter the number of instances: "))
        hourly_pricing = float(input("Enter the instance hourly pricing: "))

        weekly_cost = instances * hourly_pricing * 24 * 7
        monthly_cost = weekly_cost * 4
        yearly_cost = monthly_cost * 12

        print("\n--- Non-Dynamic Full Pricing Results ---")
        print(f"Weekly cost:  ${weekly_cost:,.2f}")
        print(f"Monthly cost: ${monthly_cost:,.2f}")
        print(f"Yearly cost:  ${yearly_cost:,.2f}")

    elif model == "2":
        # Dynamic FinOps Formula:
        # For full capacity:
        # (#instances * instance_hourly_pricing * #hours * #days) = full capacity portion of weekly cost
        # 
        # For less capacity:
        # (#instances * instance_hourly_pricing * #hours * #days) = reduced capacity portion of weekly cost
        #
        # weekly = full capacity + less capacity * 4 = monthly * 12 = yearly

        print("For FULL capacity:")
        full_instances = float(input("Enter the number of instances (full capacity): "))
        full_hourly_pricing = float(input("Enter the instance hourly pricing (full capacity): "))
        full_hours = float(input("Enter the number of hours per week at full capacity: "))
        # full_days = float(input("Enter the number of days per week at full capacity: "))

        full_capacity_weekly = full_instances * full_hourly_pricing * full_hours #* full_days

        print("\nFor REDUCED capacity:")
        less_instances = float(input("Enter the number of instances (reduced capacity): "))
        less_hourly_pricing = float(input("Enter the instance hourly pricing (reduced capacity): "))
        less_hours = float(input("Enter the number of hours per week at reduced capacity: "))
        # less_days = float(input("Enter the number of days per week at reduced capacity: "))

        less_capacity_weekly = less_instances * less_hourly_pricing * less_hours #* less_days

        total_weekly = full_capacity_weekly + less_capacity_weekly
        total_monthly = total_weekly * 4
        total_yearly = total_monthly * 12

        print("\n--- Dynamic FinOps Autoscaling Pricing Results ---")
        print(f"Weekly cost:  ${total_weekly:,.2f}")
        print(f"Monthly cost: ${total_monthly:,.2f}")
        print(f"Yearly cost:  ${total_yearly:,.2f}")

    else:
        print("Invalid selection. Please run the program again and choose 1 or 2.")

if __name__ == "__main__":
    main()
