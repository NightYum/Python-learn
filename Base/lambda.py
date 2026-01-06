# bool_list = [map((value.isdigit()), string)]

string = "123asdf"

def check_value(value: str) -> bool:
    return value.isdigit()

def_bool_list = list(map(check_value, string))
print(def_bool_list)


lamda_bool_list = list(map(lambda value: value.isdigit(), string))
print(lamda_bool_list)

lambda_func = lambda value: [i for i in range(0, value)]
print(lambda_func(10))
