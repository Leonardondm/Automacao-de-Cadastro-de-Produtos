import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.3

def abrir_chrome():
    try:
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
    except Exception as e:
        print(f"Erro ao abrir o Chrome: {e}")

def entrar_no_site(url):
    try:
        pyautogui.write(url)
        pyautogui.press("enter")
        time.sleep(3)
    except Exception as e:
        print(f"Erro ao entrar no site: {e}")

def fazer_login(email, senha):
    try:
        pyautogui.click(x=784, y=393)
        pyautogui.write(email)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(3)
    except Exception as e:
        print(f"Erro ao fazer login: {e}")

def cadastrar_produto(codigo, marca, tipo, categoria, preco, custo, obs):
    try:
        pyautogui.click(x=772, y=284)
        pyautogui.write(str(codigo))
        pyautogui.press("tab")
        pyautogui.write(str(marca))
        pyautogui.press("tab")
        pyautogui.write(str(tipo))
        pyautogui.press("tab")
        pyautogui.write(str(categoria))
        pyautogui.press("tab")
        pyautogui.write(str(preco))
        pyautogui.press("tab")
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        if not pd.isna(obs):
            pyautogui.write(str(obs))

        pyautogui.press("tab")
        pyautogui.press("enter")

        # Subir tela
        pyautogui.scroll(5000)
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")

def main():
    abrir_chrome()
    entrar_no_site("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    fazer_login("emailteste@gmail.com", "senhaqualquer")

    # Ler tabela
    try:
        tabela = pd.read_csv("produtos.csv")
    except Exception as e:
        print(f"Erro ao ler a tabela de produtos: {e}")
        return

    for i in tabela.index:
        codigo = tabela.loc[i, "codigo"]
        marca = tabela.loc[i, "marca"]
        tipo = tabela.loc[i, "tipo"]
        categoria = tabela.loc[i, "categoria"]
        preco = tabela.loc[i, "preco_unitario"]
        custo = tabela.loc[i, "custo"]
        obs = tabela.loc[i, "obs"]

        cadastrar_produto(codigo, marca, tipo, categoria, preco, custo, obs)

if __name__ == "__main__":
    main()
