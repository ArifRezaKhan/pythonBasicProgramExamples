# Taking input for principle, rate and time
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter percent of rate of interest: "))
time = float(input("Enter time in years: "))


# Calculating Simple Interest
def simple_interest():
    si = (principle * rate * time) / 100
    print("The simple interest on principle ", principle, "is", si)


# Calculating Complex Interest
def complex_interest():
    ci = principle * (pow((1 + rate / 100), time))
    print("The complex interest on principle ", principle, "is", ci)


# Driver Code
simple_interest()
complex_interest()
