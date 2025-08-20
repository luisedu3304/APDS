import sys
import argparse
from src.examen_p1 import SignalParams, run_examen_p1
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def make_report(pdf_path: str, summary: dict, repo_url: str = "AGREGA_AQUI_LA_URL_DE_TU_REPO"):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    W, H = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, H-2*cm, "Reporte: DFT de señal modulada en amplitud")

    c.setFont("Helvetica", 11)
    y = H-3*cm
    lines = [
        f"Fecha de ejecución: {__import__('datetime').datetime.now()}",
        f"Parámetros: N={summary['N']}, f_s={summary['fs']} Hz, Δf={summary['delta_f']:.6f} Hz",
        "Picos espectrales (frecuencia [Hz], amplitud relativa):"
    ]
    for L in lines:
        c.drawString(2*cm, y, L)
        y -= 0.7*cm

    if not summary["peaks"]:
        c.drawString(2.5*cm, y, "No se detectaron picos con el umbral indicado.")
        y -= 0.7*cm
    else:
        for pk in summary["peaks"]:
            c.drawString(2.5*cm, y, f"- {pk['freq']:.4f} Hz, {pk['rel_amp']:.3f}")
            y -= 0.6*cm

    # Insertar imágenes si hay espacio
    def add_image(path, y_top, title):
        c.setFont("Helvetica-Bold", 12)
        c.drawString(2*cm, y_top, title)
        c.drawImage(path, 2*cm, y_top-8.5*cm, width=16*cm, height=8*cm, preserveAspectRatio=True, anchor='n')
        return y_top-9.0*cm

    y -= 0.5*cm
    try:
        y = add_image("outputs/tiempo_continuo.png", y, "Señal continua")
    except Exception:
        pass

    if y < 10*cm:
        c.showPage()
        y = H-2*cm

    try:
        y = add_image("outputs/tiempo_discreto.png", y, "Señal discreta")
    except Exception:
        pass

    if y < 10*cm:
        c.showPage()
        y = H-2*cm

    try:
        y = add_image("outputs/espectro_mag.png", y, "Espectro de magnitud")
    except Exception:
        pass

    # URL del repositorio
    c.setFont("Helvetica", 11)
    c.drawString(2*cm, 2*cm, f"URL del repositorio: {repo_url}")
    c.save()

def main():
    parser = argparse.ArgumentParser(description="Ejecuta práctica examen_p1")
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando examen_p1
    p1 = subparsers.add_parser("examen_p1", help="Analiza la señal y calcula DFT")
    p1.add_argument("--fs", type=float, default=256.0)
    p1.add_argument("--duration", type=float, default=4.0)
    p1.add_argument("--m", type=float, default=0.5)
    p1.add_argument("--fm", type=float, default=0.5)
    p1.add_argument("--fc", type=float, default=8.0)
    p1.add_argument("--peak_threshold", type=float, default=0.05)

    args = parser.parse_args()

    if args.command == "examen_p1":
        params = SignalParams(fm=args.fm, fc=args.fc, m=args.m, fs=args.fs, duration=args.duration)
        summary = run_examen_p1(params, outdir="outputs", peak_threshold=args.peak_threshold)

        # Generar reporte PDF
        make_report("outputs/reporte.pdf", summary)

        # Mostrar en consola
        print(f"N = {summary['N']}")
        print(f"fs = {summary['fs']} Hz")
        print(f"Δf = {summary['delta_f']:.6f} Hz")
        if summary["peaks"]:
            print("Picos espectrales detectados (f [Hz], amp_rel):")
            for pk in summary["peaks"]:
                print(f" - {pk['freq']:.4f} Hz, {pk['rel_amp']:.3f}")
        else:
            print("No se detectaron picos.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
