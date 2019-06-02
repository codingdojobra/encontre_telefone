from unittest import TestCase, main

regra = {
    'A': '2',
    'E': '3',
    'G': '4',
    'L': '5',
    'M': '6',
    'O': '6',
    'T': '8',
    'V': '8',
    'Y': '9',
    '0': '0',
    '1': '1',
    ' ': ' ',
    '-': '-',
}


def traduz_para_numero(letra):
    for chave, valor in regra.items():
        if letra == chave:
            return valor
    raise Exception("Inválido")


def traduz_frase_numeros(frase):
    try:
        resultado = ''
        for letra in frase:
            resultado = resultado + traduz_para_numero(letra)
        return resultado
    except Exception as error:
        raise error


class TestTelefone(TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_a_para_2(self):
        letra = 'A'
        resultado = traduz_para_numero(letra)
        self.assertEqual(resultado, '2')

    def test_g_para_4(self):
        letra = 'G'
        resultado = traduz_para_numero(letra)
        self.assertEqual(resultado, '4')

    def test_t_para_8(self):
        letra = 'T'
        resultado = traduz_para_numero(letra)
        self.assertEqual(resultado, '8')

    def test_caractere_especial(self):
        letra = '-'
        resultado = traduz_para_numero(letra)
        self.assertEqual(resultado, '-')

    def test_frase(self):
        frase = 'MY LOVE'
        resultado = traduz_frase_numeros(frase)
        self.assertEqual(resultado, '69 5683')

    def test_caractere_especial2(self):
        letra = 'MY#'
        with self.assertRaises(Exception):
            traduz_frase_numeros(letra)


if __name__ == '__main__':
    main()
