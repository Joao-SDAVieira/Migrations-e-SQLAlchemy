CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> c358c987ac4e

CREATE TABLE pessoa (
    id INTEGER NOT NULL, 
    nome VARCHAR(50) NOT NULL, 
    email VARCHAR(50) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('c358c987ac4e');

