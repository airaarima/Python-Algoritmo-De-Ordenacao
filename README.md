# Algoritmos de Ordenação

Implementação e comparação de diferentes algoritmos de ordenação em Python, incluindo algoritmos clássicos e uma implementação autoral.

## Como executar

Execute os comandos a partir da raiz do projeto, na ordem abaixo.

### 1. Executar o exemplo principal

```bash
python __main__.py
```

Executa um exemplo de ordenação com um vetor de entrada e exibe no terminal o vetor inicial e o vetor ordenado.

### 2. Executar os testes

```bash
python -m tests.test_suite
```

Executa a suíte de testes dos algoritmos. Ela verifica casos como listas vazias, elementos repetidos, valores negativos, vetores já ordenados, vetores invertidos e entradas aleatórias.

### 3. Executar o benchmark

```bash
python -m tests.benchmark --trials 3 --plot benchmark_results.png
```

Compara o desempenho dos algoritmos em diferentes tamanhos e distribuições de dados. O parâmetro `--trials 3` define três repetições para cada cenário, enquanto `--plot benchmark_results.png` salva os gráficos gerados nesse arquivo.

O benchmark também exibe no terminal uma tabela com os tempos médios e as métricas de comparações e movimentações.

> O benchmark requer a dependência `matplotlib` instalada no ambiente Python.
```bash
python -m pip install matplotlib  
```