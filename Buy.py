# Imports
import csv
import os
from datetime import timedelta, datetime


def buy_product(name, price, expiration_date):
    Product_Is_Expired = 0
   
   
    #check if files already exists, if so append a row with new data
        
    if os.path.exists('./bought.csv') and os.path.exists('./inventory.csv') and  os.path.exists('date.txt') :

         #get current buy date from textfile
        with open('date.txt') as f:
            line = f.readline()
        
        compare_date = datetime.today().strftime('%Y-%m-%d')
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        #read bought csv file first in order to get current id
        if expiration_date > compare_date: 
            csv_file=open('bought.csv', 'r', newline = '')
            csv_reader = csv.reader(csv_file, delimiter=',')
            #Get current id from bought file.  
            id = int(list(csv_reader)[-1][-5])
        
            csv_file.close() 
            #increment id 
            id+=1   
            with open('bought.csv', 'a', newline = '') as buy_file:
            
                fieldnames = ['id','product_name','buy_date', 'buy_price', 'expiration_date']
                writer = csv.DictWriter(buy_file, fieldnames=fieldnames)
                writer.writerow({'id': id, 'product_name': name,'buy_date': todays_date, 'buy_price': price, 'expiration_date': expiration_date})
                buy_file.close() 

            print(f'{name} has been bought for {price} on {todays_date}')

        
            
            # keep count of the product in inventory 
            inventory_file=open('inventory.csv', 'r', newline = '')
            inventory_reader = csv.reader(inventory_file, delimiter=',')
            inventory_list = list(inventory_reader)

            count = 1
            for item in inventory_list:
                if name in item:
                    count +=1

                #add product to inventory   
            with open('inventory.csv', 'a', newline = '') as inventory_file:        
                    fieldnames_inventory = ['product_name','Product_id', 'buy_price', 'expiration_date', 'buy_date']
                    writer_inventory = csv.DictWriter(inventory_file, fieldnames=fieldnames_inventory)
                    writer_inventory.writerow({'product_name': name,'Product_id': count,'buy_price': price, 'expiration_date': expiration_date, 'buy_date': todays_date})
                    inventory_file.close()
        else:
            print("Product is expired")

        
    #if file doesnt exist create file with row 
    else:
        #Begin program from here
        #write todays date to file 
        todays_date = datetime.today().strftime('%Y-%m-%d')
        if expiration_date > todays_date: 
            #Write new file with popped row to inventory csv file
            datetime_file = open('date.txt', 'w')
            datetime_file.write(todays_date)
            datetime_file.close() 

            #Start ID and count of product
            id = 1
            count = 1

            #create inventory file
            with open('inventory.csv', 'w', newline = '') as inventory_file:
                fieldnames_inventory = ['product_name','Product_id', 'buy_price', 'expiration_date', 'buy_date']
                writer_inventory = csv.DictWriter(inventory_file, fieldnames=fieldnames_inventory)
                writer_inventory.writeheader()
                writer_inventory.writerow({'product_name': name,'Product_id': count,'buy_price': price, 'expiration_date': expiration_date, 'buy_date': todays_date})
                inventory_file.close()


            #create bought file
            with open('bought.csv', 'w', newline = '') as buy_file:
                fieldnames = ['id','product_name','buy_date', 'buy_price', 'expiration_date']
                writer = csv.DictWriter(buy_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'id': id, 'product_name': name,'buy_date': todays_date, 'buy_price': price, 'expiration_date': expiration_date})
                buy_file.close()

            print(f'{name} has been bought for {price} on {todays_date}')
        else:
            print("Product is expired")
            