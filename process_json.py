import json


def process_json(json_data):
    """
    Extracts the "LOCATION" addresses from the JSON of ithaca_addresses.json
    """
    location_addresses = []

    for result in json_data["results"]:
        for address in result["addresses"]:
            if address["address_purpose"] == "LOCATION":
                # Create a new address dictionary with the relevant information
                # Get rid of Country Code, phone numbers, and address purpose
                # street_address includes the street number, street name, and secondary address information
                address = {
                    "street_address": address["address_1"],
                    "city": address["city"],
                    "state": address["state"],
                    # only take first 5 digits of postal code
                    "zip": address["postal_code"][:5]
                }
                location_addresses.append(address)

    return location_addresses


with open('data/ithaca_addresses.json') as json_file:
    data = json.load(json_file)

location_addresses = process_json(data)
print(location_addresses)
