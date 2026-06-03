import numpy as np\
import matplotlib.pyplot as plt\
import pandas as pd\
\
# --------------------------------------------------\
# 1. Leitura dos 12 valores mensais\
# --------------------------------------------------\
def ler_consumo_mensal() -> list[float]:\
    valores = []\
    print("Digite o consumo mensal (kWh) para cada m\'eas (12 valores).")\
    for mes in range(1, 13):\
        while True:\
            try:\
                val = float(input(f"  M\'eas \{mes:02d\}: "))\
                if val < 0:\
                    raise ValueError\
                valores.append(val)\
                break\
            except ValueError:\
                print("  Valor inv\'e1lido. Por favor, informe um n\'famero positivo.")\
    return valores\
\
# --------------------------------------------------\
# 2. C\'e1lculos\
# --------------------------------------------------\
def calcular_metricas(consumos: list[float]) -> dict:\
    # Convers\'e3o para numpy array para opera\'e7\'f5es vetorizadas\
    arr = np.array(consumos)\
\
    # Consumo anual\
    anual = arr.sum()\
\
    # M\'e9dia mensal\
    media_mensal = anual / 12.0\
\
    # M\'e9dia di\'e1ria (30 dias por m\'eas)\
    media_diaria = media_mensal / 30.0\
\
    # Dados clim\'e1ticos\
    hsp = 4.3          # kWh/m\'b2\'b7dia\
    eta = 0.85         # Performance Ratio\
\
    # Pot\'eancia pico (kWp)\
    p_pico = media_diaria / (hsp * eta)\
\
    # Bateria \'96 12h de autonomia (metade do consumo di\'e1rio)\
    energia_autonomia = media_diaria / 2.0          # kWh\
    energia_real = energia_autonomia / eta          # kWh\
    dod = 0.90                                     # Profundidade de descarga\
    capacidade_kwh = energia_real / dod             # kWh total\
    # Convers\'e3o para Ah (tens\'e3o 48V)\
    capacidade_ah = (capacidade_kwh * 1000) / 48.0\
\
    return \{\
        "anual": anual,\
        "media_mensal": media_mensal,\
        "media_diaria": media_diaria,\
        "p_pico": p_pico,\
        "capacidade_kwh": capacidade_kwh,\
        "capacidade_ah": capacidade_ah,\
        "hsp": hsp,\
        "eta": eta,\
        "energia_autonomia": energia_autonomia,\
        "energia_real": energia_real\
    \}\
\
# --------------------------------------------------\
# 3. Visualiza\'e7\'e3o\
# --------------------------------------------------\
def plotar_graficos(consumos: list[float], metricas: dict) -> None:\
 meses = [f"\{i:02d\}" for i in range(1, 13)]\
\
    fig = plt.figure(constrained_layout=True, figsize=(12, 6))\
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 3, 3])\
\
    # Barra lateral \'96 consumo mensal\
    ax_bar = fig.add_subplot(gs[0, 0])\
    ax_bar.bar(meses, consumos, color="#4e79a7")\
    ax_bar.set_title("Consumo Mensal (kWh)")\
    ax_bar.set_xlabel("M\'eas")\
    ax_bar.set_ylabel("kWh")\
    ax_bar.tick_params(axis='x', rotation=45)\
\
    # Gr\'e1fico de m\'e9tricas \'96 linha\
    ax_line = fig.add_subplot(gs[0, 1:])\
    ax_line.plot(meses, consumos, label="Consumo Mensal", marker='o')\
    ax_line.axhline( m\'e9tricas["media_diaria"], color='g', linestyle='--',\
                     label=f"M\'e9dia Di\'e1ria (\{metrics['media_diaria']:.2f\} kWh)")\
    ax_line.axhline( m\'e9tricas["p_pico"] * 1000, color='r', linestyle='-',\
                     label=f"Pico Necess\'e1rio (\{metrics['p_pico']:.2f\} kWp)")\
    ax_line.axhline( metrics["capacidade_kwh"], color='m', linestyle='-.',\
                     label=f"Capacidade Bateria (\{metrics['capacidade_kwh']:.2f\} kWh)")\
    ax_line.set_title("M\'e9tricas de Dimensionamento")\
    ax_line.set_xlabel("M\'eas")\
    ax_line.set_ylabel("kWh / kWp")\
    ax_line.legend()\
    ax_line.tick_params(axis='x', rotation=45)\
\
    plt.suptitle("Dimensionamento Fotovoltaico \'96 Jandira-SP", fontsize=16)\
    plt.show()\
\
# --------------------------------------------------\
# 4. Programa principal\
# --------------------------------------------------\
def main() -> None:\
    consumos = ler_consumo_mensal()\
    metricas = calcular_metricas(consumos)\
\
    # Exibi\'e7\'e3o dos resultados em texto\
    print("\\n=== Resultados ===")\
    for key, val in metricas.items():\
        if isinstance(val, float):\
            print(f"\{key:20s\}: \{val:8.2f\}")\
        else:\
            print(f"\{key:20s\}: \{val\}")\
\
    # Gr\'e1ficos\
    plotar_graficos(consumos, metricas)\
\
if __name__ == "__main__":\
    main()\
}
