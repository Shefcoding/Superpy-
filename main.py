# Imports
import argparse
import csv

from datetime import date
from pathlib import Path
import os
from datetime import timedelta, datetime
from rich.console import Console
from rich.table import Table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Inventory import report_inventory, inventory_to_json
from Buy import buy_product
from Sell import sell_product
from Revenue import report_revenue, report_profit
from chart import chart_products, chart_all
from Parser import parser_all


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

   
def main():
    parser_all()
   
 
if __name__ == "__main__":
    main()
    

        
        
   




