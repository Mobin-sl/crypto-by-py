import pandas as pd
import os

OUTPUT = "output"

FILE = "output/crypto_prices.xlsx"

#save kardan dar excel
def save_excel(data):

    if not os.path.exists(OUTPUT):
        os.mkdir(OUTPUT)

    df = pd.DataFrame(data)

    df.to_excel(FILE, index=False)

    print("Excel Saved Successfully.")