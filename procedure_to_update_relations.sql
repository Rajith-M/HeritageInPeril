DELIMITER //

CREATE PROCEDURE UpdateRelationTables (
    IN p_ScientificName VARCHAR(255),
    IN p_CommonName VARCHAR(255),
    IN p_Country VARCHAR(255),
    IN p_Region VARCHAR(255),
    IN p_ThreatName VARCHAR(255),
    IN p_OrganizationName VARCHAR(255),
    IN p_ConservationLocationCountry VARCHAR(255),
    IN p_ConservationLocationRegion VARCHAR(255)
)
BEGIN
    -- Update FoundAt table if the entry doesn't already exist
    IF NOT EXISTS (
        SELECT 1 FROM FoundAt
        WHERE NaturalHabitatCountry = p_Country
        AND NaturalHabitatRegion = p_Region
        AND SpeciesScientificName = p_ScientificName
    ) THEN
        INSERT INTO FoundAt (NaturalHabitatCountry, NaturalHabitatRegion, SpeciesScientificName)
        VALUES (p_Country, p_Region, p_ScientificName);
    END IF;

    -- Update ThreatenedBy table if the entry doesn't already exist
    IF NOT EXISTS (
        SELECT 1 FROM ThreatenedBy
        WHERE SpeciesScientificName = p_ScientificName
        AND ThreatName = p_ThreatName
    ) THEN
        INSERT INTO ThreatenedBy (SpeciesScientificName, ThreatName)
        VALUES (p_ScientificName, p_ThreatName);
    END IF;

    -- Update ConservedAt table if the entry doesn't already exist
    IF NOT EXISTS (
        SELECT 1 FROM ConservedAt
        WHERE OrganizationName = p_OrganizationName
        AND ConservationLocationCountry = p_ConservationLocationCountry
        AND ConservationLocationRegion = p_ConservationLocationRegion
    ) THEN
        INSERT INTO ConservedAt (OrganizationName, ConservationLocationCountry, ConservationLocationRegion)
        VALUES (p_OrganizationName, p_ConservationLocationCountry, p_ConservationLocationRegion);
    END IF;

    -- Update ConservedBy table if the entry doesn't already exist
    IF NOT EXISTS (
        SELECT 1 FROM ConservedBy
        WHERE OrganizationName = p_OrganizationName
        AND SpeciesScientificName = p_ScientificName
    ) THEN
        INSERT INTO ConservedBy (OrganizationName, SpeciesScientificName)
        VALUES (p_OrganizationName, p_ScientificName);
    END IF;
END //

DELIMITER ;
