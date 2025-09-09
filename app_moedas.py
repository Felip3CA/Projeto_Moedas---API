import streamlit as st
import requests

st.title("Cotação de Moedas - AwesomeAPI")


moedas = {
    "Dólar → Real": "USD-BRL",
    "Euro → Real": "EUR-BRL",
    "Bitcoin → Real": "BTC-BRL",
    "Libra → Real": "GBP-BRL"
}

opcao = st.selectbox("Selecione a cotação:", list(moedas.keys()))

if st.button("Buscar cotação"):
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = list(dados.keys())[0]  # exemplo: "USDBRL"
        info = dados[chave]

        st.subheader(info["name"])
        st.write(f"**Alta do dia:** {info['high']}")
        st.write(f"**Baixa do dia:** {info['low']}")
        st.write(f"**Variação:** {info['varBid']}")
        st.write(f"**Cotação atual (compra):** R$ {info['bid']}")
        st.write(f"**Cotação atual (venda):** R$ {info['ask']}")
    else:
        st.error("Erro ao buscar a cotação.")