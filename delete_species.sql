DELIMITER //

CREATE PROCEDURE DeleteSpeciesEntries (
    IN p_CommonName VARCHAR(255),
    IN p_ScientificName VARCHAR(255)
)
BEGIN
    -- Delete entries from FoundAt table for the specified species
    DELETE FROM FoundAt 
    WHERE SpeciesScientificName = p_ScientificName;

    -- Delete entries from ConservedAt table for the specified species
    DELETE FROM ConservedAt 
    WHERE OrganizationName IN (
        SELECT OrganizationName FROM ConservedBy 
        WHERE SpeciesScientificName = p_ScientificName
    );

    -- Delete entries from ConservedBy table for the specified species
    DELETE FROM ConservedBy 
    WHERE SpeciesScientificName = p_ScientificName;

    -- Delete entries from ThreatenedBy table for the specified species
    DELETE FROM ThreatenedBy 
    WHERE SpeciesScientificName = p_ScientificName;

    -- Insert the deleted species into the deletedSpecies table
    INSERT INTO deletedSpecies(ScientificName, CommonName)
    SELECT ScientificName, CommonName FROM Species WHERE ScientificName = p_ScientificName;

    -- Delete the specified species from the Species table
    DELETE FROM Species 
    WHERE ScientificName = p_ScientificName;
END //

DELIMITER ;
