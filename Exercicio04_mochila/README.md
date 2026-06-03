# Problema da Mochila Inteira

## 📚 Disciplina

Estrutura de Dados e Complexidade de Algoritmos
Universidade Federal da Paraíba (UFPB)

---

## 🎯 Objetivo

Implementar e testar uma solução utilizando Programação Dinâmica para o Problema da Mochila Inteira (0/1 Knapsack).

O objetivo é selecionar um subconjunto de itens de forma que:

* o peso total não ultrapasse a capacidade da mochila;
* o valor total obtido seja máximo.

---

## 📁 Estrutura do Projeto

```text
knapsack/
│
├── main.py
├── knapsack.py
├── utils.py
├── resultados.txt
└── data/
```

---

## ▶️ Como Executar

Execute uma instância específica:

```bash
python main.py data/mochila01.txt
```

---

Executar todas as instâncias:

```bash
python main.py all
```

---

Limpar o arquivo de resultados:

```bash
python main.py clear
```

---

## 📄 Formato dos Arquivos de Entrada

Os arquivos seguem o padrão:

```text
n M
p1 v1
p2 v2
...
pn vn
```

Onde:

* `n` = quantidade de itens
* `M` = capacidade da mochila
* `pi` = peso do item
* `vi` = valor do item

---

## ⚙️ Algoritmo Implementado

### 🔹 Programação Dinâmica

O algoritmo utiliza Programação Dinâmica para determinar o maior valor possível sem ultrapassar a capacidade da mochila.

Além do valor máximo, a implementação também reconstrói quais itens foram escolhidos.

### Complexidade

Tempo:

```text
O(n × M)
```

Memória:

```text
O(n × M)
```

---

## 📊 Saída do Programa

O programa exibe:

* arquivo processado;
* quantidade de itens;
* capacidade da mochila;
* valor máximo encontrado;
* produtos escolhidos;
* resultado esperado (quando disponível);
* tempo de execução.

Exemplo:

```text
==================================================
Arquivo: mochila01.txt
Itens: 7
Capacidade: 23

Valor máximo: 107
Produtos escolhidos: [1, 2, 6, 7]

Resultado esperado: 107
Status: OK

Tempo: 0.000123s
==================================================
```

---

## 📄 Arquivo de Resultados

Os resultados são gravados em:

```text
resultados.txt
```

Formato:

```text
instância: mochila01.txt
valor : 107
produtos escolhidos : 1, 2, 6, 7
```

---

## 🛠️ Requisitos

* Python 3.x

---

## 👨‍💻 Autor

Anderson Philip