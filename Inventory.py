# Imports
import csv
from datetime import timedelta, datetime
from rich.console import Console
from rich.table import Table
import json 


def report_inventory(date, now, yesterday, all):

    try:
        # get current time from txt file
        with open('date.txt') as f:
            line = f.readline()

        #Get yesterdays date by getting current date from txt file and subtracting it with one day.
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        yesterdays_date = todays_date - timedelta(1)
        yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

    # report inventory to one of the three lists -- now, yesterdy or date. These are the options you have when reporting the inventory
        inventory_file=open('inventory.csv', 'r', newline = '')
        inventory_reader = csv.reader(inventory_file, delimiter=',')
        inventory_list = list(inventory_reader) 
        inventory_list = inventory_list[1:]
        nowlist=[]
        yesterdayslist=[]
        datelist=[]

        for row in inventory_list:
        #if argument now is used append the rows of today to the now list
            if now == 'now':
                if row[-1] == line:
                    nowlist.append(row)
        #if argument yesterday is used append the rows of today to the yesterday list
            elif yesterday == 'yesterday':
                if row[-1] == yesterdays_date:
                    yesterdayslist.append(row)
            #if the date argument  is used append the rows of today to the date list       
            elif date == row[-1]:
                datelist.append(row)
        
        print(datelist)
    # create a table and use the following headers; Product_name || Count || Buy_price || Expiration_date || Buy_date
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")   
        table.add_column("Product_name", style="dim", width=12)
        table.add_column("Product_id")
        table.add_column("Buy_price", justify="right")
        table.add_column("Expiration_date", justify="right")
        table.add_column("Buy_date", justify="right")

        if now == 'now':
            for row in nowlist:
                table.add_row(*row)
        elif yesterday == 'yesterday':
            for row in yesterdayslist:
                table.add_row(*row)
        elif all =='all':
            for row in inventory_list:
                table.add_row(*row)
        else:
            for row in datelist:
                table.add_row(*row)
                
        return console.print(table)
    except: print('No products in inventory, buy a product first!')

def inventory_to_json():

    try: 
        jsonArray = []
        
        #read csv file
        with open('inventory.csv', encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                jsonArray.append(row)
    
        #convert python jsonArray to JSON String and write to file
        with open('inventoryExport.json', 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)
    except: print('No products in inventory, buy a product first!')
