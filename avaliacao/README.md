# $P_1$ — Material demonstrativo de um método de RL

Atividade única e **individual**, avaliada de 0 a 10. A nota é o $P_1$ da disciplina.

> **Em uma frase:** escolha um método de RL que **não foi apresentado em aula**, entenda-o a fundo e produza o material com que ele seria ensinado: texto, formalizado na notação da disciplina, código que roda e um experimento que prova o ponto.

O produto não é um relatório. É um material: o mesmo formato das aulas 01–03 (`README.md` + `scripts/`), pronta para ser usada por quem cursar a disciplina nos próximos semestres. Os melhores materiais entram no repositório com o crédito do autor.

⚠️ **O que está sendo avaliado é compreensão, não desempenho.** Ninguém ganha ponto por bater um recorde de retorno no LunarLander. Ganha ponto quem mostra que entendeu o método a ponto de reescrevê-lo nos termos que a turma já domina.

---

## 1. O que entregar

Um diretório com esta estrutura, espelhando as aulas da disciplina:

```
NN-nome-do-tema/
├── README.md              # a aula escrita (o núcleo da entrega)
├── scripts/
│   ├── README.md          # como rodar, o que esperar de cada script
│   ├── <metodo>.py        # a implementação didática, do zero
│   ├── <experimento>.py   # o experimento que prova o ponto (pode ser o mesmo arquivo)
│   └── <demo>.ipynb       # opcional; se houver notebook, ele fica aqui
├── media/                 # figuras geradas pelos scripts (.png) e diagramas
└── requirements.txt       # dependências fixadas (ex.: numpy==2.1.0)
```

Não precisa de `aula.html` nem de slides: **o `README.md` é a entrega principal**, e é sobre ele que recai a maior parte da nota. Se quiser usar um notebook Jupyter, ele é bem-vindo, mas fica dentro de `scripts/`, e **além**dos scripts, nunca no lugar deles. Notebook não substitui código que roda por linha de comando de forma reprodutível.

### O `README.md` do material

Entre 1500 e 3000 palavras, em português, nas notações do Sutton & Barto ou Lapan usadas na disciplina (veja o glossário no README do repositório da disciplina). Sugestão de estrutura:

| Seção | Descrição|
|---|---|
| **Motivação** | que problema *concreto* o método resolve, e por que os métodos que já vimos em aula falham nele |
| **Onde isto se encaixa** | a ancoragem na disciplina |
| **O método** | a ideia em palavras antes de qualquer equação; depois a derivação, passo a passo, na nossa notação |
| **Pseudocódigo** | no estilo do livro (caixa com inicialização, laço, atualização), com os símbolos batendo com os do glossário |
| **Implementação** | as decisões que o pseudocódigo esconde: estruturas de dados, hiperparâmetros, o que quebra se for mudado |
| **Experimento** | a figura, o que ela mostra e **por que era esse o resultado esperado** |
| **Limites** | onde o método falha, e qual método vem depois para resolver isso |
| **Referências** | de onde veio cada coisa. É item de nota... |

### Sobre a Ancoragem na disciplina

O material precisa ser escrito **de dentro do curso**, não trazido de fora. Na prática, a seção *Onde isto se encaixa* responde a quatro perguntas, e o resto do texto se mantém coerente com elas:

1. **Classificação.** O método é tabular ou por aproximação? *Model-free* ou *model-based*? On-policy ou off-policy? Predição ou controle? Tarefa episódica ou contínua? Cada resposta vem com uma frase de justificativa.
2. **Genealogia.** De qual método visto em aula ele descende, e o que exatamente muda: o alvo da atualização, a política que gera os dados, a representação do valor, a forma de explorar? Escreva a regra de atualização do método conhecido e a do novo, uma embaixo da outra, e aponte a diferença.
3. **Tabela de símbolos.** Se a fonte usa outra notação — e Lapan, os papers e quase todo material da internet usam —, inclua uma tabela de tradução para os símbolos do **glossário**: $s$, $a$, $R_{t+1}$, $G_t$, $\pi(a\mid s)$, $v_\pi$, $q_\pi$, $\gamma$, $\alpha$. O texto e o código usam **os nossos**.
4. **Hipóteses.** O que o método assume para funcionar (Markov? estacionário? $\gamma < 1$? *policy improvement* garantido?) e o que acontece quando a hipótese cai.

Por que essa seção existe: ela é impossível de terceirizar. Um texto copiado da internet ou gerado por IA chega com a notação da fonte, sem saber o que a turma já viu nas aulas 01–03 nem qual frase foi usada para explicar o quê. Refazer o método na nossa notação, ligado ao que já foi apresentado, **é** a demonstração de que você entendeu.

### Sobre as Referências e uso das fontes

Um material didático que não diz de onde veio o que afirma não serve para estudar depois. As exigências:

- **Uma bibliografia explícita no fim**;
- **Citação no ponto de uso**;
- **Aponte as divergências entre fontes**. Quando houverem;
- **A notação é a da disciplina.** Inclusive no código: se a variável guarda $q_\pi(s,a)$, ela se chama `Q`, indexada por `(s, a)`, e a convenção $R_{t+1}$ vale no texto, no pseudocódigo e nos comentários.

---

## 2. Escolha do tema

**Regras**

1. Um tema por aluno, sem repetição na turma: vale a ordem de reserva (pode mandar via email). O trabalho é individual: se dois alunos quiserem o mesmo tema, o segundo escolhe outro.
2. Pode ser **qualquer método de aprendizado por reforço** que **não tenha sido apresentado em aula até a data da reserva**: dos livros da bibliografia (Sutton & Barto 2018, Lapan 2024) ou de outro livro-texto da área, como Szepesvári, Bertsekas, Powell, Graesser & Keng, Albrecht et al., o que você tiver em mãos. A tabela abaixo é um **cardápio, não um limite**.
3. **Evite o exótico.** Método que só existe em um artigo recente, sem tratamento de livro, costuma render um material ruim: a literatura é rasa demais para você conferir se entendeu, e o texto acaba sendo paráfrase do *abstract*. A régua: se o método aparece em um capítulo ou seção de algum livro-texto de RL, está aprovado; se só existe em um `arXiv` de 2024, converse comigo antes. Lembre que o que eu avalio é **compreensão, não desempenho**.
4. Qualquer que seja a fonte, o material é escrito na **notação e nos conceitos da disciplina** (§ 1). Um método vindo de outro livro dá mais trabalho de tradução — e é exatamente esse trabalho que vale ponto.
5. A reserva é feita enviando um email com título
   `[reserva] <tema> — <seu nome>`

Pedi para o Claude montar uma tabela com técnicas e o grau de dificuldade previsto. Para os mais fáceis, é esperado um estudo também de varredura de hiperparâmetros (como Grid Search ou Optuna).

### Trilha A — Métodos tabulares (Sutton & Barto, caps. 5–8)

Baratos de rodar, fáceis de depurar, e o experimento fica limpo. **Recomendada para quem quer garantir uma entrega sólida.**

| # | Tema | Onde | Ambiente sugerido | O ponto a demonstrar | Dif. |
|---|---|---|---|---|---|
| A1 | Monte Carlo: predição de primeira-visita × toda-visita | S&B 5.1–5.3 | Blackjack-v1 | a superfície de valor do blackjack emergindo de episódios inteiros, sem modelo | ⭐ |
| A2 | Monte Carlo off-policy e *importance sampling* ordinário × ponderado | S&B 5.5–5.7 | Blackjack, *racetrack* | a variância explodindo no estimador ordinário — a figura 5.3 é o alvo | ⭐⭐ |
| A3 | Expected SARSA × SARSA × Q-learning | S&B 6.4–6.6 | CliffWalking-v1 | o caminho pela beirada × o caminho seguro: on-policy e off-policy aprendem políticas *diferentes* | ⭐ |
| A4 | Viés de maximização e Double Q-learning | S&B 6.7 | MDP do exemplo 6.7 | Q-learning preferindo sistematicamente a ação ruim; o *double* corrigindo | ⭐⭐ |
| A5 | *n*-step TD e *n*-step SARSA: o meio-termo MC↔TD | S&B 7.1–7.3 | *random walk* de 19 estados | a curva em U do erro × $n$ e o acoplamento entre $n$ e $\alpha$ | ⭐⭐ |
| A6 | *n*-step Tree Backup (off-policy sem *importance sampling*) | S&B 7.5 | CliffWalking | corrigir a política-alvo sem pagar a variância do IS | ⭐⭐⭐ |
| A7 | Dyna-Q: planejamento com modelo aprendido | S&B 8.1–8.3 | labirinto do livro | 5 passos de planejamento por passo real valendo dezenas de episódios | ⭐⭐ |
| A8 | Dyna-Q+ e ambientes que mudam | S&B 8.3 | labirinto de atalho/bloqueio | o bônus de exploração $\kappa\sqrt{\tau}$ reencontrando o caminho que apareceu | ⭐⭐ |
| A9 | *Prioritized sweeping* | S&B 8.4 | labirinto grande | a mesma política com uma ordem de grandeza menos atualizações | ⭐⭐⭐ |
| A10 | *Rollout algorithms* e Monte Carlo Tree Search | S&B 8.10–8.11 | jogo da velha / Connect-4 | decidir bem **sem** aprender nada permanente: computação no lugar de memória | ⭐⭐⭐ |

### Trilha B — Aproximação de funções e traços (caps. 9–13) 🔜 parcialmente

| # | Tema | Onde | Ambiente sugerido | O ponto a demonstrar | Dif. |
|---|---|---|---|---|---|
| B1 | *Tile coding* × agregação de estados × base de Fourier | S&B 9.3–9.5 | *random walk* de 1000 estados | a representação sendo metade do problema: mesma regra, três resultados | ⭐⭐ |
| B2 | SARSA semi-gradiente com *tile coding* | S&B 10.1–10.2 | MountainCar-v0 | a superfície de "custo-para-ir" se escavando ao longo dos episódios (fig. 10.1) | ⭐⭐ |
| B3 | Recompensa média e *differential* semi-gradiente | S&B 10.3–10.5 | *access-control queuing* | por que $\gamma$ perde o sentido em tarefas contínuas | ⭐⭐⭐ |
| B4 | A tríade mortal e o contraexemplo de Baird | S&B 11.2–11.3 | MDP de Baird | divergência **real**, com os pesos indo para o infinito na sua tela | ⭐⭐⭐ |
| B5 | TD(λ) e traços de elegibilidade | S&B 12.1–12.5 | *random walk*, MountainCar | $\lambda$ interpolando entre TD(0) e MC, com um décimo da memória do *n*-step | ⭐⭐ |
| B6 | *True online* TD(λ) × TD(λ) acumulativo | S&B 12.5–12.6 | *random walk* | a equivalência exata com a visão *forward*, e onde a versão ingênua erra | ⭐⭐⭐ |
| B7 | REINFORCE e o efeito da linha de base | S&B 13.3–13.4 | *short corridor*, CartPole | a variância do gradiente caindo com a *baseline* — mostre a variância, não só o retorno | ⭐⭐ |
| B8 | Actor-Critic com um passo × REINFORCE | S&B 13.5 | CartPole-v1 | trocar o episódio inteiro por *bootstrapping*: aprendizado online | ⭐⭐ |
| B9 | Política gaussiana para ações contínuas | S&B 13.7 | Pendulum-v1 | parametrizar $\mu$ e $\sigma$; a exploração encolhendo sozinha | ⭐⭐⭐ |

### Trilha C — RL profundo (Lapan 2024) 🔜 parcialmente

Exige GPU ou paciência. **Restrinja o escopo**: um ambiente pequeno bem estudado vale mais que Atari rodando pela metade.

| # | Tema | Onde | Ambiente sugerido | O ponto a demonstrar | Dif. |
|---|---|---|---|---|---|
| C1 | *Cross-entropy method* | Lapan 4 | CartPole, FrozenLake | um método quase ingênuo resolvendo CartPole — e **falhando** no FrozenLake. O contraste é a aula | ⭐ |
| C2 | DQN: *replay buffer* e rede-alvo | Lapan 6 | CartPole, Pong | ablação: tire um dos dois e mostre o treinamento desmoronar | ⭐⭐ |
| C3 | Double DQN + Dueling | Lapan 8 | LunarLander-v3 | superestimação de $Q$ medida, não afirmada: plote $\max_a Q$ × retorno real | ⭐⭐⭐ |
| C4 | *Prioritized experience replay* | Lapan 8 | LunarLander | a correção de viés por *importance sampling* que quase todo mundo esquece | ⭐⭐⭐ |
| C5 | *NoisyNets*: exploração no espaço de parâmetros | Lapan 8 | LunarLander | exploração sem $\varepsilon$, e $\sigma$ decaindo sozinho por camada | ⭐⭐⭐ |
| C6 | DQN distribucional (C51) | Lapan 8 | LunarLander | aprender a **distribuição** do retorno: anime o histograma de um estado | ⭐⭐⭐⭐ |
| C7 | A2C e ambientes paralelos | Lapan 12 | CartPole, Pong | o efeito do número de ambientes na correlação das amostras | ⭐⭐⭐ |
| C8 | PPO: *clipping* e GAE-λ | Lapan 15 | Pendulum, LunarLander | o que o *clip* impede: plote a razão $r_t(\theta)$ e a fração cortada por época | ⭐⭐⭐ |
| C9 | TRPO → PPO: por que a região de confiança virou um *clip* | Lapan 15 | Pendulum | a mesma intenção, um custo computacional muito menor | ⭐⭐⭐⭐ |
| C10 | DDPG e TD3 | Lapan 16 | Pendulum, HalfCheetah | os três truques do TD3, um a um, em ablação | ⭐⭐⭐⭐ |
| C11 | SAC e RL com entropia máxima | Lapan 16 | Pendulum, Hopper | o que o termo de entropia compra: robustez visível a sementes | ⭐⭐⭐⭐ |
| C12 | Métodos *black-box*: estratégias evolutivas e algoritmos genéticos | Lapan 17 | CartPole, LunarLander | RL competitivo **sem gradiente de política** — e escalando com núcleos de CPU | ⭐⭐ |

### Trilha D — Fronteira e aplicações

Escopo mais solto e risco maior. Combine comigo antes de reservar.

| # | Tema | Onde | O ponto a demonstrar | Dif. |
|---|---|---|---|---|
| D1 | Bandits bayesianos: Thompson sampling × UCB × gradiente | S&B 2.5–2.9 | a aula 02 parou no $\varepsilon$-guloso; mostre o que vem depois, no mesmo *testbed* de 10 braços | ⭐⭐ |
| D2 | Bandits contextuais | S&B 2.9 | a ponte entre a aula 02 e a aula 03, com um caso de recomendação | ⭐⭐ |
| D3 | *Self-play* estilo AlphaZero | S&B 16.6 / Lapan 23 | MCTS + rede de política e valor no jogo da velha ou Connect-4 | ⭐⭐⭐⭐ |
| D4 | RL para otimização combinatória | Lapan 24 | cubo mágico, *bin packing* ou roteamento | quando a recompensa esparsa é o inimigo principal | ⭐⭐⭐⭐ |
| D5 | RL multiagente | Lapan 25 | cooperação e competição emergentes em um ambiente de grade | ⭐⭐⭐⭐ |
| D6 | RLHF e alinhamento de modelos de linguagem | Lapan 27 | onde o "ambiente" é um modelo de recompensa aprendido — e o que isso quebra | ⭐⭐⭐⭐ |
| D7 | RL *offline* | fora dos livros | aprender de um conjunto de dados fixo; o deslocamento distribucional em ação | ⭐⭐⭐⭐ |
| D8 | Aprendizado por imitação e RL inverso | fora dos livros | recuperar a recompensa a partir do comportamento | ⭐⭐⭐⭐ |
| D9 | *Reward shaping* e a arte de errar a recompensa | S&B 17.4 / Lapan | um agente que maximiza a recompensa e fracassa na tarefa. Didaticamente, dos temas mais valiosos | ⭐⭐ |
| D10 | Estudos de caso: TD-Gammon, Watson, Atari, AlphaGo | S&B cap. 16 | **exceção**: material histórico-comparativo, com reimplementação reduzida de *um* dos casos | ⭐⭐⭐ |

---

## 3. Requisitos técnicos

- **Implementação própria do método.** A ideia central (a regra de atualização, o laço de treinamento, o cálculo da perda) é escrita por você. Bibliotecas entram para ambiente (`gymnasium`), álgebra (`numpy`), redes (`torch`) e figuras (`matplotlib`). `stable-baselines3` e afins podem aparecer **como referência de comparação**, nunca como a implementação apresentada.
- **Roda em CPU em menos de 10 minutos** ou existe um modo reduzido (`--rapido`) que roda, mais os pesos treinados versionados para a demo completa. Ninguém vai esperar 6 horas para ver seu material funcionar.
- **Reprodutível:** semente fixa e configurável, `requirements.txt` com versões, e o comando exato no `scripts/README.md`. Eu vou rodar em uma máquina limpa.
- **CLI no padrão do repositório:** `argparse`, mensagens em português, valores padrão que já produzem o resultado interessante. Veja [`bandit_epsilon.py`](../01-introducao/scripts/bandit_epsilon.py) e [`bandit_metodos.py`](../02-multi-armed-bandit/scripts/bandit_metodos.py).
- **Linha de base obrigatória.** Toda figura tem um ponto de comparação: a política aleatória, o método da aula anterior ou a variante sem o truque que o material apresenta. Curva solitária não prova nada.
- **Variabilidade explícita.** Mínimo de 5 sementes em experimentos tabulares, 3 em RL profundo, com média e faixa (desvio ou min–máx) na figura. RL é ruidoso; esconder isso é o erro metodológico mais comum da área.
- **As figuras são geradas pelos scripts**, com o comando documentado. Sem captura de tela de notebook.
- **Notação da disciplina no código.** Nomes de variáveis e comentários seguem o glossário: `Q[s, a]`, `V[s]`, `gamma`, `alpha`, `epsilon`, e a recompensa que resulta de `A_t` é `R_{t+1}`. Código com a notação de outra fonte, sem a tabela de tradução da § 1, cai no item de formalização da rubrica.

💡 O `scripts/README.md` deve dizer **o que esperar** de cada execução, como faz o da aula 01 ("ε = 0,1 chega perto de 1,4 em 1000 passos"). Quem roda precisa saber se o que viu está certo.

---

## 4. O experimento que prova o ponto

A prova de que o texto e o código dizem a mesma coisa. Não é "rodei e convergiu", e não é uma competição de desempenho: é uma **pergunta com resposta medida**, cuja resposta você conseguia antecipar a partir da formalização:

> "O *replay buffer* importa mesmo?" → treine com e sem, 3 sementes cada, plote as duas curvas, explique o mecanismo que produziu a diferença.

Formatos que funcionam:

- **Ablação** — remova a peça característica do método e mostre o estrago.
- **Duelo** — o mesmo ambiente, dois métodos, a diferença de política explicada.
- **Varredura** — um hiperparâmetro ($\alpha$, $\lambda$, $n$, $\varepsilon$) no eixo x e o desempenho no eixo y; a curva em U é sempre didática.
- **Quebra** — o ambiente em que o método **falha**, e por quê. É o formato mais difícil de executar e o que ensina mais.

---

## 5. Cronograma

📅 A definir com a turma.

---

## 6. Rubrica — $P_1$ (0 a 10)

| Critério | Peso | 0–40% | 40–70% | 70–100% |
|---|:---:|---|---|---|
| **Formalização na notação da disciplina** | 2,5 | notação da fonte, copiada; símbolos sem definição; nenhuma ligação com o que foi visto em aula | traduz os símbolos, mas a ancoragem é superficial ou tem incoerências entre texto, pseudocódigo e código | classificação, genealogia, tabela de símbolos e hipóteses (§ 1) corretas e coerentes; o método aparece como continuação natural do curso |
| **Correção técnica** | 2,5 | o método está errado, ou é outro método com o nome trocado | correto na essência, com deslizes em detalhes (atualização, índices, condições de parada) | correto, com as sutilezas explicitadas (por que *este* termo, por que *este* sinal) |
| **Explicação** | 2,0 | transcrição do livro, ou um despejo de equações | correto e claro, mas sem fio condutor | tem uma ideia central que se constrói; um colega que faltou à aula aprende sozinho |
| **Referências e uso das fontes** | 1,5 | bibliografia genérica, ou ausente; trechos de origem não declarada | fontes listadas, mas sem citação no ponto de uso | capítulo e seção citados onde a afirmação é feita, origem de cada peça declarada, divergências entre fontes discutidas |
| **Código** | 1,0 | não roda, ou depende da máquina do autor | roda, mas confuso ou sem documentação | roda limpo, legível, com CLI, sementes e comentários que ensinam |
| **Experimento** | 0,5 | figura sem comparação, ou sem análise | comparação válida, análise rasa | pergunta clara, medição honesta (sementes, variabilidade), explicação do mecanismo |

---

## 7. Autoria, licença e uso do material

O repositório é MIT. Ao entregar via *pull request* você concorda em publicar sob a mesma licença, **com seu nome no cabeçalho do material** e no histórico do git. Os materiais aprovados passam a integrar o curso e serão usados em turmas futuras, sempre com o crédito preservado. Se preferir que o seu não seja publicado, diga no email de tema... a nota não é alterada por isso.

### Uso de IA generativa

Permitido e, para este projeto, esperado: usar LLMs para entender o capítulo, depurar código e revisar a escrita é uma habilidade legítima. Duas condições:

1. **Declare no final do `README.md`**: quais ferramentas, para quê. Uma frase basta.
2. **Você responde pelo que entrega.** não a IA.

⚠️ Cuidado específico desta área: LLMs erram com frequência em detalhes de RL, trocam $R_t$ por $R_{t+1}$, usam a política errada no alvo do SARSA, esquecem o `1 - done` no *bootstrapping*. Confira contra o livro.

💡 A parte do trabalho que mais vale ponto é a ancoragem na disciplina, é justamente a que nenhuma ferramenta faz por você. Ela depende de saber o que foi dito em aula, com quais símbolos e em que ordem. O texto não deve chegar com a notação de outra fonte.

---

## 8. Checklist antes de entregar

- [ ] O `README.md` tem uma ideia central, e ela aparece pelo menos três vezes.
- [ ] Toda equação tem uma frase em português antes dela.
- [ ] Os símbolos batem com o glossário do [README principal](../README.md),
      **inclusive no código e no pseudocódigo**.
- [ ] A seção *Onde isto se encaixa* responde às quatro perguntas da § 1:
      classificação, genealogia, tabela de símbolos e hipóteses.
- [ ] Se a fonte usa outra notação, a tabela de tradução está lá — e o resto do
      texto usa só a nossa.
- [ ] Você consegue derivar a regra de atualização sem consultar, e dizer de
      onde veio cada afirmação do texto.
- [ ] Toda fonte usada está na bibliografia, com capítulo e seção, e citada no
      ponto em que é usada.
- [ ] O que foi reaproveitado de terceiros está declarado como tal.
- [ ] O pseudocódigo está no estilo do livro e corresponde ao que o código faz.
- [ ] `python -m venv .venv && pip install -r requirements.txt` e os comandos do
      `scripts/README.md` funcionam em uma máquina limpa.
- [ ] Todas as figuras saem de um comando documentado.
- [ ] Todo experimento tem linha de base (baseline) e mais de uma semente.
- [ ] O `scripts/README.md` diz o que esperar de cada execução.
- [ ] Há uma seção de limites — onde o método falha.

---

## Anexo — Esqueleto para começar

```markdown
# <Método>

Autoria: <nome> · <semestre> · PPGI071 Aprendizado por Reforço (UFAL)
Referência: Sutton & Barto (2018), § X.Y / Lapan (2024), cap. Z

## Motivação
<o problema concreto; por que os métodos vistos em aula não bastam>

## Onde isto se encaixa
<classificação: tabular/aproximação, model-free/based, on/off-policy,
 predição/controle, episódico/contínuo — cada uma com justificativa>
<genealogia: de qual método da disciplina descende e o que muda na atualização>
<tabela de símbolos: notação da fonte → notação da disciplina>
<hipóteses: o que o método assume e o que quebra quando a hipótese cai>

## A ideia
<em palavras, antes de qualquer símbolo>

## Formalização
<derivação passo a passo, na notação da disciplina>

## Pseudocódigo
<caixa no estilo do livro>

## Implementação
<as decisões que o pseudocódigo esconde>

## Experimento: <a pergunta>
<figura, o que ela mostra, por que era esse o resultado esperado>

## Limites
<onde falha; qual método resolve isso>

## Referências
<bibliografia com capítulo e seção; artigos; implementações consultadas>
<divergências entre fontes e qual versão foi seguida>
```
