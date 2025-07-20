# Repositorio de Algoritmos
## Descripción General
Es un modulo que agrupa los distintos algoritmos que puede ejecutar el sistema, está desacoplado de tal forma que sea escalable y que permita implementar distintos algoritmos mas allá de los desarrollados.

## Funcionamiento
El código utiliza este módulo en el directorio *graph_normalizer\loader.py*, quien se encarga de transformar la lista recibida en un grafo de NetworkX, sin embargo este no ejecuta ningun algoritmo, solo prepara los datos.

De manera predefinida se espera un grafo no dirigido, por lo tanto, si en la solicitud que recibe el orquestador no se especifica, se ejecuta el modelo para el grafo no dirigido, en caso de que se especifique, se ejecutará el seleccionado, TRUE para grafos dirigidos, FALSE para grafos no dirigidos.

Cada algoritmo debe ser creado en el directorio *graph_normalizer\algorithms*, cada algoritmo es independiente y testeable, por lo tanto el código permite la adición de mas algoritmos de manera completamente modular.
