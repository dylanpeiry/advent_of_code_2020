
def find_two_entries_sum_to_2020(expenses) -> int:
    for i, first_exp in enumerate(expenses):
        for j, second_exp in enumerate(expenses):
            if i is not j and first_exp + second_exp == 2020:
                return first_exp * second_exp

def find_three_entries_sum_to_2020(expenses) -> int:
    for i, first_exp in enumerate(expenses):
        for j, second_exp in enumerate(expenses):
            for k, third_exp in enumerate(expenses):
                if i is not j and i is not k and j is not k and first_exp + second_exp + third_exp == 2020:
                    return first_exp * second_exp * third_exp


if __name__ == "__main__":
    path = 'input.txt'
    expenses = []
    with open(path) as f:
        for cnt, expense in enumerate(f):
            expenses.append(int(expense))

    res_2entries = find_two_entries_sum_to_2020(expenses)
    res_3entries = find_three_entries_sum_to_2020(expenses)
    print(f"Result 2 entries : {res_2entries}")
    print(f"Result 3 entries : {res_3entries}")