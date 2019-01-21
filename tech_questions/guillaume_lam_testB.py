# function return a -1 if num1 is bigger,
# 0 if both are equal,
# 1 if num2 is bigger,
# and finally a 2 if one stirng is not a number
def string_num_cmp(str_num1: str, str_num2: str)-> int:
    try:
        num1 = float(str_num1)
        num2 = float(str_num2)

        if num1 > num2:
            return -1
        elif num1 < num2:
            return 1
        else:
            return 0
    except (ValueError, TypeError):
        return 2
