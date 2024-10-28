# Análisis Super Mercado - Etapa Inicial ICI

## Introducción

En este análisis se busca determinar la viabilidad económica de abrir una nueva sucursal de supermercado en una comunidad similar a Juriquilla. Esta comunidad es conocida por su constante crecimiento poblacional, su alto nivel de desarrollo y una densidad de población considerable, factores que hacen atractivo el establecimiento de nuevas inversiones comerciales. La intención del estudio es evaluar si la nueva sucursal puede alcanzar un nivel de ventas suficiente para cubrir todos sus costos operativos y además tener una ganancia neta mensual de al menos $1,500,000.

La sucursal proyectada empleará un número significativo de trabajadores para asegurar la operatividad y el servicio al cliente. Entre los empleados considerados se encuentran cajeros, gerentes, subgerentes, conserjes, almacenistas y gestores de pasillo. Además, se incluirá personal adicional como guardias de seguridad, personal de atención al cliente y supervisores, que son fundamentales para el correcto funcionamiento de un supermercado. Los costos de nómina, ajustados a la inflación y al salario promedio en la región, representan una parte considerable de los gastos mensuales.

En términos de infraestructura, la nueva sucursal cuenta con una superficie de aproximadamente 2,000 m², un tamaño típico para grandes supermercados. Entre los gastos operativos, se han contemplado aquellos relacionados con el consumo de energía eléctrica, servicios de agua y limpieza, mantenimiento, seguros, publicidad, y la depreciación del inmueble y los equipos. Por ejemplo, el gasto en luz se estima en base a una tarifa comercial para grandes consumidores, calculando el consumo promedio en kilowatts por hora (kWh) por metro cuadrado. Según datos de la Comisión Federal de Electricidad, para un supermercado de estas dimensiones el gasto promedio de electricidad puede oscilar entre $180,000 y $220,000 mensuales, dependiendo de la eficiencia energética y del equipamiento utilizado.

Asimismo, se han considerado aspectos de la frecuencia de visitas de los clientes. Un cliente en una comunidad similar a Juriquilla suele visitar el supermercado de 2 a 3 veces por semana, lo cual implica un patrón de compras estable y recurrente. Según estudios de la industria, el ticket promedio de compra en estas comunidades puede superar los $500 MXN por visita.

Para la evaluación económica, se ha utilizado la técnica de Maximum Likelihood Estimation (MLE), la cual permite encontrar los parámetros de una función de distribución que mejor se ajustan a los datos observados. MLE se fundamenta en el principio de maximización de la probabilidad, donde se busca encontrar los parámetros que maximizan la función de verosimilitud dada una muestra de datos.

En este caso, se ha ajustado una función de densidad de probabilidad Beta, la cual es útil para modelar variables continuas en un rango limitado, como lo son las ventas normalizadas de la sucursal. La distribución Beta se caracteriza por sus dos parámetros α y β, que controlan la forma de la curva y permiten describir probabilidades asociadas a diferentes escenarios de ventas.

Para la solución del problema se ha empleado el lenguaje de programación Python, en conjunto con las bibliotecas pandas, numpy, y scipy.stats. Estas herramientas permiten realizar el análisis exploratorio de los datos, el ajuste de distribuciones estadísticas y la solución de problemas matemáticos complejos como el cálculo de costos, optimización de ventas y simulación de escenarios. 

