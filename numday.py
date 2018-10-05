'''
作者：sky
版本：1.0
作用：计算当前是这一年的第几天
日期：2018/10/05
'''

import math
from datetime import datetime

def main():
    input_data_year = datetime.now().year
    input_data_month =datetime.now().month
    input_data_day =datetime.now().day
    day_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(day_in_month_tup[:input_data_month-1])+input_data_day
    if (input_data_year % 400 == 0) or (input_data_year % 4 == 0) and (input_data_year % 100 !=0):
        if input_data_month > 2:
            days += 1
    print('当前日期为此年的第{}天。'.format(days))


if __name__ == '__main__':
    main()