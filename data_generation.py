import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta, datetime

# Initialize a Faker generator
fake = Faker()

# Define some constants
NUM_RECORDS = 10000  # for the proof of concept, we'll generate 10,000 records
START_DATE = datetime(2020, 1, 1)  # arbitrary start date
END_DATE = datetime(2023, 10, 1)  # arbitrary end date
FRUIT_TYPES = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'pear']

# Function to randomly generate the delivery date
def random_date_generator(start_date, end_date):
    return start_date + timedelta(
        # Get a random number of days between start_date and end_date
        days=random.randint(0, (end_date - start_date).days)
    )

# Create a DataFrame
data = {
    'id': [i for i in range(1, NUM_RECORDS + 1)],
    'fruit_type': [random.choice(FRUIT_TYPES) for _ in range(NUM_RECORDS)],
    'delivery_date': [random_date_generator(START_DATE, END_DATE) for _ in range(NUM_RECORDS)],
}
df = pd.DataFrame(data)

# You can now export this data to a CSV, or you could integrate with your database or application.
# For simplicity, we will save it to a CSV file.
df.to_csv('synthetic_fruit_data.csv', index=False)
