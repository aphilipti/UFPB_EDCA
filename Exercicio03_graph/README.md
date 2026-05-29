# Graph Algorithms

## 📚 Disciplina

Estrutura de Dados e Complexidade de Algoritmos
Universidade Federal da Paraíba (UFPB)

---

## 🎯 Objetivo

Implementar e testar os algoritmos de grafos:

* Prim
* Kruskal
* Dijkstra

---

## 📁 Estrutura do Projeto

```text
graph-algorithms/
│
├── main.py
├── graph_utils.py
├── prim.py
├── kruskal.py
├── dijkstra.py
├── resultados.txt
└── data/
```

---

## ▶️ Como Executar

Execute o programa via linha de comando informando:

* o arquivo de entrada (.txt)
* o algoritmo desejado

### Sintaxe:

```bash
python main.py <arquivo> <algoritmo>
```

### Exemplos:

```bash
python main.py data/dij10.txt prim
python main.py data/dij10.txt kruskal
python main.py data/dij10.txt dijkstra
```

---

## ▶️ Execução Automática

### Executar todos os algoritmos:

```bash
python main.py all
```

### Executar apenas Prim:

```bash
python main.py prim_all
```

### Executar apenas Kruskal:

```bash
python main.py kruskal_all
```

### Executar apenas Dijkstra:

```bash
python main.py dijkstra_all
```

### Limpar o arquivo de resultados:

```bash
python main.py clear
```

---

## 📄 Formato dos Arquivos de Entrada

Os arquivos `.txt` seguem o padrão:

```text
n
peso1 peso2 peso3 ...
peso1 peso2 ...
peso1 ...
```

Onde:

* A primeira linha (`n`) indica a quantidade de vértices
* As linhas seguintes representam os pesos das arestas
* O grafo é armazenado em matriz triangular superior

---

## ⚙️ Algoritmos Implementados

### 🔹 Prim

* Utilizado para encontrar a Árvore Geradora Mínima (MST)
* Complexidade: O(V²)

---

### 🔹 Kruskal

* Utilizado para encontrar a Árvore Geradora Mínima (MST)
* Utiliza Union-Find
* Complexidade: O(E log E)

---

### 🔹 Dijkstra

* Utilizado para encontrar o menor caminho
* Calcula o caminho entre o vértice 0 e o vértice n-1
* Complexidade: O(V²)

---

## 📊 Saída do Programa

O programa exibe:

* Nome do arquivo
* Algoritmo executado
* Resultado obtido
* Resultado esperado
* Status da execução
* Tempo de execução

Exemplo:

```text
==================================================
Arquivo: dij20.txt
Algoritmo: prim

Resultado obtido: 15238
Resultado esperado: 15238

Status: OK
Tempo: 0.000183s
==================================================
```

---

## 📄 Arquivo de Resultados

Além da saída no terminal, o programa salva automaticamente os resultados em:

```text
resultados.txt
```

Formato:

```text
arquivo | algoritmo | resultado | esperado | status | tempo
```

Exemplo:

```text
dij10.txt | prim | 7072 | 7072 | OK | 0.000123
dij10.txt | kruskal | 7072 | 7072 | OK | 0.000241
dij10.txt | dijkstra | 5183 | 5183 | OK | 0.000084
```

---

## 📌 Resultados Esperados

### MST

* dij10 → 7072
* dij20 → 15238
* dij40 → 26615
* dij50 → 30424

### Caminho Mínimo

* dij10 → 5183
* dij20 → 3190
* dij40 → 8928
* dij50 → 6764

---

## 🛠️ Requisitos

* Python 3.x

---

## 👨‍💻 Autor

Anderson Philip
