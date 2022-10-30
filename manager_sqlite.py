import pandas as pd
import sqlite3

class BancoDeDados():
    nome_bd: str
    nome_csv: str

    def criar_db(self):
        df = pd.read_csv(f"resources/{self.nome_csv}.csv", sep=';')
        conn = sqlite3.connect(f"{self.nome_bd}.db")
        df.to_sql("flashcards", conn, if_exists='replace', index=False)
    
    def add_palavra_bd(self, palavra, traducao):
        # query para só adicionar se não existir
        query = f"""INSERT INTO flashcards (palavra, traducao)
                          SELECT '{palavra}', '{traducao}'
                          WHERE NOT EXISTS (SELECT * FROM flashcards WHERE palavra = '{palavra}' and traducao = '{traducao}')"""

        conn = sqlite3.connect(f"{self.nome_bd}.db")
        c = conn.cursor()    
        c.execute(query)
        conn.commit()
        c.close()


if __name__ == "__main__":
    bd = BancoDeDados(nome_bd = "alemao", nome_csv = "palavras_alemao")
    bd.criar_db()