from sqlalchemy import create_engine, MetaData, Table, select

metadata = MetaData()

# t = sa.Table(
#     'comments',
#     metadata,
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(), nullable=False),
#     sa.Column('comment', sa.String(), nullable=False),
#     sa.Column('live', sa.String(), nullable=False),
#     sa.Column('created_at', sa.DateTime(), nullable=True),
#     sa.PrimaryKeyConstraint('id'),
# )

engine = create_engine('sqlite:///database.db')

metadata.create_all(engine)

t = Table('comments', metadata, autoload_with=engine)

sql = select(t)
print(sql)


# with engine.connect() as con:
#     with con.begin():
#         con.execute(
#             sa.text(
#                 f"""
#                 insert into comments (name, comment, live, created_at)
#                 values ('dunossauro', 'alow', 'youtube', '2024-01-10 12:50:47.35297');
#                 """
#             )
#         )

#     with con.begin():
#         result = con.execute(sa.text('select * from comments'))
#         print(result.fetchall())