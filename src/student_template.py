"""
TEMPLATE PARA O ALUNO — TRABALHO PRÁTICO 1 (TP1)
Disciplina: Análise e Projetos de Algoritmos (APA)

Instruções:
1. Implemente seu método de ordenação autoral na função `my_authorial_sort`.
2. O retorno deve ser obrigatoriamente a tupla: (lista_ordenada, total_comparacoes, total_movimentacoes).
3. Execute este arquivo diretamente para rodar a suíte de testes de corretude e o benchmark rápido.
"""

from typing import Any, List, Tuple
import unittest
from src.classical import bubble_sort, insertion_sort

def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
    IMPLEMENTE AQUI SEU ALGORITMO AUTORAL.

    Parâmetros:
        arr (List[Any]): Lista de entrada a ser ordenada.

    Retorno:
        Tuple[List[Any], int, int]:
            - Lista ordenada
            - Total de comparações realizadas
            - Total de movimentações/trocas realizadas
    """
    a = list(arr)
    n = len(a)
    if n <= 1:
        return a, 0, 0
    
    comps = 0
    moves = 0

    p1, p2, comps_pivo, moves_pivo = encontrar_pivos(a)
    comps += comps_pivo
    moves += moves_pivo

    jogador_esquerda = []
    jogador_meio = []
    jogador_direita = []

    # mestre distribui as cartas para os jogadores
    for i in range(n):
        comps += 1

        if a[i] < p1:
            jogador_esquerda, comps_esquerda, moves_esquerda = inserir_ordenado(jogador_esquerda, a[i])
            comps += comps_esquerda
            moves += moves_esquerda

        elif a[i] > p2:
            comps += 1
            jogador_direita, comps_direita, moves_direita = inserir_ordenado(jogador_direita, a[i])
            comps += comps_direita
            moves += moves_direita

        else:
            jogador_meio, comps_meio, moves_meio = inserir_ordenado(jogador_meio, a[i])
            comps += comps_meio
            moves += moves_meio

    a, moves_final = recolher_cartas_ordenadas(jogador_esquerda, jogador_meio, jogador_direita)
    moves += moves_final

    return a, comps, moves

def encontrar_pivos(arr: List[Any]) -> Tuple[int, int, int, int]:
    """
    Função auxiliar para encontrar pivôs amostrais.
    """

    primeiro = arr[0]
    meio = arr[len(arr) // 2]
    ultimo = arr[len(arr) - 1]

    response = [primeiro, meio, ultimo]

    comparacoes = 0
    movimentacoes = 0

    response, comps_bubble, moves_bubble = bubble_sort(response)
    comparacoes += comps_bubble
    movimentacoes += moves_bubble

    return response[0], response[1], comparacoes, movimentacoes

def inserir_ordenado(mao: List[Any], elemento: Any) -> Tuple[List[Any], int, int]:
    """
    Função auxiliar para o jogador inserir a carta ordenamente na mão.
    Utiliza o algoritmo Insertion Sort para ordenar as cartas.
    """
    comparacoes = 0
    movimentacoes = 0

    # insere a carta no final
    mao.append(elemento)
    movimentacoes += 1

    # aplica o Insertion Sort para ordenar as cartas na mão
    mao, comps, moves = insertion_sort(mao)
    comparacoes += comps
    movimentacoes += moves

    return mao, comparacoes, movimentacoes

def recolher_cartas_ordenadas(mao_esquerda: List[Any], mao_meio: List[Any], mao_direita: List[Any]) -> Tuple[List[Any], int]:
    """
    Função auxiliar para recolher as cartas ordenadas dos jogadores.
    Todas as cartas são recolhidas, resultando em um vetor final ordenado.
    """
    movimentacoes = 0

    vetor_ordenado = mao_esquerda + mao_meio + mao_direita
    movimentacoes += len(vetor_ordenado)

    return vetor_ordenado, movimentacoes

# =============================================================================
# SUÍTE DE TESTES AUTOMÁTICA DE VALIDAÇÃO
# =============================================================================
class TestStudentAuthorialSort(unittest.TestCase):
    def assert_sorted(self, original: List, result: List):
        self.assertEqual(len(result), len(original), "Tamanho divergente!")
        self.assertEqual(sorted(original), result, "A lista não foi ordenada corretamente!")

    def test_empty(self):
        res, _, _ = my_authorial_sort([])
        self.assert_sorted([], res)

    def test_single(self):
        res, _, _ = my_authorial_sort([99])
        self.assert_sorted([99], res)

    def test_sorted(self):
        data = list(range(100))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_reverse(self):
        data = list(range(100, 0, -1))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_identical(self):
        data = [5] * 50
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_random(self):
        import random
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(200)]
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)


if __name__ == "__main__":
    print("🧪 Executando testes unitários no seu algoritmo autoral...")
    unittest.main(verbosity=2)
