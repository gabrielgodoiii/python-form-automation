import pandas as pd
import pyautogui as py
import pyperclip
import time
sheets_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTOOkWNQCco21jeu6Zax8mN-M6ndFhWWhjR0Uj_BJ2bDyQgQCDpx8RMl7GswjltoAKERLNrgauV-Zxl/pub?output=csv'
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyperclip.copy(link)
py.PAUSE = 0.5
time.sleep(2)
df = pd.read_csv(sheets_link)
df = df.fillna('-')
py.press('win')
py.write('Google Chrome')
py.press('enter')
time.sleep(1)
py.hotkey('ctrl', 'v')
py.press('enter')
time.sleep(1)
py.press('tab')
py.write('gabriel@email.com')
py.press('tab')
py.write('senha123')
py.press('tab')
py.press('enter')
time.sleep(1)
py.press('tab')
for linha in df.index:
    codigo = df.loc[linha, 'Código do Produto']
    marca = df.loc[linha, 'Marca do Produto']
    tipo = df.loc[linha, 'Tipo do Produto']
    categoria = df.loc[linha, 'Categoria do Produto']
    preco = df.loc[linha, 'Preço Unitário do Produto']
    custo = df.loc[linha, 'Custo do Produto']
    obs = df.loc[linha, 'OBS']
    py.write(str(codigo))
    py.press('tab')
    py.write(str(marca))
    py.press('tab')
    py.write(str(tipo))
    py.press('tab')
    py.write(str(categoria))
    py.press('tab')
    py.write(str(preco))
    py.press('tab')
    py.write(str(custo))
    py.press('tab')
    py.write(str(obs))
    py.press('tab')
    py.press('enter')
    py.click(326, 258)
