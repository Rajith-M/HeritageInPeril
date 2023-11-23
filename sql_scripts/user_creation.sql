CREATE ROLE "Explorer";
CREATE ROLE "Collaborator";
GRANT SELECT, INSERT, UPDATE, DELETE ON heritage_in_peril.* TO "Collaborator";
GRANT SELECT ON heritage_in_peril.* TO "Explorer";