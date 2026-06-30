import numpy as np
import matplotlib.pyplot as plt

#Constante del coulomb
k = 9e9 
#Carga de las particulas
q = 5e-6
#Ubicación de las cargas en el plano XY
cargas = [
    (-3, 3, q),
    (3, 3, -q),
    (-3, -3, -q),
    (3, -3, q)
]

#Creación de una malla de puntos en el plano XY
#Usamos linspace para crear un rango de valores para x e y, 
#es decir, un conjunto de puntos equidistantes entre -8 y 8, 
#con 25 puntos en total.
x = np.linspace(-8, 8, 15)
y = np.linspace(-8, 8, 15)

#Creamos la cuadrícula de puntos a partir de los vectores x e y usando np.meshgrid.
#meshgrid toma dos vectores 1D y devuelve dos matrices 2D que representan
#todas las combinaciones posibles de los valores de x e y.
X, Y = np.meshgrid(x, y)

#Creamos dos matrices vacías del mismo tamaño que X e Y para almacenar
#los componentes del campo eléctrico en cada punto de la malla.
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)


#
for xc, yc, qc in cargas:

    dx = X - xc
    dy = Y - yc

    r = np.sqrt(dx**2 + dy**2)

    r[r == 0] = 1e-10

    Ex += k * qc * dx / r**3
    Ey += k * qc * dy / r**3

# Magnitud del campo
magnitud = np.sqrt(Ex**2 + Ey**2)

# Evita divisiones por cero
magnitud[magnitud == 0] = 1

# Normalización
Ex_n = Ex / magnitud
Ey_n = Ey / magnitud


#Gráfica del campo eléctrico
plt.figure(figsize=(10,10))

# Flechas coloreadas según la intensidad del campo eléctrico.
plt.quiver(
    X, Y,
    Ex_n, Ey_n,
    magnitud,
    cmap="turbo",
    pivot="middle",
    scale=35,
    width=0.0035
)

# Barra de colores
cbar = plt.colorbar()
cbar.set_label("Magnitud del campo eléctrico |E| (N/C)", fontsize=11)

# Dibujar las cargas
for xc, yc, qc in cargas:

    if qc > 0:
        plt.scatter(
            xc,
            yc,
            color="red",
            s=220,
            edgecolors="black",
            zorder=5
        )

        plt.text(
            xc,
            yc,
            "+",
            color="white",
            fontsize=15,
            ha="center",
            va="center",
            weight="bold"
        )

        plt.text(
            xc+0.15,
            yc+0.45,
            "+5 μC",
            color="darkred",
            fontsize=11,
            weight="bold"
        )

    else:

        plt.scatter(
            xc,
            yc,
            color="royalblue",
            s=220,
            edgecolors="black",
            zorder=5
        )

        plt.text(
            xc,
            yc,
            "−",
            color="white",
            fontsize=18,
            ha="center",
            va="center",
            weight="bold"
        )

        plt.text(
            xc+0.15,
            yc+0.45,
            "−5 μC",
            color="navy",
            fontsize=11,
            weight="bold"
        )

# Ejes principales resaltados
plt.axhline(
    0,
    color="black",
    linewidth=2
)

plt.axvline(
    0,
    color="black",
    linewidth=2
)

# Cuadrícula
plt.grid(
    True,
    linestyle="--",
    alpha=0.4
)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.xlabel("x (m)", fontsize=12)
plt.ylabel("y (m)", fontsize=12)

plt.title(
    "Campo eléctrico generado por cuatro cargas",
    fontsize=15,
    weight="bold"
)
#Configuramos la relación de aspecto de la gráfica para que sea igual en ambos ejes,
#lo que significa que un paso en el eje x es igual a un paso en el eje y
plt.axis("equal")
#Hacemos que los elementos de la gráfica no se superpongan y se vean correctamente.
plt.tight_layout()

plt.show()