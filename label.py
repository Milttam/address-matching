import usaddress
import json
# example addresses
address_a = '136 Hoy Rd, Ithaca, NY 14850'
address_b = '401 Cayuga Park Ln Suite 101, Ithaca, NY 14850'
address_c = '101 Dates Dr, Ithaca, NY 14850'
# address dictionary for parsing.
address_map_dict = {
    'AddressNumber': 'address_number',
    'AddressNumberPrefix': 'address_number',
    'AddressNumberSuffix': 'address_number',
    'StreetName': 'street_name',
    'StreetNamePreDirectional': 'street_name',
    'StreetNamePreModifier': 'street_name',
    'StreetNamePreType': 'street_name',
    'StreetNamePostDirectional': 'street_name',
    'StreetNamePostModifier': 'street_name',
    'StreetNamePostType': 'street_name',
    'CornerOf': 'street_name',
    'IntersectionSeparator': 'street_name',
    'OccupancyType': 'secondary_address',
    'OccupancyIdentifier': 'secondary_address',
    'SubaddressIdentifier': 'secondary_address',
    'SubaddressType': 'secondary_address',
    'PlaceName': 'city',
    'StateName': 'state',
    'ZipCode': 'postal_code', }
# examples using the dictionary
example = usaddress.tag(address_c, tag_mapping=address_map_dict)
example2 = usaddress.tag('Cayuga Medical Center ' +
                         address_c, tag_mapping=address_map_dict)

# Make an expanded mapping with more features in the future

# pretty print an example
add = "62 Main Street Suite 4b, New Paltz, NY 12561"
od = usaddress.tag(add, tag_mapping=address_map_dict)
print("\nOriginal Address:" + add + "\n")
print(json.dumps(od, indent=4))
