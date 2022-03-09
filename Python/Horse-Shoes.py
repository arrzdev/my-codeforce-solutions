shoes_indexes = input()

seen = []
change = 0

for shoe_index in shoes_indexes.split():
    if shoe_index in seen:
        change += 1
    else:
        seen.append(shoe_index)

print(change)        