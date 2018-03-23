#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A prepared statement that will retrieve information about activities from a zip code
"""
def installationsParCodePostal():
    return """
    SELECT
    a.ComInsee as "NumInsee",
    a.ComLib as "NomCommune",
    a.ActLib as 'Activites',
    e.EquNom as 'NomEquipements',
    i.Latitude as 'Latitude',
    i.Longitude as 'Longitude',
    i."Numero de la voie" as "NumVoie",
    i."Nom de la voie" as "Voie",
    i."Nom du lieu dit" as "LieuDit",
    i."Code postal" as "CodePostal"
    FROM activites a, installations i, equipements e
    WHERE a.ComInsee IN (
      SELECT distinct "Code INSEE" as "CodeInsee"
      FROM installations i
      WHERE i."Code postal" LIKE ?
    )
    """