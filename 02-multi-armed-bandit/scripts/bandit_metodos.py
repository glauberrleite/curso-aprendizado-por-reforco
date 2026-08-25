"""
As politicas da aula 02, lado a lado no testbed de 10 bracos.

Reproduz as figuras 2.2, 2.3 e 2.4 do Sutton & Barto num experimento so:
10 acoes com valor verdadeiro q*(a) ~ N(0, 1); escolher a acao a devolve uma
recompensa sorteada de N(q*(a), 1). O que muda de uma curva para outra e
apenas COMO a acao e escolhida.

    guloso      argmax Q(a), sem exploracao nenhuma
    eps         eps-guloso: com probabilidade eps, sorteia uniformemente
    otimista    Q1(a) = 5 e passo alfa constante; guloso o tempo todo
    ucb         argmax [ Q(a) + c sqrt(ln t / N(a)) ]
    gradiente   softmax de preferencias H(a), com linha de base

Todas as execucoes de todas as politicas usam a mesma semente, entao elas
enfrentam os mesmos problemas: a diferenca entre as curvas e so a politica.

A simulacao e vetorizada nas execucoes (uma linha por execucao), o que torna
2000 execucoes viaveis em alguns segundos.

Requer numpy (matplotlib apenas para a figura).

Usar:
    python bandit_metodos.py
    python bandit_metodos.py --politicas guloso eps ucb --execucoes 2000
    python bandit_metodos.py --eps 0.01 --c 1 --sem-figura
"""

import argparse

import numpy as np

POLITICAS = ("guloso", "eps", "otimista", "ucb", "gradiente")


def escolha_gulosa(valores, rng):
    """argmax por linha, com empate desfeito por sorteio.

    Sem o desempate aleatorio o guloso puro ficaria preso na acao 0, que e a
    primeira do argmax quando todas as estimativas ainda valem o mesmo.
    """
    melhores = valores == valores.max(axis=1, keepdims=True)
    return (melhores * rng.random(valores.shape)).argmax(axis=1)


def experimento(politica, execucoes, passos, k, rng,
                eps=0.1, c=2.0, q1=5.0, alfa=0.1):
    """Devolve (recompensa media por passo, % de acao otima por passo)."""
    linhas = np.arange(execucoes)

    q_estrela = rng.normal(0.0, 1.0, size=(execucoes, k))   # o problema
    melhor = q_estrela.argmax(axis=1)

    inicial = q1 if politica == "otimista" else 0.0
    Q = np.full((execucoes, k), float(inicial))             # estimativas
    N = np.zeros((execucoes, k))                            # contagens
    H = np.zeros((execucoes, k))                            # preferencias
    media_r = np.zeros(execucoes)                           # linha de base

    rec = np.zeros(passos)
    opt = np.zeros(passos)

    for t in range(passos):
        if politica == "gradiente":
            expo = np.exp(H - H.max(axis=1, keepdims=True))
            pi = expo / expo.sum(axis=1, keepdims=True)
            a = (pi.cumsum(axis=1) < rng.random((execucoes, 1))).sum(axis=1)
        elif politica == "ucb":
            # N(a) = 0 vale infinito: acao nunca tentada e sempre maximizadora
            with np.errstate(divide="ignore"):
                bonus = np.where(N == 0, np.inf, c * np.sqrt(np.log(t + 1) / np.maximum(N, 1)))
            a = escolha_gulosa(Q + bonus, rng)
        else:
            a = escolha_gulosa(Q, rng)
            if politica == "eps":
                explora = rng.random(execucoes) < eps
                a = np.where(explora, rng.integers(0, k, execucoes), a)

        r = rng.normal(q_estrela[linhas, a], 1.0)

        N[linhas, a] += 1
        if politica == "gradiente":
            media_r += (r - media_r) / (t + 1)              # linha de base
            um_quente = np.zeros((execucoes, k))
            um_quente[linhas, a] = 1.0
            H += alfa * (r - media_r)[:, None] * (um_quente - pi)
        elif politica == "otimista":
            Q[linhas, a] += alfa * (r - Q[linhas, a])       # passo constante
        else:
            Q[linhas, a] += (r - Q[linhas, a]) / N[linhas, a]   # media amostral

        rec[t] = r.mean()
        opt[t] = 100.0 * (a == melhor).mean()

    return rec, opt


def rotulo(politica, args):
    return {
        "guloso": "guloso (Q1 = 0)",
        "eps": f"eps-guloso, eps = {args.eps:g}",
        "otimista": f"otimista, Q1 = {args.q1:g}, alfa = {args.alfa:g}",
        "ucb": f"UCB, c = {args.c:g}",
        "gradiente": f"gradiente, alfa = {args.alfa:g}",
    }[politica]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--politicas", nargs="+", default=list(POLITICAS), choices=POLITICAS)
    ap.add_argument("--execucoes", type=int, default=2000)
    ap.add_argument("--passos", type=int, default=1000)
    ap.add_argument("--bracos", type=int, default=10)
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--c", type=float, default=2.0)
    ap.add_argument("--q1", type=float, default=5.0)
    ap.add_argument("--alfa", type=float, default=0.1)
    ap.add_argument("--semente", type=int, default=20250824)
    ap.add_argument("--sem-figura", action="store_true")
    args = ap.parse_args()

    print(f"{args.bracos} bracos · {args.execucoes} execucoes · {args.passos} passos")
    print()
    print(f"{'politica':<34} {'rec. media (ult. 100)':>22} {'% otima (ult. 100)':>20}")
    print("-" * 78)

    resultados = []
    for politica in args.politicas:
        # mesma semente para todas: os problemas sorteados sao os mesmos
        rng = np.random.default_rng(args.semente)
        rec, opt = experimento(politica, args.execucoes, args.passos, args.bracos, rng,
                               eps=args.eps, c=args.c, q1=args.q1, alfa=args.alfa)
        resultados.append((politica, rec, opt))
        print(f"{rotulo(politica, args):<34} {rec[-100:].mean():>22.3f} {opt[-100:].mean():>19.1f}%")

    if args.sem_figura:
        return

    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    for politica, rec, opt in resultados:
        ax1.plot(rec, lw=1.1, label=rotulo(politica, args))
        ax2.plot(opt, lw=1.1)

    ax1.set_ylabel("recompensa media")
    ax1.legend(frameon=False, fontsize=9)
    ax2.set_ylabel("% de acoes otimas")
    ax2.set_xlabel("passos")
    ax2.set_ylim(0, 100)
    for ax in (ax1, ax2):
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Testbed de 10 bracos — as politicas da aula 02")
    fig.tight_layout()
    fig.savefig("bandit_metodos.png", dpi=150)
    print("\nfigura salva em bandit_metodos.png")


if __name__ == "__main__":
    main()
