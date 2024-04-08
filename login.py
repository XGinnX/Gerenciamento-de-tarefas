import flet as ft
import sqlite as sql
#Criar tela de login
# 1. Criar Opção pai e filho
# 1.1 - Criar opção de login diferente para cada versão
# 1.1 - Mudar para uma tela chamada Home

def main (pagina):
    title = ft.Text("Página de gerenciamento de tarefas")
    title_home = ft.Text("Pagina Logado com sucesso")
    pagina.add(title)
    
    form_login = ft.Column()
    def entrar_tela(evento):
      
      # Verificando se o usuário está logado com sucesso
      if sql.verificar_usuario(login.value):
          pagina.remove(login, senha, categoria, botao, title)
          pagina.add(title_home)
          pagina.update()
      else:
          mensagem_erro = ft.Text("Erro ao logar")
          pagina.add(mensagem_erro)
        
    login = ft.TextField(
        label="Digite seu e-mail",
        width=350
        )
    senha = ft.TextField(
        label="Digite a sua senha",
        can_reveal_password=True,
        password=True,
        width=350)
    botao = ft.ElevatedButton("Entrar", on_click=entrar_tela)
    categoria = ft.Dropdown(
        label="Categoria",
        width=150,
        options=[
            ft.dropdown.Option("Responsável"),
            ft.dropdown.Option("Filhos"),
        ],
    )
    pagina.add(login,senha,categoria,botao)
   
ft.app(target=main)