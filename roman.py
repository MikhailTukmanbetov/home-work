def roman_to_int(s):
    count_num = 0
    numbers = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in numbers:
        count_num = numbers[i] * s.count(numbers[i])
        s.replace(numbers[i], '')
    return count_num

def int_to_roman(num):
    info = ['I', 'X', 'C', 'M']
    weird_number = ''
    i = 0
    num = str(num)
    for j in range(len(num) - 1, -1, -1):
        weird_number += int(num[j]) * info[i]
        i += 1
        num = str(num)
    res = weird_number[::-1]
    res = res.replace('IIIIIIIII', 'IX')
    res = res.replace('IIIII', 'V')
    res = res.replace('IIII', 'IV')
    res = res.replace('XXXXXXXXX', 'XC')
    res = res.replace('XXXXX', 'L')
    res = res.replace('XXXX', 'XL')
    res = res.replace('CCCCCCCCC', 'CM')
    res = res.replace('CCCCC', 'D')
    res = res.replace('CCCC', 'CD')
    return res
