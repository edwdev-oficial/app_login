# import streamlit as st
# import json
# import hashlib
# import os

# # Funções auxiliares
# def carregar_dados():
#     with open("usuarios.json", "r") as f:
#         return json.load(f)

# def salvar_dados(dados):
#     with open("usuarios.json", "w") as f:
#         json.dump(dados, f, indent=4)

# def hash_senha(senha):
#     return hashlib.sha256(senha.encode()).hexdigest()

# # Interface
# st.title("Minha aplicação com login")

# dados = carregar_dados()
# pagina = st.sidebar.selectbox("Acesso", ["Login", "Cadastro"])

# if pagina == "Cadastro":
#     st.subheader("Criar nova conta")
#     email = st.text_input("Email")
#     nome = st.text_input("Nome")
#     senha = st.text_input("Senha", type="password")
#     confirmar = st.text_input("Confirmar senha", type="password")

#     if st.button("Cadastrar"):
#         if email not in dados["autorizados"]:
#             st.error("Email não autorizado para cadastro.")
#         elif email in dados["usuarios"]:
#             st.warning("Este email já está cadastrado.")
#         elif senha != confirmar:
#             st.warning("As senhas não coincidem.")
#         else:
#             dados["usuarios"][email] = {
#                 "nome": nome,
#                 "senha_hash": hash_senha(senha)
#             }
#             salvar_dados(dados)
#             st.success("Cadastro realizado com sucesso!")

# elif pagina == "Login":
#     st.subheader("Login")
#     email = st.text_input("Email")
#     senha = st.text_input("Senha", type="password")

#     if st.button("Entrar"):
#         usuario = dados["usuarios"].get(email)
#         if usuario and usuario["senha_hash"] == hash_senha(senha):
#             st.success(f"Bem-vindo, {usuario['nome']}!")
#             # Aqui entra o conteúdo protegido da aplicação
#             st.write("Conteúdo protegido...")
#         else:
#             st.error("Credenciais inválidas.")

import streamlit as st
import json
import hashlib
import os

# Funções auxiliares
def carregar_dados():
    if not os.path.exists("usuarios.json"):
        # Arquivo inicial
        with open("usuarios.json", "w") as f:
            json.dump({"autorizados": [], "usuarios": {}}, f, indent=4)
    with open("usuarios.json", "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open("usuarios.json", "w") as f:
        json.dump(dados, f, indent=4)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def logout():
    st.session_state.logado = False
    st.session_state.email = ""
    st.session_state.nome = ""

# Inicializa estado de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.email = ""
    st.session_state.nome = ""

# Ocultar sidebar e menus se estiver logado
if st.session_state.logado:
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📊 Bem-vindo à Aplicação!")
    st.success(f"Olá, {st.session_state.nome}!")

    # Conteúdo principal da aplicação
    st.write("✅ Aqui está o conteúdo protegido da sua aplicação.")
    st.write("Exemplo: dashboards, tabelas, gráficos, etc.")

    if st.button("Sair"):
        logout()
        st.rerun()

else:
    st.title("Minha aplicação com login")
    dados = carregar_dados()

    pagina = st.sidebar.selectbox("Acesso", ["Login", "Cadastro"])

    if pagina == "Cadastro":
        st.subheader("Criar nova conta")
        email = st.text_input("Email")
        nome = st.text_input("Nome")
        senha = st.text_input("Senha", type="password")
        confirmar = st.text_input("Confirmar senha", type="password")

        if st.button("Cadastrar"):
            if email not in dados["autorizados"]:
                st.error("Email não autorizado para cadastro.")
            elif email in dados["usuarios"]:
                st.warning("Este email já está cadastrado.")
            elif senha != confirmar:
                st.warning("As senhas não coincidem.")
            else:
                dados["usuarios"][email] = {
                    "nome": nome,
                    "senha_hash": hash_senha(senha)
                }
                salvar_dados(dados)
                st.success("Cadastro realizado com sucesso!")

    elif pagina == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            usuario = dados["usuarios"].get(email)
            if usuario and usuario["senha_hash"] == hash_senha(senha):
                st.session_state.logado = True
                st.session_state.email = email
                st.session_state.nome = usuario["nome"]
                st.rerun()
            else:
                st.error("Credenciais inválidas.")
