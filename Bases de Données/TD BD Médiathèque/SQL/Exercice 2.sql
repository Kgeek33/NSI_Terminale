-- Question a --
SELECT *
FROM livre
WHERE annee >= 2000;

-- Question b --
SELECT titre
FROM livre
WHERE annee >= 1990
ORDER BY annee;

-- Question c --
SELECT titre
FROM livre
WHERE editeur = "Dargaud"
AND annee >= 1970
AND annee <= 1980;

-- Question d --
SELECT titre
FROM livre
WHERE titre LIKE "%Astérix%"
ORDER BY titre;

-- Question e --
SELECT titre AS "le titre", isbn AS "numéro isbn"
FROM livre
WHERE annee >= 2000;

-- Question f --
SELECT DISTINCT editeur
FROM livre
ORDER BY editeur;
