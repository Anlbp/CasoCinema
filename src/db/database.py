import sqlite3
import os
 
DB_PATH = "cinema.db"
 
 
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
 
 
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
 
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS cinema (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nome    TEXT    NOT NULL,
            cidade  TEXT    NOT NULL,
            estado  TEXT    NOT NULL,
            endereco TEXT   NOT NULL,
            capacidade INTEGER NOT NULL
        );
 
        CREATE TABLE IF NOT EXISTS filme (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT    NOT NULL,
            duracao_min INTEGER NOT NULL,
            genero      TEXT    NOT NULL,
            diretor     TEXT    NOT NULL,
            elenco      TEXT
        );
 
        CREATE TABLE IF NOT EXISTS sessao (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id  INTEGER NOT NULL REFERENCES cinema(id),
            filme_id   INTEGER NOT NULL REFERENCES filme(id),
            data_hora  TEXT    NOT NULL,
            sala       TEXT    NOT NULL
        );
 
        CREATE TABLE IF NOT EXISTS registro_publico (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            sessao_id INTEGER NOT NULL REFERENCES sessao(id),
            data      TEXT    NOT NULL,
            publico   INTEGER NOT NULL CHECK(publico >= 0)
        );
    """)
 
    conn.commit()
    conn.close()
    print("Banco de dados iniciado.")
 
 
if __name__ == "__main__":
    init_db()
 
