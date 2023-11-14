import random

dummy_data_list = [
        {
        'commonName': 'Kangaroo',
        'scientificName': 'Macropus rufus',
        'populationSize': 5000000,
        'description': 'The kangaroo is an iconic Australian marsupial.',
        'estimatedExtinctionDate': '2050-01-01',
        'closestNeighbourCommonName': 'Wallaby',
        'closestNeighbourScientificName': 'Macropus_eugenii',
        'region': 'New South Wales',
        'latitude': '-33.8688',  # Latitude for Sydney, Australia
        'longitude': '151.2093',  # Longitude for Sydney, Australia
        'threatName': 'Habitat Loss',
        'threatDescription': 'Loss of natural habitats due to urbanization.',
        'severity': 3,
        'organizationName': 'Australian Wildlife Conservation Society',
        'projectDescription': 'Conservation project for kangaroo preservation.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-33.8688',  # Latitude for Sydney, Australia
        'cloclongitude': '151.2093',  # Longitude for Sydney, Australia
        'cloccountry': 'Australia',
        'clocregion': 'New South Wales',
        'conservationPark': 'Outback National Park'
    },
    {
        'commonName': 'Koala',
        'scientificName': 'Phascolarctos cinereus',
        'populationSize': 80000,
        'description': 'The koala is an arboreal herbivorous marsupial native to Australia.',
        'estimatedExtinctionDate': '2040-01-01',
        'closestNeighbourCommonName': 'Possum',
        'closestNeighbourScientificName': 'Trichosurus_vulpecula',
        'region': 'Queensland',
        'latitude': '-27.4698',  # Latitude for Brisbane, Australia
        'longitude': '153.0251',  # Longitude for Brisbane, Australia
        'threatName': 'Bushfires',
        'threatDescription': 'Increasing frequency of bushfires affecting habitats.',
        'severity': 4,
        'organizationName': 'Australian Koala Foundation',
        'projectDescription': 'Conservation project for koala habitats.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-27.4698',  # Latitude for Brisbane, Australia
        'cloclongitude': '153.0251',  # Longitude for Brisbane, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Queensland',
        'conservationPark': 'Eucalyptus Grove Conservation Reserve'
    },
    {
        'commonName': 'Emu',
        'scientificName': 'Dromaius novaehollandiae',
        'populationSize': 120000,
        'description': 'The emu is the world\'s second-largest bird.',
        'estimatedExtinctionDate': '2035-01-01',
        'closestNeighbourCommonName': 'Cassowary',
        'closestNeighbourScientificName': 'Casuarius_casuarius',
        'region': 'Victoria',
        'latitude': '-37.8136',  # Latitude for Melbourne, Australia
        'longitude': '144.9631',  # Longitude for Melbourne, Australia
        'threatName': 'Climate Change',
        'threatDescription': 'Changing climate affecting food sources and breeding.',
        'severity': 2,
        'organizationName': 'Australian Bird Conservation Society',
        'projectDescription': 'Conservation project for emu habitats.',
        'startDate': '2022-01-01',
        'endDate': '2023-12-31',
        'cloclatitude': '-37.8136',  # Latitude for Melbourne, Australia
        'cloclongitude': '144.9631',  # Longitude for Melbourne, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Victoria',
        'conservationPark': 'Open Plains Nature Reserve'
    },
    {
        'commonName': 'Wombat',
        'scientificName': 'Vombatus ursinus',
        'populationSize': 30000,
        'description': 'The wombat is a herbivorous marsupial native to Australia.',
        'estimatedExtinctionDate': '2045-01-01',
        'closestNeighbourCommonName': 'Kangaroo',
        'closestNeighbourScientificName': 'Macropus_rufus',
        'region': 'Tasmania',
        'latitude': '-42.8821',  # Latitude for Hobart, Australia
        'longitude': '147.3272',  # Longitude for Hobart, Australia
        'threatName': 'Invasive Species',
        'threatDescription': 'Introduction of invasive species impacting wombat habitats.',
        'severity': 3,
        'organizationName': 'Tasmanian Wildlife Preservation Society',
        'projectDescription': 'Conservation project for wombat populations.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-42.8821',  # Latitude for Hobart, Australia
        'cloclongitude': '147.3272',  # Longitude for Hobart, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Tasmania',
        'conservationPark': 'Tasmanian Wilderness Sanctuary'
    },
    {
        'commonName': 'Cockatoo',
        'scientificName': 'Cacatua',
        'populationSize': 150000,
        'description': 'Cockatoos are a family of parrots native to Australia.',
        'estimatedExtinctionDate': '2030-01-01',
        'closestNeighbourCommonName': 'Galah',
        'closestNeighbourScientificName': 'Eolophus_roseicapilla',
        'region': 'Western Australia',
        'latitude': '-31.9505',  # Latitude for Perth, Australia
        'longitude': '115.8605',  # Longitude for Perth, Australia
        'threatName': 'Illegal Pet Trade',
        'threatDescription': 'Illegal capture and trade impacting cockatoo populations.',
        'severity': 4,
        'organizationName': 'Western Australian Avian Conservation',
        'projectDescription': 'Conservation project for cockatoo welfare.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-31.9505',  # Latitude for Perth, Australia
        'cloclongitude': '115.8605',  # Longitude for Perth, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Western Australia',
        'conservationPark': 'Eucalyptus Canopy Conservation Area'
    },
    {
        'commonName': 'Platypus',
        'scientificName': 'Ornithorhynchus anatinus',
        'populationSize': 10000,
        'description': 'The platypus is a unique egg-laying mammal native to Australia.',
        'estimatedExtinctionDate': '2055-01-01',
        'closestNeighbourCommonName': 'Echidna',
        'closestNeighbourScientificName': 'Tachyglossus_aculeatus',
        'region': 'South Australia',
        'latitude': '-34.9285',  # Latitude for Adelaide, Australia
        'longitude': '138.6007',  # Longitude for Adelaide, Australia
        'threatName': 'Water Pollution',
        'threatDescription': 'Pollution of water sources impacting platypus habitats.',
        'severity': 3,
        'organizationName': 'South Australian Mammal Preservation',
        'projectDescription': 'Conservation project for platypus ecosystems.',
        'startDate': '2022-01-01',
        'endDate': '2023-12-31',
        'cloclatitude': '-34.9285',  # Latitude for Adelaide, Australia
        'cloclongitude': '138.6007',  # Longitude for Adelaide, Australia
        'cloccountry': 'Australia',
        'clocregion': 'South Australia',
        'conservationPark': 'Murray River Conservation Reserve'
    },
        {
        'commonName': 'Cassowary',
        'scientificName': 'Casuarius casuarius',
        'populationSize': 5000,
        'description': 'Cassowaries are large, flightless birds native to the tropical forests of New Guinea and nearby islands.',
        'estimatedExtinctionDate': '2042-01-01',
        'closestNeighbourCommonName': 'Emu',
        'closestNeighbourScientificName': 'Dromaius_novaehollandiae',
        'region': 'Queensland',
        'latitude': '-27.4698',  # Latitude for Brisbane, Australia
        'longitude': '153.0251',  # Longitude for Brisbane, Australia
        'threatName': 'Deforestation',
        'threatDescription': 'Clearing of forests impacting cassowary habitats.',
        'severity': 4,
        'organizationName': 'Queensland Bird Conservation Alliance',
        'projectDescription': 'Conservation project for cassowary environments.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-27.4698',  # Latitude for Brisbane, Australia
        'cloclongitude': '153.0251',  # Longitude for Brisbane, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Queensland',
        'conservationPark': 'Tropical Rainforest Reserve'
    },
    {
        'commonName': 'Echidna',
        'scientificName': 'Tachyglossus aculeatus',
        'populationSize': 15000,
        'description': 'The echidna, also known as the spiny anteater, is one of the few monotremes.',
        'estimatedExtinctionDate': '2048-01-01',
        'closestNeighbourCommonName': 'Platypus',
        'closestNeighbourScientificName': 'Ornithorhynchus_anatinus',
        'region': 'South Australia',
        'latitude': '-34.9285',  # Latitude for Adelaide, Australia
        'longitude': '138.6007',  # Longitude for Adelaide, Australia
        'threatName': 'Land Development',
        'threatDescription': 'Urban development impacting echidna habitats.',
        'severity': 2,
        'organizationName': 'South Australian Wildlife Preservation Society',
        'projectDescription': 'Conservation project for echidna populations.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-34.9285',  # Latitude for Adelaide, Australia
        'cloclongitude': '138.6007',  # Longitude for Adelaide, Australia
        'cloccountry': 'Australia',
        'clocregion': 'South Australia',
        'conservationPark': 'Adelaide Hills Wildlife Sanctuary'
    },
    {
        'commonName': 'Galah',
        'scientificName': 'Eolophus roseicapilla',
        'populationSize': 100000,
        'description': 'The galah is one of the most common and widespread cockatoos.',
        'estimatedExtinctionDate': '2033-01-01',
        'closestNeighbourCommonName': 'Cockatoo',
        'closestNeighbourScientificName': 'Cacatua',
        'region': 'Western Australia',
        'latitude': '-31.9505',  # Latitude for Perth, Australia
        'longitude': '115.8605',  # Longitude for Perth, Australia
        'threatName': 'Pesticide Poisoning',
        'threatDescription': 'Contamination of food sources due to pesticide use.',
        'severity': 3,
        'organizationName': 'Western Australian Parrot Conservation',
        'projectDescription': 'Conservation project for galah habitats.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-31.9505',  # Latitude for Perth, Australia
        'cloclongitude': '115.8605',  # Longitude for Perth, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Western Australia',
        'conservationPark': 'Coastal Eucalyptus Reserve'
    },
    {
        'commonName': 'Tasmanian Devil',
        'scientificName': 'Sarcophilus harrisii',
        'populationSize': 5000,
        'description': 'The Tasmanian devil is a carnivorous marsupial found only on the island of Tasmania.',
        'estimatedExtinctionDate': '2050-01-01',
        'closestNeighbourCommonName': 'Quoll',
        'closestNeighbourScientificName': 'Dasyurus',
        'region': 'Tasmania',
        'latitude': '-42.8821',  # Latitude for Hobart, Australia
        'longitude': '147.3272',  # Longitude for Hobart, Australia
        'threatName': 'Devil Facial Tumor Disease',
        'threatDescription': 'Contagious cancer affecting Tasmanian devil populations.',
        'severity': 5,
        'organizationName': 'Tasmanian Wildlife Conservation Society',
        'projectDescription': 'Conservation project for Tasmanian devil health.',
        'startDate': '2022-01-01',
        'endDate': '2023-12-31',
        'cloclatitude': '-42.8821',  # Latitude for Hobart, Australia
        'cloclongitude': '147.3272',  # Longitude for Hobart, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Tasmania',
        'conservationPark': 'Tasmanian Wilderness Sanctuary'
    },
]


def get_random_dummy_data():
    return random.choice(dummy_data_list)
