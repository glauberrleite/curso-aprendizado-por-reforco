# Motivação

Considere que você precisa escolher entre $n$ _slot machines_/_bandits_ em qual jogar. Cada uma delas tem uma probabilidade de prêmio, desconhecida por você. Cada jogada fornece uma recompensa (pode ser só no _jackpot_ ou um valor proporcional).

[Slot machines em cassino](https://proddigital.com.br/wp-content/uploads/maquinas-caca-niqueis-2.jpg)

É um caso especial de problema em que temos apenas um estado e $n$ ações possíveis.

Cada ação vai ter uma recompensa esperada para quando ela for selecionada, vamos chamar essa expectativa de valor (_value_) da ação.

Digamos que o valor real da ação $a \in mathcal{A}$ é $q(a)$. Se tivéssemos acesso a ela, a escolha seria apenas uma otimização em que escolhemos a ação com maior $q(a)$.
No entanto, teremos apenas o valor estimado dessa função $Q_t (a)$ para um determinado momento $t$ do tempo.

Vamos explorar melhor o conceito de _exploration_ vs _exploitation_.

# Métodos Ação-Valor

Uma abordagem simples de considerar a esperança de recompensa, a partir de múltiplas tentativas $N_t(a)$ realizada para uma ação, é armazenar a recompensa de cada uma delas $R_i$, com $i = 1, \dots, N_t(a)$. Com isso, calcular a média:

$$Q_t(a) = \sum_{i = 1}^{N_t(a)} \frac{R_i}{N_t(a)}$$

Se $N_t(a) = 0$, então definimos $Q_t(a)$ como um valor padrão, como 0 por exemplo. 

💡A lei dos grandes números (lá de probabilidade e estatística) diz que $N_t(a) \rightarrow \infty \Rightarrow Q_t(a) \rightarrow q(a)$

Uma regra simples de seleção de ação é escolher a ação com maior valor estimado. Essa abordagem gulosa pode ser escrita como:

$$A_t = \arg \max_{a \in \mathcal{A}} Q_t(a)$$

Essa abordagem sempre vai selecionar a melhor opção em cima do **conhecimento atual** (_exploitation_), mas pode perder potencial de melhoria através de exploração.

⚠️Para que a lei dos grandes números aconteça com todas as ações $a$, precisamos explorar o ambiente. 

Podemos balancear isso com uma abordagem _near-greedy_ conhecida como $\varepsilon$_-greedy_. A ideia é que, numa pequena probabilidade $\varepsilon$, deixamos de lado a seleção de ação pelo argmax e usamos a seleção da ação através de uma distribuição uniforme. A seguir está o pseudocódigo.
```
INICIALIZE, para a = 1 até n:
    Q(a) ← 0
    N(a) ← 0
REPITA, para sempre:
    Amostre p aleatoriamente ~ U(0, 1)
    SE p > ε ENTÃO
        A ← argmax{a} Q(a)
    SENÃO
        Escolha A aleatoriamente ~ U(1,n)
    FIMSE
    R ← bandit(A)
    N(A) ← N(A) + 1
    Q(A) ← média(Q(A), R)
```

Um problema que precisamos resolver logo, antes de tentar rodar, é o da média(Q(A)), pois precisamos guardar todos os valores de recompensa de uma determinada ação, indefinidamente.

# Abordagem incremental

Para lidar com o problema de espaço de memória e limitações computacionais, podemos usar a seguinte relação, com base na recursividade:

$$Q_{k+1} = \frac{1}{k} \sum_{i=1}^{k} R_i = Q_k + \frac{1}{k} [R_k - Q_k]$$

Nesse caso, só precisamos da informação atual para computar o novo valor de $Q_t(a)$.

Essa regra de atualização pode ser reescrita da forma:

> NewEstimate $\leftarrow$ OldEstimate + StepSize [Target - OldEstimate]

Note que o parâmetro de passo (_StepSize_), se usado da forma como fizemos $\frac{1}{k}$ vai reduzir a medida que fazemos mais observações. Isso funciona em um problema com distribuição estacionária.

# Lidando com problema não estacionário

Se a distribuição da recompensa do _bandit_ está mudando com o tempo. Nesse caso, faz sentido ponderar mais as recompensas atuais do que as passadas.

Vamos modificar a lei de atualização de forma que passo é definido por $\alpha \in (0, 1]$ constante.

Então temos o pseudocódigo novamente:

```
INICIALIZE, para a = 1 até n:
    Q(a) ← 0
    N(a) ← 0
REPITA, para sempre:
    Amostre p aleatoriamente ~ U(0, 1)
    SE p > ε ENTÃO
        A ← argmax{a} Q(a)
    SENÃO
        Escolha A aleatoriamente ~ U(1,n)
    FIMSE
    R ← bandit(A)
    N(A) ← N(A) + 1
    Q(A) ← Q(A) + α(R - Q(a))
```

Agora conseguimos programar um script para testar o problema, variando os valores de $\varepsilon$ e avaliando como se comporta a média da recompensa a medida que o número de passos (tentativas) aumenta.
De acordo com o livro do Sutton:
> This was a set of 2000 randomly generated $n$-armed bandit tasks with $n = 10$. For each bandit, the action values, $q(a)$, $a \in \{1, ... , 10\}$, were selected according to a normal (Gaussian) distribution with mean $0$ and variance $1$. On $t$-th time step with a given bandit, the actual reward $R_t$ was the $q(A_t)$ for the bandit (where $A_t$ was the action selected) plus a normally distributed noise term that was mean $0$ and variance $1$. Averaging over bandits, we can plot the performance and behavior of various methods as they improve with experience over 1000 steps.

# Seleçao de ação por Upper-Confidence-Bound

> Exploration is needed because the estimates of the action values are uncertain.

Enquanto o $\varepsilon$_-greedy_ tenta, através da exploração, ações aleatórias de forma indiscriminada, a abordagem _Upper-Confidence-Bound_ (UCB) usa a variância de $a$ para favorecer exploração de opções que não tem a melhor média, mas uma chance estatisticamente considerável de melhoria.

Para isso, podemos mudar a seleção:

$$A_t = \arg \max_{a \in \mathcal{A}} \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$$

Em que $c > 0$ é o número que controla o grau de exploração. Se $N_t(a) = 0$ então $a$ é considerada uma ação que maximiza.

# Outras abordagens possíveis

- Gradient Bandits
- Contextual Bandits

# Próxima aula

Vamos explorar o processo de decisão de Markov, explorando antes um processo de Markov, então um processo com recompensa, até chega no processo de decisão.

# Material suplementar

[Multi-armed bandits](https://gibberblot.github.io/rl-notes/single-agent/multi-armed-bandits.html)