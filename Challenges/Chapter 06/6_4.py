string = "Where now? Who now? When now?"

split_list = string.split("?")

for i in range(0,len(split_list)-1):
    split_list[i] = split_list[i] + "?"

print(split_list[:len(split_list)-1])
