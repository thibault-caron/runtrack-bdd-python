USE LaPlateforme;

SELECT COUNT(*) AS nombre_etudiants FROM etudiant
WHERE age < 18;

-- vérification
SELECT * FROM etudiant
WHERE age < 18;