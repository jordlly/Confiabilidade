##############################################################################
# CONFIA.py                                                                  #
# Exemplo introdutório de análise de confiabilidade estrutural.              #
#                                                                            #
# Desenvolvimento: Jordlly Silva                                             #
# Criado em: 04/03/2022   Modificado em: 14/03/2022                          #
##############################################################################                        

import numpy as np               # Módulo Numpy
import matplotlib.pyplot as plt  # Função Pyplot

### Função da distribuição normal:
def f(x,μ,σ):
    return 1/(σ*np.sqrt(2*np.pi))*np.exp(-(x-μ)**2/(2*σ**2))

### Função probabilidade de falha (Monte Carlo):
def FalhaMonteCarlo(Amostra, Simulacoes):
    contador = 0
    for i in range(0, Simulacoes): 
        if Amostra[i] < 0: contador = contador+1
    ProbFalha = contador/Simulacoes*100 
    return ProbFalha

### Função de plotagem dos gráficos:
def PlotGraf(p, LimInfx, LimSupx, variavel, ProbFalha):
    count, x, ignored = plt.hist(p, 20, density=True)
    if (variavel == 'Material A') or (variavel == 'Material B'):
        plt.plot(x, f(x,μ,σ), linewidth=2, color='r')
        legenda = ('Distribuição normal', 'Histograma')
    else:
        variavel = variavel+' - Prob. Falha: '+str(round(ProbFalha,2))+'%'
        legenda = ('Histograma', '')
    plt.legend(legenda, shadow=True, loc='upper left', 
               bbox_to_anchor=(0.010, 0.99), handlelength=2.5, fontsize=14)
    plt.title(variavel, fontsize=14)     
    plt.grid(True) 
    plt.xlabel("Variável",   fontsize=14)
    plt.ylabel("Frequência", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14) 
    plt.axis([LimInfx, LimSupx, 0, 0.030]) 
    plt.show()
  
### Material A:
μ, σ, Simulacoes = 200, 40, 100000
RA = np.random.normal(μ, σ, Simulacoes)
PlotGraf(RA, 0, 400, 'Material A', 0)

### Material B:
μ, σ, Simulacoes = 200, 20, 100000
RB = np.random.normal(μ, σ, Simulacoes)
PlotGraf(RB, 0, 400, 'Material B', 0)

### Carga:
μ, σ, Simulacoes = 100, 20, 100000
S = np.random.normal(μ, σ, Simulacoes)

### Função de falha A:
GA = RA-S
ProbFalhaA = FalhaMonteCarlo(GA, Simulacoes)
PlotGraf(GA, -100, 300, 'Função de falha - Caso A', ProbFalhaA)

### Função de falha B:
GB = RB-S
ProbFalhaB = FalhaMonteCarlo(GB, Simulacoes)
PlotGraf(GB, -100, 300, 'Função de falha - Caso B', ProbFalhaB)
