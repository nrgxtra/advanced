def battle_of_numbers(a):
    numbers = [int(x) for x in a.split()]
    positives = []
    negatives = []
    for el in numbers:
        if el >= 0:
            positives.append(el)
        else:
            negatives.append(el)
    print(sum(negatives))
    print(sum(positives))
    if sum(positives) > abs(sum(negatives)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


battle_of_numbers(input())

