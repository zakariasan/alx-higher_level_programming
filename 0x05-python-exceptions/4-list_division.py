#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for item in range(0, list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except (TypeError):
            print("wrong type")
            result = 0
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            total.append(result)
    return total
