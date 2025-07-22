import sys
import json
from platform import system
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QInputDialog,
    QCheckBox,
)

if system() == "Windows":
    reatores_path = "dados\\reatores.json"
    cache_reator = "dados\\cache_reator.txt"
    config_path = "config.json"
else:
    reatores_path = "dados/reatores.json"
    cache_reator = "dados/cache_reator.txt"
    config_path = "config.json"

termos = ("Sigma T", "Sigma S0", "Sigma S1", "Sigma S2", "Fonte", "Ni*Sigma F")


class propriedades(QMainWindow):
    def __init__(self):
        global janelas, widgets, config, reatores, tabelas
        # Iniciando variáveis
        widgets = []
        tabelas = []

        # Carregando dados
        try:
            with open(reatores_path, "r", encoding="utf8") as file:
                reatores = json.load(file)
        except json.decoder.JSONDecodeError:
            QMessageBox.information(
                None,
                "ATENÇÃO: ARQUIVO DE PROPRIEDADES NÃO ENCONTRADO",
                "Certifique-se de possuir um arquivo com reatores cadastrados.\n",
            )
            return

        with open(config_path, "r", encoding="utf8") as file:
            config = json.load(file)

        super().__init__()

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: rgb(52, 73, 94);
            }
            """
        )

        self.setWindowTitle("Propriedades - 1 Grupo")
        self.setGeometry(0, 0, 705, 466)

        # Criação do QTabWidget
        self.tabela_reatores = QTabWidget()
        self.setCentralWidget(self.tabela_reatores)

        # Criando Cadastrar e remover Reator
        self.cadastrar_reator = QPushButton("CADASTRAR CONJUNTO")
        self.cadastrar_reator.setMinimumHeight(30)
        self.cadastrar_reator.setStyleSheet(
            """
            font-size: 11pt; /* Tamanho da fonte dos cabeçalhos */
            font-weight: bold; /* Negrito nos cabeçalhos */                            
            """
        )

        self.remover_reator = QPushButton("REMOVER CONJUNTO")
        self.remover_reator.setMinimumHeight(30)
        self.remover_reator.setStyleSheet(
            """
            font-size: 11pt; /* Tamanho da fonte dos cabeçalhos */
            font-weight: bold; /* Negrito nos cabeçalhos */                            
            """
        )

        self.atualizar_reator = QPushButton("ATUALIZAR CONJUNTO")
        self.atualizar_reator.setMinimumHeight(30)
        self.atualizar_reator.setStyleSheet(
            """
            font-size: 11pt; /* Tamanho da fonte dos cabeçalhos */
            font-weight: bold; /* Negrito nos cabeçalhos */                            
            """
        )

        self.selecionar_reator = QPushButton("SELECIONAR CONJUNTO")
        self.selecionar_reator.setMinimumHeight(30)
        self.selecionar_reator.setStyleSheet(
            """
            font-size: 11pt; /* Tamanho da fonte dos cabeçalhos */
            font-weight: bold; /* Negrito nos cabeçalhos */                            
            """
        )

        # Adicionando botões
        layout_botoes = QGridLayout()
        layout_botoes.addWidget(self.cadastrar_reator, 0, 1)
        layout_botoes.addWidget(self.remover_reator, 1, 1)
        layout_botoes.addWidget(self.atualizar_reator, 0, 0)
        layout_botoes.addWidget(self.selecionar_reator, 1, 0)

        # Layout principal da janela
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabela_reatores)
        main_layout.addLayout(layout_botoes)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.center_window()

        self.cadastrar_reator.clicked.connect(self.cadastro)

        self.atualizar_reator.clicked.connect(self.atualizacao)

        self.remover_reator.clicked.connect(self.remocao)

        self.selecionar_reator.clicked.connect(self.selecao)

        for nome, propriedades in reatores.items():
            janela = QWidget()
            layout = QVBoxLayout(janela)
            tabela = QTableWidget()
            tabela.setStyleSheet(
                """
                QTableWidget {
                    font-size: 11pt; /* Altera o tamanho da fonte para toda a tabela */
                }
                QHeaderView::section {
                    font-size: 10pt; /* Tamanho da fonte dos cabeçalhos */
                    font-weight: bold; /* Negrito nos cabeçalhos */
                }
                """
            )
            tabela.setRowCount(len(propriedades["Sigma T"]))
            tabela.setColumnCount(len(propriedades))

            # Adicionando nome das zonas
            for i in range(len(propriedades["Sigma T"])):
                titulo = QTableWidgetItem(f"Zona {i+1}")
                tabela.setVerticalHeaderItem(i, titulo)

            # Adicionado tipos dos dados
            for i, termo in enumerate(termos):
                titulo = QTableWidgetItem(termo)
                tabela.setHorizontalHeaderItem(i, titulo)

            # Adicionando valores as celulas
            for j, valor in enumerate(propriedades.values()):
                for i, item in enumerate(valor):
                    tabela.setItem(i, j, QTableWidgetItem(item))

            layout.addWidget(tabela)

            self.tabela_reatores.addTab(janela, nome)
            tabelas.append(tabela)
            widgets.append(janela)

    def cadastro(self):
        global reatores, tabelas, widgets, termos

        # CRIANDO MENSAGEM DE CADASTRO
        msg_box = QInputDialog()
        msg_box.setWindowTitle("Cadastro de Conjunto")
        msg_box.setLabelText("Digite o nome do conjunto a ser cadastrado: ")
        msg_box.setInputMode(QInputDialog.TextInput)  # Para entrada de texto

        # Renomeando botões Aplicar e Cancelar
        msg_box.setOkButtonText("Aplicar")
        msg_box.setCancelButtonText("Cancelar")

        aplicar = msg_box.exec()

        if aplicar:
            # Coleta o texto digitado
            texto = msg_box.textValue()
            if texto:
                for key in reatores.keys():
                    if key.lower() == texto.lower():
                        QMessageBox.information(
                            None,
                            "ATENÇÃO: CONUNTO DUPLICADO",
                            "Digite o nome de um conjunto que ainda não foi cadastrado.\n"
                            f"Caso queira alterar os valores do conjunto {key}, navegue até ele, altere os valores e clique em atualizar.",
                        )
                        return

                qtd_zonas, ok = QInputDialog.getInt(
                    None,
                    "Quantidade de Zonas",
                    "Digite a quantidade de zonas que deseja adiconar: ",
                    value=10,  # Valor inicial
                    minValue=1,  # Mínimo
                    step=1,  # Incremento por passo (seta para cima/baixo)
                )

                if ok:
                    janela = QWidget()
                    layout = QVBoxLayout(janela)
                    tabela = QTableWidget()
                    tabela.setStyleSheet(
                        """
                        QTableWidget {
                            font-size: 11pt; /* Altera o tamanho da fonte para toda a tabela */
                        }
                        QHeaderView::section {
                            font-size: 10pt; /* Tamanho da fonte dos cabeçalhos */
                            font-weight: bold; /* Negrito nos cabeçalhos */
                        }
                        """
                    )
                    tabela.setRowCount(qtd_zonas)
                    tabela.setColumnCount(len(termos))

                    # Adicionando nome das zonas
                    for i in range(qtd_zonas):
                        titulo = QTableWidgetItem(f"Zona {i+1}")
                        tabela.setVerticalHeaderItem(i, titulo)

                    # Adicionado tipos dos dados
                    for i, termo in enumerate(termos):
                        titulo = QTableWidgetItem(termo)
                        tabela.setHorizontalHeaderItem(i, titulo)

                    # Adicionando valores as celulas
                    for j in range(len(termos)):
                        for i in range(qtd_zonas):
                            tabela.setItem(i, j, QTableWidgetItem("0.0"))

                    layout.addWidget(tabela)

                    self.tabela_reatores.addTab(janela, texto)
                    tabelas.append(tabela)
                    widgets.append(janela)

                    if config["mostrar_lembrete_props"]:
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Lembrete")
                        msg_box.setText(
                            "Preencha os campos com os valores escolhidos e depois clique em ATUALIZAR CONJUNTO"
                        )

                        nao_mostrar = QCheckBox("Não me lembrar novamente")
                        msg_box.setCheckBox(nao_mostrar)

                        msg_box.exec()

                        if nao_mostrar.isChecked():
                            self.nao_mostrar_novamente()

                else:
                    return

    def remocao(self):
        global reatores
        n_janela = self.tabela_reatores.currentIndex()
        titulo_janela = self.tabela_reatores.tabText(n_janela)

        # CRIANDO MENSAGEM DE CONFIRMAÇÃO
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirmação")
        msg_box.setText(f"Deseja mesmo remover o conjunto {titulo_janela}?")
        msg_box.setInformativeText("Esta ação não pode ser desfeita.")
        msg_box.setIcon(QMessageBox.Question)  # Define o ícone de pergunta

        # Criando botões sim e não
        botao_sim = msg_box.addButton("Sim", QMessageBox.AcceptRole)
        botao_nao = msg_box.addButton("Não", QMessageBox.RejectRole)

        # Define o botão padrão
        msg_box.setDefaultButton(botao_nao)

        # Exibe a caixa de mensagem
        msg_box.exec()
        resposta = msg_box.clickedButton()

        if resposta == botao_sim:
            if self.tabela_reatores.count() <= 1:
                QMessageBox.information(
                    None,
                    "ATENÇÃO: ÚLTIMO CONJUNTO",
                    "Você precisa ter ao menos um conjunto cadastrado.\n"
                    "Caso realmente queira remover este conjunto, cadastre um novo e posteriormente remova este.",
                )
            else:
                self.tabela_reatores.removeTab(n_janela)
                reatores.pop(titulo_janela)

                # Colocando valores no arquivo de dados
                with open(reatores_path, "w", encoding="utf8") as file:
                    json.dump(reatores, file, indent=2)

    def selecao(self):
        n_janela = self.tabela_reatores.currentIndex()
        titulo_janela = self.tabela_reatores.tabText(n_janela)

        with open(cache_reator, "w", encoding="utf8") as file:
            file.write(f"{titulo_janela}")

    def atualizacao(self):
        global tabelas, widgets, reatores, termos

        # Identificando janela
        n_janela = self.tabela_reatores.currentIndex()
        titulo_janela = self.tabela_reatores.tabText(n_janela)

        # Verificando se existe uma tabela na janela
        widget_atual = self.tabela_reatores.currentWidget()
        if widget_atual == widgets[n_janela]:
            tabela = tabelas[n_janela]
        else:
            QMessageBox.information(
                None,
                "ATENÇÃO: TABELA INEXISTENTE",
                "Você não possui uma tabela nesta janela.\n"
                "Por favor, remova o conjunto que não possui tabela e cadastre/ou utilize um novo reator.",
            )
            return 0

        # Atualizando valores
        try:
            propriedades = reatores[titulo_janela]
        except KeyError:
            reatores.update({titulo_janela: {}})
            propriedades = reatores[titulo_janela]

        linhas = tabela.rowCount()

        for coluna, chave in enumerate(termos):
            dados = []
            for linha in range(linhas):
                dados.append(tabela.item(linha, coluna).text())
            propriedades[chave] = dados

        reatores[titulo_janela] = propriedades

        # Colocando valores no arquivo de dados
        with open(reatores_path, "w", encoding="utf8") as file:
            json.dump(reatores, file, indent=2)

    def nao_mostrar_novamente(self):
        global config

        config["mostrar_lembrete_props"] = 0
        with open(config_path, "w", encoding="utf8") as file:
            json.dump(config, file, indent=2)

    def center_window(self):
        # Pega o retângulo da tela principal
        ret_tela = QApplication.primaryScreen().availableGeometry()

        # Pega o tamanho da janela atual
        ret_janela = self.frameGeometry()

        # Centraliza a posição da janela na tela
        centro = ret_tela.center()
        ret_janela.moveCenter(centro)

        # Ajusta a posição da janela
        self.move(ret_janela.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = propriedades()
    window.show()
    sys.exit(app.exec())
