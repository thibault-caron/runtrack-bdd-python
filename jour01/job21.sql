USE `LaPlateforme`;

SELECT COUNT(*) AS `nombre_etudiants` FROM `etudiant`
WHERE `age` BETWEEN 18 AND 25;

-- vérification
SELECT * FROM `etudiant`
WHERE `age` BETWEEN 18 AND 25;