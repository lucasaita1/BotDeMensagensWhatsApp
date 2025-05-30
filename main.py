import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Caminhos seguros e portáveis
base_dir = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(base_dir, 'Contatos.xlsx')
perfil_chrome = os.path.join(base_dir, 'selenium_profile')

# Leitura do Excel
contatos = pd.read_excel(arquivo)
contatos.columns = contatos.columns.str.strip().str.upper()

# Mensagem base
mensagem_base = "Olá {nome}, tudo bem? Estou te enviando uma mensagem automática via WhatsApp."

# Configurações do Selenium
options = Options()
options.add_argument(f"--user-data-dir={perfil_chrome}")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

input("📲 Escaneie o QR Code e pressione ENTER para continuar...")

lote_tamanho = 30

for i in range(0, len(contatos), lote_tamanho):
    lote = contatos.iloc[i:i + lote_tamanho]
    print(f"\n🔄 Enviando lote {i // lote_tamanho + 1} com {len(lote)} contatos...")

    for index, contato in lote.iterrows():
        nome = contato['NOME']
        telefone = str(contato['TELEFONE']).strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if not telefone.startswith("+"):
            telefone = "+55" + telefone
        mensagem = mensagem_base.replace("{nome}", nome)

        url = f"https://web.whatsapp.com/send?phone={telefone}"
        driver.get(url)

        try:
            wait = WebDriverWait(driver, 30)
            campo_msg = wait.until(EC.presence_of_element_located((By.XPATH, '//footer//div[@contenteditable="true"]')))
            campo_msg.click()
            time.sleep(1)
            campo_msg.send_keys(mensagem)
            time.sleep(0.5)
            campo_msg.send_keys(Keys.ENTER)
            print(f"✅ Mensagem enviada para {nome}")
        except Exception as e:
            print(f"❌ Erro ao enviar para {nome}: {e}")

        time.sleep(10)

    print("⏳ Aguardando 60 segundos antes do próximo lote...")
    time.sleep(60)

driver.quit()
print("🏁 Fim do envio!")