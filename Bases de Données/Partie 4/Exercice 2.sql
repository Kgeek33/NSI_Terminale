SELECT Nom,Sejours.Station,Stations.Lieu,Stations.Region,Stations.Tarif
FROM Sejours JOIN Clients ON Id_Client = Id
JOIN Stations ON Sejours.Station = Nom_Station
ORDER BY Stations.Tarif*Sejours.Nb_Places