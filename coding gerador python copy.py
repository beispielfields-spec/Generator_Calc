\par import numpy as np
\par import matplotlib.pyplot as plt
\par import pandas as pd
\par 
\par # --------------------------------------------------
\par # 1. Leitura dos 12 valores mensais
\par # --------------------------------------------------
\par def ler_consumo_mensal() -> list[float]:
\par     valores = []
\par     print("Digite o consumo mensal (kWh) para cada m\'eas (12 valores).")
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 for mes in range(1, 13):
\par         while True:
\par             try:
\par                 val = float(input(f"  M\'eas \{mes:02d\}: "))
\par                 if val < 0:
\par                     raise ValueError
\par                 valores.append(val)
\par                 break
\par             except ValueError:
\par                 print("  Valor inv\'e1lido. }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 Por favor, informe um n\'famero positivo.")
\par     return valores
\par 
\par # --------------------------------------------------
\par # 2. C\'e1lculos
\par # --------------------------------------------------
\par def calcular_metricas(consumos: list[float]) -> dict:
\par     # Convers\'e3o para numpy array para opera\'e7\'f5es vetorizadas
\par     arr = np.array(consumos)
\par 
\par     # Consumo anual
\par     anual = arr.sum()
\par 
\par     # M\'e9dia mensal
\par     media_mensal = anual / 12.0
\par 
\par     # M\'e9dia di\'e1ria (30 dias por m\'eas)
\par     media_diaria = media_mensal / 30.0
\par 
\par     # Dados clim\'e1ticos
\par     hsp = 4.3          # kWh/m\'b2\'b7dia
\par     eta = 0.85         # Performance Ratio
\par 
\par     # Pot\'eancia pico (kWp)
\par     p_pico = media_diaria / (hsp * eta)
\par 
\par     # Bateria \endash  12h de autonomia (metade do consumo di\'e1rio)
\par     energia_autonomia = media_diaria / 2.0          # kWh
\par     energia_real = energia_autonomia / eta          # kWh
\par     dod = 0.90                                     # Profundidade de descarga
\par     capacidade_kwh = energia_real / dod             # kWh total
\par     # Convers\'e3o para Ah (tens\'e3o 48V)
\par     capacidade_ah = (capacidade_kwh * 1000) / 48.0
\par 
\par     return \{
\par         "anual": anual,
\par         "media_mensal": media_mensal,
\par         "media_diaria": media_diaria,
\par         "p_pico": p_pico,
\par         "capacidade_kwh": capacidade_kwh,
\par         "capacidade_ah": capacidade_ah,
\par         "hsp": hsp,
\par         "eta": eta,
\par         "energia_autonomia": energia_autonomia,
\par         "energia_real": energia_real
\par     \}
\par 
\par # --------------------------------------------------
\par # 3. Visualiza\'e7\'e3o
\par # --------------------------------------------------
\par def plotar_graficos(consumos: list[float], metricas: dict) -> None:
\par     meses = [f"\{i:02d\}" for i in range(1, 13)]
\par 
\par     fig = plt.figure(constrained_layout=True, figsize=(12, 6))
\par     gs = fig.add_gridspec(1, 3, width_ratios=[1, 3, 3])
\par 
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 # Barra lateral \endash  consumo mensal
\par     ax_bar = fig.add_subplot(gs[0, 0])
\par     ax_bar.bar(meses, consumos, color="#4e79a7")
\par     ax_bar.set_title("Consumo Mensal (kWh)")
\par     ax_bar.set_xlabel("M\'eas")
\par     ax_bar.set_ylabel("kWh")
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 ax_bar.tick_params(axis='x', rotation=45)
\par 
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 # Gr\'e1fico de m\'e9tricas \endash  linha
\par     ax_line = fig.add_subplot(gs[0, 1:])
\par     ax_line.plot(meses, consumos, label="Consumo Mensal", marker='o')
\par     ax_line.axhline( m\'e9tricas["media_diaria"], color='g', linestyle='--',
\par                      label=f"M\'e9dia Di\'e1ria (\{metrics['media_diaria']:.2f\} kWh)")
\par     ax_line.axhline( m\'e9tricas["p_pico"] * 1000, color='r', linestyle='-',
\par                      label=f"Pico Necess\'e1rio (\{metrics['p_pico']:.2f\} kWp)")
\par     ax_line.axhline( metrics["capacidade_kwh"], color='m', linestyle='-.',
\par                      label=f"Capacidade Bateria (\{metrics['capacidade_kwh']:.2f\} kWh)")
\par     ax_line.set_title("M\'e9tricas de Dimensionamento")
\par     ax_line.set_xlabel("M\'eas")
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 ax_line.set_ylabel("kWh / kWp")
\par     ax_line.legend()
\par     ax_line.tick_params(axis='x', rotation=45)
\par 
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 plt.suptitle("Dimensionamento Fotovoltaico \endash  Jandira-SP", fontsize=16)
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 plt.show()
\par 
\par # --------------------------------------------------
\par # 4. Programa principal
\par # --------------------------------------------------
\par def main() -> None:
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 consumos = ler_consumo_mensal()
\par     metricas = calcular_metricas(consumos)
\par 
\par     # Exibi\'e7\'e3o dos resultados em texto
\par     print("\\n=== Resultados ===")
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 for key, val in metricas.items():
\par         if isinstance(val, float):
\par             print(f"\{key:20s\}: \{val:8.2f\}")
\par         else:
\par             print(f"\{key:20s\}: \{val\}")
\par 
\par     }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \lang1046\langfe1033\langnp1046\insrsid5395146\charrsid5395146 # Gr\'e1ficos
\par     plotar_graficos(consumos, metricas)
\par 
\par }{\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid5395146 if __name__ == "__main__"
