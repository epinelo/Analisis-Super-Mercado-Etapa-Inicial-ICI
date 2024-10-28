import pandas as pd
import numpy as np
from scipy.stats import beta, norm

# Cargar los datos de ventas del supermercado
df = pd.read_csv("SuperMarketData.csv")
sales = np.array(df["Sales"]) * 19.88 

# Normalización de las ventas
max_sales = max(sales)
min_sales = min(sales)
sales_norm = 1 / (max_sales - min_sales) * sales

# Ajuste de la distribución Beta a los datos de ventas
a, b, _, _ = beta.fit(sales)
mu_norm = a / (a + b)
var_norm = (a * b) / (((a + b)**2) * (a + b + 1))
desv_norm = np.sqrt(var_norm)

# Conversión de los parámetros normalizados a la escala original
mu = (max_sales - min_sales) * mu_norm
var = ((max_sales - min_sales)**2) * var_norm

# Definición de los días de trabajo y el factor de ajuste
dias_t = 24
fact = 1.15

# Cálculo de salarios para diferentes tipos de empleados
sal_cajeros = 258.25
num_cajeros = 30
tot_cajeros = sal_cajeros * num_cajeros * dias_t

sal_conserjes = 5000
num_conserjes = 20
tot_conserjes = sal_conserjes * num_conserjes

gerente = 100000
sub_gerentes = 45000
num_subgerentes = 4
tot_gerentes = gerente + sub_gerentes * num_subgerentes

sal_almacenistas = 262.13
num_almacenistas = 40
tot_almacenistas = sal_almacenistas * num_almacenistas * dias_t

sal_gpasillo = 264.65
num_gpasillo = 40
tot_gpasillo = sal_gpasillo * num_gpasillo * dias_t

sal_guardias = 257.88  
num_guardias = 10
tot_guardias = sal_guardias * num_guardias * dias_t

sal_atencion = 280
num_atencion = 15
tot_atencion = sal_atencion * num_atencion * dias_t

sal_supervisores = 836.7  
num_supervisores = 5
tot_supervisores = sal_supervisores * num_supervisores

# Cálculo del costo de nómina total
nom_total = (tot_cajeros + tot_conserjes + tot_almacenistas + tot_gpasillo + tot_guardias + tot_atencion) * fact + tot_gerentes + tot_supervisores

# Cálculo del gasto en luz con una superficie de 2000 m²
consumo_kwh_m2 = 20  # Consumo promedio en kWh por m² (aproximado)
precio_kwh = 2.3  # Precio por kWh (tarifa comercial)
gasto_luz = consumo_kwh_m2 * 2000 * precio_kwh * 30  # Consumo mensual

# Otros gastos estimados
mantenimiento = 100000  # Mantenimiento general
publicidad = 200000  # Publicidad y marketing
equipos = 150000  # Mantenimiento de equipos y refrigeración
otros_gastos = mantenimiento + publicidad + equipos

# Cálculo de los gastos totales
gastos_tot = nom_total + gasto_luz + otros_gastos + 1500000

# Cálculo del número de clientes requerido utilizando la distribución normal
om = norm.ppf(0.01)
a_ = mu**2
b_ = -2 * mu * gastos_tot - om**2 * var
c_ = gastos_tot**2
N1 = (-b_ + np.sqrt(b_**2 - 4 * a_ * c_)) / (2 * a_)
N2 = (-b_ - np.sqrt(b_**2 - 4 * a_ * c_)) / (2 * a_)

# Selección de la solución correcta para el número de clientes
if (gastos_tot / N1 - mu > 0):
    N = N1
else:
    N = N2

# Suponiendo que un cliente promedio visita el supermercado 2.5 veces por semana
visitas_semanales = 2.5
porc_pob = N / (160000 * visitas_semanales)
print(f"Porcentaje de la población objetivo requerido: {porc_pob * 100:.2f}%")