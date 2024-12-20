SELECT COUNT(Id_Client) AS total
FROM Sejours
WHERE Station = "Victoria";


SELECT AVG(Prix) AS prix_moyen_activités_Tanger
FROM Activites 
WHERE Nom_Station = "Tanger"