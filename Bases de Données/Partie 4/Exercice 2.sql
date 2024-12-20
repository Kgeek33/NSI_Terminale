SELECT Nom_Station, Lieu, stations.Region, Clients.nom, Stations.Tarif * Sejours.Nb_Places
FROM  Clients
JOIN Sejours on Sejours.Id_Client = Clients.Id
JOIN Stations on Nom_Station = Sejours.Station
ORDER BY Stations.Tarif * Sejours.Nb_Places