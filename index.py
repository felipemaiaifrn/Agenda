from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
import streamlit as st

class IndexUI:
    
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      #if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"
      #if op == "Manter Serviços": st.session_state["page"] = "manter_servicoUI"
      #if op == "Manter Agenda": st.session_state["page"] = "manter_agendaUI"

    def main():
      IndexUI.sidebar()
      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()
      #if st.session_state["page"] == "manter_servicoUI": ManterServicoUI.main()
      #if st.session_state["page"] == "manter_agendaUI": ManterAgendaUI.main()

IndexUI.main()