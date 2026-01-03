def compute_simple_interest(amount, interest_rate, years):
    result = (amount * interest_rate * years) / 100
    return result

principal_amount = float(input("Enter principal amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time_period = float(input("Enter time in years: "))

print("Simple Interest =", compute_simple_interest(principal_amount, rate_of_interest, time_period))
