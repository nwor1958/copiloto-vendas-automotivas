# 🚗 Auto Sales AI Assistant (Copiloto de Vendas Automotivas)

[PT] Assistente virtual inteligente desenvolvido para otimizar a rotina de consultores de vendas no setor automotivo, cobrindo avaliação de veículos, estratégias de financiamento, geração de copy para anúncios e contorno de objeções.

[EN] Intelligent virtual assistant built to optimize automotive sales consultants' routines, covering vehicle evaluation, financing strategies, ad copywriting, and objection handling.

---

## 🇧🇷 Português

### 📌 Sobre o Projeto
O **Auto Sales AI Assistant** é um copiloto de inteligência artificial voltado ao mercado automotivo. O projeto conecta uma interface responsiva construída em Streamlit ao modelo `gemini-flash-latest` utilizando a biblioteca da OpenAI (`openai-python`) integrada à API do Google Generative AI via endpoint de compatibilidade.

### 🚀 Funcionalidades Principais
- **Consultoria Automotiva:** Suporte técnico sobre modelos, prós/contras e inspeção rápida.
- **Financiamentos & Matemática Financeira:** Orientação sobre CDC, leasing, consórcios e argumentos de custo-benefício.
- **Copywriting Automático:** Roteiros prontos para Reels/TikTok e anúncios para plataformas como Webmotors, OLX e Facebook Marketplace.
- **Técnicas de Negociação:** Estratégias e argumentos práticos para contorno de objeções de clientes.

### 🛠️ Stack Técnica
- **Linguagem:** Python 3.10+
- **Interface:** Streamlit
- **Provedor de LLM:** Google GenAI (Modelo `gemini-flash-latest`)
- **Integração:** `openai-python` SDK (OpenAI compatibility endpoint)
- **Gerenciamento de Estado:** `st.session_state` para persistência de memória do chat

---

## 🇺🇸 English

### 📌 About the Project
**Auto Sales AI Assistant** is an AI copilot tailored for the automotive market. The application connects a responsive Streamlit UI to the `gemini-flash-latest` model using the `openai-python` library integrated with Google's Generative AI API via their OpenAI compatibility endpoint.

### 🚀 Key Features
- **Automotive Consulting:** Technical guidance on vehicle specs, pros/cons, and inspection checklists.
- **Financing & Financial Strategy:** Advice on interest rates, amortization, automotive loans, and value proposition arguments.
- **Automated Copywriting:** Ready-to-use scripts for Reels/TikTok and copy for auto listing marketplaces.
- **Sales Negotiation:** Practical objection-handling techniques and closing strategies for sales professionals.

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **UI Framework:** Streamlit
- **LLM Provider:** Google GenAI (`gemini-flash-latest` model)
- **Integration:** `openai-python` SDK (OpenAI compatibility endpoint)
- **State Management:** `st.session_state` for chat memory persistence

---

## 📁 Como Executar o Projeto / How to Run

1. **Clone o repositório / Clone the repo:**
   ```bash
   git clone [https://github.com/nwor1958/auto-sales-ai-assistant.git](https://github.com/nwor1958/auto-sales-ai-assistant.git)
   cd auto-sales-ai-assistant
