-- Question a --
SELECT livre.titre, emprunt.isbn
FROM emprunt
JOIN livre
WHERE livre.isbn = emprunt.isbn;

-- Question b --
SELECT livre.titre, emprunt.retour
FROM emprunt
JOIN livre
WHERE livre.isbn = emprunt.isbn AND emprunt.retour <= date("2020-02-01");

-- Question c --
SELECT livre.titre, emprunt.retour, usager.nom, usager.prenom
FROM emprunt
JOIN livre
JOIN usager
WHERE livre.isbn = emprunt.isbn AND emprunt.retour <= date("2020-02-01");--c normal que ce soit pareil ici qu'à la b (Flo)--
