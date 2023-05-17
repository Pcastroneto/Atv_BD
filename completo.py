from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribo")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(nome_tribo,num_hab,renda,escolaridade, trab_salar):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO tribo (nome_tribo,num_hab,renda_mensal,escolaridade,trab_salar) VALUES (%s, %s,%s,%s,%s)"
    val = (nome_tribo,num_hab,renda,escolaridade,trab_salar)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()



def deletar(codigo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM tribo WHERE id = %s"
    val = (codigo,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()




# chama a função conectar
conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Deletar uma tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    print("Essas são as tribos que foram inseridas: \n")
    listar(conn, cursor)
  
  elif opcao == 2:
    
    nome_tribo = input("Digite o nome da tribo: ")
    num_hab = int(input("Digite o número de habitantes: "))
    renda = float(input("Digite a randa média mensal da tribo: "))
    escolaridade =input("Digite o nivel de escolaridade(Fundamental, médio ou superior): ")
    trab_salar = input("Possuem trabalho assalariado?(sim ou não): ")
    
    inserir(nome_tribo,num_hab,renda,escolaridade, trab_salar)

  elif opcao == 3:
    
    codigo = int(input("Digite o id da tribo que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()