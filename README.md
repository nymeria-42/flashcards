# Flashcards
Aplicação desenvolvida com o objetivo de facilitar o aprendizado de termos ou palavras. Pode ser gerada com qualquer arquivo csv contendo uma palavra e sua tradução. O exemplo criado a partir do arquivo disponibilizado em resources é para aprendizado e treinamento de palavras em alemão. Para flashcards relacionados a outras categorias, basta gerar um arquivo csv no mesmo formato e modificar os nomes da categoria em main e nome_csv e nome_bd em manager_sqlite.

Necessário SQLite instalado na máquina. Para instalar no ubuntu: `sudo apt install sqlite3`

## Para criar banco de dados sqlite:
Rodar `manager_sqlite.py`. Ele usa o arquivo csv armazenado em resources como padrão para inicializar a base da dados. Cuidado ao rodar esse comando pois ele substitui o banco de dados existente e cria um novo.

## Para rodar a aplicação:
Rodar `main.py`. O menu oferece a opção de começar uma partida ou adicionar palavras ao banco de dados. 
