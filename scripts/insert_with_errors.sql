
-- Il y a une clé primaire sur l'attribut matricule, 2 bateaux ne peuvent pas avoir le même matricule, donc le 2e insert déclenche une erreur
INSERT INTO Bateaux VALUES ("FYTDMKH8", "Santa Maria");
INSERT INTO Bateaux VALUES ("FYTDMKH8", "HMS Victory");

-- Il y a une clé étrangère sur l'attribut numTypeMarchandise qui impose que sa valeur soit présente dans la table TypeMarchandises, ce n'est pas le cas ici donc ça déclenche une erreur
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (2);

