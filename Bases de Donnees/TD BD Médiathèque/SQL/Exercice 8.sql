SELECT DISTINCT A.isbn, e.titre, b.a_id, B.nom, B.prenom, C.a_id, C.nom, c.prenom
FROM auteur_de A, auteur B,auteur C, auteur_de D, livre E
WHERE a.a_id = B.a_id AND a.isbn = d.isbn AND c.a_id < a.a_id AND c.a_id = d.a_id AND a.isbn = e.isbn
ORDER BY A.isbn, e.titre, b.a_id, B.nom, B.prenom, C.a_id, C.nom, c.prenom
