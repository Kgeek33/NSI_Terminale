-- Question a --
SELECT DISTINCT nom
FROM usager;

-- Question b --
SELECT isbn, retour
FROM emprunt
WHERE retour <= date("2020-02-01");

-- Question c --
SELECT nom
FROM auteur
ORDER BY nom;

-- Question d --
SELECT nom
FROM usager
WHERE cp = "75012" OR cp = "75013";

-- Question e --
SELECT nom, adresse
FROM usager
WHERE adresse NOT like "%rue%";
