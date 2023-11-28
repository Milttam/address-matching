import requests
import json
states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'AS', 'AE', 'AP', 'AA', 'GU', 'MP', 'MH', 'FM', 'VI']


def get_process_data():
    """
    Returns a list of dictionaries containing the addresses of the first 100 
    providers with a "surgery" specality in each state
    """
    # for each state, return first 100 providers with a "surgery" specality
    # after submitting requests, should create a new JSON file with all of the addresses in a specified format
    addresses = []
    for state in states:
        url = "https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=surgery&name_purpose=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=" + \
            state + "&postal_code=&country_code=US&limit=20&skip=&pretty=&version=2.1"
        response = requests.get(url)
        json_data = response.json()
        print(state)
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
                    addresses.append(address)
    return addresses  # list of dictionaries
