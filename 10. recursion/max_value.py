def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    if numbers[0] > max_of_rest:
        return numbers[0]
    else:
        return max_of_rest



if __name__ == "__main__":
    my_list = [3, 7, 2, 9, 1]
    print(find_max(my_list))