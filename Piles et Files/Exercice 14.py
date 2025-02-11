from random import choice
from une_file_avec_une_liste_chainée_TBC import File

T_ALIM_MIN = 7
TPS_CTS = [4, 6, 8, 12]
NB_TYPES = len(TPS_CTS)


def simuler(duree_h: int) -> str:
    """
    prend en parametre la duree en heures, duree_h
    d'alimentation en pièces du poste de ctl
    """
    tmps_minutes = 0
    duree_minutes = duree_h * 60
    en_attente = File()  # file d'attente des pièces
    tps_restant_en_ctl = 0  # temps restant à contrôler la pièce
    tps_total_en_ctl = 0  # temps total passé à contrôler
    tps_continu_en_ctl = 0
    nb_pieces_controlees = 0

    en_attente.ajouter(choice(TPS_CTS))
    tps_restant_en_ctl = en_attente.tete.valeur()

    while tmps_minutes < duree_minutes or not en_attente.est_vide():
        # if duree_minutes % 240 == 0:
        #     duree_minutes -= 15
        #     continue

        if tmps_minutes % T_ALIM_MIN == 0:
            en_attente.ajouter(choice(TPS_CTS))
            if len(en_attente) == 1:
                tps_restant_en_ctl = en_attente.tete.valeur()

        if tps_restant_en_ctl == 0:
            tps_continu_en_ctl += en_attente.retirer()
            nb_pieces_controlees += 1
            if not en_attente.est_vide():
                tps_restant_en_ctl = en_attente.tete.valeur()

        print(
            f"time ={tmps_minutes // 60}:{tmps_minutes % 60},"
            f"tps_restant_ctl = {tps_restant_en_ctl} et "
            f"durées successives des pièces en attente : {en_attente}"
            f"pour {len(en_attente)} pièce{"s" if len(en_attente) > 1 else ""}"
        )
        tmps_minutes += 1
        tps_total_en_ctl += 1
        tps_restant_en_ctl -= 1
        duree_minutes -= 1

    return (
        "\n"
        f"C'est la fin !\n"
        "La durée de séjour moyenne des pièces dans le poste de contrôle"
        f"a été de {round(tps_continu_en_ctl / nb_pieces_controlees, 2)}"
        "minutes"
    )


# print(simuler(1))
print(simuler(80))
