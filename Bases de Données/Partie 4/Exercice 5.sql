SELECT count(Station) AS Total
FROM Sejours
WHERE Station = "Victoria";

SELECT avg(Prix) AS prix_moyen_activités_Tanger
FROM Activites
WHERE Nom_Station = "Tanger";