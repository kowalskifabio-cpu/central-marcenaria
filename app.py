import streamlit as st
from PIL import Image

# 1. Configuração da Página
st.set_page_config(page_title="Portal de Gestão - Marcenaria", layout="wide")

# 2. Estilização dos Botões (O "Pulo do Gato")
st.markdown("""
    <style>
    /* Estilo Geral dos Botões */
    div.stButton > button {
        height: 80px;
        border-radius: 10px;
        font-size: 20px !important;
        font-weight: bold;
        color: white !important;
    }
    /* Cores Individuais (Baseado na ordem) */
    div.stButton:nth-of-type(1) button { background-color: #2E86C1; } /* Azul */
    div.stButton:nth-of-type(2) button { background-color: #E67E22; } /* Laranja */
    div.stButton:nth-of-type(3) button { background-color: #27AE60; } /* Verde */
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho com sua Imagem
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    try:
        # Tenta carregar sua imagem PNG do GitHub
        img = Image.open("image_7d4f7b.png") 
        st.image(img, width=150)
    except:
        st.write("🪵") # Caso a imagem não seja encontrada

with col_titulo:
    st.title("Portal de Gestão Operacional")
    st.write("Selecione a operação desejada:")

st.divider()

# 4. Organização Horizontal
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📋 CONSULTORIA")
    st.caption("https://diagnostico-status-marcenaria.streamlit.app")
    st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with col2:
    st.markdown("### 📏 TERCEIROS")
    st.caption("https://sistemamedicao.streamlit.app/")
    st.link_button("Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("### 🏗️ PRODUÇÃO")
    st.caption("https://status-operacao.streamlit.app")
    st.link_button("Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso restrito à equipe operacional.")
