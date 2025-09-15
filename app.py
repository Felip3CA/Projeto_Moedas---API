import streamlit as st

# Configurações da página
st.set_page_config(page_title="Bem-estar Mental", page_icon="🌿", layout="centered")

# CSS para fundo e cores
st.markdown(
    """
    <style>
    body {
        background-color: #FFF7E4;
        color: #1D3557;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #A8DADC;
        color: #1D3557;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stTextArea textarea {
        background-color: #C7F9CC;
    }
    .stRadio>div>label {
        background-color: #FADCD9;
        padding: 6px;
        border-radius: 6px;
        margin: 4px;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("🌿 Bem-estar Mental")
st.subheader("Um espaço para você refletir e se sentir melhor")

# Diário emocional
st.markdown("### Como você está se sentindo hoje?")
diario = st.text_area("Escreva seus pensamentos e sentimentos aqui:")

if diario:
    st.write("Obrigado por compartilhar! 💛")
    st.write(f"Você escreveu: {diario}")

# Teste de humor simples
st.markdown("### Como você se sente agora?")
humor = st.radio("", ["Feliz 😄", "Triste 😢", "Ansioso 😰", "Neutro 😐"])

if st.button("Ver Dica"):
    if humor == "Feliz 😄":
        st.success("Continue cultivando momentos felizes! 🌟")
    elif humor == "Triste 😢":
        st.info("Tente fazer algo que você gosta ou conversar com alguém de confiança. 💛")
    elif humor == "Ansioso 😰":
        st.warning("Respire fundo e tente exercícios de relaxamento. 🌬️")
    else:
        st.write("Lembre-se de cuidar de si mesmo todos os dias! 💚")
