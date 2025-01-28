# values = [1, 2, "rahul", 4, 5]
# # List is data type that allows multiple values and can be different data types
# print(values[0]) # 1
# print(values[3]) # 4
# print(values[-1]) # last value of the list
# print(values[1:3]) # 2 rahul
# values.insert(3, "shetty") # [1, 2, 'rahul', 'shetty', 4, 5]
# print(values)
# values.append("End") # [1, 2, 'rahul', 'shetty', 4, 5, 'End']
# print(values)
#
# values[2] = "RAHUL" # updating
#
# del values[0] # deleting 1 value of the list
#
# print(values) # [2, 'RAHUL', 'shetty', 4, 5, 'End']

# # Tuple - Same as List data type but immutable
# val = (1, 2, "rahul", 4.5)
# print(val[1])
# print(val)
# val[2] = "RAHUL"  # NOT UPDATING BECAUSE TypeError: 'tuple' object does not support item assignment


# Dictionary
dic = {"a":2, 4:"bcd", "c":"Hello world"}
print(dic[4])
print(dic["c"])
print(dic)


#
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
dict["gender"] = "Male"

print(dict)
print(dict["lastname"])


