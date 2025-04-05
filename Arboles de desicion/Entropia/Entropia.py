import pandas as pd
import numpy as np

df = pd.read_csv("robot.csv")

Prob_Avanzar = len(df[df["Accion"] == "Frente"]) /len(df["Accion"])
Prob_Derecha = len(df[df["Accion"] == "Derecha"]) /len(df["Accion"])
Prob_Izquier = len(df[df["Accion"] == "Izquierda"]) /len(df["Accion"])
Prob_Atras = len(df[df["Accion"] == "Atras"]) /len(df["Accion"])


print("Probabilidad de Avanzar: ", Prob_Avanzar)
print("Probabilidad de Derecha: ", Prob_Derecha)
print("Probabilidad de Izquierda: ",Prob_Izquier)
print("Probabilidad de Atras: ", Prob_Atras)


Prob_S = [Prob_Avanzar, Prob_Derecha, Prob_Izquier, Prob_Atras]
print(Prob_S)

Entro_Shannon = -sum(p*np.log2(p) for p in Prob_S if p > 0)

print(Entro_Shannon)
