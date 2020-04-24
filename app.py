from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
import os

# Atenção o arquivo "chromedriver" deve ser baixado de acordo com sua versão do Google Chrome,
# segue o link para download: https://sites.google.com/a/chromium.org/chromedriver/downloads
# OBS: A versão que está no repositório é a 81

# Menssagem a ser enviada, onde o espaço deve ser substituído por "%20"
message = "Hello%20World!"

# Número do telefone para quem enviará a mensagem "55 88 912345678"
numero = "55 88 912345678"

# URL formatada com as informações
url="https://web.whatsapp.com/send?phone="+numero+"&text="+message

# O local de execução do nosso script
dir_path = os.getcwd()

# O caminho do chromedriver
chromedriver = os.path.join(dir_path, "chromedriver")

# Caminho onde será criada pasta profile
profile = os.path.join(dir_path, "profile", "wpp")


options = webdriver.ChromeOptions()

# Configurando a pasta profile, para mantermos os dados da seção
options.add_argument(r"user-data-dir={}".format(profile))

# Inicializa o webdriver
driver = webdriver.Chrome(
chromedriver, chrome_options=options)

# Abre o whatsappweb
driver.get(url)

# Aguarda 15 segundos para validar o QRCODE
driver.implicitly_wait(15)

# Aguarda 4 segundos até o element ser carregado e ficar visivel na página
WebDriverWait(driver, timeout=10).until(condition.visibility_of(driver.find_element_by_class_name("_35EW6")))

# Seleciona o botão de enviar
botao_enviar = driver.find_element_by_class_name("_35EW6")

# Envia a menssagem
botao_enviar.click()

# Encerra a sessão e fecha o navegador
driver.quit()
