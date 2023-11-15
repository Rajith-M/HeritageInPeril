from flask import Flask, render_template, request, url_for, redirect, flash
import requests
from flask_mysqldb import MySQL
import yaml
from dummy_data import get_random_dummy_data  # Importing the get_random_dummy_data function

app = Flask(__name__)
app.secret_key = 'lalala'

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
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  # Get the email value from the form
        password = request.form.get('password')  # Get the password value from the form
        explorer_collaborator = request.form.get('explorerCollaborator')  # Get the explorer/collaborator value from the form

        print("Email:", email)  # Print email to the console
        print("Password:", password)  # Print password to the console
        print("Explorer/Collaborator:", explorer_collaborator)  # Print explorer/collaborator to the console

        # Check if the user exists in the User table
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM User WHERE User_Email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:  # If the user exists in the User table
            # Validate password - You should implement password hashing and verification
            if user['User_Password'] == password:
                # Password matches, user exists and can log in
                # Redirect or render a different template after successful login
                # For example, redirect to the index page
                return redirect(url_for('index'))
            else:
                # Incorrect password
                flash('Incorrect password. Please try again.', 'error')
                return render_template('login.html')
        else:
            # User does not exist
            flash('User does not exist. Please register.', 'error')
            return render_template('login.html')

    return render_template('login.html')



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
            SELECT Country, Region FROM naturalhabitat WHERE Country = %s AND Region = %s
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
            SELECT Country, Region FROM conservationlocation WHERE Country = %s AND Region = %s
        """, (cloccountry, clocregion))
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

from flask import render_template, request

@app.route('/map_page', methods=['GET', 'POST'])
def map_page():
    if request.method == 'POST':
        new_species_details = request.form

        # Extract filter values from the form
        region_filter = new_species_details.get('region')
        severity_filter = int(new_species_details.get('conservation-status'))
        limit_filter = int(new_species_details.get('limit'))

        # Construct the WHERE clause based on filters
        conditions = []
        parameters = []

        if region_filter:
            conditions.append("nh.Country = %s")
            parameters.append(region_filter)
        if severity_filter:
            conditions.append("t.Severity = %s")
            parameters.append(severity_filter)

        # Construct the SQL query with dynamic WHERE clause and placeholders
        filter_query = f"""
            SELECT
                s.ScientificName,
                s.CommonName,
                s.PopulationSize,
                s.Description,
                s.EstimatedDateOfExtinction,
                nh.Country AS HabitatCountry,
                nh.Region AS HabitatRegion,
                nh.Latitude AS HabitatLatitude,
                nh.Longitude AS HabitatLongitude,
                t.ThreatName,
                t.Description AS ThreatDescription,
                t.Severity AS ThreatSeverity
            FROM
                species s
            JOIN FoundAt fa ON s.ScientificName = fa.SpeciesScientificName
            JOIN NaturalHabitat nh ON fa.NaturalHabitatCountry = nh.Country AND fa.NaturalHabitatRegion = nh.Region
            JOIN ThreatenedBy tb ON s.ScientificName = tb.SpeciesScientificName
            JOIN Threats t ON tb.ThreatName = t.ThreatName            
            WHERE nh.Region = \"{region_filter}\" AND t.Severity = {str(severity_filter)};
        """


        print("filter query:", filter_query)
        # Execute the query with the filter values
        cur = mysql.connection.cursor()
        cur.execute(filter_query)
        filtered_species = cur.fetchall()

        print("filtered species", filtered_species)
        cur.close()

        output_dict_list = [{
                    'ScientificName': data[0],
                    'CommonName': data[1],
                    'PopulationSize': data[2],
                    'Description': data[3],
                    'EstimatedDateOfExtinction': data[4],
                    'Country': data[5],
                    'Region': data[6],
                    'Latitude': data[7],
                    'Longitude': data[8],
                    'ThreatName': data[9],
                    'ThreatDescription': data[10],
                    'Severity': data[11]
                } for data in filtered_species]
        
        # Render the template with the filtered species data
        return render_template('map.html', filtered_species=output_dict_list, css_url=url_for('static', filename='cssmap-australia/cssmap-australia.css'))

    # If not a POST request, render the initial map.html
    return render_template('map.html', css_url=url_for('static', filename='cssmap-australia/cssmap-australia.css'))

if __name__ == '__main__':
    app.run(debug=True)


