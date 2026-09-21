A ideia aqui é trazer o básico necessário em tecnologias de simulação e aprendizado profundo (*Deep Learning*).
Especificamente, nesta disciplina, essa parte vai trazer conceitos que usam a lib Gymnasium e PyTorch.

# Sobre simulação

## Vantagens do treinamento no mundo real
- Nada representa o ambiente de forma mais completa do que o próprio ambiente real;
- Você não precisa gastar tempo criando e validando um modelo;
- É uma necessidade, para ambientes difíceis ou com mudanças constantes.

## Vantagens do treinamento com simulação
- Simulações rodam mais rápido que o mundo real e podem ser paralelas;
- Pode treinar com condições que seriam muito difíceis de aplicar em ambiente prático (falhas críticas ou teste interplanetário);
- Não existe risco de danificar o equipamento.

## Ambientes conhecidos para simulação (especialmente em robótica)

- Gazebo
- CoppeliaSim
- MATLAB SimScape
- Genesis AI

## O conceito de *cheap simulation*

Para treinar um agente de RL, ele precisa interagir com o ambiente por milhares ou milhões de episódios (tentativa e erro). Se o seu ambiente de simulação for pesado, o treinamento pode demorar dias ou semanas.

- Fast Execution (desativar visualização e animação pode ser uma boa)
- Low Memory Usage
- Simplified Solvers

Dá para aplicar esses conceitos nos ambientes apresentados antes. Aqui vamos usar o [Gymnasium](https://gymnasium.farama.org/), um fork do lib *OpenAI Gym* que reimplementa a API, que já não é mais mantida.

