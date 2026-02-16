import streamlit as st
import base64

# 1. Configuração de tela cheia
st.set_page_config(page_title="Portal Status Marcenaria", layout="wide")

# 2. Função para carregar a imagem de fundo do cabeçalho
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 3. CSS "Pesado" para forçar as cores e o layout
st.markdown(f"""
    <style>
    /* Estilizando o fundo do cabeçalho */
    .header-container {{
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
    }}
    
    /* Forçando cores nos botões do Streamlit */
    div.stButton > button {{
        width: 100%;
        height: 100px !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 12px !important;
        transition: 0.3s;
    }}
    
    /* Botão Consultoria (Azul) */
    div.stButton:nth-of-type(1) button {{ background-color: #2E86C1 !important; }}
    div.stButton:nth-of-type(1) button:hover {{ background-color: #21618C !important; opacity: 0.9; }}

    /* Botão Terceiros (Laranja) */
    [data-testid="column"]:nth-of-type(2) div.stButton button {{ background-color: #E67E22 !important; }}
    
    /* Botão Produção (Verde) */
    [data-testid="column"]:nth-of-type(3) div.stButton button {{ background-color: #27AE60 !important; }}
    
    /* Ajuste de subtítulos */
    .setor-card {{
        text-align: center;
        padding: 10px;
        font-weight: bold;
        color: #555;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Cabeçalho com o Logo Status Marcenaria
try:
    # Usando a imagem que você forneceu
    st.image("Status Apresentação.jpg", use_container_width=True)
except:
    st.title("🛠️ STATUS MARCENARIA - Portal Operacional")

st.markdown("<h2 style='text-align: center;'>Portal de Gestão Operacional</h2>", unsafe_allow_html=True)
st.divider()

# 5. Colunas com Botões Coloridos
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='setor-card'>📋 CONSULTORIA</div>", unsafe_allow_html=True)
    st.link_button("Abrir Diagnóstico", "https://diagnostico-status-marcenaria.streamlit.app", use_container_width=True)

with col2:
    st.markdown("<div class='setor-card'>📏 TERCEIROS</div>", unsafe_allow_html=True)
    st.link_button("Acessar Medição", "https://sistemamedicao.streamlit.app/", use_container_width=True)

with col3:
    st.markdown("<div class='setor-card'>🏗️ PRODUÇÃO</div>", unsafe_allow_html=True)
    st.link_button("Status Operação", "https://status-operacao.streamlit.app", use_container_width=True)

st.divider()
st.caption("Acesso exclusivo para colaboradores Status Marcenaria.")
