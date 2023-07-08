def say_hello(name):
    return f"Hello {name}"


def total(*numbers):
    jumlah = 0
    for num in numbers:
        jumlah = jumlah + num
    return jumlah