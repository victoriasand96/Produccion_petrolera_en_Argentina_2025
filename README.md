# Análisis de la Producción Petrolera en Argentina (2025)

## Descripción

Este proyecto presenta un análisis exploratorio de datos y un dashboard interactivo desarrollado en Power BI utilizando datos abiertos de la Secretaría de Energía de la Nación correspondientes a la producción petrolera de Argentina durante el año 2025.

El objetivo fue transformar una base de datos con más de 900.000 registros en información útil para comprender la distribución de la producción, las características de los pozos y el aporte de las principales empresas, provincias, cuencas y formaciones geológicas.

---

## Objetivos

- Realizar la limpieza y validación de los datos.
- Analizar la producción petrolera argentina.
- Identificar las provincias, cuencas y formaciones más productivas.
- Comparar la producción convencional y no convencional.
- Desarrollar un dashboard interactivo para facilitar la exploración de la información.

---

## Herramientas utilizadas

- Python
  - Pandas
  - NumPy
- Power BI


---

## Limpieza de datos

Durante el procesamiento de los datos se realizaron las siguientes tareas:

- Estandarización de nombres de empresas, corrigiendo registros donde el año aparecía incorporado en el nombre de la operadora.
- Filtrado de pozos petroleros activos para centrar el análisis en la producción efectiva.
- Revisión de registros con producción igual a cero para verificar su consistencia.
- Identificación y validación de valores extremos, confirmando la existencia de pozos con producción excepcional en la formación Vaca Muerta.
- Construcción de tablas resumen para optimizar el análisis y la visualización.

---

## Principales resultados

- Aproximadamente el **91 %** de los pozos corresponden a producción convencional.
- Sin embargo, los pozos **no convencionales generan el 62,3 % de la producción total anual**, evidenciando una productividad significativamente mayor.
- La **Cuenca Neuquina** concentra la mayor producción nacional gracias al desarrollo de los recursos no convencionales.
- Le siguen la **Cuenca del Noroeste** y la **Cuenca del Golfo San Jorge**.
- La formación **Vaca Muerta** constituye el principal polo productivo del país.
- **YPF** lidera la producción anual entre las empresas operadoras.
- La provincia de **Neuquén** concentra gran parte de la producción nacional.

---

## Dashboard

El dashboard permite explorar la producción mediante filtros por:

- Provincia
- Empresa
- Cuenca
- Tipo de recurso

![Dashboard](Images/dashboard.png)


---

## 🚀 Próximos pasos

Este proyecto continuará incorporando nuevas funcionalidades:

- Análisis de series temporales para estudiar la evolución de la producción.
- Evaluación de tendencias productivas por provincia, empresa y cuenca.
- Análisis de la productividad de los pozos de mayor rendimiento.
- Estudio del potencial de los pozos actualmente en etapa de exploración.

---

## Fuente de datos

Secretaría de Energía de la Nación – Datos Abiertos

