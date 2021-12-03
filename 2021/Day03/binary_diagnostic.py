diag_input = [i for i in open('puzzle_input.txt', 'r').read().strip().split("\n")]

index = len(diag_input[0])
gamma_rate = []
epsilon_rate = []

oxygen_rating = []
co2_rating = []

def calculate():
    for bit in range(index):
        count_zeroes, count_ones = 0, 0
        for number in diag_input:
            if number[bit] == "0":
                count_zeroes += 1
            else:
                count_ones += 1
        # print(f"Zeroes {count_zeroes} - Ones {count_ones}")
        if count_ones > count_zeroes:
            gamma_rate.append("1")
        else:
            gamma_rate.append("0")

def convert(list):
    res = int("".join(map(str, list)))
    return res

def inverse(lst):
    res = ''.join(("1" if x == "0" else "0" for x in lst))
    return res

def binToDecimal(lst):
    decimal = 0
    for digit in lst:
        decimal = decimal*2 + int(digit)
    return decimal
    

def part_one():
    calculate()
    print(convert(gamma_rate))
    print(inverse(gamma_rate))
    print(binToDecimal(gamma_rate))
    epsilon_rate = inverse(gamma_rate)
    print(binToDecimal(epsilon_rate))

    power_consumption = binToDecimal(gamma_rate) * binToDecimal(epsilon_rate)
    print(f"Power Consumption: {power_consumption}")

# part_one()