-- Running downgrade b9275e825712 -> f2406adf822f

DROP TABLE notas;

UPDATE alembic_version SET version_num='f2406adf822f' WHERE alembic_version.version_num = 'b9275e825712';

-- Running downgrade f2406adf822f -> 223416704ed1

ALTER TABLE pessoa2 DROP COLUMN sexo;

UPDATE alembic_version SET version_num='223416704ed1' WHERE alembic_version.version_num = 'f2406adf822f';

