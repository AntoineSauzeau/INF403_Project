DROP TABLE IF EXISTS Conteneurs;
DROP TABLE IF EXISTS TypeMarchandises;
DROP TABLE IF EXISTS Bateaux;
DROP TABLE IF EXISTS Entrepots;
DROP TABLE IF EXISTS StockEntrepots;
DROP TABLE IF EXISTS Importations;
DROP TABLE IF EXISTS Quais;


-- Conteneurs (numConteneur, numTypeMarchandise)
CREATE TABLE Conteneurs (
    numConteneur INTEGER PRIMARY KEY AUTOINCREMENT,
    numTypeMarchandise INTEGER NOT NULL,

    FOREIGN KEY (numTypeMarchandise) REFERENCES TypeMarchandises (numTypeMarchandise)
);

-- TypeMarchandises (numTypeMarchandise, nomMarchandise, poidsMarchandise)
CREATE TABLE TypeMarchandises (
    numTypeMarchandise INTEGER PRIMARY KEY AUTOINCREMENT,
    nomMarchandise TEXT NOT NULL,
    poidsMarchandise INTEGER NOT NULL
);

-- Bateaux (matriculeBateau, nomBateau)
CREATE TABLE Bateaux (
    matriculeBateau TEXT PRIMARY KEY,
    nomBateau TEXT NOT NULL
);

-- Entrepots (numEntrepot, tailleEntrepot, secteurEntrepot)
CREATE TABLE Entrepots (
    numEntrepot INTEGER PRIMARY KEY AUTOINCREMENT,
    tailleEntrepot INTEGER NOT NULL,
    secteurEntrepot TEXT NOT NULL
);

-- StockEntrepots (numEntrepot, numConteneur)
CREATE TABLE StockEntrepots (
    numStock INTEGER PRIMARY KEY AUTOINCREMENT,
    numConteneur INTEGER UNIQUE NOT NULL,
    numEntrepot INTEGER NOT NULL,

    FOREIGN KEY (numEntrepot) REFERENCES Entrepots (numEntrepot),
    FOREIGN KEY (numConteneur) REFERENCES Conteneurs (numConteneur)
);

-- Importations (numConteneur, dateArriveeImportation, matriculeBateau, numQuai)
CREATE TABLE Importations (
    numImportation INTEGER PRIMARY KEY AUTOINCREMENT,
    numConteneur INTEGER UNIQUE NOT NULL,
    dateArriveeImportation TEXT NOT NULL,
    matriculeBateau INTEGER NOT NULL,
    numQuai INTEGER NOT NULL,

    FOREIGN KEY (numConteneur) REFERENCES Conteneurs (numConteneur),
    FOREIGN KEY (matriculeBateau) REFERENCES Bateaux (matriculeBateau),
    FOREIGN KEY (numQuai) REFERENCES Quais (numQuai)
);

-- Quais (numQuai, secteurQuai)
CREATE TABLE Quais (
    numQuai INTEGER PRIMARY KEY AUTOINCREMENT,
    secteurQuai TEXT NOT NULL
);