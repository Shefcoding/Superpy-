import argparse
from Inventory import report_inventory, inventory_to_json
from Buy import buy_product
from Sell import sell_product
from Revenue import report_revenue, report_profit
from chart import chart_products, chart_all
import os
from datetime import timedelta, datetime

def advance_time(time):

    if os.path.exists('./date.txt'):
        # if date file already exists, read the date from file and advance the time 
        with open('date.txt') as f:
            line = f.readline()
    
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        result = todays_date + timedelta(time) 
        result = result.strftime('%Y-%m-%d')
        print(f'The time is advanced from {todays_date} to {result} ')
    else:
        #if file doesn't exist use todays date to advance the time
        result = datetime.today() + timedelta(time) 
        result = result.strftime('%Y-%m-%d')
        print(f'The time is advanced from {datetime.today()} to {result} ')


    datetime_file = open('date.txt', 'w')
    datetime_file.write(result)
    datetime_file.close()          

def parser_all():
      # Create the parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')


    # parser for "buy" command
    parser_buy = subparsers.add_parser('buy_product')
    parser_buy.add_argument('--product_name',  type=str.lower, help = 'Enter the name of the product you want to buy')
    parser_buy.add_argument('--buy_price', type=str, help = 'Enter the price of the product you want to buy')
    parser_buy.add_argument('--expiration_date', type=str, help = 'Enter the expiration date of the product you want to buy')
    parser_buy.set_defaults(func=buy_product)

    #parser for "sell" command
    parser_sell = subparsers.add_parser('sell_product')
    parser_sell.add_argument('--product_name',  type=str.lower, help = 'Enter the name of the product you want to sell')
    parser_sell.add_argument('--sell_price', type=str, help = 'Enter the price of the product you want to sell')
    parser_sell.set_defaults(func=sell_product)

    # parser for "report inventory" command
    parser_buy = subparsers.add_parser('report_inventory', help= 'Report your inventory on any given timeframe. Use the available commands')
    parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the inventory')
    parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the inventory today')
    parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the inventory yesterday')
    parser_buy.add_argument('--all', action='store_const', const='all', help = 'Report the whole history of the inventory')
    parser_buy.set_defaults(func=report_inventory)

    # parser for "report revenue" command
    parser_buy = subparsers.add_parser('report_revenue', help = 'Report revenue on any given timeframe.  Use the --now, --yesterday or --date commands')
    parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the revenue')
    parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the revenue today')
    parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the revenue yesterday')
    parser_buy.set_defaults(func=report_revenue)

    # parser for "report profit" command
    parser_buy = subparsers.add_parser('report_profit', help = 'Report profit on any given timeframe.  Use the --now, --yesterday or --date commands')
    parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the profit')
    parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the profit today')
    parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the profit yesterday')
    parser_buy.set_defaults(func=report_profit)
        


    #parser for "chart product" command
    parser_sell = subparsers.add_parser('chart_products', help='Chart up to five products. Handy for comparing products individually')
    parser_sell.add_argument('--product_name1',  type=str.lower, help= 'Enter the first product you want to chart')
    parser_sell.add_argument('--product_name2',  type=str.lower, help= 'Enter the second product you want to chart')
    parser_sell.add_argument('--product_name3',  type=str.lower, help= 'Enter the third product you want to chart')
    parser_sell.add_argument('--product_name4',  type=str.lower, help= 'Enter the fourth product you want to chart')
    parser_sell.add_argument('--product_name5',  type=str.lower, help= 'Enter the fifth product you want to chart')
    parser_sell.set_defaults(func=chart_products)

    #parser for "chart all" command
    parser_sell = subparsers.add_parser('chart_all', help = "All the products in your inventory will get charted")
    parser_sell.set_defaults(func=chart_all)

    #parser for "inventory to json" command
    parser_sell = subparsers.add_parser('inventory_to_json', help = "Convert your inventory file to json format")
    parser_sell.set_defaults(func=inventory_to_json)

    #parser for "advance time" command
    parser_sell = subparsers.add_parser('advance_time', help = "Advance time in your text file")
    parser_sell.add_argument('--time',  type=int, help = "Fill in how many days you would like to advance time. 1= one day, 2 = two days etc")
    parser_sell.set_defaults(func=advance_time)

    args = parser.parse_args()
    
    if args.command == "buy_product":
            buy_product( args.product_name, args.buy_price, args.expiration_date)
    elif args.command == "sell_product":
            sell_product(args.product_name, args.sell_price)
    elif args.command == "report_inventory":
            report_inventory(args.date, args.now, args.yesterday, args.all)
    elif args.command == "report_revenue":
            report_revenue(args.date, args.now, args.yesterday)
    elif args.command == "report_profit":
            report_profit(args.date, args.now, args.yesterday)
    elif args.command == "advance_time":
            advance_time(args.time)
    elif args.command == "chart_products":
            chart_products(args.product_name1, args.product_name2, args.product_name3, args.product_name4, args.product_name5)
    elif args.command == "chart_all":
            chart_all()
    elif args.command == "inventory_to_json":
            inventory_to_json()