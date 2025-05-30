# 🤖 Bot de Envio de Mensagens no WhatsApp

Automação para envio de mensagens personalizadas via **WhatsApp Web**, utilizando Python, Selenium e planilhas Excel. Ideal para mensagens em massa com controle de lotes.

---

## 🚀 Funcionalidades

- 📄 Leitura automática de planilhas `.xlsx`
- ✍️ Mensagens personalizadas com o nome de cada contato
- 📱 Integração com WhatsApp Web via Selenium
- 🧑‍🤝‍🧑 Envio em **lotes de 30 contatos**
- ⏱️ Pausa de 10s entre mensagens e 60s entre lotes
- ✅ Envio automático sem interação manual (Enter)

---

## 🧰 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [pandas](https://pandas.pydata.org/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) ou SafariDriver (macOS)

---

## 📁 Estrutura esperada do Excel

O arquivo `.xlsx` deve conter as seguintes colunas:

| NOME           | TELEFONE        |
|----------------|------------------|
| João da Silva  | +5511999999999   |
| Maria Lima     | +5511988888888   |

---

## ⚙️ Como usar

### 1. Clone o repositório:

```bash
git clone https://github.com/lucasaita1/BotDeMensagensWhatsApp.git
cd BotDeMensagensWhatsApp

```

### 2. Crie seu ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

> 💡 Se não tiver um `requirements.txt`, instale manualmente:
> `pip install selenium pandas`

### 4. Coloque o arquivo `contatos.xlsx` na pasta raiz do projeto

### 5. Execute o script:

```bash
python Main.py
```

---

## 🔐 Segurança e limitações

- **O WhatsApp Web deve estar logado no navegador.**
- O script usa um **perfil de navegador isolado**, não afeta seu navegador pessoal.
- **Não envie spam.** Respeite os termos de uso do WhatsApp.

---

## 📦 Extras

- 💬 Planeja-se implementar envio de mídia?
- 💻 Interface gráfica para usuários não técnicos?
- ☁️ Deploy em nuvem para automação contínua?

Fica fácil de evoluir com essa base sólida.

---

## 👨‍💻 Autor

**Lucas Prates Aita**
📧 [lucasaita4000@gmail.com](mailto:lucasaita4000@gmail.com)
🔗 [linkedin.com/in/lucasaita](https://www.linkedin.com/in/lucas-aita-56b4b3231/)
🐙 [github.com/lucasaita1](https://github.com/lucasaita1)

---

## 📝 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.
