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
            WHERE nh.Region = "Queensland" AND t.Severity = 3;