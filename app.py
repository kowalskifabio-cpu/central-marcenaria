import streamlit as st

# Configurações Visuais
st.set_page_config(page_title="Portal Marcenaria", page_icon="🪵", layout="wide")

# Estilo para os botões ficarem maiores
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
    }
    </style>""", unsafe_allow_html=True)

# Substituição do Foguete pela Logo mantendo proporção e alinhamento
col_logo, col_titulo = st.columns([0.1, 0.9]) # Define colunas para logo e texto lado a lado

with col_logo:
    # O arquivo enviado foi 'logo.jpg'. Ajuste para 'logo.png' se necessário no GitHub.
    st.image("logo.png", width=100") 

with col_titulo:
    st.title("Central de Operações - Marcenaria")

st.divider()

# Organizando em 3 Colunas para os seus 3 Apps Principais
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 **Consultoria**")
    st.write("Visão Geral e Diagnóstico")
    st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app")

with col2:
    st.warning("📏 **Terceiros**")
    st.write("Controle de Medição")
    st.link_button("Sistema de Medição", "https://sistema-medicao.streamlit.app")

with col3:
    st.success("🏗️ **Produção**")
    st.write("Status ERCI - Gates")
    st.link_button("Status Operação", "https://status-operacao.streamlit.app")

st.divider()
st.caption("Acesso restrito à equipe operacional da Marcenaria.")
