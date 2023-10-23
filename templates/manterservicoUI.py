import streamlit as st
import pandas as pd
from view import View
import time

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.listar()
        with tab2:
            st.write("Inserir")
            #ManterServicoUI.inserir()
        with tab3:
            st.write("Atualizar")
            #ManterServicoUI.atualizar()
        with tab4:
            st.write("Excluir")
            #ManterServicoUI.excluir()
    def listar():
        servicos = View.servico_listar()
        dic = []
        for s in servicos:
            dic.append(s.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)