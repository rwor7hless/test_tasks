# Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000

def sum_even_odd():
    even_sum = 0
    odd_sum = 0
    for i in range(100, 1001):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum
    
print(sum_even_odd())