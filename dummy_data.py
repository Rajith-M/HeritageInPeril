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
        'region': 'NewSouthWales',
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
        'clocregion': 'NewSouthWales',
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
        'region': 'WesternAustralia',
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
        'clocregion': 'WesternAustralia',
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
        'region': 'SouthAustralia',
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
        'clocregion': 'SouthAustralia',
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
        'region': 'SouthAustralia',
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
        'clocregion': 'SouthAustralia',
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
        'region': 'WesternAustralia',
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
        'clocregion': 'WesternAustralia',
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
    {
        'commonName': 'Numbat',
        'scientificName': 'Myrmecobius fasciatus',
        'populationSize': 1000,
        'description': 'The numbat is a small marsupial native to Western Australia.',
        'estimatedExtinctionDate': '2048-01-01',
        'closestNeighbourCommonName': 'Bilby',
        'closestNeighbourScientificName': 'Macrotis lagotis',
        'region': 'WesternAustralia',
        'latitude': '-31.9505',  # Latitude for Perth, Australia
        'longitude': '115.8605',  # Longitude for Perth, Australia
        'threatName': 'Predation',
        'threatDescription': 'Threats from introduced predators impacting numbat populations.',
        'severity': 4,
        'organizationName': 'Western Australian Wildlife Preservation',
        'projectDescription': 'Conservation project for numbat habitats.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-31.9505',  # Latitude for Perth, Australia
        'cloclongitude': '115.8605',  # Longitude for Perth, Australia
        'cloccountry': 'Australia',
        'clocregion': 'WesternAustralia',
        'conservationPark': 'Numbat Nature Reserve'
    },
    {
        'commonName': 'Leadbeater\'s Possum',
        'scientificName': 'Gymnobelideus leadbeateri',
        'populationSize': 2000,
        'description': 'Leadbeater\'s possum is a critically endangered marsupial native to Victoria.',
        'estimatedExtinctionDate': '2040-01-01',
        'closestNeighbourCommonName': 'Squirrel Glider',
        'closestNeighbourScientificName': 'Petaurus norfolcensis',
        'region': 'Victoria',
        'latitude': '-37.8136',  # Latitude for Melbourne, Australia
        'longitude': '144.9631',  # Longitude for Melbourne, Australia
        'threatName': 'Habitat Fragmentation',
        'threatDescription': 'Loss and fragmentation of habitat impacting possum populations.',
        'severity': 5,
        'organizationName': 'Victorian Wildlife Preservation Society',
        'projectDescription': 'Conservation project for Leadbeater\'s possum.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-37.8136',  # Latitude for Melbourne, Australia
        'cloclongitude': '144.9631',  # Longitude for Melbourne, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Victoria',
        'conservationPark': 'Leadbeater\'s Possum Conservation Area'
    }, 
    {
        'commonName': 'Western Swamp Tortoise',
        'scientificName': 'Pseudemydura umbrina',
        'populationSize': 50,
        'description': 'A critically endangered freshwater turtle found in Western Australia.',
        'estimatedExtinctionDate': '2035-01-01',
        'closestNeighbourCommonName': 'Long-necked Turtle',
        'closestNeighbourScientificName': 'Chelodina oblonga',
        'region': 'WesternAustralia',
        'latitude': '-31.9505',  # Latitude for Perth, Australia
        'longitude': '115.8605',  # Longitude for Perth, Australia
        'threatName': 'Habitat Loss and Predation',
        'threatDescription': 'Habitat destruction and predation impacting tortoise populations.',
        'severity': 5,
        'organizationName': 'Western Australian Turtle Conservation Society',
        'projectDescription': 'Conservation project for Western Swamp Tortoise.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-31.9505',  # Latitude for Perth, Australia
        'cloclongitude': '115.8605',  # Longitude for Perth, Australia
        'cloccountry': 'Australia',
        'clocregion': 'WesternAustralia',
        'conservationPark': 'Western Swamp Tortoise Conservation Area'
    },
    {
        'commonName': 'Regent Honeyeater',
        'scientificName': 'Anthochaera phrygia',
        'populationSize': 400,
        'description': 'The regent honeyeater is a critically endangered bird known for its distinctive markings.',
        'estimatedExtinctionDate': '2040-01-01',
        'closestNeighbourCommonName': 'Swift Parrot',
        'closestNeighbourScientificName': 'Lathamus discolor',
        'region': 'New South Wales',
        'latitude': '-32.7157',  # Latitude for Sydney, Australia
        'longitude': '152.147',  # Longitude for Sydney, Australia
        'threatName': 'Habitat Loss and Fragmentation',
        'threatDescription': 'Loss and fragmentation of woodlands impacting honeyeater populations.',
        'severity': 4,
        'organizationName': 'New South Wales Bird Conservation Group',
        'projectDescription': 'Conservation project for regent honeyeaters.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-32.7157',  # Latitude for Sydney, Australia
        'cloclongitude': '152.147',  # Longitude for Sydney, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NewSouthWales',
        'conservationPark': 'Regent Honeyeater Reserve'
    },
    {
        'commonName': 'Giant Gippsland Earthworm',
        'scientificName': 'Megascolides australis',
        'populationSize': 2000,
        'description': 'The giant Gippsland earthworm is one of the largest earthworms in the world.',
        'estimatedExtinctionDate': '2043-01-01',
        'closestNeighbourCommonName': 'Common Eastern Earthworm',
        'closestNeighbourScientificName': 'Aporrectodea longa',
        'region': 'Victoria',
        'latitude': '-38.1368',  # Latitude for Gippsland, Victoria, Australia
        'longitude': '146.4309',  # Longitude for Gippsland, Victoria, Australia
        'threatName': 'Habitat Destruction',
        'threatDescription': 'Loss of habitat due to human development impacting earthworm populations.',
        'severity': 5,
        'organizationName': 'Victorian Earthworm Conservation Society',
        'projectDescription': 'Conservation project for the giant Gippsland earthworm.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-38.1368',  # Latitude for Gippsland, Victoria, Australia
        'cloclongitude': '146.4309',  # Longitude for Gippsland, Victoria, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Victoria',
        'conservationPark': 'Gippsland Earthworm Sanctuary'
    },
    {
        'commonName': 'Gouldian Finch',
        'scientificName': 'Erythrura gouldiae',
        'populationSize': 2500,
        'description': 'The Gouldian finch is a brightly colored bird found in Northern Australia.',
        'estimatedExtinctionDate': '2046-01-01',
        'closestNeighbourCommonName': 'Zebra Finch',
        'closestNeighbourScientificName': 'Taeniopygia guttata',
        'region': 'NorthernTerritory',
        'latitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'longitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'threatName': 'Habitat Fragmentation',
        'threatDescription': 'Fragmentation of grassland habitats impacting Gouldian finch populations.',
        'severity': 4,
        'organizationName': 'Northern Territory Finch Preservation Society',
        'projectDescription': 'Conservation project for the Gouldian finch.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'cloclongitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NorthernTerritory',
        'conservationPark': 'Gouldian Finch Reserve'
    },
    {
        'commonName': 'Bilby',
        'scientificName': 'Macrotis lagotis',
        'populationSize': 500,
        'description': 'The bilby is a small marsupial known for its long ears and burrowing habits.',
        'estimatedExtinctionDate': '2050-01-01',
        'closestNeighbourCommonName': 'Numbat',
        'closestNeighbourScientificName': 'Myrmecobius fasciatus',
        'region': 'NorthernTerritory',
        'latitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'longitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'threatName': 'Predation and Habitat Loss',
        'threatDescription': 'Introduced predators and habitat destruction impacting bilby populations.',
        'severity': 4,
        'organizationName': 'Northern Territory Bilby Conservation Society',
        'projectDescription': 'Conservation project for the bilby population.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'cloclongitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NorthernTerritory',
        'conservationPark': 'Bilby Protection Area'
    },
    {
        'commonName': 'Golden Bandicoot',
        'scientificName': 'Isoodon auratus',
        'populationSize': 600,
        'description': 'The golden bandicoot is a small marsupial with distinctive golden fur.',
        'estimatedExtinctionDate': '2048-01-01',
        'closestNeighbourCommonName': 'Northern Brown Bandicoot',
        'closestNeighbourScientificName': 'Isoodon macrourus',
        'region': 'NorthernTerritory',
        'latitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'longitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'threatName': 'Habitat Fragmentation and Invasive Species',
        'threatDescription': 'Habitat fragmentation and invasive species impacting bandicoot habitats.',
        'severity': 3,
        'organizationName': 'Northern Territory Bandicoot Conservation Alliance',
        'projectDescription': 'Conservation project for the golden bandicoot.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'cloclongitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NorthernTerritory',
        'conservationPark': 'Golden Bandicoot Sanctuary'
    },
    {
        'commonName': 'Helmeted Honeyeater',
        'scientificName': 'Lichenostomus melanops cassidix',
        'populationSize': 250,
        'description': 'The helmeted honeyeater is a critically endangered bird endemic to Victoria.',
        'estimatedExtinctionDate': '2045-01-01',
        'closestNeighbourCommonName': 'Yellow-tufted Honeyeater',
        'closestNeighbourScientificName': 'Lichenostomus melanops',
        'region': 'Victoria',
        'latitude': '-37.8136',  # Latitude for Melbourne, Victoria, Australia
        'longitude': '144.9631',  # Longitude for Melbourne, Victoria, Australia
        'threatName': 'Habitat Loss and Predation',
        'threatDescription': 'Loss of habitat and predation impacting helmeted honeyeater populations.',
        'severity': 5,
        'organizationName': 'Victorian Helmeted Honeyeater Preservation Society',
        'projectDescription': 'Conservation project for the helmeted honeyeater.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-37.8136',  # Latitude for Melbourne, Victoria, Australia
        'cloclongitude': '144.9631',  # Longitude for Melbourne, Victoria, Australia
        'cloccountry': 'Australia',
        'clocregion': 'Victoria',
        'conservationPark': 'Helmeted Honeyeater Reserve'
    },
    {
        'commonName': 'Mallee Fowl',
        'scientificName': 'Leipoa ocellata',
        'populationSize': 300,
        'description': 'The Mallee fowl is a ground-dwelling bird known for its large nesting mounds.',
        'estimatedExtinctionDate': '2049-01-01',
        'closestNeighbourCommonName': 'Brush Bronzewing',
        'closestNeighbourScientificName': 'Phaps elegans',
        'region': 'SouthAustralia',
        'latitude': '-34.9285',  # Latitude for Adelaide, South Australia, Australia
        'longitude': '138.6007',  # Longitude for Adelaide, South Australia, Australia
        'threatName': 'Habitat Degradation and Predation',
        'threatDescription': 'Habitat degradation and introduced predators affecting Mallee fowl habitats.',
        'severity': 4,
        'organizationName': 'South Australian Mallee Fowl Conservation Group',
        'projectDescription': 'Conservation project for the Mallee fowl.',
        'startDate': '2022-01-01',
        'endDate': '2025-01-01',
        'cloclatitude': '-34.9285',  # Latitude for Adelaide, South Australia, Australia
        'cloclongitude': '138.6007',  # Longitude for Adelaide, South Australia, Australia
        'cloccountry': 'Australia',
        'clocregion': 'SouthAustralia',
        'conservationPark': 'Mallee Fowl Habitat Preservation Area'
    },
    {
        'commonName': 'Night Parrot',
        'scientificName': 'Pezoporus occidentalis',
        'populationSize': 50,
        'description': 'The night parrot is an elusive and rarely seen nocturnal bird.',
        'estimatedExtinctionDate': '2050-01-01',
        'closestNeighbourCommonName': 'Bourke\'s Parrot',
        'closestNeighbourScientificName': 'Neopsephotus bourkii',
        'region': 'WesternAustralia',
        'latitude': '-31.9505',  # Latitude for Perth, Western Australia, Australia
        'longitude': '115.8605',  # Longitude for Perth, Western Australia, Australia
        'threatName': 'Habitat Loss and Feral Predators',
        'threatDescription': 'Habitat loss and feral predators impacting night parrot populations.',
        'severity': 5,
        'organizationName': 'Western Australian Night Parrot Conservancy',
        'projectDescription': 'Conservation project for the night parrot.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-31.9505',  # Latitude for Perth, Western Australia, Australia
        'cloclongitude': '115.8605',  # Longitude for Perth, Western Australia, Australia
        'cloccountry': 'Australia',
        'clocregion': 'WesternAustralia',
        'conservationPark': 'Night Parrot Conservation Reserve'
    },
    {
        'commonName': 'Central Rock Rat',
        'scientificName': 'Zyzomys pedunculatus',
        'populationSize': 100,
        'description': 'The central rock rat is a small, rare rodent species.',
        'estimatedExtinctionDate': '2046-01-01',
        'closestNeighbourCommonName': 'Fawn Hopping Mouse',
        'closestNeighbourScientificName': 'Notomys cervinus',
        'region': 'NorthernTerritory',
        'latitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'longitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'threatName': 'Habitat Fragmentation and Predation',
        'threatDescription': 'Habitat fragmentation and predation impacting central rock rat populations.',
        'severity': 4,
        'organizationName': 'Northern Territory Rock Rat Conservation Society',
        'projectDescription': 'Conservation project for the central rock rat.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'cloclongitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NorthernTerritory',
        'conservationPark': 'Central Rock Rat Protection Area'
    },
    {
        'commonName': 'Quokka',
        'scientificName': 'Setonix brachyurus',
        'populationSize': 15000,
        'description': 'The quokka is a small marsupial known for its friendly appearance and smile.',
        'estimatedExtinctionDate': '2040-01-01',
        'closestNeighbourCommonName': 'Coastal Taipan',
        'closestNeighbourScientificName': 'Oxyuranus scutellatus',
        'region': 'NorthernTerritory',
        'latitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'longitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'threatName': 'Habitat Destruction and Human Encroachment',
        'threatDescription': 'Habitat destruction and human encroachment impacting Central Ranges taipan populations.',
        'severity': 5,
        'organizationName': 'Northern Territory Taipan Conservation Group',
        'projectDescription': 'Conservation project for the Central Ranges taipan.',
        'startDate': '2022-01-01',
        'endDate': '2024-01-01',
        'cloclatitude': '-12.4634',  # Latitude for Darwin, Northern Territory, Australia
        'cloclongitude': '130.8456',  # Longitude for Darwin, Northern Territory, Australia
        'cloccountry': 'Australia',
        'clocregion': 'NorthernTerritory',
        'conservationPark': 'Central Ranges Taipan Sanctuary'
    }
]


def get_random_dummy_data():
    return random.choice(dummy_data_list)
