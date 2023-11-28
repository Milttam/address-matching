import pandas as pd
import json
import random


def make_entries():
    """
    Creates a pandas dataframe with the following columns: address1, address2, label, 
    where each entry represents a pair of addresses and their label (0 for different, 1 for same)
    """
    # initialize pandas dataframe with defined columns
    df = pd.DataFrame(columns=['address1', 'address2', 'label'])

    # open addresses json file
    with open('addresses_data.json') as f:
        addresses = json.load(f)
    addresses = addresses["res"]

    # add case1 entries
    df = pd.concat([df, case1(addresses)], ignore_index=True)

    # add case4 entries
    df = pd.concat([df, case4(addresses)], ignore_index=True)

    return df


def case1(addresses):
    """
    Given a list of addresses, return a DF with the following entries as epcified by case1:
    For every address object, create an entry with the unstructured address to itself with a label of 1
    """
    df = pd.DataFrame(columns=['address1', 'address2', 'label'])
    for address in addresses:
        string_add = address["street_address"] + ", " + \
            address["city"] + ", " + address["state"] + " " + address["zip"]
        df.loc[len(df)] = {'address1': string_add, 'address2': string_add,
                           'label': 1}
    return df


def case4(addresses):
    """
    Given a list of addresses, return a DF with the 10000 entries as epcified by case4:
    Select two random addresses with label 0
    """
    df = pd.DataFrame(columns=['address1', 'address2', 'label'])
    for i in range(10000):
        # select two random addresses
        address1 = random.choice(addresses)
        address2 = random.choice(addresses)
        # make sure they are different
        while address1 == address2:
            address2 = random.choice(addresses)
        # create entry
        string_add1 = address1["street_address"] + ", " + \
            address1["city"] + ", " + address1["state"] + " " + address1["zip"]
        string_add2 = address2["street_address"] + ", " + \
            address2["city"] + ", " + address2["state"] + " " + address2["zip"]
        df.loc[len(df)] = {'address1': string_add1,
                           'address2': string_add2, 'label': 0}
    return df


print(make_entries())
