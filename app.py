from flask import Flask, render_template, request, url_for
import requests
from flask_mysqldb import MySQL
import yaml
from dummy_data import get_random_dummy_data  # Importing the get_random_dummy_data function

app = Flask(__name__)

# configure the db
with open('db.yaml', 'r') as yamlfile:
    db = yaml.load(yamlfile, Loader=yaml.FullLoader)
    
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        email = userDetails['email']
        if(email!= ""):
            cur = mysql.connection.cursor()
            cur.execute("SELECT email FROM User WHERE email = %s", (email,))
            existing_email = cur.fetchone()
            if existing_email:
                cur.close()
                return "Email already exists!"
            else:
                cur.execute("INSERT INTO User (email) VALUES (%s)", (email,))
                mysql.connection.commit()
                cur.close()
                return "Success! New email added."
        else:
            return "No email entered"
    
    return render_template('index.html')

@app.route('/enter_species_details', methods=['GET', 'POST'])
def enter_species_details():
    if request.method == 'POST':
        new_species_details = request.form

        scientific_name = new_species_details['scientificName']
        common_name = new_species_details['commonName']
        population_size = new_species_details['populationSize']
        description = new_species_details['description']
        extinction_date = new_species_details['estimatedExtinctionDate']
        country = new_species_details['country']
        region = new_species_details['region']
        latitude = new_species_details['latitude']
        longitude = new_species_details['longitude']
        threat_name = new_species_details['threatName']
        threat_description = new_species_details['threatDescription']
        severity = new_species_details['severity']
        organization_name = new_species_details['organizationName']
        project_description = new_species_details['projectDescription']
        start_date = new_species_details['startDate']
        end_date = new_species_details['endDate']
        cloclatitude = new_species_details['cloclatitude']
        cloclongitude = new_species_details['cloclongitude']
        cloccountry = new_species_details['cloccountry']
        clocregion = new_species_details['clocregion']
        conservationPark = new_species_details['conservationPark']

        cur = mysql.connection.cursor()

        # Check if the species already exists in the 'species' table
        cur.execute("SELECT ScientificName FROM species WHERE ScientificName = %s", (scientific_name,))
        existing_species = cur.fetchone()

        if existing_species:
            return "Species already exists!"

        # Insert into 'species' table
        cur.execute("""
            INSERT INTO species (ScientificName, CommonName, PopulationSize, Description, EstimatedDateOfExtinction)
            VALUES (%s, %s, %s, %s, %s)
        """, (scientific_name, common_name, population_size, description, extinction_date))


        # NaturalHabitat table
        cur.execute("""
            SELECT Country FROM naturalhabitat WHERE Country = %s AND Region = %s
        """, (country, region))
        existing_natural_habitat = cur.fetchone()
        if not existing_natural_habitat:
            cur.execute(""" INSERT INTO NaturalHabitat (Country, Region, Latitude, Longitude)
                VALUES (%s, %s, %s, %s)
            """, (country, region, latitude, longitude))


        # Threats table
        cur.execute("""
            SELECT ThreatName FROM threats WHERE ThreatName = %s
        """, (threat_name,))
        existing_threat = cur.fetchone()
        if not existing_threat:
            cur.execute("""
                INSERT INTO Threats (ThreatName, Description, Severity)
                VALUES (%s, %s, %s)
            """, (threat_name, threat_description, severity))

        # ConservationEfforts table
        cur.execute("""
            SELECT OrganizationName FROM conservationefforts WHERE OrganizationName = %s
        """, (organization_name,))
        existing_conservation_effort = cur.fetchone()
        if not existing_conservation_effort:
            cur.execute("""
                INSERT INTO ConservationEfforts (OrganizationName, ProjectDescription, StartDate, EndDate)
                VALUES (%s, %s, %s, %s)
            """, (organization_name, project_description, start_date, end_date))

        # ConservationLocation table
        cur.execute("""
            SELECT Country FROM conservationlocation WHERE Country = %s AND ConservationPark = %s
        """, (country, conservationPark))
        existing_conservation_location = cur.fetchone()
        if not existing_conservation_location:
            cur.execute("""
                INSERT INTO ConservationLocation (Latitude, Longitude, Country, Region, ConservationPark)
                VALUES (%s, %s, %s, %s, %s)
            """, (cloclatitude, cloclongitude, cloccountry, clocregion, conservationPark))


        cur.execute("CALL UpdateRelationTables(%s, %s, %s, %s, %s, %s, %s, %s)",
            (scientific_name, common_name, country, region, threat_name,
             organization_name, cloccountry, clocregion))

        mysql.connection.commit()
        cur.close()
        return "Successfully entered species and details!"
    
    dummy_data = get_random_dummy_data()
    return render_template('enter_species_details.html', dummy_data = dummy_data)

def get_unsplash_image_url(keyword):
    # Replace 'YOUR_ACCESS_KEY' with your Unsplash API access key
    access_key = 'kotZy7ftGWCC1Cmpi9V3HA2ayzFbyneCKmRd_YQckiE'
    base_url = 'https://api.unsplash.com/photos/random'
    params = {
        'query': keyword,
        'client_id': access_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data and 'urls' in data:
            return data['urls']['regular']
    return None

@app.route('/map_page')
def map_page():
    keyword = "animals"  # You can change this to any keyword you want
    # image_url = get_unsplash_image_url(keyword)

    # Pass the image URL to the template
    return render_template('map.html', css_url=url_for('static', filename='cssmap-australia/cssmap-australia.css'))

if __name__ == '__main__':
    app.run(debug=True)


