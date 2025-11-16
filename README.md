# GENESIS (General and Effective Neutron Evaluation System for Interactive Shielding)

Projeto de IC do Instituto Politécnico da Universidade do Estado do Rio de
Janeiro

# ATENÇÃO:

O MÉTODO **DIAMOND DIFFERENCE** APRESENTA UM ERRO QUANDO UTILIZA-SE DUAS REGIOES COM ZONAS MATERIAIS IGUAIS, PORÉM, ESPESSURA DE NODO DIFERENTES

# QUICKSTART

## INICIALIZAÇÃO DO REPOSITÓRIO:

### Clonando o Repositório:

0: No Linux, abra qualquer terminal. No Windows, abra o Git Bash.

1: No terminal, digite:

```md
git clone https://github.com/ogcelio/genesis.git
```

2: Caminhe para a pasta do simulador:

```md
cd genesis
```

### Criando ambiente de trabalho:

3: Por segurança, crie um ambiente virtual:

No Linux:

```md
python3 -m venv venv
```

No Windows:

```md
python -m venv venv
```

Obs.: O segundo venv representa o nome da pasta do ambiente virtual que, por
convenção, é venv.

4: IMPORTANTE: Habilite o ambiente virtual:

No Linux:

```md
source venv/bin/activate
```

No Windows:

```md
.\venv\Scripts\activate
```

5: Instale todos os requerimentos para o funcionamento do simulador:

```md
pip install -r requirements.txt
```

6: Certifique-se que o código está sendo interpretado com o python correto, o
que pode ser conferido na parte de baixo do VS Code Exemplo: Python 3.13.1
('venv':venv)

5: Pronto, você pode rodar normalmente o simulador. Toda alteração ou instalação
feita com o ambiente virtual ativado não afeta o computador de forma global.
Para desativar, basta digitar no terminal:

```md
deactivate
```

## OBSERVAÇÃO:

Para fazer um push, você deve, primeiramente, registrar sua conta no seu sistema.
