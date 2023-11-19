DELIMITER //

CREATE PROCEDURE UpdateSpeciesDetails (
    IN p_CommonName VARCHAR(255),
    IN p_ScientificName VARCHAR(255),
    IN p_PopulationSize INT,
    IN p_Description TEXT,
    IN p_EstimatedExtinctionDate DATE,
    IN p_Country VARCHAR(255),
    IN p_Region VARCHAR(255),
    IN p_Latitude DECIMAL(10, 6),
    IN p_Longitude DECIMAL(10, 6),
    IN p_ThreatName VARCHAR(255),
    IN p_ThreatDescription TEXT,
    IN p_Severity TINYINT,
    IN p_OrganizationName VARCHAR(255),
    IN p_ProjectDescription TEXT,
    IN p_StartDate DATE,
    IN p_EndDate DATE,
    IN p_Cloclatitude DECIMAL(10, 6),
    IN p_Cloclongitude DECIMAL(10, 6),
    IN p_Cloccountry VARCHAR(255),
    IN p_Clocregion VARCHAR(255),
    IN p_ConservationPark VARCHAR(255)
)
BEGIN
    -- Update or insert into the species table
    INSERT INTO species (ScientificName, CommonName, PopulationSize, Description, EstimatedDateOfExtinction)
    VALUES (p_ScientificName, p_CommonName, p_PopulationSize, p_Description, p_EstimatedExtinctionDate)
    ON DUPLICATE KEY UPDATE
        CommonName = VALUES(CommonName),
        PopulationSize = VALUES(PopulationSize),
        Description = VALUES(Description),
        EstimatedDateOfExtinction = VALUES(EstimatedDateOfExtinction);

    -- Update or insert into the NaturalHabitat table
    INSERT INTO NaturalHabitat (Country, Region, Latitude, Longitude)
    VALUES (p_Country, p_Region, p_Latitude, p_Longitude)
    ON DUPLICATE KEY UPDATE
        Latitude = VALUES(Latitude),
        Longitude = VALUES(Longitude);

    -- Update or insert into the FoundAt table
    CALL UpdateRelationTables(p_ScientificName, p_CommonName, p_Country, p_Region, p_ThreatName, p_OrganizationName, p_Cloccountry, p_Clocregion);
    
    -- Update or insert into the Threats table
    INSERT INTO Threats (ThreatName, Description, Severity)
    VALUES (p_ThreatName, p_ThreatDescription, p_Severity)
    ON DUPLICATE KEY UPDATE
        Description = VALUES(Description),
        Severity = VALUES(Severity);

    -- Update or insert into the ConservationEfforts table
    INSERT INTO ConservationEfforts (OrganizationName, ProjectDescription, StartDate, EndDate)
    VALUES (p_OrganizationName, p_ProjectDescription, p_StartDate, p_EndDate)
    ON DUPLICATE KEY UPDATE
        ProjectDescription = VALUES(ProjectDescription),
        StartDate = VALUES(StartDate),
        EndDate = VALUES(EndDate);

    -- Update or insert into the ConservationLocation table
    INSERT INTO ConservationLocation (Country, Region, Latitude, Longitude, ConservationPark)
    VALUES (p_Cloccountry, p_Clocregion, p_Cloclatitude, p_Cloclongitude, p_ConservationPark)
    ON DUPLICATE KEY UPDATE
        Latitude = VALUES(Latitude),
        Longitude = VALUES(Longitude),
        ConservationPark = VALUES(ConservationPark);

    -- Check if the updated population size is zero and call DeleteSpeciesEntries if true
    IF p_PopulationSize = 0 THEN
        CALL ExtinctSpecies(p_CommonName, p_ScientificName);
    END IF;

END //

DELIMITER ;
