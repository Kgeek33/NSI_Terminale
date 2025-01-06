select distinct A.isbn, e.titre, b.a_id, B.nom, B.prenom, C.a_id, C.nom, c.prenom
from auteur_de A, auteur B,auteur C, auteur_de D, livre E
where a.a_id = B.a_id and a.isbn = d.isbn and c.a_id < a.a_id and c.a_id = d.a_id and a.isbn = e.isbn
order by A.isbn, e.titre, b.a_id, B.nom, B.prenom, C.a_id, C.nom, c.prenom
