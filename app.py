import streamlit as st

# Configuração da página
st.set_page_config(page_title="Central de Operações", layout="wide")

# CSS para forçar o visual da imagem de referência
st.markdown("""
    <style>
    /* Estilo dos botões coloridos */
    div.stButton > button {
        width: 100% !important;
        height: 60px !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
    }
    
    /* Cores exatas da referência */
    /* Coluna 1 - Azul */
    [data-testid="column"]:nth-of-type(1) div.stButton button { background-color: #2E86C1 !important; }
    /* Coluna 2 - Laranja */
    [data-testid="column"]:nth-of-type(2) div.stButton button { background-color: #E67E22 !important; }
    /* Coluna 3 - Verde */
    [data-testid="column"]:nth-of-type(3) div.stButton button { background-color: #27AE60 !important; }

    /* Ajuste do cabeçalho */
    .header-text {
        font-size: 32px;
        font-weight: bold;
        margin-left: -20px;
    }
    .sub-text {
        color: #666;
        margin-top: -10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO (Logo e Título lado a lado) ---
col_logo, col_tit = st.columns([1, 8])
with col_logo:
    try:
        st.image("logo.png", width=80)
    except:
        st.write("🪵")

with col_tit:
    st.markdown('<p class="header-text">Portal de Gestão Operacional</p>', unsafe_allow_html=True)

st.write("Selecione a operação desejada:")
st.markdown("---")

# --- CORPO (Botões com links e ícones) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🎯 **CONSULTORIA**")
    st.caption("https://diagnostico-status-marcenaria.streamlit.app")
    st.link_button("📋 Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with col2:
    st.markdown("📐 **TERCEIROS**")
    st.caption("https://sistemamedicao.streamlit.app/")
    st.link_button("📏 Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("🏗️ **PRODUÇÃO**")
    st.caption("https://status-operacao.streamlit.app")
    st.link_button("🏠 Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.markdown("---")
st.caption("Acesso restrito à equipe operacional.")
