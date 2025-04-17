class quadratura_invalida(Exception):
    pass


class nodo_invalido(Exception):
    pass


class espessura_zero(Exception):
    pass


class regiao_invalida(Exception):
    pass


class regiao_float(Exception):
    pass


def detectar_erros(sigmaT, N, NN, regioes, esp_R):
    if N % 2 != 0 or N <= 0:
        raise quadratura_invalida(
            "O Valor digitado para quadratura é ímpar, zero, não inteiro ou negativo."
        )

    for nodo in NN:
        if nodo <= 0:
            raise nodo_invalido(
                "O número de nodos digitado não é inteiro ou é menor/igual a zero."
            )

    for espessura in esp_R:
        if espessura <= 0:
            raise espessura_zero("A espessura da região deve ser maior que zero.")

    for regiao in regioes:
        if regiao < 1 or regiao > len(sigmaT) or type(regiao) != int:
            raise regiao_invalida(
                f"O número da zona está fora das regiões permitidas: Inteiros entre [1:{len(sigmaT)}]"
            )
