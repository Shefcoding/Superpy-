import argparse
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def chart_products(product1, product2, product3, product4, product5):
#Chart up to five products independently. You can use this to compare 1,2,3,4 or 5 products in whichever order. 


    inventory_file=open('inventory.csv', 'r', newline = '')
    inventory_reader = csv.reader(inventory_file, delimiter=',')
    inventory_list = list(inventory_reader) 
    inventory_list = inventory_list[1:]

  #Get largest count of product1 
    largest_count_product1 = 0
    for item in inventory_list[1:]:
        if product1 in item:
            if int(item[1])>largest_count_product1:
                largest_count_product1 = int(item[1])
    inventory_file.close()  

      #Get largest count of product2
    largest_count_product2 = 0
    for item2 in inventory_list[1:]:
        if product2 in item2:
            if int(item2[1])>largest_count_product2:
                largest_count_product2 = int(item2[1])
    inventory_file.close()  

      #Get largest count of product3 
    largest_count_product3= 0
    for item in inventory_list[1:]:
        if product3 in item:
            if int(item[1])>largest_count_product3:
                largest_count_product3 = int(item[1])
    inventory_file.close() 

      #Get largest count of product4 
    largest_count_product4 = 0
    for item in inventory_list[1:]:
        if product4 in item:
            if int(item[1])>largest_count_product4:
                largest_count_product4 = int(item[1])
    inventory_file.close()   

      #Get largest count of product5
    largest_count_product5 = 0
    for item in inventory_list[1:]:
        if product5 in item:
            if int(item[1])>largest_count_product5:
                largest_count_product5 = int(item[1])
 

    inventory_file.close()  

    
    count_product1 = largest_count_product1
    count_product2 = largest_count_product2
    count_product3 = largest_count_product3
    count_product4 = largest_count_product4
    count_product5 = largest_count_product5

    if not product5 and product4:
        labels =[product1, product2, product3, product4]
        count_products=[count_product1, count_product2, count_product3, count_product4]
    elif not product5 and not product4 and product3:
        labels =[product1, product2, product3]
        count_products=[count_product1, count_product2, count_product3]
    elif not product5 and not product4 and not product3 and product2:
        labels =[product1, product2]
        count_products=[count_product1, count_product2]
    elif not product5 and not product4 and not product3 and not product2 and product1:
        labels =[product1]
        count_products=[count_product1]
    else:
        labels =[product1, product2, product3, product4, product5]
        count_products=[count_product1, count_product2, count_product3, count_product4, count_product5]

   
    x= np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, count_products, width, label='Count')

    ax.set_ylabel('Count')
    ax.set_title('Products in inventory')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()

def chart_all():


    # load the data with pd.read_csv
    record = pd.read_csv('inventory.csv')
 
  
    # Get the highest counts of the different products. 
    highest_counts = record.groupby('product_name')['count'].max()
    next = highest_counts.to_dict()
    print(next)
    # Get key(unique) values 
    labels= list(next.keys())


    x= np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, highest_counts, width, label='Count')

    ax.set_ylabel('Count')
    ax.set_title('Products in inventory')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()   