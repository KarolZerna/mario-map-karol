# Mario Map

### Problem-Solver Agent

### Formulación del objetivo: 
Encontrar la tubería más cercana para que Mario vuelva al mundo y rescate a la princesa.

### Formulación del problema:
Los muros son altos y no puede saltar sobre ellos

### Estado inicial
![mapaMario](https://user-images.githubusercontent.com/65570079/111385759-a447bc80-8681-11eb-951d-e4ae0044780a.png)

Mapa de Mario

### Estado objetivo
Llegar a la tubería más cercana

### Test del objetivo
	Está Mario cerca de una tubería o de un muro??

### Acciones
	MOVE DOWN
	MOVE UP
	MOVE LEFT
	MOVE RIGHT

### Función de transición
TRANSITION(MARIO, MOVE DOWN)

### Costo
1 cada casilla

### Buscar, solucionar y ejecutar
BFS ya que garantiza encontrar la solución óptima

### Cómo funcionará mi algoritmo?? Cómo resolverá el problema??

