---
title: 'Trabalho: Projeto de Otimização com Pyomo'
author: "Leo Alec"
date: "2025-05-05"
output: html_document
---

## O que Queremos Otimizar?

Uma fábrica produz dois tipos de produtos (A e B) com os seguintes dados:

- **Produto A**: Lucro de R$ 30 por unidade, usa 2 horas de máquina e 3 unidades de matéria-prima  
- **Produto B**: Lucro de R$ 50 por unidade, usa 3 horas de máquina e 2 unidades de matéria-prima  

**Restrições:**

- Máximo de 100 horas de máquina disponíveis  
- Máximo de 120 unidades de matéria-prima disponíveis  

**Objetivo:** Maximizar o lucro decidindo quantas unidades de A e B produzir (variáveis inteiras)

---

## Por que?

O problema apresentado segue uma lógica de **programação linear inteira mista (MILP)**. Uma das especializações do `glpk` é a MILP.

- Função objetivo linear (maximizar lucro)  
- Restrições lineares (tempo de máquina e matéria-prima)  
- Variáveis inteiras não-negativas  

O `glpk` é especializado nesse tipo de problema. Existem outras opções mais rápidas, mas com requerimentos mais burocráticos, tornando o `glpk` mais viável (por ser gratuito) para soluções acadêmicas.

Desejamos integrar o `glpk` e o **Pyomo**. Felizmente, o `glpk` torna isso muito mais prático, permitindo que modelos matemáticos sejam escritos de forma **declarativa e legível**.

---

## Formulação Matemática do Problema

**Função Objetivo:**

$$
\text{Maximizar } Z = 30x + 50y
$$

**Restrições:**

Horas de máquina:  
$$
2x + 3y \leq 100
$$

Unidades de matéria-prima:  
$$
3x + 2y \leq 120
$$

**Números não negativos:**  
$$
x \geq 0, \quad y \geq 0
$$

**Variáveis inteiras:**  
$$
x, y \in \mathbb{Z}
$$

---

## Resultado do Script

- **Lucro máximo:** R$ 1660,00  
- **Produzir:** 2 unidades do produto A  
- **Produzir:** 32 unidades do produto B
