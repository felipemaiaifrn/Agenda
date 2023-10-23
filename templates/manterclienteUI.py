import streamlit as st
import pandas as pd
import time
from view import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()
    def listar():
        clientes = View.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.experimental_rerun()
    def atualizar():
        option = st.selectbox(
            'Atualização de Clientes',
            (View.cliente_listar()))
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        id = option.get_id()
        if st.button("Atualizar"):
            View.cliente_atualizar(id, nome, email, fone)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.experimental_rerun()
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
          st.write("Nenhum cliente cadastrado")
        else:  
          op = st.selectbox("Exclusão de Clientes", clientes)
          if st.button("Excluir"):
            View.cliente_excluir(op.get_id())
            st.success("Cliente excluído com sucesso")
            time.sleep(2)
            st.experimental_rerun()