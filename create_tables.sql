-- Species Table:

create database heritage_in_peril;
use heritage_in_peril;

CREATE TABLE species (
    ScientificName VARCHAR(255) PRIMARY KEY,
    CommonName VARCHAR(255) NOT NULL,
    PopulationSize INT NOT NULL,
    Description TEXT NOT NULL,
    EstimatedDateOfExtinction DATE
);

-- Closest Neighbour Table:
CREATE TABLE ClosestNeighbour (
    CommonName VARCHAR(255) NOT NULL,
    ScientificName VARCHAR(255) NOT NULL,
    PRIMARY KEY (CommonName, ScientificName),
    FOREIGN KEY (ScientificName) REFERENCES species(ScientificName)
);

-- NaturalHabitat Table:
CREATE TABLE NaturalHabitat (
    Country VARCHAR(255),
    Region VARCHAR(255),
    PRIMARY KEY (Country, Region),
    Latitude VARCHAR(50),
    Longitude VARCHAR(50)
);

-- FoundAt Table:
CREATE TABLE FoundAt (
    NaturalHabitatCountry VARCHAR(255),
    NaturalHabitatRegion VARCHAR(255),
    SpeciesScientificName VARCHAR(255),
    PRIMARY KEY (NaturalHabitatCountry, NaturalHabitatRegion, SpeciesScientificName),
    FOREIGN KEY (NaturalHabitatCountry, NaturalHabitatRegion) REFERENCES NaturalHabitat(Country, Region),
    FOREIGN KEY (SpeciesScientificName) REFERENCES species(ScientificName)
);

-- Threats Table:
CREATE TABLE Threats (
    ThreatName VARCHAR(255) PRIMARY KEY,
    Description TEXT NOT NULL,
    Severity TINYINT NOT NULL CHECK (Severity >= 1 AND Severity <= 5)
);

-- ThreatenedBy table:
CREATE TABLE ThreatenedBy (
    SpeciesScientificName VARCHAR(255),
    ThreatName VARCHAR(255),
    PRIMARY KEY (SpeciesScientificName, ThreatName),
    FOREIGN KEY (SpeciesScientificName) REFERENCES species(ScientificName),
    FOREIGN KEY (ThreatName) REFERENCES Threats(ThreatName)
);

-- ConservationEfforts Table:
CREATE TABLE ConservationEfforts (
    OrganizationName VARCHAR(255) PRIMARY KEY,
    ProjectDescription TEXT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL
);

-- Conservation Location Table:
CREATE TABLE ConservationLocation (
    Country VARCHAR(255),
    Region VARCHAR(255),
    PRIMARY KEY (Country, Region),
    Latitude DECIMAL(10, 6) NOT NULL,
    Longitude DECIMAL(10, 6) NOT NULL,
    ConservationPark VARCHAR(255)
);

-- ConservedBy:
CREATE TABLE ConservedBy (
    OrganizationName VARCHAR(255),
    SpeciesScientificName VARCHAR(255),
    PRIMARY KEY (OrganizationName, SpeciesScientificName),
    FOREIGN KEY (OrganizationName) REFERENCES ConservationEfforts(OrganizationName),
    FOREIGN KEY (SpeciesScientificName) REFERENCES species(ScientificName)
);

-- ConservedAt Table:
CREATE TABLE ConservedAt (
    OrganizationName VARCHAR(255),
    ConservationLocationCountry VARCHAR(255),
    ConservationLocationRegion VARCHAR(255),
    PRIMARY KEY (OrganizationName, ConservationLocationCountry, ConservationLocationRegion),
    FOREIGN KEY (OrganizationName) REFERENCES ConservationEfforts(OrganizationName),
    FOREIGN KEY (ConservationLocationCountry, ConservationLocationRegion) REFERENCES ConservationLocation(Country, Region)
);

-- User table (for people who subscribe to the page and for monthly newsletters, etc.)
CREATE TABLE User (
    User_Email VARCHAR(50),
    User_Password VARCHAR(50),
    User_Type VARCHAR(50),
    PRIMARY KEY (User_Email)
);
