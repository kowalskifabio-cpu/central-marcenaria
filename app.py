import streamlit as st

# Configurações Visuais - Wide expande a tela para os lados
st.set_page_config(page_title="Portal Marcenaria", page_icon="🪵", layout="wide")

st.title("🚀 Central de Operações - Marcenaria")
st.markdown("Clique nos botões abaixo para acessar os sistemas:")
st.divider()

# Criando 3 colunas iguais
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 **Consultoria**")
    st.write("Visão Geral e Diagnóstico")
    st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with col2:
    st.warning("📏 **Terceiros**")
    st.write("Medição de Terceiros")
    st.link_button("Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with col3:
    st.success("🏗️ **Produção**")
    st.write("Status ERCI - Gates")
    st.link_button("Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
