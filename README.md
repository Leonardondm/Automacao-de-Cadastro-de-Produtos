# Automacao-de-Cadastro-de-Produtos

 Script Python para automação de cadastro de produtos em um site usando PyAutoGUI e dados de produtos em formato CSV.

## Sobre o projeto

Projeto de automação desenvolvido em Python para realizar o cadastro de produtos em um sistema web. O projeto utiliza a biblioteca PyAutoGUI para automatizar a interação com a interface gráfica do navegador Chrome e o Pandas para manipulação de dados.

## Descrição

O objetivo deste projeto é automatizar o processo de cadastro de produtos em um sistema web. O código realiza as seguintes etapas:
<ul>
  <li>Abre o navegador Chrome.
  <li> Acessa um site específico.
  <li>Realiza o login com as credenciais fornecidas.
  <li>Lê os dados de um arquivo CSV chamado "produtos.csv".
  <li>Itera sobre os dados do arquivo CSV e cadastra os produtos no sistema web.
</ul>

O arquivo "produtos.csv" contém informações sobre os produtos a serem cadastrados, como código, marca, tipo, categoria, preço unitário, custo e observações.

## Instruções de Uso

Clone este repositório para o seu ambiente local:

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```
 Instale as dependências necessárias. Você pode criar um ambiente virtual para isso:

```
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate  # No Windows, utilize "venv\Scripts\activate"
pip install -r requirements.txt
```

Edite o arquivo "main.py" para inserir as suas credenciais de login e, se necessário, ajuste as coordenadas de clique na interface gráfica do sistema web.

Certifique-se de que o arquivo "produtos.csv" está na mesma pasta que o "main.py" e contém os dados dos produtos que deseja cadastrar.

Execute o código principal:

```
python main.py
```

O código irá automatizar o processo de cadastro de produtos conforme os dados do arquivo "produtos.csv". Certifique-se de ter o navegador Chrome instalado e que ele está atualizado.

## Notas

Este projeto foi desenvolvido apenas como exemplo e pode requerer ajustes para se adequar ao seu ambiente específico.
Certifique-se de cumprir os termos de uso e políticas de automação do sistema web em questão.


## Autor

Leonardo Nascimento Dias

