
#instalar e importar as bibliotecas (os, streamlit, dotenv, google (genai e types))
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

#Carrega variáveis locais
load_dotenv()
#Busca o valor da chave (Nuvem ou local)
try:
    GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")  

#inicializa o cliente
cliente_gemini = genai.Client(api_key=GEMINI_KEY) if GEMINI_KEY else None

#Título e configuração da página
st.title("🚗 Assistente do Consultor de Vendas Wilson Luis")
st.caption("Especialista em veículos, financiamentos, marketing automotivo e negociação")

#Definição do Prompt do Sistema 
PROMPT_SISTEMA = """
Você é o Copiloto do Wilson, um especialista de elite em consultoria de vendas de veículos, 
estudante de Gestão de Vendas e entusiasta do mercado financeiro e investimentos.

Seu objetivo é ajudá-lo a ser um vendedor de extrema alta performance, cobrindo:

1. **Conhecimento Automotivo e Avaliação:**
   - Detalhes técnicos, prós e contras de modelos populares aos de luxo.
   - Dicas de inspeção, mecânica rápida e pontos de atenção para compra/troca.

2. **Financiamentos e Estratégias Financeiras:**
   - Dicas sobre taxas de juros, amortização, entrada, parcelamento, CDC, Leasing e Consórcios.
   - Estratégias ocultas e argumentos para ajudar o cliente a entender o custo-benefício da compra.
   - Noções de investimentos para ajudar o Wilson e orientar clientes sobre planejamento financeiro.

3. **Marketing Automotivo e Conteúdo:**
   - Criação de roteiros para Reels, TikTok, Stories e fotos de anúncios.
   - Textos persuasivos (Copywriting) para marketplaces (OLX, Webmotors, Facebook Marketplace).
   - Técnicas de gatilhos mentais para vendas no Instagram.

4. **Técnicas de Vendas e Negociação:**
   - Quebra de objeções (ex: "está caro", "vou falar com a esposa", "o juro está alto").
   - Técnicas de contorno e fechamento rápido com foco na máxima assertividade.

**Diretrizes de Resposta:**
- Mantenha um tom profissional, encorajador, direto ao ponto e focado em resultados de vendas.
- Sempre que criar um roteiro ou texto de anúncio, use formatos prontos para copiar e colar.
"""

#Cria histórico de sessão
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

#Exibir histórico de conversas na tela:
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

#Campo para o usuário mandar mensagem:
mensagem_usuario = st.chat_input("Digite sua mensagem aqui")

#Exibe e salva a mensagem do usuário
if mensagem_usuario:
    if not cliente_gemini:
        st.error("Erro: Chave da API do Gemini não configurada.")
    else:
        st.chat_message("user").write(mensagem_usuario)
        st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})
        #Converte em formato SDK google-genai / papel = model e não assistant
        historico_formatado = []
        for m in st.session_state["lista_mensagens"]:
            papel = "model" if m["role"] == "assistant" else "user"
            historico_formatado.append(
                types.Content(
                    role=papel,
                    parts=[types.Part.from_text(text=m["content"])]
                )
            )

#Chamada à API    
    try:
        resposta_modelo = cliente_gemini.models.generate_content(
            model="gemini-3.5-flash",
            contents=historico_formatado,
            config=types.GenerateContentConfig(
                system_instruction=PROMPT_SISTEMA,
                temperature=0.7,
            ),
        )
        resposta_ia = resposta_modelo.text
    
    #Exibe e salva a resposta da IA
        st.chat_message("assistant").write(resposta_ia)    
        st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})

    except Exception as e:
        st.error(f"Ocorreu um erro ao gerar a resposta: {e}")