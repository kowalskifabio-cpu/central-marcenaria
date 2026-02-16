import streamlit as st

# 1. Configuração de tela wide
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. CSS para forçar o layout da sua referência (Cores e Alinhamento)
st.markdown("""
    <style>
    /* Ajuste do Cabeçalho: Logo e Título */
    .header-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    
    /* Configuração Geral dos Botões */
    div.stButton > button {
        width: 100% !important;
        height: 80px !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
    }

    /* Cores obrigatórias por coluna */
    [data-testid="column"]:nth-of-type(1) div.stButton button { background-color: #2E86C1 !important; } /* Azul */
    [data-testid="column"]:nth-of-type(2) div.stButton button { background-color: #E67E22 !important; } /* Laranja */
    [data-testid="column"]:nth-of-type(3) div.stButton button { background-color: #27AE60 !important; } /* Verde */

    /* Subtítulos dos Setores */
    .setor-label {
        font-weight: bold;
        margin-bottom: 5px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Logo e Título lado a lado)
col_img, col_txt = st.columns([1, 10])
with col_img:
    try:
        st.image("logo.png", width=100)
    except:
        st.write("🪵")

with col_txt:
    st.markdown("<h1 style='margin-top: 10px;'>Portal de Gestão Operacional</h1>", unsafe_allow_html=True)

st.write("Selecione a operação desejada:")
st.divider()

# 4. Botões Coloridos com Ícones
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<p class='setor-label'>📋 CONSULTORIA</p>", unsafe_allow_html=True)
    st.link_button("📄 Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with c2:
    st.markdown("<p class='setor-label'>📏 TERCEIROS</p>", unsafe_allow_html=True)
    st.link_button("📐 Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with c3:
    st.markdown("<p class='setor-label'>🏗️ PRODUÇÃO</p>", unsafe_allow_html=True)
    st.link_button("🏭 Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso restrito à equipe operacional Status Marcenaria.")
