SELECT Nom
FROM Clients
JOIN Sejours
ON Id = Id_Client
WHERE Station = "La Bourboule";

SELECT DISTINCT Station
FROM Sejours
JOIN Clients
ON Id = Id_Client
WHERE Region = "Europe";
