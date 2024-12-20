SELECT Nom_Station
FROM Stations
WHERE Capacite >= 200;

SELECT Nom
FROM Clients
WHERE Nom
LIKE "J%"
OR Solde > 10000;

SELECT Nom_Station
FROM Activites
WHERE Libelle = "Plongée";
