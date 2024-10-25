import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, norm

df = pd.read_csv("SuperMarketData.csv")
print(df.head())

sales = np.array(df["Sales"])*19.88

max_sales = max(sales)
min_sales = min(sales)
sales_norm = 1/(max_sales-min_sales) * sales

print(sales_norm)

a,b,_,_=beta.fit(sales)
print(a,b)

mu_norm = a/(a + b)
var_norm = (a * b) / (((a + b)**2)*(a + b + 1))
desv_norm = np.sqrt(var_norm)

mu = (max_sales - min_sales) * mu_norm
var = ((max_sales - min_sales)**2) * var_norm

print(mu_norm, desv_norm)

dias_t = 24
fact = 1.15

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

nom_total = (tot_cajeros + tot_conserjes + tot_almacenistas + tot_gpasillo) * fact + tot_gerentes

print(nom_total)

gasto_luz = 120*2000*12*2.3*30
print(gasto_luz)

gastos_tot = nom_total + gasto_luz + 1500000
print(gastos_tot)

om = norm.ppf(0.01)
a_ = mu**2
b_ = -2 * mu * gastos_tot - om**2 * var
c_ = gastos_tot**2
N1 = (-b_+np.sqrt(b_**2-4*a_*c_))/(2*a_)
N2 = (-b_-np.sqrt(b_**2-4*a_*c_))/(2*a_)

print(N1, N2)

if(gastos_tot/N1-mu > 0):
  N = N1
else :
  N = N2

porc_pob = N/160000
print(porc_pob)