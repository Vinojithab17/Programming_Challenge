#to read input from the file input.txt
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            while True:
                Row = file.readline().strip().split()
                if len(Row)>0:
                    return [int(x) for x in Row]
                if not Row:
                    break
            return [int(x) for x in Row]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file.\n{e}")


def find_unique_odd_index(numbers):
    Unique_odds = {}  # Dictionary to store the index and value of each unique odd number

    for i, num in enumerate(numbers):
        if num % 2 == 1:
            if numbers.count(num) == 1:
                Unique_odds [num]= i
            else: continue

    if len(Unique_odds)>1:
        keys = Unique_odds.keys()
        return Unique_odds[max(keys)]
    elif len(Unique_odds) ==1:
        first_key = next(iter(Unique_odds))
        first_value = Unique_odds[first_key]
        return first_value

    else: return None


# read the data in the file
num_list = read_file(input())

index = find_unique_odd_index(num_list)

if index is not None:
    print(index)
else:
    print("None")
