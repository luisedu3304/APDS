import argparse
import os
import sys
import subprocess
import shutil
from src.examen_p2 import SignalParams, run_examen_p2

def _abs(path: str) -> str:
    return os.path.abspath(path)

def _open_in_vscode(path: str) -> bool:
    """Intenta abrir el archivo en la ventana actual de VS Code."""
    code = shutil.which("code") or shutil.which("code.cmd") or shutil.which("code.exe")
    if not code:
        return False
    try:
        # --reuse-window abre en la misma ventana de VS Code
        subprocess.run([code, "--reuse-window", _abs(path)], check=False)
        print(f"Abriendo en VS Code: {path}")
        return True
    except Exception:
        return False

def _open_in_system(path: str):
    """Fallback: abre con el visor por defecto del SO."""
    try:
        if os.name == "nt":  # Windows
            subprocess.run(["cmd", "/c", "start", "", _abs(path)], shell=False, check=False)
        elif sys.platform == "darwin":  # macOS
            subprocess.run(["open", _abs(path)], check=False)
        else:  # Linux
            subprocess.run(["xdg-open", _abs(path)], check=False)
        print(f"Abriendo en el sistema: {path}")
    except Exception as e:
        print(f"No pude abrir {path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ejecuta práctica examen_p2 (señal discreta + ruido determinista)")
    sp = parser.add_subparsers(dest="command")

    p2 = sp.add_parser("examen_p2", help="Genera señal, añade ruido tonal y analiza con DFT")
    p2.add_argument("--f1", type=float, default=8.0)
    p2.add_argument("--a1", type=float, default=1.0)
    p2.add_argument("--f2", type=float, default=20.0)
    p2.add_argument("--a2", type=float, default=0.5)
    p2.add_argument("--fn", type=float, default=12.0)
    p2.add_argument("--an", type=float, default=0.4)
    p2.add_argument("--fs", type=float, default=256.0)
    p2.add_argument("--duration", type=float, default=6.0)
    p2.add_argument("--peak_threshold", type=float, default=0.05)

    args = parser.parse_args()
    if args.command == "examen_p2":
        params = SignalParams(
            f1=args.f1, a1=args.a1, f2=args.f2, a2=args.a2,
            fn=args.fn, an=args.an, fs=args.fs, duration=args.duration
        )
        summary = run_examen_p2(params, outdir="outputs", peak_threshold=args.peak_threshold)

        # Consola
        print(f"N = {summary['N']}")
        print(f"fs = {summary['fs']} Hz")
        print(f"Δf = {summary['delta_f']:.6f} Hz")
        print("Picos (limpia):")
        for pk in summary["peaks_clean"]:
            print(f" - {pk['freq']:.4f} Hz, {pk['rel_amp']:.3f}")
        print("Picos (con ruido):")
        for pk in summary["peaks_noisy"]:
            print(f" - {pk['freq']:.4f} Hz, {pk['rel_amp']:.3f}")

        # Abrir automáticamente las imágenes generadas → primero VS Code, si no, el sistema
        to_open = [
            "outputs/tiempo_discreto_limpia.png",
            "outputs/tiempo_discreto_ruido.png",
            "outputs/espectro_limpia.png",
            "outputs/espectro_ruido.png",
            "outputs/espectro_comparacion.png",
        ]
        for p in to_open:
            if os.path.exists(p):
                if not _open_in_vscode(p):
                    _open_in_system(p)
            else:
                print(f"[Aviso] No existe: {p}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
