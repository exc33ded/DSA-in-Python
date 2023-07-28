# Temperature Average

ask = int(input("How many Day's temperature? "))

lst = []

for i in range(1, ask+1):
    temp = float(input(f"Day {i}'s high temp: "))
    lst.append(temp)

avg = sum(lst)/len(lst)

print("Average:", avg)    