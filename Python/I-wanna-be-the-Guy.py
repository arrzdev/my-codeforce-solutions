max_level = int(input())
X_levels = input()
Y_levels = input()

for level in range(1, max_level+1):
    if str(level) in X_levels or str(level) in Y_levels:

        if level == max_level:
            print("I become the guy.")
    else:
        print("Oh, my keyboard!")
        break
