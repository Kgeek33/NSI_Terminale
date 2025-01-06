-- Question a --
SELECT DISTINCT usager.nom, usager.prenom
FROM livre
JOIN emprunt 
JOIN usager ON emprunt.code_barre = usager.code_barre;

-- Question b --
SELECT DISTINCT usager.nom, usager.prenom
FROM livre
JOIN emprunt
JOIN usager ON emprunt.code_barre = usager.code_barre
ORDER BY retour DESC;

-- Question c --
SELECT titre
FROM livre
WHERE livre.annee < (
SELECT annee
FROM livre
WHERE titre = "Dune"
);

-- Question d --
SELECT DISTINCT auteur.nom, auteur.prenom
FROM livre
JOIN auteur
JOIN auteur_de ON livre.isbn = auteur_de.isbn AND auteur.a_id = auteur_de.a_id
WHERE livre.annee < (
	SELECT annee
	FROM livre
	WHERE titre = "Dune"
)

-- Question e --
SELECT DISTINCT count(auteur.nom), count(auteur.prenom)
FROM livre
JOIN auteur
JOIN auteur_de ON livre.isbn = auteur_de.isbn AND auteur.a_id = auteur_de.a_id
WHERE livre.annee < (
	SELECT annee
	FROM livre
	WHERE titre = "Dune"
);
