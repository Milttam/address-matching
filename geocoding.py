import requests
import time


def geocode_address(address):
    """
    Geocode an address using the Maps.co Geocoding API.
    See https://geocode.maps.co 
    Input: 
      address: A dictionary containing address information with keys:
        - number: Street number
        - street: Street name
        - city: City name
        - state: State name or abbreviation
        - zip: ZIP code
        - country: Country name or abbreviation
    Output:
      A tuple with the latitude and longitude of the input address
      or None if the address could not be geocoded.
    """
    base_url = "https://geocode.maps.co/search"

    # parameteres for the API request
    params = {
        'street': f"{address['number']} {address['street']}",
        'city': address['city'],
        'state': address['state'],
        'postalcode': address['zip'],
        'country': address['country']
    }

    # use requests to call the API using params
    response = requests.get(base_url, params=params)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # parse the JSON response
        data = response.json()

        # extract latitude and longitude from the first result
        if data and len(data) > 0:
            result = data[0]
            coordinates = float(result['lat']), float(result['lon'])
            return coordinates
        else:
            print("No results found for the provided address.")
            return None
    else:
        # Print an error message if the request was not successful
        print(f"Error {response.status_code}: {response.text}")
        return None

# Function to limit requests to one every 0.5 seconds


def geocode_with_delay(address):
    coordinates = geocode_address(address)

    if coordinates:
        print(f"Coordinates: {coordinates}")

    # delay .5 seconds before returning to account for API rate limits
    time.sleep(0.5)


# test address
address = {
    'number': '62',
    'street': 'Beaumont Drive',
    'city': 'Plainview',
    'state': 'NY',
    'zip': '11803',
    'country': 'US'
}

# test function call
geocode_with_delay(address)
