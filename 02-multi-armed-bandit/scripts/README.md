# Scripts — Aula 02 · Multi-armed bandits

Três scripts independentes, todos com `numpy` (o `matplotlib` só é usado na
figura, que pode ser dispensada com `--sem-figura`).

| Script | Para quê | Figura do Sutton |
|---|---|---|
| [`bandit_metodos.py`](./bandit_metodos.py) | As cinco políticas da aula lado a lado (§§ 03, 04, 07, 08, 09) | 2.2, 2.3, 2.4 |
| [`bandit_nao_estacionario.py`](./bandit_nao_estacionario.py) | Média amostral × passo constante com os `q*(a)` derivando (§§ 05, 06) | exercício 2.5 |
| [`bandit_varredura.py`](./bandit_varredura.py) | Qual ε, qual `c`, qual α, qual `Q1` — o estudo de parâmetros | 2.6 |

```bash
pip install numpy matplotlib
```

As simulações são **vetorizadas nas execuções**: uma linha da matriz por
execução, e o laço de Python percorre apenas os passos. É o que torna as 2000
execuções do livro uma questão de segundos.

## 1. As políticas lado a lado

```bash
python bandit_metodos.py
python bandit_metodos.py --politicas guloso eps ucb --execucoes 2000
python bandit_metodos.py --eps 0.01 --c 1 --sem-figura
```

Dez ações com `q*(a) ~ N(0,1)` e recompensa ruidosa. Todas as políticas usam a
mesma semente, então enfrentam **os mesmos problemas** — a diferença entre as
curvas é só a regra de escolha.

O que esperar com os valores padrão em 1000 passos (média dos últimos 100):

| Política | Recompensa média | % de ação ótima |
|---|---:|---:|
| guloso (`Q1 = 0`) | ~1,05 | ~36% |
| ε-guloso (`ε = 0,1`) | ~1,36 | ~80% |
| otimista (`Q1 = 5`, `α = 0,1`) | ~1,50 | ~86% |
| UCB (`c = 2`) | ~1,48 | ~85% |
| gradiente (`α = 0,1`) | ~1,49 | ~85% |

Três coisas para procurar na figura: o **patamar** do guloso, que trava em uma
ação subótima; o **pico agudo** do UCB no passo 10, quando termina a varredura
inicial dos braços com `N(a) = 0`; e a **cova** do otimista no começo, quando
ele está explorando de propósito e pagando por isso.

## 2. O bandit que anda

```bash
python bandit_nao_estacionario.py
python bandit_nao_estacionario.py --passos 20000 --alfa 0.05
python bandit_nao_estacionario.py --sigma 0 --inicio normal --sem-figura
```

Exercício 2.5 do livro: os dez braços começam iguais e cada `q*(a)` recebe um
incremento `N(0, σ²)` por passo. Dois agentes ε-gulosos idênticos, diferentes
apenas no passo da atualização.

Com os valores padrão (10 000 passos, σ = 0,01), na segunda metade da execução:

| Passo | Recompensa média | % de ação ótima |
|---|---:|---:|
| `1/N` (média amostral) | ~0,93 | ~44% |
| `α = 0,1` | ~1,14 | ~72% |

A terceira faixa da figura mostra os `q*(a)` de uma execução: dá para ver o
melhor braço **mudando de dono**. É isso que a média amostral não consegue
acompanhar — com o peso da n-ésima recompensa caindo como `1/n`, ela para de
responder.

Vale rodar o contraexemplo: `--sigma 0 --inicio normal` devolve o problema
estacionário, e aí a vantagem se inverte.

## 3. Qual valor de parâmetro

```bash
python bandit_varredura.py
python bandit_varredura.py --execucoes 1000
python bandit_varredura.py --metodos eps ucb --sem-figura
```

Cada método tem exatamente um parâmetro; o script o varre em potências de 2 e
resume o desempenho em um número só — a recompensa média ao longo de toda a
execução. Este script importa as políticas de `bandit_metodos.py`, então
**rode-o a partir desta pasta**.

Todas as curvas têm forma de U invertido: parâmetro de menos e o agente explora
pouco, parâmetro demais e ele gasta jogadas à toa. Repare que o vencedor da
comparação **depende do horizonte** — aumente `--passos` e as curvas se deslocam,
porque exploração é um custo que se paga uma vez e um benefício que se colhe
até o fim.

## Sugestões de extensão

- Guardar também o **arrependimento** acumulado, `Σ [q*(ótimo) − q*(A_t)]`, e
  comparar seu crescimento: logarítmico para o UCB, linear para o ε-guloso com
  ε fixo.
- Fazer ε **decair** com o tempo (`ε_t = 1/t`, por exemplo) e ver onde isso se
  encaixa na tabela do § 10.
- Trocar o ruído normal por um bandit de Bernoulli (prêmio ou nada) e refazer a
  varredura: a escala das recompensas muda, e com ela o `c` bom para o UCB.
