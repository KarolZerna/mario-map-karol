# Mario Map

### Problem-Solver Agent

### Formulación del objetivo: 
	Encontrar la tubería más cercana para que Mario vuelva a su mundo y rescate a la princesa.

### Formulación del problema:
	Los muros son altos y no puede saltar sobre ellos.

### Estado inicial
![mapaMario](https://user-images.githubusercontent.com/65570079/111385759-a447bc80-8681-11eb-951d-e4ae0044780a.png)

	Mapa del mundo extraño, Mario se encuentra en la posición (0,0)

### Estado objetivo
	Llegar a la tubería más cercana en este caso la tubería (3,0)

### Test del objetivo
	Está Mario cerca de una tubería?

### Acciones
	MOVE DOWN
	MOVE UP
	MOVE LEFT
	MOVE RIGHT

### Función de transición
	TRANSITION((pos_Mario_x, pos_Mario_y), MOVE DOWN)
	TRANSITION((pos_Mario_x, pos_Mario_y), MOVE UP)
	TRANSITION((pos_Mario_x, pos_Mario_y), MOVE LEFT)
	TRANSITION((pos_Mario_x, pos_Mario_y), MOVE RIGHT)

### Costo
	1 cada casilla hasta llegar a la tuberia

### Buscar, solucionar y ejecutar
En este caso la mejor solución es usar BFS ya que con DFS si tendriamos 4 casillas vacías formando un cuadrado no funcionaría de manera óptima, BFS garantiza encontrar la solución óptima y el costo de la solución es mínino.

### Cómo funcionará mi algoritmo?? Cómo resolverá el problema??
Resuelve el problema usando el algoritmo de BFS el cuál utiliza colas y creando un array para la posición de Mario vamos revisando si llega a una tuberia y con las acciones revisamos el camino por donde puede avanzar ya que hay muros que no puede saltar, si encontramos el camino libre para avanzar añadimos las posiciones a la cola y al array de Mario.


