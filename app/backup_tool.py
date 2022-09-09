from sqlalchemy import create_engine, select
from models import db as Base
import os
import sys

target_filename = "database.sqlite"
target_isfile = True
current_version = "1"
TRAGET_DB_URI = 'sqlite:///database.sqlite'
SOURCE_DB_URI = 'postgresql://xkzpsbhiivbdsp:2e1dc35aba1f3297ee82834be5d60f0f06630095d486417aaba15e3cbfd7e4d2@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d3gdpfgq4vt2c5'

if target_isfile and os.path.isfile(target_filename):
    print("Same file found.")
    if input("Continue? [Y/n]").lower() == "n":
        print("Exiting backup tool! Reconsider target filename.")
        exit()
    os.remove(target_filename)
    print("Previous version has been deleted, current_version is v."+current_version)

engine_lite = create_engine(TRAGET_DB_URI)
engine_cloud = create_engine(SOURCE_DB_URI)
table_list = sorted(list(Base.metadata.tables.keys()))
ind = 0

print("Connecting the target and source databases", end=" ")
sys.stdout.flush()

try:
    with engine_lite.connect() as conn_lite:
        with engine_cloud.connect() as conn_cloud:
            print("✅")
            print("Creating the tables fetched from the schema", end=" ")
            sys.stdout.flush()
            try:
                Base.metadata.create_all(engine_lite)
                print("✅")
                print("-"*20)
            except Exception as e:
                print("ERROR ON CREATING TABLES")
                print("-"*20)
                print(e)
            for table in Base.metadata.sorted_tables:
                print("backing up table - "+table_list[ind], end=" ")
                sys.stdout.flush()
                try:
                    data = [dict(row)
                            for row in conn_cloud.execute(select(table.c))]
                    print(len(data), "rows", end=" ")
                    if len(data) > 0:
                        conn_lite.execute(table.insert().values(data))
                    print("✅")
                except Exception as e:
                    print("FACED ERROR !!!  on table "+table_list[ind])
                    print("-"*20)
                    print(e)
                ind += 1
except Exception as e:
    print(e)
