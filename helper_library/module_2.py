def decimal_fraction_to_base(number, base, precision=10):
    """
    Преобразует десятичную дробь в другую систему счисления.
    
    :param number: десятичная дробь (float или str)
    :param base: основание системы счисления (2-36)
    :param precision: количество дробных разрядов
    :return: строка с числом в новой системе счисления
    """
    if base < 2 or base > 36:
        raise ValueError("Основание системы должно быть от 2 до 36")
    
    # Разделяем число на целую и дробную части
    if isinstance(number, str):
        number = float(number)
    integer_part = int(number)
    fractional_part = number - integer_part
    
    # Преобразуем целую часть
    if integer_part == 0:
        int_result = '0'
    else:
        int_result = ''
        while integer_part > 0:
            remainder = integer_part % base
            int_result = (str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)) + int_result
            integer_part = integer_part // base
    
    # Преобразуем дробную часть
    frac_result = ''
    for _ in range(precision):
        if fractional_part == 0:
            break
        fractional_part *= base
        digit = int(fractional_part)
        frac_result += str(digit) if digit < 10 else chr(ord('A') + digit - 10)
        fractional_part -= digit
    
    return int_result + ('.' + frac_result if frac_result else '')


def first_task(f_d1, s1, f_d2, s2, sign, end_s):
    f_d1 = str(f_d1).split(".")
    f_d2 = str(f_d2).split(".")
    a1, a2 = 0, 0
    for i in range(len(f_d1[0])):
        curr = f_d1[0][-1 - i]
        if curr in "ABCDEF":
            curr = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}[curr]
        a1 += (s1 ** i) * int(curr)
    for i in range(len(f_d1[1])):
        curr = f_d1[1][i]
        if curr in "ABCDEF":
            curr = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}[curr]
        a1 += (s1 ** (-1 - i) * int(curr))
    for i in range(len(f_d2[0])):
        curr = f_d2[0][-1 - i]
        if curr in "ABCDEF":
            curr = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}[curr]
        a2 += (s2 ** i) * int(curr)
    for i in range(len(f_d2[1])):
        curr = f_d2[1][i]
        if curr in "ABCDEF":
            curr = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}[curr]
        a2 += (s2 ** (-1 - i) * int(curr))
    if sign == "+":
        summ = a1 + a2
    else:
        summ = a1 - a2
    print(summ)
    return decimal_fraction_to_base(summ, end_s)
        