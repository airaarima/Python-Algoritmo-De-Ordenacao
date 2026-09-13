from typing import Any, List, Tuple
import unittest
from src.classical import bubble_sort, insertion_sort

def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
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

    p1, p2, comps_pivo, moves_pivo = encontrar_pivos(a, n)
    comps += comps_pivo
    moves += moves_pivo

    jogador_esquerda = []
    jogador_meio = []
    jogador_direita = []

    # mestre distribui as cartas para os jogadores
    for i in range(n):
        comps += 1

        if a[i] < p1:
            jogador_esquerda, c, m = inserir_ordenado(jogador_esquerda, a[i])
            comps += c
            moves += m

        elif a[i] > p2:
            comps += 1
            jogador_direita, c, m = inserir_ordenado(jogador_direita, a[i])
            comps += c
            moves += m

        else:
            jogador_meio, c, m = inserir_ordenado(jogador_meio, a[i])
            comps += c
            moves += m

    a, moves_final = recolher_cartas_ordenadas(jogador_esquerda, jogador_meio, jogador_direita)
    moves += moves_final

    return a, comps, moves

def encontrar_pivos(arr: List[Any], tamanho_vetor: int) -> Tuple[int, int, int, int]:
    """
    Função auxiliar para encontrar pivôs amostrais 
    em espaços distribuídos proporcionalmente pelo vetor.
    """

    tamanho_amostra = max(9, int(tamanho_vetor ** 0.5) + 1)
    quantidade_elementos_amostra = min(tamanho_amostra, tamanho_vetor)
 
    if quantidade_elementos_amostra <= 2:
        return arr[0], arr[-1], 0, 0
 
    indices = []

    for i in range(quantidade_elementos_amostra):
        indice = round(
            i * (tamanho_vetor - 1) / (quantidade_elementos_amostra - 1)
        )
        indices.append(indice)
    indices = set(indices)

    amostra = [arr[i] for i in indices]
    
    amostra_ordenada, comparacoes, movimentacoes = insertion_sort(amostra)
    amostra_ordenada_tamanho = len(amostra_ordenada)
    p1 = amostra_ordenada[amostra_ordenada_tamanho // 3]
    p2 = amostra_ordenada[(2 * amostra_ordenada_tamanho) // 3]

    return p1, p2, comparacoes, movimentacoes

def inserir_ordenado(mao: List[Any], elemento: Any) -> Tuple[List[Any], int, int]:
    """
    Função auxiliar para o jogador inserir a carta ordenamente na mão.
    Verifica se a carta é menor que a última carta da mão e, caso seja, realiza a troca até que a carta esteja na posição correta.
    """
    comparacoes = 0
    movimentacoes = 0

    # insere a carta no final
    mao.append(elemento)
    movimentacoes += 1

    j = len(mao) - 1
    while j > 0:
        comparacoes += 1
        if mao[j - 1] > mao[j]:
            mao[j - 1], mao[j] = mao[j], mao[j - 1]
            movimentacoes += 1
            j -= 1
        else:
            break

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
