# -*- coding: utf-8 -*- 

def stat_statistic(content,cmp_obj1,cmp_obj2):
    """this function will used to calculate the total statistics record times and check if they are correct """
    
    #import 
    content = content.strip('\n')
    cmp_obj1 = cmp_obj1
    cmp_obj2 = cmp_obj2
    count_total = 0        # total operation attempts counts
    count_pass = 0         # passed operation attempts counts
    count_fail = 0         # failed operation attempts counts
    max_time_lists = []    # maximum
    result_list = []       # will return thsi result at last
    
    if content.count(cmp_obj1) == content.count(cmp_obj2):
        result_list.append('threshold success')
    else:
        result_list.append('threshold fail')
    
    content_lists = content.split('\n')
    print(content_lists)
    for list in content_lists:
        list = ('/'.join(list.split(' ')[-2:])).split('/')
        count_total += int(list[0])
        count_pass += int(list[1])
        count_fail += int(list[2])
        max_time_lists.append(list[5])
    print(count_total)
    print(count_pass)
    print(count_fail)
    print(max_time_lists)
    if  count_total == count_pass + count_fail:
        if count_fail > 0:
            if max(max_time_lists) > int(cmp_obj1.strip('[').strip(']')):
                result_list.append('count success')
            else:
                result_list.append('count fail')
        else:
            result_list.append('count success')                
    else:
        result_list.append('count fail')           
    return result_list
        
    
    
    