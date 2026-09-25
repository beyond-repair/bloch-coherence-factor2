"""Print a one-shot analytic + 9-mode scan for the default point."""

from .scan import condensing_params, ratio_scan


def main() -> None:
    p = condensing_params()
    result = ratio_scan(p, n_max=4, n_k=33)
    print("bloch-coherence-factor2  one-shot scan")
    print("parameters: W={W} λ={lam} M={M} c={c} μ={mu}".format(**p.__dict__))
    for key, val in result.items():
        print(f"  {key}: {val}")
    print("assertion R_analytic == 2:", result["R_analytic"] == 2.0)


if __name__ == "__main__":
    main()
