#to read input from the file input.txt
def read_data_line_by_line(file_path):
    Matrix = []
    try:
        with open(file_path, 'r') as file:
            while True:
                Row = file.readline().strip().split()
                if len(Row)>0:  # An empty string indicates the end of the file
                    Matrix.append([int(x) for x in Row])
                if not Row:
                    break
            return Matrix
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file.\n{e}")
    
#function to get the prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


#function to get the second largest number
def find_second_largest_number(arr):
    largest = second_largest = float('-inf') #negative infinity
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num;
        elif num > second_largest:
            second_largest = num

    return second_largest;

#to store the prime numbers Matrix
matrix = []
inputmatrix = read_data_line_by_line(input())
for i in range(len(inputmatrix)):
    matrix.append([x for x in inputmatrix[i] if is_prime(x)])

#to store the 2nd largest prime number of each row
second_largetNumer_from_each_row = []

#to get the second largest number from each row
for i in matrix:
    second_largetNumer_from_each_row.append(find_second_largest_number(i))

# will print the smallest prime number
print(min(second_largetNumer_from_each_row))
