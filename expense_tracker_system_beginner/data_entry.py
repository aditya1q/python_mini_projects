import pandas as pd
import csv
from datetime import datetime


set_date = input('Enter the date: ')
set_amount = int(input('Enter amount: '))
set_category = input('Enter the category: ')
set_description = input('Enter description: ')


class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']

    @classmethod  # because we don't want instance variable in this funciton
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print('Entry added successfullly')


CSV.initialize_csv()
CSV.add_entry(set_date, set_amount, set_category, set_description)
