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

#function to get the prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#to get the largest prime sum
def largest_prime_sum_indices(nums):
    largest_prime = -1
    indices = None
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            current_sum = nums[i] + nums[j]
            if is_prime(current_sum) and current_sum > largest_prime:
                largest_prime = current_sum
                indices = (i, j)
    
    return indices


input_array = read_file(input())
result_indices = largest_prime_sum_indices(input_array)
if result_indices:
    print(result_indices[0], result_indices[1])
    print(input_array[result_indices[0]]+ input_array[result_indices[1]])
else:
    print("None")
