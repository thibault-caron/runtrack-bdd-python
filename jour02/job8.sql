CREATE TABLE `cage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_animaux` int DEFAULT '0',
  `superficie` int NOT NULL,
  `capacite` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `cage_chk_1` CHECK ((`capacite` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `race` varchar(50) NOT NULL,
  `cage_id` int DEFAULT NULL,
  `date_de_naissance` date NOT NULL,
  `pays_origine` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_animal_cage` (`cage_id`),
  CONSTRAINT `fk_animal_cage` FOREIGN KEY (`cage_id`) REFERENCES `cage` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `animal` 
  VALUES 
  (1,'Dumbo','Elephant',1,'2002-10-07','Kenya'),
  (2,'Lady','Elephant',1,'1999-12-11','Tanzania'),
  (3,'Tarzan','Gorilla',3,'2008-08-08','Paraguay'),
  (4,'Jeanne','Gorilla',3,'2014-10-10','Paraguay'),
  (5,'Speed','Macaque',3,'2000-12-11','Japan'),
  (6,'Cool','Macaque',3,'2002-10-10','China'),
  (7,'Rafiki','Gibons',3,'1997-08-04','Kenya'),
  (8,'Goldie','Gibons',3,'1996-12-10','Kenya');