import streamlit as st

# Configurações Visuais
st.set_page_config(page_title="Portal Marcenaria", page_icon="🪵")

st.title("🚀 Central de Operações - Marcenaria")
st.markdown("Clique nos botões abaixo para acessar os sistemas:")

# Coluna 1: Consultoria
st.info("📊 **Consultoria**")
st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app")

st.divider()

# Coluna 2: Sistema de Medição (O que deu erro)
st.warning("📏 **Terceiros**")
# IMPORTANTE: Substitua o link abaixo pelo link real que você usa para abrir a Medição
st.link_button("Acessar Sistema de Medição", "COLE_AQUI_O_LINK_DO_APP_DE_MEDICAO")

st.divider()

# Coluna 3: Produção
st.success("🏗️ **Produção**")
st.link_button("Status Operação (ERCI)", "https://status-operacao.streamlit.app")
