import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.8

# Passo 1: Abrir o sistema da empresa

pyautogui.press("Win")

pyautogui.write("Chrome")

pyautogui.press("Enter")

pyautogui.click(x=588, y=324)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("Enter")

time.sleep(0.5)

# Passo 2: Fazer login

pyautogui.press("Tab")

pyautogui.write("pythonteste@python.com")

pyautogui.press("Tab")

pyautogui.write("pythonsenha")

pyautogui.press("Enter")

time.sleep(1.2)

# Passo 3: Importar Banco de Dados

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=418, y=306)  # clica no primeiro campo

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("Tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("Tab")

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    # Preço unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("Tab")

    # Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    # Observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")

    pyautogui.press("Enter")

    pyautogui.scroll(+1000)




