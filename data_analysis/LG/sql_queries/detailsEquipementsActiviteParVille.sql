select a.ComLib as "Nom Commune",
a.ComInsee as "N° INSEE",
a.ActLib as 'Activités',
e.EquNom as 'Nom Équipements',
i.Latitude as 'Latitude',
i.Longitude as 'Longitude',
i."Numero de la voie" as "N° voie",
i."Nom de la voie" as "Voie",
i."Nom du lieu dit" as "Lieu-dit",
i."Code postal" as "Code Postal"
from activites a, equipements e, installations i
where a.ComLib like 'Orvault'
      AND e.InsNumeroInstall = i."Numéro de l'installation"
      AND a.ComInsee = e.ComInsee
      AND e.ComInsee = i."Code INSEE";

/*
Renseigne:
- Nom de l'activité partiquable
- Nom de l'équipements
- Latitude
- Longitude
- N° de voirie
- Nom de la voirie
- Nom du lieu dit
- Code Postal
*/