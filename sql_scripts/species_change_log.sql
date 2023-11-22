DELIMITER //

CREATE TRIGGER TrackSpeciesDataChanges
AFTER UPDATE ON species
FOR EACH ROW
BEGIN
    DECLARE change_info TEXT;

    -- Check if PopulationSize changed
    IF OLD.PopulationSize <> NEW.PopulationSize THEN
        SET change_info = CONCAT('PopulationSize changed from ', OLD.PopulationSize, ' to ', NEW.PopulationSize);
        INSERT INTO SpeciesChangeLog (ScientificName, CommonName, ChangeInfo, ChangeDateTime)
        VALUES (NEW.ScientificName, NEW.CommonName, change_info, NOW());
    END IF;

    -- Check if EstimatedDateOfExtinction changed
    IF OLD.EstimatedDateOfExtinction <> NEW.EstimatedDateOfExtinction THEN
        SET change_info = CONCAT('EstimatedDateOfExtinction changed from ', OLD.EstimatedDateOfExtinction, ' to ', NEW.EstimatedDateOfExtinction);
        INSERT INTO SpeciesChangeLog (ScientificName, CommonName, ChangeInfo, ChangeDateTime)
        VALUES (NEW.ScientificName, NEW.CommonName, change_info, NOW());
    END IF;

    -- Repeat similar checks for other fields and log changes if needed
END;
//
DELIMITER ;
