"""
Bandit nao estacionario: media amostral x passo constante (secoes 05 e 06).

E o exercicio 2.5 do Sutton & Barto. Os 10 bracos comecam iguais
(q*(a) = 0 para todo a) e cada q*(a) recebe, a cada passo, um incremento
normal de media 0 e desvio sigma. O melhor braco muda de dono ao longo do
tempo.

Dois agentes eps-gulosos, identicos em tudo menos no passo da atualizacao:

    1/N     Q(A) <- Q(A) + (1/N(A)) [R - Q(A)]     media amostral
    alfa    Q(A) <- Q(A) + alfa     [R - Q(A)]     media com desconto exponencial

A media amostral converge — e esse e exatamente o problema: com o peso da
n-esima recompensa caindo como 1/n, ela deixa de responder a uma mudanca.
O passo constante nunca converge de todo, e por isso consegue esquecer.

Com sigma = 0 o problema volta a ser estacionario e a vantagem se inverte.

Requer numpy (matplotlib apenas para a figura).

Usar:
    python bandit_nao_estacionario.py
    python bandit_nao_estacionario.py --passos 20000 --alfa 0.05
    python bandit_nao_estacionario.py --sigma 0 --sem-figura
"""

import argparse

import numpy as np


def escolha_gulosa(valores, rng):
    """argmax por linha, com empate desfeito por sorteio."""
    melhores = valores == valores.max(axis=1, keepdims=True)
    return (melhores * rng.random(valores.shape)).argmax(axis=1)


def experimento(passo, execucoes, passos, k, rng, eps=0.1, alfa=0.1, sigma=0.01,
                inicio="iguais"):
    """passo e 'media' (1/N) ou 'alfa' (constante)."""
    linhas = np.arange(execucoes)

    if inicio == "iguais":
        q_estrela = np.zeros((execucoes, k))   # exercicio 2.5: todos comecam iguais
    else:
        q_estrela = rng.normal(0.0, 1.0, size=(execucoes, k))
    Q = np.zeros((execucoes, k))
    N = np.zeros((execucoes, k))

    rec = np.zeros(passos)
    opt = np.zeros(passos)

    for t in range(passos):
        q_estrela += rng.normal(0.0, sigma, size=(execucoes, k))   # o problema anda
        melhor = q_estrela.argmax(axis=1)

        a = escolha_gulosa(Q, rng)
        explora = rng.random(execucoes) < eps
        a = np.where(explora, rng.integers(0, k, execucoes), a)

        r = rng.normal(q_estrela[linhas, a], 1.0)

        N[linhas, a] += 1
        if passo == "media":
            Q[linhas, a] += (r - Q[linhas, a]) / N[linhas, a]
        else:
            Q[linhas, a] += alfa * (r - Q[linhas, a])

        rec[t] = r.mean()
        opt[t] = 100.0 * (a == melhor).mean()

    return rec, opt


def passeio_exemplo(passos, k, sigma, semente):
    """Uma execucao dos q*(a), so para a figura."""
    rng = np.random.default_rng(semente + 1)
    caminho = np.cumsum(rng.normal(0.0, sigma, size=(passos, k)), axis=0)
    return caminho


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--execucoes", type=int, default=200)
    ap.add_argument("--passos", type=int, default=10000)
    ap.add_argument("--bracos", type=int, default=10)
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--alfa", type=float, default=0.1)
    ap.add_argument("--sigma", type=float, default=0.01)
    ap.add_argument("--inicio", choices=("iguais", "normal"), default="iguais",
                    help="q*(a) inicial: todos em zero (exercicio 2.5) ou sorteados de N(0,1)")
    ap.add_argument("--semente", type=int, default=20250824)
    ap.add_argument("--sem-figura", action="store_true")
    args = ap.parse_args()

    print(f"{args.bracos} bracos · {args.execucoes} execucoes · {args.passos} passos "
          f"· sigma = {args.sigma:g} · eps = {args.eps:g} · inicio {args.inicio}")
    print()
    metade = args.passos // 2
    print(f"{'passo':<22} {'rec. media (2a metade)':>24} {'% otima (2a metade)':>21}")
    print("-" * 70)

    resultados = []
    for passo, nome in (("media", "1/N (media amostral)"), ("alfa", f"alfa = {args.alfa:g}")):
        rng = np.random.default_rng(args.semente)
        rec, opt = experimento(passo, args.execucoes, args.passos, args.bracos, rng,
                               eps=args.eps, alfa=args.alfa, sigma=args.sigma,
                               inicio=args.inicio)
        resultados.append((nome, rec, opt))
        print(f"{nome:<22} {rec[metade:].mean():>24.3f} {opt[metade:].mean():>20.1f}%")

    dif = resultados[1][1][metade:].mean() - resultados[0][1][metade:].mean()
    print()
    if args.sigma == 0 and args.inicio == "iguais":
        print("sigma = 0 com inicio 'iguais': os bracos sao identicos e nao ha o que "
              "aprender. Rode com --inicio normal para o caso estacionario de verdade.")
    elif args.sigma == 0:
        print("sigma = 0: problema estacionario. A media amostral converge e o passo "
              "constante fica balancando no ruido. A vantagem se inverte, e a diferenca "
              "cresce com o horizonte.")
    elif dif > 0:
        print(f"vantagem do passo constante: {dif:+.3f} de recompensa media na segunda metade.")
    else:
        print(f"a media amostral ainda segura o resultado ({dif:+.3f}): a deriva e pequena "
              "para este horizonte.")
    print(f"janela efetiva de memoria com alfa = {args.alfa:g}: "
          f"meia-vida de {np.log(0.5) / np.log(1 - args.alfa):.1f} passos.")

    if args.sem_figura:
        return

    import matplotlib.pyplot as plt

    def suavizar(v, j=100):
        nucleo = np.ones(j) / j
        return np.convolve(v, nucleo, mode="valid")

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
    for nome, rec, opt in resultados:
        ax1.plot(suavizar(rec), lw=1.1, label=nome)
        ax2.plot(suavizar(opt), lw=1.1)

    ax3.plot(passeio_exemplo(args.passos, args.bracos, args.sigma, args.semente),
             lw=0.8, alpha=0.8)

    ax1.set_ylabel("recompensa media")
    ax1.legend(frameon=False)
    ax2.set_ylabel("% de acoes otimas")
    ax2.set_ylim(0, 100)
    ax3.set_ylabel("q*(a) de uma execucao")
    ax3.set_xlabel("passos")
    for ax in (ax1, ax2, ax3):
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Bandit nao estacionario — quem esquece leva vantagem")
    fig.tight_layout()
    fig.savefig("bandit_nao_estacionario.png", dpi=150)
    print("figura salva em bandit_nao_estacionario.png")


if __name__ == "__main__":
    main()
