import re
from dataclasses import dataclass


@dataclass
class CPF:
    CPF: str

    def __post_init__(self):
        CPF.validate_cpf(self.CPF)

    @classmethod
    # https://www.dio.me/articles/como-fazer-uma-validacao-de-cpf-com-python
    def validate_cpf(cls) -> bool:
        cpf = cls.CPF

        # Retira apenas os dígitos do CPF, ignorando os caracteres especiais
        numeros = [int(digito) for digito in cpf if digito.isdigit()]

        formatacao = False
        quant_digitos = False
        validacao1 = False
        validacao2 = False

        # Verifica a estrutura do CPF (111.222.333-44)
        if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
            formatacao = True

        if len(numeros) == 11:
            quant_digitos = True

            soma_produtos = sum(a * b for a, b in zip(numeros[0:9], range(10, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if numeros[9] == digito_esperado:
                validacao1 = True

            soma_produtos1 = sum(a * b for a, b in zip(numeros[0:10], range(11, 1, -1)))
            digito_esperado1 = (soma_produtos1 * 10 % 11) % 10
            if numeros[10] == digito_esperado1:
                validacao2 = True

            if quant_digitos and formatacao and validacao1 and validacao2:
                print(f"O CPF {cpf} é válido.")
            else:
                print(f"O CPF {cpf} não é válido... Tente outro CPF...")

        else:
            print(f"O CPF {cpf} não é válido... Tente outro CPF...")
