
# print("Hello World")

import pyautogui
import time
import pandas  

pyautogui.PAUSE = .5

# pyautogui.click
# pyautogui.press
# pyautogui.scroll
# pyautogui.write

pyautogui.press("win")
pyautogui.write("edger")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=775, y=458)

pyautogui.write("teste@gmail.com")

pyautogui.press("tab")
pyautogui.write("12345")

pyautogui.press("tab")
pyautogui.press("enter")

table = pandas.read_csv("produtos.csv")

time.sleep(3)

for linha in table.index: 
    pyautogui.click(x=695, y=305)

    # codigo
    codigo = table.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = table.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = table.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = table.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    precoUnitario = table.loc[linha, "preco_unitario"]
    pyautogui.write(str(precoUnitario))
    pyautogui.press("tab")

    # custo
    custo = table.loc[linha, "custo"]
    pyautogui.write(str(custo))  
    pyautogui.press("tab")

    # obs
    obs = str(table.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")


    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo

    pyautogui.scroll(10000)