lst = [10,20,30,40,50,60,70,80,90,100]
target = 40

def search(lst, target):
    if target in lst:
        return True
    return False

print(search(lst, target))