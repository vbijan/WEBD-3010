# input from console
num = input("Enter a number: ")
try:
    for i in range(1,11):
        print(f"{int(num)} x {i} = {int(num)*i}")
except Exception as e:
    print("Integer Expected", e)

print("more codes...")
print("more codes...")
