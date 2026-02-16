import streamlit as st

# 1. Configuração de tela
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. CSS para forçar o layout e as cores da sua referência
st.markdown("""
    <style>
    /* Ajuste dos Botões Coloridos */
    div.stButton > button {
        width: 100% !important;
        height: 70px !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
    }

    /* Cores obrigatórias por coluna */
    [data-testid="column"]:nth-of-type(1) div.stButton button { background-color: #2E86C1 !important; }
    [data-testid="column"]:nth-of-type(2) div.stButton button { background-color: #E67E22 !important; }
    [data-testid="column"]:nth-of-type(3) div.stButton button { background-color: #27AE60 !important; }

    /* Alinhamento do Cabeçalho */
    .header-container { display: flex; align-items: center; gap: 20px; }
    .setor-label { font-weight: bold; color: #444; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho: Logo (logo.png) + Título
col_logo, col_tit = st.columns([1, 8])
with col_logo:
    try:
        st.image("logo.png", width=100)
    except:
        st.write("🪵")

with col_tit:
    st.markdown("<h1 style='margin-top: 15px;'>Portal de Gestão Operacional</h1>", unsafe_allow_html=True)

st.write("Selecione a operação desejada:")
st.divider()

# 4. Botões com Links Reais (Certifique-se de que os links abaixo abrem no navegador)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("<p class='setor-label'>📋 CONSULTORIA</p>", unsafe_allow_html=True)
    st.link_button("📄 Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with c2:
    st.markdown("<p class='setor-label'>📐 TERCEIROS</p>", unsafe_allow_html=True)
    # ATENÇÃO: Verifique se este link abaixo é o link correto do seu app de medição
    st.link_button("📐 Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with c3:
    st.markdown("<p class='setor-label'>🏗️ PRODUÇÃO</p>", unsafe_allow_html=True)
    st.link_button("🏭 Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso restrito à equipe operacional Status Marcenaria.")
