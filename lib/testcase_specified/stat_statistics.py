# -*- coding: utf-8 -*- 

def stat_statistic(content,cmp_obj1,cmp_obj2):
    """this function will used to calculate the total statistics record times and check if they are correct """
    
    #import 
    content = content
    cmp_obj1 = cmp_obj1
    cmp_obj2 = cmp_obj2
    result_list = []
    if content.count(cmp_obj1) == content.count(cmp_obj2):
        result_list.append('')
    content_list = content.split('\n')
    
    