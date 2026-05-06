def find_max(numbers):
    max_val = numbers[0]  # Potential issue here
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

aa = find_max([-5, -10, -2])  # This will return -2, but if the list had positive numbers, it would fail
print(aa)