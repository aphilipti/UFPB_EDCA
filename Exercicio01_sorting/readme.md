# Ordenação por Comparação

## 📚 Disciplina

Estrutura de Dados e Complexidade de Algoritmos
UFPB

---

## 🎯 Objetivo

Implementar e comparar os algoritmos:

* Selection Sort
* Insertion Sort

---

## 📁 Estrutura

```
sorting/
│
├── main.py
├── selection_sort.py
├── insertion_sort.py
├── data/
└── resultados.txt
```

---

## ▶️ Execução

### 🔹 Executar um arquivo específico

```
python main.py data/num.1000.2.in selection
python main.py data/num.1000.2.in insertion
```

---

### 🔹 Executar todos os testes

```
python main.py all
```

Executa:

* todos os arquivos da pasta `data`
* com os dois algoritmos

---

### 🔹 Executar apenas Selection Sort

```
python main.py selection_all
```

---

### 🔹 Executar apenas Insertion Sort

```
python main.py insertion_all
```

---

### 🔹 Limpar arquivo de resultados

```
python main.py clear
```

---

## 📄 Formato dos arquivos `.in`

```
n
valor1
valor2
...
```

* `n`: quantidade de elementos
* restante: valores do vetor

---

## 📊 Saída

### Terminal:

* tamanho da entrada
* tempo de execução
* primeiros 10 elementos ordenados

### Arquivo `resultados.txt`:

```
arquivo | algoritmo | tempo
--------------------------------
num.1000.2.in | selection | 0.002341
num.1000.2.in | insertion | 0.001287
```

---

## ⚙️ Complexidade

| Algoritmo      | Complexidade |
| -------------- | ------------ |
| Selection Sort | O(n²)        |
| Insertion Sort | O(n) a O(n²) |

---

## 🛠️ Requisitos

* Python 3.x

---

## 👨‍💻 Autor

Anderson Philip
