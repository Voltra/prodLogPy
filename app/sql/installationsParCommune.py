#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A prepared statement for optimization purpose, retrieves 'installations' based upon a 'ComInsee'
"""
def installationParCommune():
    return """
    SELECT
    s.ComInsee as "N° Insee",
    s.ComLib as "Nom Commune",
    s.ActLib as 'Activité',
    s.EquNom as 'Nom Équipement',
    s.Latitude as 'Latitude',
    s.Longitude as 'Longitude',
    s."Numero de la voie" as "N° Voie",
    s."Nom de la voie" as "Voie",
    s."Nom du lieu dit" as "Lieu-dit",
    s."Code postal" as "Code Postal"
    FROM (
      SELECT *
      FROM equipements e, activites a, installations i
      WHERE a.ComLib = e.ComLib
        AND e.ComInsee = i."Code INSEE"
        AND e.InsNumeroInstall = i."Numéro de l'installation"
        AND e.EquipementId = a.EquipementId
    ) s
    WHERE s.ComInsee IN (
      SELECT distinct "Code INSEE" as "CodeInsee"
      FROM installations ins
      WHERE ins."Nom de la commune" LIKE :commune
    );
    
    """
#