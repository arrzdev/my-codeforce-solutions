number_of_drinks = int(input())
percentage_per_drink = input()

summ = 0

for percentage in percentage_per_drink.split():
    summ += int(percentage)

print(summ/number_of_drinks)