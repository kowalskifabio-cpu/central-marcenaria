import streamlit as st

# 1. Configuração de tela wide
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. CSS Blindado para Forçar o Visual da Referência
st.markdown("""
    <style>
    /* Ajuste dos Botões: Cores, Tamanho e Fonte */
    div.stButton > button {
        width: 100% !important;
        height: 85px !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }

    /* Cores obrigatórias por coluna */
    [data-testid="column"]:nth-of-type(1) div.stButton button { background-color: #2E86C1 !important; } /* Azul */
    [data-testid="column"]:nth-of-type(2) div.stButton button { background-color: #E67E22 !important; } /* Laranja */
    [data-testid="column"]:nth-of-type(3) div.stButton button { background-color: #27AE60 !important; } /* Verde */

    /* Alinhamento do Cabeçalho (Logo e Título) */
    .header-text {
        font-size: 36px;
        font-weight: bold;
        margin-top: 10px;
    }
    .setor-top-label {
        font-weight: bold;
        color: #444;
        margin-bottom: 8px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho (Logo e Título Lado a Lado)
col_logo, col_tit = st.columns([1, 8])
with col_logo:
    try:
        # Tenta carregar o logo.png pequeno
        st.image("logo.png", width=90)
    except:
        st.write("🪵")

with col_tit:
    st.markdown('<p class="header-text">Portal de Gestão Operacional</p>', unsafe_allow_html=True)

st.write("Selecione a operação desejada:")
st.divider()

# 4. Botões com Links Reais e Ícones Internos
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<p class='setor-top-label'>📋 CONSULTORIA</p>", unsafe_allow_html=True)
    st.link_button("📄 Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with c2:
    st.markdown("<p class='setor-top-label'>📐 TERCEIROS</p>", unsafe_allow_html=True)
    # Link corrigido para evitar o erro da barra de endereços
    st.link_button("📐 Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with c3:
    st.markdown("<p class='setor-top-label'>🏗️ PRODUÇÃO</p>", unsafe_allow_html=True)
    st.link_button("🏭 Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso exclusivo para colaboradores Status Marcenaria.")
