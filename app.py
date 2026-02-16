import streamlit as st

# 1. Configuração de tela wide
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. CSS Blindado para Cores e Layout
st.markdown("""
    <style>
    /* Remove espaços inúteis no topo */
    .block-container { padding-top: 1rem; }
    
    /* Configuração Geral dos Botões */
    div.stButton > button {
        width: 100% !important;
        height: 120px !important;
        border-radius: 15px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        color: white !important;
        border: none !important;
        transition: 0.3s;
    }

    /* FORÇANDO AS CORES POR COLUNA */
    /* Botão 1 - Azul */
    [data-testid="column"]:nth-of-type(1) div.stButton button {
        background-color: #2E86C1 !important;
    }
    /* Botão 2 - Laranja/Bronze */
    [data-testid="column"]:nth-of-type(2) div.stButton button {
        background-color: #E67E22 !important;
    }
    /* Botão 3 - Verde */
    [data-testid="column"]:nth-of-type(3) div.stButton button {
        background-color: #27AE60 !important;
    }

    /* Efeito de destaque ao passar o mouse */
    div.stButton > button:hover {
        transform: scale(1.02);
        filter: brightness(1.1);
    }
    
    /* Centralizar títulos dos setores */
    .setor-titulo {
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 10px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho com o seu logo.png
try:
    st.image("logo.png", use_container_width=True)
except:
    st.error("Erro: O arquivo 'logo.png' não foi encontrado no seu GitHub.")

st.markdown("<h1 style='text-align: center;'>Portal de Gestão Operacional</h1>", unsafe_allow_html=True)
st.divider()

# 4. Organização dos Botões lado a lado
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='setor-titulo'>📋 CONSULTORIA</div>", unsafe_allow_html=True)
    st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with col2:
    st.markdown("<div class='setor-titulo'>📏 TERCEIROS</div>", unsafe_allow_html=True)
    st.link_button("Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("<div class='setor-titulo'>🏗️ PRODUÇÃO</div>", unsafe_allow_html=True)
    st.link_button("Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso restrito à equipe Status Marcenaria.")
