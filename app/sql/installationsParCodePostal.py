#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A prepared statement that will retrieve information about activities from a zip code
"""
def installationsParCodePostal():
    return """
    SELECT
    s.ComInsee as "N° Insee",
    s.ComLib as "Nom Commune",
    s.ActLib as 'Activité',
    s.EquNom as 'Nom Equipement',
    s."Numero de la voie" as "N° Voie",
    s."Nom de la voie" as "Voie",
    s."Nom du lieu dit" as "Lieu-dit",
    s."Code postal" as "Code Postal",
    s.Latitude as 'Latitude',
    s.Longitude as 'Longitude'
    FROM (
      SELECT *
      FROM equipements e, activites a, installations i
      WHERE a.ComInsee = e.ComInsee
        AND e.ComInsee = i."Code INSEE"
        AND e.InsNumeroInstall = i."Numéro de l'installation"
        AND e.EquipementId = a.EquipementId
    ) s
    WHERE s.ComInsee IN (
      SELECT distinct "Code INSEE" as "CodeInsee"
      FROM installations ins
      WHERE ins."Code postal" LIKE :zip
    );
    """