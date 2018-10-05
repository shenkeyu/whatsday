'''
作者：sky
版本：1.0
作用：计算当前是这一年的第几天
日期：2018/10/05
'''

import math
from datetime import datetime

def is_leap_year(input_data_year):
    is_leap = False
    if (input_data_year % 400 == 0) or (input_data_year % 4 == 0) and (input_data_year % 100 !=0):
        is_leap = True
    return is_leap


def main():
    input_data_year = datetime.now().year
    input_data_month = datetime.now().month
    input_data_day = datetime.now().day

    days_set = input_data_day
    day_in_month_set1 = {4, 6, 9, 11}
    day_in_month_set2 = {1, 3, 5, 7, 8, 10, 12}
    for i in range(1, input_data_month):
        if i in day_in_month_set1:
            days_set += 30
        elif i in day_in_month_set2:
            days_set += 31
        else:
            days_set += 28
    if is_leap_year(input_data_month):
        days_set += 1


    day_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    day_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(day_in_month_tup[:input_data_month-1])+input_data_day
    if input_data_month > 2 and is_leap_year(input_data_year):
        days += 1
        day_in_month_list[1] = 29
    days_list = sum(day_in_month_list[:input_data_month-1])+input_data_day
    print('当前日期为此年的第{}天。tup方式'.format(days))
    print('当前日期为此年的第{}天。list方式'.format(days_list))
    print('当前日期为此年的第{}天。set方式'.format(days_set))

if __name__ == '__main__':
    main()