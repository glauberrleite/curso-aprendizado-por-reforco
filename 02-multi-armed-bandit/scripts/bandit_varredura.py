"""
Estudo de parametros: qual eps, qual c, qual alfa, qual Q1 (secao 08).

E a figura 2.6 do Sutton & Barto. Cada metodo tem exatamente um parametro;
aqui ele varre potencias de 2 e o desempenho e resumido por UM numero: a
recompensa media ao longo de todos os passos da execucao.

Ler o grafico resultante e o exercicio: todas as curvas tem forma de U
invertido — parametro de menos, o agente explora pouco; parametro demais, ele
gasta jogadas a toa. Nenhum metodo e bom em toda a faixa, e o vencedor depende
do horizonte: aumente --passos e as curvas se deslocam.

Este script reaproveita as politicas de bandit_metodos.py, entao rode-o a
partir desta pasta.

Requer numpy (matplotlib apenas para a figura).

Usar:
    python bandit_varredura.py
    python bandit_varredura.py --execucoes 1000 --passos 1000
    python bandit_varredura.py --metodos eps ucb --sem-figura
"""

import argparse

import numpy as np

try:
    from bandit_metodos import experimento
except ImportError:                                   # rodou de outra pasta
    raise SystemExit(
        "bandit_varredura.py precisa de bandit_metodos.py na mesma pasta.\n"
        "Entre em 02-multi-armed-bandit/scripts e rode de la."
    )

# expoentes de 2 varridos por metodo, como na figura 2.6 do livro
FAIXAS = {
    "eps":       (-7, -1, "eps"),
    "gradiente": (-5, 2, "alfa"),
    "ucb":       (-4, 2, "c"),
    "otimista":  (-2, 2, "Q1"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metodos", nargs="+", default=list(FAIXAS), choices=list(FAIXAS))
    ap.add_argument("--execucoes", type=int, default=500)
    ap.add_argument("--passos", type=int, default=1000)
    ap.add_argument("--bracos", type=int, default=10)
    ap.add_argument("--semente", type=int, default=20250824)
    ap.add_argument("--sem-figura", action="store_true")
    args = ap.parse_args()

    print(f"{args.bracos} bracos · {args.execucoes} execucoes · {args.passos} passos")
    print("resumo = recompensa media ao longo de TODOS os passos")
    print()

    resultados = {}
    for metodo in args.metodos:
        de, ate, nome_par = FAIXAS[metodo]
        expoentes = list(range(de, ate + 1))
        valores, medias = [], []
        print(f"{metodo} ({nome_par})")
        for e in expoentes:
            par = 2.0 ** e
            rng = np.random.default_rng(args.semente)
            extra = {"eps": 0.1, "c": 2.0, "q1": 5.0, "alfa": 0.1}
            extra[{"eps": "eps", "gradiente": "alfa", "ucb": "c", "otimista": "q1"}[metodo]] = par
            rec, _ = experimento(metodo, args.execucoes, args.passos, args.bracos, rng, **extra)
            valores.append(par)
            medias.append(rec.mean())
            print(f"    2^{e:<3} = {par:>8.4f}   recompensa media {rec.mean():.3f}")
        melhor = int(np.argmax(medias))
        print(f"    melhor: {nome_par} = {valores[melhor]:g} "
              f"(recompensa media {medias[melhor]:.3f})")
        print()
        resultados[metodo] = (expoentes, medias, nome_par)

    if args.sem_figura:
        return

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    for metodo, (expoentes, medias, nome_par) in resultados.items():
        ax.plot(expoentes, medias, marker="o", ms=3.5, lw=1.2, label=f"{metodo} ({nome_par})")
    ax.set_xlabel("valor do parametro (expoente de 2)")
    ax.set_ylabel(f"recompensa media nos {args.passos} passos")
    ax.set_xticks(sorted({e for e, _, _ in resultados.values() for e in e}))
    ax.set_xticklabels([f"$2^{{{e}}}$" for e in
                        sorted({e for e, _, _ in resultados.values() for e in e})])
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Estudo de parametros — cada metodo tem seu ponto doce")
    fig.tight_layout()
    fig.savefig("bandit_varredura.png", dpi=150)
    print("figura salva em bandit_varredura.png")


if __name__ == "__main__":
    main()
