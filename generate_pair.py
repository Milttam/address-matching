import random


def generate_similar_address(original_address, randomness_factor=0.3):
    # Split the original address into components
    components = original_address.split()

    # Define abbreviation options
    abbreviation_options = {
        'St.': ['Street', 'St.'],
        'Ave.': ['Avenue', 'Ave.'],
        'Fl.': ['Floor', 'Fl.'],
        'E.': ['East', 'E.'],
        'W.': ['West', 'W.'],
        'N.': ['North', 'N.'],
        'S.': ['South', 'S.'],
        'Apt.': ['Apartment', 'Apt.'],
        'Rear': ['Rear', 'Rear'],
        'Suite': ['Suite', 'Ste.'],
        'Blvd.': ['Boulevard', 'Blvd.'],
        'Rd.': ['Road', 'Rd.'],
        'Ln.': ['Lane', 'Ln.'],
        'Ct.': ['Court', 'Ct.'],
        'Pl.': ['Place', 'Pl.'],
        'Hwy.': ['Highway', 'Hwy.'],
    }

    # Apply variations to each component
    modified_components = []
    for component in components:
        if component in abbreviation_options:
            # Randomly choose an abbreviation variation
            modified_component = random.choice(abbreviation_options[component])
        else:
            modified_component = component

        # Randomly change the order of components
        if random.random() < randomness_factor:
            modified_components.insert(0, modified_component)
        else:
            modified_components.append(modified_component)

    # Randomly add commas between components
    modified_address = ' '.join(modified_components)
    if random.random() < randomness_factor:
        modified_address = ', '.join(modified_components)

    return original_address, modified_address


# Example usage:
original_address = "123 Main East Street Floor 2, Plainview NY 11803"
pair_of_addresses = generate_similar_address(original_address)
print(pair_of_addresses)
