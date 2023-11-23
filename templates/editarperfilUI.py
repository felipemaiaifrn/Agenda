import streamlit as st
import time
from views import View

class EditarPerfilUI:
    def main():
        st.header('Editar Perfil')
        EditarPerfilUI.editar()

    def editar():
        id = st.session_state["cliente_id"]
        nome_admin = st.session_state["cliente_nome"]
        
        if nome_admin == 'admin':
            nome = nome_admin
            email = st.text_input('Informe o novo e-mail')
            telefone = st.text_input('Informe o novo telefone')
            senha = st.text_input('Informe a nova senha')
        else:
            nome = st.text_input('Informe o novo nome')
            email = st.text_input('Informe o novo e-mail')
            telefone = st.text_input('Informe o novo telefone')
            senha = st.text_input('Informe a nova senha')

        if st.button('Editar'):
            View.editar_perfil(id, nome, email, telefone, senha)
            st.success('Perfil editado com sucesso!')
            time.sleep(1)
            st.rerun()