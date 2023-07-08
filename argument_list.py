def jumlah(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(f"Total {numbers}: {total}")


jumlah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
