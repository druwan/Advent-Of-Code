course = [line for line in open('puzzle_input.txt', 'r').read().strip(" ").split("\n")]


def part_one():
    vertical_count = 0
    horizontal_count = 0

    try:
        for index in range(len(course)):
            direction = course[index].split(" ")[0]
            steps = int(course[index].split(" ")[1])

            if direction == 'forward':
                horizontal_count += steps
            if direction == 'down':
                vertical_count += steps
            if direction == 'up':
                vertical_count -= steps
            if direction == "":
                print("Finished")

        print(f"Final horizontal position {horizontal_count} times final depth {vertical_count} = {horizontal_count * vertical_count}")

    except IndexError:
        print(f"Final horizontal position {horizontal_count} times final depth {vertical_count} = {horizontal_count * vertical_count}")


def part_two():
    aim = 0
    horizontal_count = 0
    vertical_count = 0

    try:
        for index in range(len(course)):
            direction = course[index].split(" ")[0]
            steps = int(course[index].split(" ")[1])

            if direction == 'forward':
                horizontal_count += steps
                vertical_count += steps * aim

            if direction == 'down':
                aim += steps
            if direction == 'up':
                aim -= steps
            if direction == "":
                print("Finished")

        print(f"Final horizontal position {horizontal_count} times final depth {vertical_count} = {horizontal_count * vertical_count}")

    except IndexError:
        print(f"Final horizontal position {horizontal_count} times final depth {vertical_count} = {horizontal_count * vertical_count}")


part_two()