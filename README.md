# Análisis Super Mercado - Etapa Inicial ICI

## Introducción

En este análisis se busca determinar la viabilidad económica de abrir una nueva sucursal de supermercado en una comunidad similar a Juriquilla. Esta comunidad es conocida por su constante crecimiento poblacional, su alto nivel de desarrollo y una densidad de población considerable, factores que hacen atractivo el establecimiento de nuevas inversiones comerciales. La intención del estudio es evaluar si la nueva sucursal puede alcanzar un nivel de ventas suficiente para cubrir todos sus costos operativos y además tener una ganancia neta mensual de al menos $1,500,000.

La sucursal proyectada empleará un número significativo de trabajadores para asegurar la operatividad y el servicio al cliente. Entre los empleados considerados se encuentran cajeros, gerentes, subgerentes, conserjes, almacenistas y gestores de pasillo. Además, se incluirá personal adicional como guardias de seguridad, personal de atención al cliente y supervisores, que son fundamentales para el correcto funcionamiento de un supermercado. Los costos de nómina, ajustados a la inflación y al salario promedio en la región, representan una parte considerable de los gastos mensuales.

En términos de infraestructura, la nueva sucursal cuenta con una superficie de aproximadamente 2,000 m², un tamaño típico para grandes supermercados. Entre los gastos operativos, se han contemplado aquellos relacionados con el consumo de energía eléctrica, servicios de agua y limpieza, mantenimiento, seguros, publicidad, y la depreciación del inmueble y los equipos. Por ejemplo, el gasto en luz se estima en base a una tarifa comercial para grandes consumidores, calculando el consumo promedio en kilowatts por hora (kWh) por metro cuadrado. Según datos de la Comisión Federal de Electricidad, para un supermercado de estas dimensiones el gasto promedio de electricidad puede oscilar entre $180,000 y $220,000 mensuales, dependiendo de la eficiencia energética y del equipamiento utilizado.

Asimismo, se han considerado aspectos de la frecuencia de visitas de los clientes. Un cliente en una comunidad similar a Juriquilla suele visitar el supermercado de 2 a 3 veces por semana, lo cual implica un patrón de compras estable y recurrente. Según estudios de la industria, el ticket promedio de compra en estas comunidades puede superar los $500 MXN por visita.

Para la evaluación económica, se ha utilizado la técnica de Maximum Likelihood Estimation (MLE), la cual permite encontrar los parámetros de una función de distribución que mejor se ajustan a los datos observados. MLE se fundamenta en el principio de maximización de la probabilidad, donde se busca encontrar los parámetros que maximizan la función de verosimilitud dada una muestra de datos.

En este caso, se ha ajustado una función de densidad de probabilidad Beta, la cual es útil para modelar variables continuas en un rango limitado, como lo son las ventas normalizadas de la sucursal. La distribución Beta se caracteriza por sus dos parámetros α y β, que controlan la forma de la curva y permiten describir probabilidades asociadas a diferentes escenarios de ventas.

Para la solución del problema se ha empleado el lenguaje de programación Python, en conjunto con las bibliotecas pandas, numpy, y scipy.stats. Estas herramientas permiten realizar el análisis exploratorio de los datos, el ajuste de distribuciones estadísticas y la solución de problemas matemáticos complejos como el cálculo de costos, optimización de ventas y simulación de escenarios. 

## Análisis

### Salarios de Empleados

Cajeros: El salario de un cajero se ha estimado en $258.25 MXN por día, en base a las tarifas del salario mínimo en México reportadas por la Secretaría del Trabajo. La cantidad de cajeros se ha determinado como 30, reflejando la necesidad de atención directa a los clientes en horarios amplios y de alta concurrencia.

Conserjes: Los conserjes tienen un salario mensual de $5,000 MXN, acorde a los salarios promedio de trabajos de limpieza en México según Glassdoor.

Almacenistas: Estos empleados perciben un salario de $262.13 MXN por día, basado en estudios de salario y los requerimientos operativos de un supermercado de tamaño medio. El número total de almacenistas se ha establecido en 40 para manejar adecuadamente la carga de trabajo.

Gerente y Subgerentes: El salario mensual de un gerente ha sido estimado en $100,000 MXN, mientras que los subgerentes perciben $45,000 MXN. Estos salarios reflejan la escala de responsabilidad y experiencia requerida para estos puestos según estudios de mercado laboral en el sector de retail.

Guardias de Seguridad: Se han incluido 10 guardias con un salario de $257.88 MXN por día, aen base a las tarifas del salario mínimo en México reportadas por la Secretaría del Trabajo.

Empleados de Atención al Cliente: Los empleados de atención al cliente tienen un salario diario de $280 MXN, en línea con la responsabilidad y carga de trabajo asociada.

Supervisores: El salario diario de un supervisor se ha estimado en $836.7 MXN, acorde a los salarios promedio de trabajos como supervisor en supermercados en México según Glassdoor. Se han asignado 5 supervisores para garantizar el correcto funcionamiento y supervisión de las distintas áreas del supermercado.

### Costos Operativos

Energía Eléctrica: El consumo de electricidad para un supermercado ha sido calculado en 20 kWh por metro cuadrado por mes, tomando en cuenta el tamaño de 2000 m². El costo unitario se ha establecido en $2.3 MXN por kWh, que corresponde a las tarifas comerciales reportadas por la Comisión Federal de Electricidad (CFE). Este cálculo refleja el consumo necesario para iluminación, refrigeración, y funcionamiento de diversos equipos eléctricos.

Mantenimiento General: Se ha estimado un gasto mensual de $100,000 MXN para cubrir el mantenimiento rutinario de instalaciones, reparaciones menores y limpieza de áreas comunes. Este gasto está basado en benchmarks de la industria para supermercados de tamaño similar, que tienden a gastar entre 0.5% y 1% de sus ingresos mensuales en mantenimiento.

Publicidad y Marketing: Se ha asignado un presupuesto mensual de $200,000 MXN para publicidad y marketing, basado en el porcentaje estándar de entre 1.5% y 3% de los ingresos totales de un supermercado. Este gasto es esencial para atraer y retener clientes mediante campañas publicitarias y promociones.

Mantenimiento de Equipos y Refrigeración: El mantenimiento de equipos de refrigeración y maquinaria crítica ha sido presupuestado en $150,000 MXN al mes, en línea con los costos de mantenimiento de supermercados en México. Esto incluye la revisión y reparación periódica de refrigeradores, congeladores, y maquinaria en general.

* Frecuencia de visitas: Se ha supuesto que un cliente promedio visita el supermercado 2.5 veces por semana, basado en estudios de comportamiento del consumidor para tiendas de autoservicio y supermercados.

## Resultados 

### Análisis de Porcentaje de la Población Objetivo

En este análisis, se calculó el porcentaje de la población objetivo que necesitaría visitar la nueva sucursal para cubrir todos los costos operativos y lograr una ganancia mensual de al menos $1,500,000 MXN. Para ello, se utilizó la técnica de Maximum Likelihood Estimation (MLE) para ajustar una distribución Beta a los datos de ventas simuladas. Posteriormente, se definió el número de clientes necesarios utilizando la distribución normal para modelar la incertidumbre de los ingresos totales.

El resultado mostró que, asumiendo que un cliente promedio visita el supermercado 2.5 veces por semana, se necesitaría captar aproximadamente un 1.66% de la población objetivo de 160,000 personas en la comunidad. Este porcentaje refleja un objetivo de ventas alcanzable si se logra una campaña de marketing y fidelización efectiva.

### Probabilidad de Lograr un Rating Promedio de 8.5 o más

Para evaluar la satisfacción de los clientes y la percepción de la nueva sucursal, se analizó la distribución de ratings obtenidos en un supermercado similar en una comunidad comparable a Juriquilla. La media de los ratings fue de aproximadamente 6.97 con una desviación estándar de 1.72, lo que sugiere que, en promedio, los clientes califican positivamente la experiencia.

Utilizando el Teorema del Límite Central (CLT), se estimó la probabilidad de obtener un rating promedio de 8.5 o más, asumiendo una muestra de 1000 encuestas. El análisis mostró que la probabilidad de lograr un rating promedio de 8.5 o más es de 0%, lo cual revela un desafío significativo en términos de satisfacción del cliente. Este resultado subraya la necesidad de enfocarse en mejorar la atención al cliente, la calidad del servicio y las instalaciones para aumentar la percepción positiva de los consumidores. Para poder aumentar la probabilidad de onbtener un mejor rating podemos hacer cambios a los datos del análisis y modificar algunas cosas a tomar en cuenta para la apertura de esta nueva sucursal.

## Conclusiones

Los resultados sugieren que la nueva sucursal tiene una alta probabilidad de alcanzar la viabilidad económica si se logra captar al menos un 1.66% de la población objetivo de 160,000 habitantes. Este porcentaje parece factible, especialmente si se consideran campañas de marketing bien diseñadas y estrategias de fidelización de clientes.

Por otro lado, el análisis de los ratings revela una probabilidad nula de alcanzar un promedio de 8.5 o más, lo cual indica que es fundamental mejorar la calidad del servicio al cliente y la experiencia de compra. La administración del supermercado debe enfocarse en áreas clave como la capacitación del personal, la gestión eficiente de los tiempos de espera y la optimización de las instalaciones.

Para mantener la competitividad y el atractivo de la nueva sucursal, se recomienda monitorear constantemente la satisfacción del cliente, implementar mejoras continuas y optimizar los costos operativos para maximizar las ganancias.

## Referencias

- Instituto Nacional de Estadística y Geografía (INEGI).

- Encuesta Nacional de Ocupación y Empleo (ENOE).

- Comisión Federal de Electricidad (CFE).

- Deloitte. Reportes de benchmarking y análisis del sector de retail.

- Nielsen. Estudios de mercado y comportamiento del consumidor en supermercados.

- Kantar. Reportes de comportamiento del consumidor en el sector retail.

- Glassdoor MX