def check_balance (my_string):
    count1 = 0 # count of '['
    count2 = 0 # count of ']'
    for i in my_string:
        if i == '[':
            count1 += 1
        if i == ']':
            count2 += 1
        
    if count1 == count2:
        print('it is balanced')
    else:
        print('it is unbalanced')

check_balance('[[[[][]]]]')