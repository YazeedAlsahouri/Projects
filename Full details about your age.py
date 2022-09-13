age=int(input("Enter your age: ").strip())
monts=age*12
weeks=monts*4
days=age*365 
hours=days*24
minutes=hours*60
seconds=minutes*60
print("Your lived for: ")
print(f"{monts} Monts.")
print(f"{weeks} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")