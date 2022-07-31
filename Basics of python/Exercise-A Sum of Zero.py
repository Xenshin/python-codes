def check_sum(num_list):
    for i in range(len(num_list)):
        base = num_list[i]
        for j in range(i+1,len(num_list)):
            if (base + num_list[j] == 0):
                return True
    return False

print(check_sum([10, -14, 26, 5, -3, 13, -5]))