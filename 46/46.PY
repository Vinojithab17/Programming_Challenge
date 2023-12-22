#to read input from the file input.txt
def read_data_line_by_line(file_path):
    Numbers = []
    try:
        with open(file_path, 'r') as file:
            while True:
                Row = file.readline().strip().split()
                if len(Row)>0: 
                    Numbers += [int(x) for x in Row]
                if not Row:
                    break
            return list(set(Numbers))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file.\n{e}")

#function to check for palindrome
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number
numbers = read_data_line_by_line(input())

palindrome = []
for i in numbers:
    if (is_palindrome((i))): palindrome.append(i)
palindrome.sort()


if(len(palindrome)):
    print(" ".join(map(str,palindrome)))
else: print("None")
