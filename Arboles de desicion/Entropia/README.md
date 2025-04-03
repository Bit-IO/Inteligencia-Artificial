# Entropia de un robot movil

Dado un robot movil con 3 sensores los cuales su ubicacion son S1 a la izquierda, S2 al frente y S3 a la derecha, segun sea lo que detecte dara una respuesta de "Si" y "No".

|Sensores|Deteccion (y)|
|:------------:|:-----:|
|Izquierda (S1)|Si / No|
|Frente (S2)   |Si / No|
|Derecha (S3)  |Si / No|

La entropia del arbol de desicion es denotada por:

$$
Entropy(y, S) = \sum_{c_j\in dom(y)} -P_y(S) log_2 P_y(S)
$$

Donde:

$$
P_y(S) = \left(\frac{|\sigma_{y=c_i}S|}{|S|},...,\frac{|\sigma_{y=c_{|dom(y)|}}S|}{|S|} \right)
$$
