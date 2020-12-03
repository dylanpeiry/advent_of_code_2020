

def get_valid_passwords(data) -> int:
    valid_passwords = 0
    for i,s in enumerate(data):
        vals = s.split(' ')
        range = vals[0].split('-')
        min = int(range[0])
        max = int(range[1])
        char = vals[1].split(':')[0]
        password = vals[2]

        char_count = password.count(char)
        if char_count >= min and char_count <= max:
            valid_passwords += 1
    return valid_passwords


if __name__ == '__main__':
    file = 'input.txt'

    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line)
    
    valid_passwords = get_valid_passwords(data)
    print(f"There are {valid_passwords} valid passwords!")