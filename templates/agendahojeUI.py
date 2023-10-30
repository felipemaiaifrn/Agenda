import streamlit as st
import pandas as pd
from views import View

class AgendaHojeUI:
    def main():
        st.header("Agenda de Hoje")
        AgendaHojeUI.hoje()
    
    def hoje():
        hoje = View.Agenda_ListarHoje()
        dic = []
        for agenda in hoje: dic.append(agenda.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df)