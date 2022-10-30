from dataclasses import dataclass
import random
import sqlite3
import manager_sqlite

@dataclass
class Flashcard:
    palavra: str
    traducao: str

    def get_traducoes(self):
        traducoes = self.traducao.split("/")
        return traducoes

    def __str__(self):
        return f"{self.palavra} = {self.traducao}"

@dataclass
class FlashcardJogo:
    acertos: int = 0
    erros: int = 0

    def main(self, categoria):
        while True:
            print("========= MENU ============ \n1 - começar partida\n2 - adicionar palavra ao banco de dados\n3 - sair")
            resposta = int(input("Opção: "))
            if resposta == 1:
                self.comecar_partida()
            elif resposta == 2:
                self.adicionar_palavra(categoria)
            elif resposta == 3:
                break
            else:
                print("Opção inválida")

    
    def comecar_partida(self, categoria):
        print("COMEÇANDO PARTIDA")
        while True:
            palavra = self.get_flashcard_random(categoria)
            card = Flashcard(palavra = palavra[0], traducao=palavra[1])
            print("\nSe desejar sair, digite 'SAIR!' ou '0'")
            print (f"A palavra é: {card.palavra}")
            resposta = input("Resposta: ")
            if resposta.upper() == "SAIR!" or resposta == "0":
                break
            print(self.checar_respostas(card, resposta))

        print(f"FIM DE JOGO! Você acertou {self.acertos} de um total de {self.acertos+self.erros}.\n")

    def checar_respostas(self, flashcard: Flashcard, resposta: str):
        for traducao in (traducoes:=flashcard.get_traducoes()):
            if resposta.strip().lower() == traducao.split('(')[0].strip().lower():
                self.acertos += 1
                if len(flashcard.get_traducoes())>1:
                    return f"Parabéns, você acertou! Outras traduções incluem: {'/'.join(t for t in traducoes if not t==traducao)}"
                return "Parabéns, você acertou!"
        self.erros += 1
        return f"Errado! A resposta é {flashcard.traducao}"

    @staticmethod
    def adicionar_palavra(categoria):
        palavra = input("Qual a palavra? ").strip()
        traducao = input("E a tradução? ").strip()
        
        manager_sqlite.BancoDeDados(nome_bd=categoria).add_palavra_bd(palavra, traducao)
        print(f"\nPalavra '{palavra}' adicionada ao BD com traducao '{traducao}'\n")

    @staticmethod
    def get_flashcard_random(categoria):
        conn = sqlite3.connect(f'{categoria}.db')
        c = conn.cursor()
        return random.choice(c.execute('''SELECT * FROM flashcards''').fetchall())


jogo = FlashcardJogo()
jogo.main(categoria = "alemao")
