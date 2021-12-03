from typing import List

report = [i for i in open('puzzle_input.txt', 'r').read().strip().split("\n")]

def get_criteria(rows, rating_type: str, bit_position: int) -> str:
    bits_dict = {"0": 0, "1": 0}

    for r in rows:
        bits_dict[r[bit_position]] += 1
    
    if rating_type == "oxygen":
        if bits_dict["0"] > bits_dict["1"]:
            return "0"
        return "1"
    
    if rating_type == "co2":
        if bits_dict["0"] <= bits_dict["1"]:
            return "0"
        return "1"
    
 
def calculate_generator(report: List[str], type: str) -> str:
    for idx in range(len(report[0])):
        bit_criteria = get_criteria(report, type, idx)
        report = [r for r in report if r[idx] == bit_criteria]
        if len(report) == 1:
            return report[0]

# print(int(calculate_generator(report, "oxygen"), 2))
# print(int(calculate_generator(report, "co2"), 2))
print(int(calculate_generator(report, "oxygen"), 2) * int(calculate_generator(report, "co2"), 2))