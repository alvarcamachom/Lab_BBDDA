-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
CREATE DATABASE new_database;
-- ddl-end --


-- object: peliculas | type: SCHEMA --
-- DROP SCHEMA IF EXISTS peliculas CASCADE;
CREATE SCHEMA peliculas;
-- ddl-end --
ALTER SCHEMA peliculas OWNER TO postgres;
-- ddl-end --

SET search_path TO pg_catalog,public,peliculas;
-- ddl-end --

-- object: peliculas.personas | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.personas CASCADE;
CREATE TABLE peliculas.personas (
	nombre text,
	nacionalidad text,
	"año_nacimiento" date,
	codigo_personas numeric NOT NULL,
	CONSTRAINT personal_pk PRIMARY KEY (codigo_personas)
);
-- ddl-end --
COMMENT ON COLUMN peliculas.personas.nombre IS E'Nombre de la persona';
-- ddl-end --
COMMENT ON COLUMN peliculas.personas.nacionalidad IS E'Nacionalidad de la persona';
-- ddl-end --
COMMENT ON COLUMN peliculas.personas."año_nacimiento" IS E'Año de nacimiento';
-- ddl-end --
COMMENT ON COLUMN peliculas.personas.codigo_personas IS E'Código de cada persona';
-- ddl-end --
ALTER TABLE peliculas.personas OWNER TO postgres;
-- ddl-end --

-- object: peliculas.peliculas | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.peliculas CASCADE;
CREATE TABLE peliculas.peliculas (
	"año" integer,
	titulo text,
	duracion integer,
	idioma char(2),
	calificacion text,
	codigo_pelicula numeric NOT NULL,
	codigo_director numeric,
	CONSTRAINT peliculas_pk PRIMARY KEY (codigo_pelicula)
);
-- ddl-end --
COMMENT ON COLUMN peliculas.peliculas."año" IS E'Año de la película';
-- ddl-end --
COMMENT ON COLUMN peliculas.peliculas.titulo IS E'Titulo de la película';
-- ddl-end --
COMMENT ON COLUMN peliculas.peliculas.duracion IS E'Duración de la película';
-- ddl-end --
COMMENT ON COLUMN peliculas.peliculas.idioma IS E'Idioma de la película, dos caracteres: ES (Español), EN (Inglés), etc';
-- ddl-end --
COMMENT ON COLUMN peliculas.peliculas.calificacion IS E'Calificación entre 0 y 10 estrellas';
-- ddl-end --
ALTER TABLE peliculas.peliculas OWNER TO postgres;
-- ddl-end --

-- object: peliculas.actua | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.actua CASCADE;
CREATE TABLE peliculas.actua (
	codigo_pelicula_peliculas numeric NOT NULL,
	codigo_personas_personas numeric,
	CONSTRAINT actua_pk PRIMARY KEY (codigo_pelicula_peliculas)
);
-- ddl-end --

-- object: peliculas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.actua DROP CONSTRAINT IF EXISTS peliculas_fk CASCADE;
ALTER TABLE peliculas.actua ADD CONSTRAINT peliculas_fk FOREIGN KEY (codigo_pelicula_peliculas)
REFERENCES peliculas.peliculas (codigo_pelicula) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: peliculas.generos | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.generos CASCADE;
CREATE TABLE peliculas.generos (
	genero text NOT NULL,
	codigo_pelicula_peliculas numeric NOT NULL,
	CONSTRAINT generos_pk PRIMARY KEY (genero,codigo_pelicula_peliculas)
);
-- ddl-end --
COMMENT ON COLUMN peliculas.generos.genero IS E'Género de la película';
-- ddl-end --
ALTER TABLE peliculas.generos OWNER TO postgres;
-- ddl-end --

-- object: peliculas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.generos DROP CONSTRAINT IF EXISTS peliculas_fk CASCADE;
ALTER TABLE peliculas.generos ADD CONSTRAINT peliculas_fk FOREIGN KEY (codigo_pelicula_peliculas)
REFERENCES peliculas.peliculas (codigo_pelicula) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: peliculas.criticas | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.criticas CASCADE;
CREATE TABLE peliculas.criticas (
	puntuacion integer,
	texto text,
	fecha date NOT NULL,
	codigo_pelicula_peliculas numeric NOT NULL,
	codigo_personas_personas numeric NOT NULL,
	CONSTRAINT criticas_pk PRIMARY KEY (fecha,codigo_pelicula_peliculas,codigo_personas_personas)
);
-- ddl-end --
COMMENT ON COLUMN peliculas.criticas.puntuacion IS E'Puntuación de la película de 0 a 10';
-- ddl-end --
COMMENT ON COLUMN peliculas.criticas.texto IS E'Texto de la crítica';
-- ddl-end --
COMMENT ON COLUMN peliculas.criticas.fecha IS E'Fecha de la crítica';
-- ddl-end --
ALTER TABLE peliculas.criticas OWNER TO postgres;
-- ddl-end --

-- object: personas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.actua DROP CONSTRAINT IF EXISTS personas_fk CASCADE;
ALTER TABLE peliculas.actua ADD CONSTRAINT personas_fk FOREIGN KEY (codigo_personas_personas)
REFERENCES peliculas.personas (codigo_personas) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: personas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.peliculas DROP CONSTRAINT IF EXISTS personas_fk CASCADE;
ALTER TABLE peliculas.peliculas ADD CONSTRAINT personas_fk FOREIGN KEY (codigo_director)
REFERENCES peliculas.personas (codigo_personas) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: peliculas.visualizaciones | type: TABLE --
-- DROP TABLE IF EXISTS peliculas.visualizaciones CASCADE;
CREATE TABLE peliculas.visualizaciones (
	fecha date,
	codigo_personas_personas numeric,
	codigo_pelicula_peliculas numeric

);
-- ddl-end --
COMMENT ON COLUMN peliculas.visualizaciones.fecha IS E'Fecha de la visualización de la película';
-- ddl-end --
ALTER TABLE peliculas.visualizaciones OWNER TO postgres;
-- ddl-end --

-- object: personas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.visualizaciones DROP CONSTRAINT IF EXISTS personas_fk CASCADE;
ALTER TABLE peliculas.visualizaciones ADD CONSTRAINT personas_fk FOREIGN KEY (codigo_personas_personas)
REFERENCES peliculas.personas (codigo_personas) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: peliculas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.visualizaciones DROP CONSTRAINT IF EXISTS peliculas_fk CASCADE;
ALTER TABLE peliculas.visualizaciones ADD CONSTRAINT peliculas_fk FOREIGN KEY (codigo_pelicula_peliculas)
REFERENCES peliculas.peliculas (codigo_pelicula) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: peliculas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.criticas DROP CONSTRAINT IF EXISTS peliculas_fk CASCADE;
ALTER TABLE peliculas.criticas ADD CONSTRAINT peliculas_fk FOREIGN KEY (codigo_pelicula_peliculas)
REFERENCES peliculas.peliculas (codigo_pelicula) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --

-- object: personas_fk | type: CONSTRAINT --
-- ALTER TABLE peliculas.criticas DROP CONSTRAINT IF EXISTS personas_fk CASCADE;
ALTER TABLE peliculas.criticas ADD CONSTRAINT personas_fk FOREIGN KEY (codigo_personas_personas)
REFERENCES peliculas.personas (codigo_personas) MATCH FULL
ON DELETE RESTRICT ON UPDATE RESTRICT;
-- ddl-end --


