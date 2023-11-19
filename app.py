from flask import Flask, render_template, request, url_for, redirect, flash, session, abort
import requests
from flask_mysqldb import MySQL
import yaml
from dummy_data import get_random_dummy_data  # Importing the get_random_dummy_data function

app = Flask(__name__)
app.secret_key = 'lalala'

commonNameOfTheSpeciesToUpdate = "abc"
scientificNameOfTheSpeciesToUpdate = "abc"

# configure the db
with open('db.yaml', 'r') as yamlfile:
    db = yaml.load(yamlfile, Loader=yaml.FullLoader)
    
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


def get_unsplash_image_url(keyword):
    access_key = 'kotZy7ftGWCC1Cmpi9V3HA2ayzFbyneCKmRd_YQckiE'
    base_url = 'https://api.unsplash.com/search/photos'
    params = {
        'query': keyword,
        'client_id': access_key,
        'per_page': 1,
        'orientation': 'landscape'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['regular']
    return None


@app.route('/', methods=['GET', 'POST'])
def index():    
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') 
        
        print("Login Information")
        print("Email:", email)  
        print("Password:", password) 

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM User WHERE User_Email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:  
            if user[1] == password:
                session["user"] = user[2]
                return redirect(url_for('index'))
            else:
                flash('Incorrect password. Please try again.', 'error')
                return render_template('login.html')
        else:
            flash('User does not exist. Please register.', 'error')
            return render_template('login.html')

    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        explorer_collaborator = request.form.get('explorerCollaborator')
        print(email, password, explorer_collaborator)

        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM User WHERE User_Email = %s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            flash('User already exists. Please log in.', 'error')
            return redirect(url_for('login'))

        cur.execute("INSERT INTO User (User_Email, User_Password, User_Type) VALUES (%s, %s, %s)", (email, password, explorer_collaborator))

        mysql.connection.commit()
        cur.close()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')




@app.route('/enter_species_details', methods=['GET', 'POST'])
def enter_species_details():
    if "user" not in session or session["user"] != "Collaborator":
        abort(403)  # Return a forbidden response if the user is not a collaborator
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
    
    if "user" in session:
        dummy_data = get_random_dummy_data()
        return render_template('enter_species_details.html', dummy_data = dummy_data)


@app.route('/search_for_update', methods=['GET', 'POST'])
def search_for_update():
    if "user" not in session or session["user"] != "Collaborator":
        abort(403)  # Return a forbidden response if the user is not a collaborator
    
    if request.method == 'POST':
        # Assuming form data is being submitted, process it here
        species_details = request.form
        commonName = species_details['commonName']
        scientificName = species_details['scientificName']

        print(commonName, scientificName)

        cur = mysql.connection.cursor()

        # Check if the species already exists in the 'species' table
        cur.execute("SELECT ScientificName, CommonName FROM species WHERE ScientificName = %s AND CommonName = %s", (scientificName, commonName))
        existing_species = cur.fetchone()

        if existing_species:
            global scientificNameOfTheSpeciesToUpdate, commonNameOfTheSpeciesToUpdate
            scientificNameOfTheSpeciesToUpdate = scientificName
            commonNameOfTheSpeciesToUpdate = commonName
            return redirect(url_for('update_species_details'))
        else:
            return "Not editable! Species does not exist in the database"        
        
    if "user" in session:
        return render_template('search_for_update.html')
    
    
@app.route('/update_species_details', methods=['GET', 'POST'])
def update_species_details():
    if "user" not in session or session["user"] != "Collaborator":
        abort(403)  # Return a forbidden response if the user is not a collaborator
    
    if request.method == 'POST':
        # Assuming form data is being submitted, process it here
        species_details = request.form

        print('------species_details: ------- \n', species_details)

        # Extracting form data
        scientific_name = species_details['scientificName']
        common_name = species_details['commonName']
        population_size = species_details['populationSize']
        description = species_details['description']
        estimated_extinction_date = species_details['estimatedExtinctionDate']
        country = species_details['country']
        region = species_details['region']
        latitude = species_details['latitude']
        longitude = species_details['longitude']
        threat_name = species_details['threatName']
        threat_description = species_details['threatDescription']
        severity = species_details['severity']
        organization_name = species_details['organizationName']
        project_description = species_details['projectDescription']
        start_date = species_details['startDate']
        end_date = species_details['endDate']
        cloclatitude = species_details['cloclatitude']
        cloclongitude = species_details['cloclongitude']
        cloccountry = species_details['cloccountry']
        clocregion = species_details['clocregion']
        conservation_park = species_details['conservationPark']

        # Prepare the parameters for the stored procedure
        params = (
            common_name,
            scientific_name,
            int(population_size),
            description,
            estimated_extinction_date,
            country,
            region,
            float(latitude),
            float(longitude),
            threat_name,
            threat_description,
            int(severity),
            organization_name,
            project_description,
            start_date,
            end_date,
            float(cloclatitude),
            float(cloclongitude),
            cloccountry,
            clocregion,
            conservation_park
        )

        # Execute the stored procedure
        cur = mysql.connection.cursor()
        cur.callproc('UpdateSpeciesDetails', params)
        mysql.connection.commit()
        cur.close()
        return 'update successful!'  # Return a response after processing
        
    if "user" in session:
        scientific_name = scientificNameOfTheSpeciesToUpdate
        common_name = commonNameOfTheSpeciesToUpdate
    
        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT s.CommonName, s.ScientificName, s.PopulationSize, s.Description, s.EstimatedDateOfExtinction,
            nh.Country, nh.Region, nh.Latitude AS nh_latitude, nh.Longitude AS nh_longitude,
            t.ThreatName, t.Description AS threat_description, t.Severity,
            ce.OrganizationName, ce.ProjectDescription, ce.StartDate, ce.EndDate,
            cl.Latitude AS cl_latitude, cl.Longitude AS cl_longitude, cl.Country AS cloccountry, cl.Region AS clocregion,
            cl.ConservationPark
            FROM species s
            LEFT JOIN FoundAt fa ON s.ScientificName = fa.SpeciesScientificName
            LEFT JOIN NaturalHabitat nh ON fa.NaturalHabitatCountry = nh.Country AND fa.NaturalHabitatRegion = nh.Region
            LEFT JOIN ThreatenedBy tb ON s.ScientificName = tb.SpeciesScientificName
            LEFT JOIN Threats t ON tb.ThreatName = t.ThreatName
            LEFT JOIN ConservedBy cb ON s.ScientificName = cb.SpeciesScientificName
            LEFT JOIN ConservationEfforts ce ON cb.OrganizationName = ce.OrganizationName
            LEFT JOIN ConservedAt ca ON ce.OrganizationName = ca.OrganizationName
            LEFT JOIN ConservationLocation cl ON ca.ConservationLocationCountry = cl.Country AND ca.ConservationLocationRegion = cl.Region
            WHERE s.ScientificName = %s AND s.CommonName = %s
            """, (scientific_name, common_name)
        )

        species_data = cur.fetchone()

        print(species_data)

        output_dict = {
            'commonName': species_data[0],
            'scientificName': species_data[1],
            'populationSize': species_data[2],
            'description': species_data[3],
            'estimatedExtinctionDate': species_data[4],
            'country': species_data[5],
            'region': species_data[6],
            'latitude': species_data[7],
            'longitude': species_data[8],
            'threatName': species_data[9],
            'threatDescription': species_data[10],
            'severity': species_data[11],
            'organizationName': species_data[12],
            'projectDescription': species_data[13],
            'startDate': species_data[14],
            'endDate': species_data[15],
            'cloclatitude': species_data[16],
            'cloclongitude': species_data[17],
            'cloccountry': species_data[18],
            'clocregion': species_data[19],
            'conservationPark': species_data[20]
        }

        print(output_dict)
        return render_template('update_species_details.html', species_data = output_dict)


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
        return render_template('map.html', filtered_species=output_dict_list, css_url=url_for('static', filename='cssmap-australia/cssmap-australia.css'), get_unsplash_image_url=get_unsplash_image_url)

    # If not a POST request, render the initial map.html
    return render_template('map.html', css_url=url_for('static', filename='cssmap-australia/cssmap-australia.css'), get_unsplash_image_url=get_unsplash_image_url)

if __name__ == '__main__':
    app.run(debug=True)


