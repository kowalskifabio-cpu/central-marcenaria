import streamlit as st

# 1. Configuração de tela
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. CSS REAL: Este bloco garante as cores e o layout da sua imagem de referência
st.markdown("""
    <style>
    /* Estilização dos Botões Coloridos */
    div.stButton > button {
        width: 100% !important;
        height: 70px !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
    }

    /* Cores obrigatórias por coluna conforme a imagem aprovada */
    [data-testid="column"]:nth-of-type(1) div.stButton button { background-color: #2E86C1 !important; } /* Azul */
    [data-testid="column"]:nth-of-type(2) div.stButton button { background-color: #E67E22 !important; } /* Laranja */
    [data-testid="column"]:nth-of-type(3) div.stButton button { background-color: #27AE60 !important; } /* Verde */

    /* Alinhamento do Cabeçalho */
    .header-box {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .setor-top-label {
        font-weight: bold;
        color: #444;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho: Logo Pequena + Título (Lado a Lado)
col_logo, col_titulo = st.columns([1, 8])
with col_logo:
    try:
        st.image("logo.png", width=100)
    except:
        st.write("🪵")

with col_titulo:
    st.markdown("<h1 style='margin-top: 15px;'>Portal de Gestão Operacional</h1>", unsafe_allow_html=True)

st.write("Selecione a operação desejada:")
st.divider()

# 4. Corpo: 3 Colunas com os Botões Coloridos e Ícones
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<p class='setor-top-label'>📋 CONSULTORIA</p>", unsafe_allow_html=True)
    st.link_button("📄 Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with c2:
    st.markdown("<p class='setor-top-label'>📐 TERCEIROS</p>", unsafe_allow_html=True)
    st.link_button("📐 Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with c3:
    st.markdown("<p class='setor-top-label'>🏗️ PRODUÇÃO</p>", unsafe_allow_html=True)
    st.link_button("🏭 Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso restrito à equipe operacional Status Marcenaria.")
