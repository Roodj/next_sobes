def oddeven(a):
    return "Нечетное число" if a % 2 else "Четное число"

if __name__ == "__main__":
    user_input = int(input("Введите число: "))
    print(oddeven(user_input))    