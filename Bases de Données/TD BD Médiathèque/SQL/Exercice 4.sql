-- Question a --
SELECT count(titre) AS "nombre_asterix"
FROM livre
WHERE titre LIKE "%Astérix%";

-- Question b --
SELECT round(avg(annee), 0) AS "parution_moyenne"
FROM livre;

-- Question c --
SELECT max(annee)
FROM livre
WHERE editeur = "Dargaud";

-- Question d --
SELECT min(annee)
FROM livre
JOIN auteur
WHERE auteur.nom = "Uderzo";
