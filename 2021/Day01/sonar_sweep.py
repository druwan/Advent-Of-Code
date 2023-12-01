# Part 1
measurements = [int(input) for input in open('puzzle_input.txt', 'r').read().strip().split('\n')]

def part_one():
    count = 0
    for entry in range(len(measurements)):
        if (measurements[entry] > measurements[entry - 1]):
            count += 1
    print(f"The number of times the depth increased: {count}")
        
# Part 2
def part_two():
    full_sum = []
    for entry in range(len(measurements)):
        try:
            full_sum.append(measurements[entry] + measurements[entry + 1] + measurements[entry + 2])
        except IndexError:
            pass

    count_sum = 0
    for index in range(len(full_sum)):
        if (full_sum[index] > full_sum[index-1]):
            count_sum += 1
    print(f"The number of sums are larger than the previous: {count_sum}")
    
part_one()
part_two()


    

    

    

