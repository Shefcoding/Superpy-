# Imports
import csv
from itertools import product
import os
from datetime import timedelta, datetime


def sell_product(name, price):
    Product_Is_Expired = 0
    Product_In_Inventory = 0
    Product_doesnt_exist = 0
     
    
    
    if os.path.exists('./inventory.csv'):
        #get current sell date
        with open('date.txt') as f:
            line = f.readline()

        todays_date = datetime.strptime(line, '%Y-%m-%d').date()

        #read inventory file and make a list with read file. Search for chosen product name and highest count. Remove that row from the list
        inventory_file=open('inventory.csv', 'r', newline = '')
        inventory_reader = csv.reader(inventory_file, delimiter=',')
        inventory_list = list(inventory_reader)
        
        #Get largest count of product 
        largest_count = 0
        if inventory_list[1:]:
            for item in inventory_list[1:]:
                if name in item:
                    Product_In_Inventory = 1

                    if int(item[1])>largest_count:
                        largest_count = int(item[1])                      
        else:
            print("No products in inventory list")
            Product_doesnt_exist = 1
            


        if Product_doesnt_exist == 0:
        # use the largest count to remove your sold product from the list
            for item in inventory_list[1:]:
                #convert str datetype to datetime type
                expirationdate= datetime.strptime(item[3], '%Y-%m-%d').date()
                if name in item:           
                    if expirationdate > todays_date:                                                           
                        if (int(item[1]) == largest_count):
                                inventory_list.remove(item);  
                                                          
                    else:
                        print("Product is expired")
                        Product_Is_Expired = 1
                               
    
        inventory_file.close()       
    

        #Write new file with popped row to inventory csv file
        inventory_file = open('inventory.csv', 'w', newline = '')
        writer = csv.writer(inventory_file, delimiter=',')
        writer.writerows(inventory_list)
        inventory_file.close()
    else:
        print("No products in inventory list")   

    if os.path.exists('./sold.csv'):
        if Product_doesnt_exist == 0 and Product_In_Inventory == 1:
                #read csv file first in order to get id       
            csv_file=open('sold.csv', 'r', newline = '')
            csv_reader = csv.reader(csv_file, delimiter=',')
            sold_list = list(csv_reader)
            
            id = int(sold_list[-1][-4])

            csv_file.close() 

            id+=1   
            if Product_Is_Expired == 0:
                with open('sold.csv', 'a', newline = '') as sell_file:
                    
                        fieldnames = ['id','product_name','sell_date', 'sell_price']
                        writer = csv.DictWriter(sell_file, fieldnames=fieldnames)
                        writer.writerow({'id': id, 'product_name': name,'sell_date': todays_date, 'sell_price': price})
                        sell_file.close()       

    else: 
         if Product_doesnt_exist == 0 and Product_In_Inventory == 1:
            #If file doesn't exist create file and start the first item with id 1
            id = 1
            with open('sold.csv', 'w', newline = '') as sell_file:
                fieldnames = ['id','product_name','sell_date', 'sell_price']
                writer = csv.DictWriter(sell_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'id': id, 'product_name': name,'sell_date': todays_date, 'sell_price': price })
                sell_file.close()
            