import usaddress
# example addresses
address_a='136 Hoy Rd, Ithaca, NY 14850'
address_b ='401 Cayuga Park Ln Suite 101, Ithaca, NY 14850'
address_c='101 Dates Dr, Ithaca, NY 14850'
# address_c=
address_map_dict={
   'AddressNumber': 'Street Number',
   'AddressNumberPrefix': 'Street Number',
   'AddressNumberSuffix': 'Street Number',
   'StreetName': 'Street Name',
   'StreetNamePreDirectional': 'Street Name',
   'StreetNamePreModifier': 'Street Name',
   'StreetNamePreType': 'Street Name',
   'StreetNamePostDirectional': 'address1',
   'StreetNamePostModifier': 'Street Name',
   'StreetNamePostType': 'Street Name',
   'CornerOf': 'Street Name',
   'IntersectionSeparator': 'Street Name',
   'OccupancyType': 'Suite/apartment/room',
   'OccupancyIdentifier': 'Suite/apartment/room',
   'SubaddressIdentifier': 'Suite/apartment/room',
   'SubaddressType': 'Suite/apartment/room',
   'PlaceName': 'City',
   'StateName': 'State',
   'ZipCode': 'Postal_code',}
example = usaddress.tag(address_c, tag_mapping=address_map_dict)
example2 = usaddress.tag('Cayuga Medical Center '+address_c, tag_mapping=address_map_dict)