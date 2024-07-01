immutable_var = (1, 2, 3, 4, 5, True)
print(immutable_var)
#immutable_var[0] = 2
print(immutable_var)
#Выдает ошибку, потому что, кортеж не изменяем
mutable_list = [1.2, "RUSSIA", 3]
print(mutable_list)
mutable_list[1] = "USA"
print(mutable_list)
