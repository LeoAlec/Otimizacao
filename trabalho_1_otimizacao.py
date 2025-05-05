# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 13:12:11 2025

@author: leo.alec
"""

from pyomo.environ import *

# --- 1. DADOS DO PROBLEMA ---
# Aqui, guardamos as informações sobre os podrutos

# Dados dos produtos 'A' e 'B'
lucro = {'A': 30, 'B': 50}  #Opção A: 30R$, Opção B: 50R$
horas_maquina = {'A': 2, 'B': 3} #Opção A: 2 horas, Opção B: 3 horas
materia_prima = {'A': 3, 'B': 2} #Opção A: 3 unidades de matéria-prima, Opção B: 2 unidades de matéria-prima

# Definição de Restrições
limite_horas = 100 # Máximo de 100 horas de máquina
limite_materia = 120 # 120 unidades de matériaprima disponíveis

# Maximos de horas e de unidades de materiais
restricoes = {'horas': 100, 'materiais': 120} # Máximo de 100 horas de máquina e 120 unidades de matériaprima disponíveis.

# --- 2. CRIANDO O MODELO ---
# Aqui, vamos montar o modelo matemático usando o Pyomo.

modelo = ConcreteModel() # Cria um modelo concreto (onde os dados são definidos diretamente)

# --- 3. CONJUNTOS DE OPÇÕES ---
# Vamos criar "listas" (conjuntos) para as opções de ida e volta.

modelo.P = Set(initialize=lucro.keys()) # {'A', 'B'} (opcoes de lucro)

# --- 4. VARIÁVEIS DE ESCOLHA ---
# Criamos variáveis para representar se cada produto foi escolhida ou não.

modelo.x = Var(modelo.P, within=NonNegativeIntegers) # Nosso problema pede numeros inteiros nao negativos; Conjunto: ['A', 'B']

# --- 5. FUNÇÃO OBJETIVO ---
# Maximizar o lucro total; Função objetivo do modelo; o solver tentará maximizar isso
modelo.lucro_total = Objective(
    expr=sum(lucro[p] * modelo.x[p] for p in modelo.P), # Expressão matemática: soma do lucro unitário (lucro[p]) multiplicado pelo número de unidades produzidas (modelo.x[p]) para cada produto p no conjunto de produtos P
    sense=maximize # Maximizamos o lucro total
)

# --- 6. RESTRIÇÕES ---
# Restrição relacionada ao uso de horas de máquina.
modelo.restr_horas = Constraint(
    expr=sum(horas_maquina[p] * modelo.x[p] for p in modelo.P) <= limite_horas # O total de horas de máquina utilizadas por produto deve ser menor ou igual ao limite máximo disponível
)

# Restrição relacionada ao uso da matéria prima.
modelo.restr_materia = Constraint(
    expr=sum(materia_prima[p] * modelo.x[p] for p in modelo.P) <= limite_materia # O total de matéria-prima consumida (por produto) deve ser menor ou igual ao limite disponível
)

# --- 7. RESOLVENDO O PROBLEMA ---
solucionador = SolverFactory('glpk') # Instancia o objeto solver 'glpk'
resultados = solucionador.solve(modelo) # Utiliza o objeto para solucionar o problema

# --- 8. MOSTRANDO O RESULTADO ---
print("Status da solução:", resultados.solver.status)

if resultados.solver.status == SolverStatus.ok:
    print("Lucro máximo:", modelo.lucro_total())
    for p in modelo.P:
        print(f"Produzir {modelo.x[p]()} unidades do produto {p}")
else:
    print("Não foi possível encontrar uma solução ótima.")
    
# --- 9. RESULTADO DO SCRIPT ---

'''
%runfile C:/Users/leozi/.spyder-py3/temp.py --wdir
Status da solução: ok
Lucro máximo: 1660.0
Produzir 2.0 unidades do produto A
Produzir 32.0 unidades do produto B
'''