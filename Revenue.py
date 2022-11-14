# Imports
import csv
from datetime import timedelta, datetime


def report_revenue(date, now, yesterday):

        # get current time from txt file
        with open('date.txt') as f:
            line = f.readline()

        #Get yesterdays date by getting current date from txt file and subtracting it with one day.
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        yesterdays_date = todays_date - timedelta(1)
        yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

        #read sold file and the third row to get total revenue 
        csv_file=open('sold.csv', 'r', newline = '')
        csv_reader = csv.reader(csv_file, delimiter=',')
        sold_list = list(csv_reader)
        revenue_now = 0.0
        revenue_yesterday = 0.0
        revenue_date = 0.0
        for item in sold_list[1:]:
            if now == 'now':
                if item[2]==line:
                    revenue_now += float(item[3])                    
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     revenue_yesterday += float(item[3])            
            elif date == item[2]:
                 revenue_date += float(item[3])  

        if now == 'now':
            print(f'Total revenue now is : {round(revenue_now,1)}')
        elif yesterday == 'yesterday':
            print(f'Total revenue yesterday is : {round(revenue_yesterday,1)}')
        else:
            print(f'Total revenue on {date} is : {round(revenue_date,1)}')

        csv_file.close()

def report_profit(date, now, yesterday):
        # get current time from txt file
        with open('date.txt') as f:
            line = f.readline()
         #Get yesterdays date by getting current date from txt file and subtracting it with one day.
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        yesterdays_date = todays_date - timedelta(1)
        yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

        #read sold and bought file to get the total profit  

        # Get total revenue from sold file
        sold_file=open('sold.csv', 'r', newline = '')
        sold_reader = csv.reader(sold_file, delimiter=',')
        sold_list = list(sold_reader)
        revenue_now = 0.0
        revenue_yesterday = 0.0
        revenue_date = 0.0

        for item in sold_list[1:]:
            if now == 'now':
                if item[2]==line:
                    revenue_now += float(item[3])
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     revenue_yesterday += float(item[3])            
            elif date == item[2]:
                revenue_date += float(item[3])  

        sold_file.close()
        

        # Get total amount paid from bought file
        bought_file=open('bought.csv', 'r', newline = '')
        bought_reader = csv.reader(bought_file, delimiter=',')
        bought_list = list(bought_reader)
        costs_now = 0.0
        costs_yesterday = 0.0
        costs_date = 0.0

        for item in bought_list[1:]:
            if now == 'now':
                if item[2]==line:
                    costs_now += float(item[3])
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     costs_yesterday += float(item[3])            
            elif date == item[2]:
                costs_date += float(item[3])  

        bought_file.close()

        if now == 'now':
            total_profits_now = revenue_now - costs_now
            if total_profits_now < 0:
                total_profits_now = 0
            print(f'Total profit now is : {round(total_profits_now,1)}')
        elif yesterday == 'yesterday':
            total_profits_yesterday = revenue_yesterday - costs_yesterday
            if total_profits_yesterday < 0:
                total_profits_yesterday = 0
            print(f'Total profit yesterday is : {round(total_profits_yesterday,1)}')
        else:
            total_profits_date = revenue_date - costs_date
            if total_profits_date < 0:
                total_profits_date = 0
            print(f'Total profit on {date} is : {round(total_profits_date,1)}')
