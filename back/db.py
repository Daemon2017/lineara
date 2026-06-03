import json
import re

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

with open('config.json', 'r') as f:
    config = json.load(f)

db_url = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
engine = create_engine(db_url, pool_pre_ping=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def stop_pool():
    engine.dispose()
    print("PostgreSQL pool closed.")


def search_eurasiatic_cognate(minoan_variant):
    if not minoan_variant:
        return []
    cleaned_word = minoan_variant \
        .replace("ʰ", "") \
        .replace("̥", "") \
        .strip()
    cleaned_word = re.sub(r'[uo]', 'U', cleaned_word)
    cleaned_word = re.sub(r'[ei]', 'I', cleaned_word)
    cleaned_word = re.sub(r'[a]', 'A', cleaned_word)
    with Session() as session:
        query = text(
            """
            SELECT DISTINCT 
                eurasiatic, 
                eurasiatic_meaning, 
                indoeuropean, 
                indoeuropean_meaning, 
                altaic, 
                altaic_meaning
            FROM dictionary
            WHERE variant = :variant
            """
        )
        result = session.execute(query, {"variant": cleaned_word})
        return [dict(row._mapping) for row in result]
