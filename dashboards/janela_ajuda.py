from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtGui import QTextBlockFormat, QTextCursor

from PySide6.QtCore import Qt
import sys


class Janela_Instrucoes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AJUDA")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Criando QTextEdit para exibir as instruções (somente leitura)
        self.texto = QTextEdit()

        font = QFont("Segoe UI", 12)
        self.texto.setFont(font)
        self.texto.setPlainText(
            "Bem-vindo ao guia do simulador!\n\n"
            "1. MENSAGENS DE ERRO:\n\n"
            "ATENÇÃO: Estes erros também podem ocorrer quando alguma caixa de escrita esteja selecionada no momento em que um código for iniciado. Certifique-se de não nenhuma caixa de escrita esteja selecionada, ou seja, com cor diferente das outras. Isso também pode implicar na execução do código com valores antigos/não atualizados.\n\n"
            "1.1 VI: VALOR INVÁLIDO:\n\n"
            "1.1.1 VI-001:\n\n"
            "\tEste erro ocorre sempre que algum valor inválido, como uma letra digitada para o valor da ordem de quadratura, for inserido. Certifique-se de que todos os valores estão corretos. \n\n"
            "1.1.2 VI-002:\n\n"
            "\tEste erro ocorre sempre que um valor ímpar, não inteiro ou menor/igual a zero é digitado para a ordem da quadratura e algum método é iniciado. Para realizar os cálculos corretamente, certifique-se de que o valor da ordem da quadratura é um valor par, inteiro e maior que zero.\n\n"
            "1.1.3 VI-003:\n\n"
            "\tEste erro ocorre sempre que um valor menor ou igual a 0 ou que não seja inteiro é digitado para o número de nodos de alguma das regiões. Para realizar os cálculos corretamente, certifique-se de digitar um número de nodos válido para todas as regiões.\n\n"
            "1.1.4 VI-004:\n\n"
            "\tEste erro ocorre sempre que um valor menor ou igual a zero é digitado para a espessura de alguma das regiões. Certifique-se de que cada região possua uma determinada espessura maior que zero.\n\n"
            "1.1.5 VI-005:\n\n"
            '\tEste erro ocorre sempre que um valor inválido é digitado para alguma das zonas escolhidas. Certifique-se que o número da zona esteja entre 1 e o valor máximo, que pode ser conferido na janela de "Propriedades Físico Materiais".\n\n'
            "1.1.6 VI-006:\n\n"
            "\tEste erro ocorre sempre que um valor não inteiro ou menor/igual a zero é inserido para a quantidade de regiões. Certifique-se de que você escolheu um valor inteiro maior que zero para a quantidade de regiões.\n\n"
            "1.2 AI: AÇÃO INVÁLIDA:\n\n"
            "1.2.1 AI-001:\n\n"
            '\tEste erro ocorre sempre que o operador tenta gerar um gráfico na opção "Abrir Gráfico" em um momento em que nenhum cálculo foi feito previamente. Certifique-se de que algum dos métodos foi iniciado e finalizado para que os devidos resultados sejam mostrados\n\n'
            "1.2.2 AI-002:\n\n"
            '\tEste erro ocorre sempre que o operador, na janela de "Resultados Numéricos", tenta mostrar os resultados de um cálculo, em uma situação onde nenhum cálculo foi realizado previamente. Certifique-se de que algum dos métodos foi iniciado e finalizado para que os devidos resultados sejam mostrados\n\n'
            "1.2.3 AI-003:\n\n"
            "\tEste erro ocorre quando um conjunto não está registrado no histórico. Certifique-se de abrir a janela PROPRIEDADES e selecionar um conjunto para que o método seja executado.\n\n"
        )
        self.texto.setReadOnly(True)  # Impede edição do texto
        layout.addWidget(self.texto)

        # Justificando o texto
        text_format = QTextBlockFormat()
        text_format.setAlignment(Qt.AlignJustify)
        cursor = self.texto.textCursor()

        # Selecionando o documento inteiro
        cursor.select(QTextCursor.Document)
        cursor.mergeBlockFormat(text_format)
        self.texto.setTextCursor(cursor)

        cursor.clearSelection()
        cursor.movePosition(QTextCursor.Start)
        self.texto.setTextCursor(cursor)

        # Criando os botões para alterar a fonte
        self.aumentar_fonte = QPushButton("Aumentar Fonte")
        self.diminuir_fonte = QPushButton("Diminuir Fonte")

        # Conectando os botões às funções
        self.aumentar_fonte.clicked.connect(self.aumentar)
        self.diminuir_fonte.clicked.connect(self.diminuir)

        layout.addWidget(self.aumentar_fonte)
        layout.addWidget(self.diminuir_fonte)

        self.setLayout(layout)

    def aumentar(self):
        """Aumenta o tamanho da fonte do QTextEdit"""
        font = self.texto.font()
        font.setPointSize(font.pointSize() + 2)
        self.texto.setFont(font)

    def diminuir(self):
        """Diminui o tamanho da fonte do QTextEdit"""
        font = self.texto.font()
        if font.pointSize() > 10:  # Define um tamanho mínimo
            font.setPointSize(font.pointSize() - 2)
            self.texto.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela_Instrucoes()
    window.show()
    sys.exit(app.exec())
