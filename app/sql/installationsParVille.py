#!/usr/bin/python3
# -*- coding: utf-8 -*-

def installationsParVille():
    return """
    select a.ComLib as "NomCommune",
    a.ComInsee as "NumInsee",
    a.ActLib as 'Activites',
    e.EquNom as 'NomEquipements',
    i.Latitude as 'Latitude',
    i.Longitude as 'Longitude',
    i."Numero de la voie" as "NumVoie",
    i."Nom de la voie" as "Voie",
    i."Nom du lieu dit" as "LieuDit",
    i."Code postal" as "CodePostal"
    from activites a, equipements e, installations i
    where a.ComLib like ?
    """
#