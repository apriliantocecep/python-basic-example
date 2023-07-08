def jumlahkan(*numbers):
    total = 0
    for number in numbers:
        total += number
    return numbers, total


angka, totalkan = jumlahkan(1, 2, 3, 4, 5)
print(f"Total {angka}: {totalkan}")
