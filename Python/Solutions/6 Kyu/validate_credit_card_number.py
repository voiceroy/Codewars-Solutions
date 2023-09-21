def validate(n: int) -> bool:
    str_num = str(n)

    if len(str_num) % 2 == 0:
        nums = [
            int(str_num[i]) * 2 if i % 2 == 0 else int(str_num[i])
            for i in range(len(str_num))
        ]
    elif len(str_num) % 2 != 0:
        nums = [
            int(str_num[i]) * 2 if i % 2 != 0 else int(str_num[i])
            for i in range(0, len(str_num))
        ]

    for i in range(len(nums)):
        if nums[i] > 9:
            nums[i] -= 9

    num = sum(nums)

    return num % 10 == 0
