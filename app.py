import streamlit as st
import json
import hashlib
import os

# Funções auxiliares
def carregar_dados():
    with open("usuarios.json", "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open("usuarios.json", "w") as f:
        json.dump(dados, f, indent=4)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Interface
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
            st.success(f"Bem-vindo, {usuario['nome']}!")
            # Aqui entra o conteúdo protegido da aplicação
            st.write("Conteúdo protegido...")
        else:
            st.error("Credenciais inválidas.")
