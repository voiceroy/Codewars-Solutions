def thirt(n: int) -> int:
    num = n

    while True:
        temp = 0
        pattern = [1, 10, 9, 12, 3, 4]
        pattern_index = 0

        for digit in reversed(str(num)):
            temp += int(digit) * pattern[pattern_index % 6]
            pattern_index += 1

        if temp == num:
            return temp
        else:
            num = temp
