Biorreactor-Energy-Predictor:

Desarrollo de un programa basado en el lenguaje de Python para la predicción de las necesidades energéticas de biorreactores tipo Batch (tanque agitado con chaqueta).


Resumen


Para modelación de procesos biotecnológicos es necesario contar con parámetros y variables, siendo las asociadas a la cinética térmica y crecimiento las de mayor interés. En este proyecto se ha desarrollado una herramienta para el cálculo de las necesidades energéticas en biorreactores tipo Batch, como complemento al diseño de bioprocesos. La aplicación se diseñó en el lenguaje de programación de Python, el programa tiene variables de entrada como la temperatura, el tiempo de operación, variables asociadas a la transferencia de calor (cp, coeficiente global y área de transferencia de calor) y como variables de salida, obtenemos la cinética térmica y de crecimiento microbiano ajustado al modelo de Arrhenius.  La versión 1.0 del aplicativo, es capaz de simular de manera básica y aproximada, las necesidades energéticas en biorreactores tipo Batch, proporciona una primera aproximación de valores energéticos y se espera que las versiones posteriores se puedan acoplar a sensores de los biorreactores para el monitoreo de bioprocesos en tiempo real.

Palabras claves: Procesos biotecnológicos, modelo matemático, biorreactores, necesidades energéticas, Python.

Ecuaciones de transferencias de calor describen cómo se transmite el calor dentro del reactor:

imagen 2. ecuacion 1.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/2b0cd8ff-b866-4304-9f9c-3aeeffe1daaf)

imagen 3. ecuacion 2.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/d8869449-7c74-4418-ac04-797ba69d3a8b)

imagen 4. ecuacion 3.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/13666d57-43cc-40ce-b07f-30621673133d)

imagen 5. ecuacion 4.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/23f776b9-1e79-4184-a084-fc01e44111d2)

tabla 1. Datos experimentales de las variables utilizadas en la aplicacion.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/f4849477-fba0-49c8-87b9-f5a7a59cb8e9)

imagen 6. flujograma de la metodologia.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/0b7665f5-108c-4ba5-b001-7c299e6147c5)

Resultados:

se logor obtener una herramienta prometedora para el cálculo de las necesidades energéticas en biorreactores tipo Batch en la modelación de procesos biotecnológicos. Con futuras actualizaciones y su integración con sensores, esta herramienta tiene el potencial de impactar positivamente en la industria biotecnológica al optimizar el diseño y monitoreo de bioprocesos, mejorando así la eficiencia y los resultados obtenidos.

imagen 7. version 1.0 de la aplicacion Biorreactor-Energy-Predictor.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/4f554a36-64c5-4eb6-8bda-ee3351ab8aaa)

imagen 8. version 2.0 de la aplicacion Biorreactor-Energy-Predictor.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/2a986545-2979-4fe3-bdfe-8bddb2b6e87d)

imagen 9. resultado despues de ejecutar el programa.

![image](https://github.com/EnergyBiorreactor/BEP/assets/137831522/f63b3f3f-fb80-4b8b-b0ba-be73a0b514a1)




