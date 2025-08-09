# Funcionamiento
Este microservicio es un agregado al sistema, que basicamente tiene una lista fija de nodos en mantenimiento semanalmente, utilizando MOD 7 para los calculos. Estos datos están quemados, no son dinámicos, pero funcionan perfectamente para simular un escenario empresarial en el cual unas ciudades están en mantenimeinto, con ello tambien apegandonos al requerimiento del profesor acerca del proyecto.

La labor de este microservicio es calcular que nodos estarán en mantenimeinto dado una fecha o bien una sumatoria de dias a partir del 2025-01-01, esta ifnormación es editable desde el config.py, donde hay un pequeño comentario explicativo.

La idea, es que esto sea un modulo desacoplado, y que, routing-service, pueda realizar cálculos a partir de consultarle a este microservicio el mantenimeinto, y así realizar algoritmos a partir de una lista dada de nodos en mantenimiento. La lista la carga el sistema desde groups_map.json.