import streamlit as st

def logout():
    st.session_state.logado = False
    st.session_state.email = ""
    st.session_state.nome = ""

def show():
    st.title("📊 Bem-vindo à Aplicação!")
    st.success(f"Olá, {st.session_state.nome}!")

    # Conteúdo principal da aplicação
    st.write("✅ Aqui está o conteúdo protegido da sua aplicação.")
    st.write("Exemplo: dashboards, tabelas, gráficos, etc.")

    if st.button("Sair"):
        logout()
        st.rerun()    