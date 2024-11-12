def morethan(lst):
    nums = [i for i in lst if i > 13]
    return nums


if __name__ == "__main__":
    user_input = list(range(100))
    print(morethan(user_input))    