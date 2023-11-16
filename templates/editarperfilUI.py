import streamlit as st
from views import View
import time

class EditarPerfilUI:
  def main():
    st.header("Editar perfil")
    EditarPerfilUI.editar()

  def editar():
    id = st.session_state['cliente_id']
    nome = st.text_input("Informe o novo nome")
    email = st.text_input("Informe o novo e-mail")
    fone = st.text_input("Informe o novo fone")
    senha = st.text_input("Informe a nova senha")
    if st.button("Editar"):
      cliente = View.editar_perfil(id, nome, email, fone, senha) 
      st.success("Perfil editado com sucesso!")
      time.sleep(2)
      st.rerun()  