# 🧪 Checkpoint 05 - Quality Assurance Tests

Este projeto consiste em um conjunto de testes automatizados desenvolvidos para validar funcionalidades 
críticas da aplicação [Restful Booker Platform](https://automationintesting.online/admin), 
com foco em **login** e **listagem de quartos**, utilizando Selenium WebDriver com Python.

---

## 📁 Estrutura do Projeto

Check-Point-05-Compliance-Quality-Assurance-Tests/ 
├── evidencias/ │ 
    ├── login_tela.png │
    ├── login_sucesso.png │ 
    ├── login_negativo.png │ 
    ├── listagem_quartos.png 
    │ └── listagem_negativa.png 
├── selenium/ │ 
  ├── test_login.py 
  │ └── test_room_list.py 
  ├── requirements.txt 
  └── README.md


---

## 🧠 Objetivo dos Testes

### ✅ `test_login.py`
Testa o fluxo de autenticação da plataforma administrativa.

- **Teste Positivo**: Realiza login com credenciais válidas.
- **Teste Negativo**: Tenta login com credenciais inválidas.
- **Evidências**: Captura de tela do formulário, sucesso e falha.

### ✅ `test_room_list.py`
Verifica a listagem de quartos após o login.

- **Teste Positivo**: Confirma a presença de elementos de quartos.
- **Teste Negativo**: Acessa uma URL incorreta intencionalmente para simular erro.

---

## ⚙️ Tecnologias Utilizadas

- `Python 3.12`
- `Selenium`
- `WebDriver Manager`
- `ChromeDriver`

---

## 📦 Dependências

Instale os requisitos com:

```bash
pip install -r requirements.txt

selenium
webdriver-manager
pytest

## ▶️ Como Executar os Testes

### Teste de Login

```bash
python selenium/test_login.py
Username: admin
Password: password

### Teste de Listagem de Quartos
python selenium/test_room_list.py

