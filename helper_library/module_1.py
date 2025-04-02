import struct

def float_to_hex(num, digit_type:str) -> str:
    """
    Преобразует число с плавающей запятой в его представление в памяти компьютера
    и возвращает это представление в шестнадцатеричном виде.
    """
    # Преобразуем float в байты
    bytes_val = struct.pack(digit_type, num)
    print(bytes_val)
    # Преобразуем байты в шестнадцатеричное представление
    hex_val = str(bytes_val.hex())
    ans=''
    for i in range(len(hex_val)):
        ans += hex_val[-2 * (i//2 + 1) + i % 2]
    return ans.upper()