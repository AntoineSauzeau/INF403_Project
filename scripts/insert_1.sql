INSERT INTO Bateaux VALUES ("FYTDMKH8", "Santa Maria");
INSERT INTO Bateaux VALUES ("NDTFMYS2", "Mayflower");
INSERT INTO Bateaux VALUES ("UGDNEIF6", "HMS Victory");
INSERT INTO Bateaux VALUES ("KDNEGHF5", "USS Constitution");

INSERT INTO Entrepots (tailleEntrepot, secteurEntrepot) VALUES (85, "Secteur A");
INSERT INTO Entrepots (tailleEntrepot, secteurEntrepot) VALUES (42, "Secteur B");
INSERT INTO Entrepots (tailleEntrepot, secteurEntrepot) VALUES (150, "Secteur B");
INSERT INTO Entrepots (tailleEntrepot, secteurEntrepot) VALUES (25, "Secteur C");

INSERT INTO Quais (secteurQuai) VALUES ("Secteur A");
INSERT INTO Quais (secteurQuai) VALUES ("Secteur A");
INSERT INTO Quais (secteurQuai) VALUES ("Secteur B");
INSERT INTO Quais (secteurQuai) VALUES ("Secteur C");

INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Stylos", 150);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Roue", 3000);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Classeur", 300);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Lampe torche", 200);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Voiture", 1500);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Ventilateur", 750);
INSERT INTO TypeMarchandises (nomMarchandise, poidsMarchandise) VALUES ("Armoire", 1500);

INSERT INTO Conteneurs (numTypeMarchandise) VALUES (2);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (5);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (1);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (6);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (3);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (6);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (4);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (6);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (2);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (7);
INSERT INTO Conteneurs (numTypeMarchandise) VALUES (1);

INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (1, 4);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (2, 3);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (3, 1);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (4, 2);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (5, 2);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (6, 3);
INSERT INTO StockEntrepots (numConteneur, numEntrepot) VALUES (7, 4);

INSERT INTO Importations (numConteneur, dateArriveeImportation, matriculeBateau, numQuai) VALUES (8, "2022-07-02 14:58:24", "FYTDMKH8", 1);
INSERT INTO Importations (numConteneur, dateArriveeImportation, matriculeBateau, numQuai) VALUES (9, "2022-05-39 05:13:51", "NDTFMYS2", 1);
INSERT INTO Importations (numConteneur, dateArriveeImportation, matriculeBateau, numQuai) VALUES (10, "2022-07-02 14:58:24", "UGDNEIF6", 2);
INSERT INTO Importations (numConteneur, dateArriveeImportation, matriculeBateau, numQuai) VALUES (11,"2022-07-02 14:58:24", "KDNEGHF5", 3);











