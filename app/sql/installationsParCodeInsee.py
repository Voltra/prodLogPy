#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A prepared statement for optimization purpose, retrieves 'installations' based upon a 'ComInsee'
"""
def installationsParCodeInsee():
    return """
    SELECT s.ComInsee as "N° Insee",
    s.ComLib as "Nom Commune",
    s.ActLib as 'Activité',
    s.EquNom as 'Nom Equipement',
    s."Numero de la voie" as "N° de Voie",
    s."Nom de la voie" as "Voie",
    s."Nom du lieu dit" as "Lieu-Dit",
    s."Code postal" as "Code Postal",
    s.Latitude as 'Latitude',
    s.Longitude as 'Longitude'
    FROM (
      SELECT *
      FROM activites a, equipements e, installations i
      WHERE a.ComInsee = e.ComInsee
      AND e.ComInsee = i."Code INSEE"
      AND a.EquipementId = e.EquipementId
      AND e.InsNumeroInstall = i."Numéro de l'installation"
    ) s
    where s.ComInsee LIKE :insee;
    """
#