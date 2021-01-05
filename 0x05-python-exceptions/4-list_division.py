#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Div_list = []
    for i in range(0, list_length):
        try:
            Div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            Div = 0
        except ZeroDivisionError:
            print("division by 0")
            Div = 0
        except IndexError:
            print("out of range")
            Div = 0
        finally:
            Div_list.append(Div)
    return Div_list
