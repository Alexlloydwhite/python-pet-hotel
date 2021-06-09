CREATE TABLE pets(
  "id" SERIAL PRIMARY KEY,
  "owner_id" INT REFERENCES "owner",
  "name" VARCHAR (250) NOT NULL,
  "breed" VARCHAR (100) NOT NULL,
  "color" VARCHAR (15) NOT NULL,
  "checked_in" BOOLEAN DEFAULT FALSE,
  "checked_in_date" DATE
);

CREATE TABLE "owner"(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR (100) NOT NULL
);

INSERT INTO "owner" ("name") VALUES ('Chloe'), ('Eyram'), ('Alex'), ('Christian');

SELECT * FROM "owner";

SELECT * FROM "pets";

INSERT INTO pets ("owner_id", "name", "breed", "color", "checked_in") VALUES 
(1, 'Russel', 'Naked Mole Rat', 'Pink', 'true'),
(4, 'Mark', 'Hamster', 'Maroon', 'true'),
(1, 'Bruno', 'Frenchie', 'Black', 'false'),
(2, 'Finley', 'Aussie Doodle', 'Black', 'true'),
(3, 'Venga Boi', 'Kitty', 'Brown', 'true'),
(4, 'Ellen', 'Parrot', 'Green', 'true');

SELECT COUNT(*) FROM pets p