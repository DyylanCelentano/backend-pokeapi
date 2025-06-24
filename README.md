[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Hg0ouXFc)
# Backend PokeAPI

## Temas

- Git
- Trabajo en equipo
- Testing
- Bases de Datos Relacionales (Sqlite)
- Desarrollo BackEnd (Framework: FastAPI)


## Consigna



## Endpoints

### Generaciones

#### Listar Generaciones existentes
```
GET /api/generaciones/
```
Devuelve su ID y nombre y estarán ordenadas de menor a mayor.

### Pokemon

#### Obtener un pokemon específico a partir de su ID

```
GET /api/pokemon/30
```
Devuelve su ID, nombre, imagen, altura, peso, generaciones, tipos, habilidades, stats, evoluciones y movimientos según su método de aprendizaje (huevo, máquina de tiempo, nivel).

#### Listar todos los pokemon

```
GET /api/pokemon
```
Devuelve de cada pokemon su ID, nombre, imagen, generaciones y tipos:

#### Filtrar pokemon

El endpoint recién nombrado deberá además poder filtrar la lista de pokemones:

```
GET /api/pokemon?tipo=4
GET /api/pokemon?nombre_parcial=ido
```

La respuesta mostrará una lista que sólo va a contener pokemones que tengan ese `tipo` y/o que contengan el `nombre_parcial` dentro de su nombre.


### Movimientos

#### Obtener la información de un movimiento a partir de su ID

```
GET /api/movimientos/<id>
```
Devuelve su ID, nombre, su tipo (Roca, Planta, etc), categoría (Fisico, Estado, Especial, etc), potencia (power), precision (accuracy), puntos de poder (pp), generación en la que fue introducido, efecto en texto, Pokemon que lo pueden aprenden (separado según si es por huevo, máquina, o nivel)


#### Listar movimientos

```
GET /api/movimientos
```
Devuelve cada movimiento con su ID, nombre, tipo (Roca, Planta, etc), categoría (Fisico, Estado, Especial, etc), potencia (power), precision (accuracy), puntos de poder (pp), generación en la que fue introducido y efecto en texto.

#### Filtrar movimientos

```
GET /api/movimiento?tipo=4
GET /api/movimiento?nombre_parcial=ido
```

La respuesta mostrará una lista que sólo va a contener movimientos que sean de ese `tipo` y/o que contengan el `nombre_parcial` dentro de su nombre.


### Equipos

Condiciones de un equipo:
  - se le asocia una generación que es la "máxima" generación que se permite: lo que implica que sus pokemones, movimientos y etc deben existir en esa generación o una anterior.
  - se permiten como máximo 6 integrantes, pero puede existir un equipo con 0 integrantes.
  - cada integrante debe referenciar a un Pokemon existente según la generación elegida.
  - cada integrante debe tener no más de 4 movimientos, pero puede tener 0 movimientos.
  - los movimientos elegidos para cada integrante deben ser válidos para ese Pokemon y esa generación.


#### Obtener la información de un equipo a partir de su ID:
```
GET /api/equipos/<id>
```
que devolverá su ID, nombre, generación y la lista de integrantes con su información.

#### Listar equipos
```
GET /api/equipos
```
que devolverá para una lista de equipos, donde para cada equipo detallará su ID, nombre, cantidad de integrantes y generación.

#### Crear un equipo
```
POST /api/equipos

Body:
{
    "nombre": "Equipo Rocket",
    "id_generacion": 4
}
```
que recibirá la información del equipo a crear (nombre único y ID de su generación)
y devolverá la información del equipo creado.

#### Actualizar un equipo
```
PUT /api/equipos/<id_equipo>

Body:
{
    "nombre": "Team Rocket",
    "id_generacion": 4
}
```
que permite cambiar el nombre o generación del equipo (si el equipo ya cuenta con integrantes, no se puede asignar una generación inválida con los mismos).
Devolverá la misma información que en el endpoint de crear equipo

#### Eliminar equipo
```
DELETE /api/equipos/<id_equipo>
```
que permite eliminar un equipo creado. Todos los integrantes deben ser eliminados también.
Devolverá la información completa del equipo eliminado

#### Agregar un Integrante a un equipo
```
POST /api/equipos/<id_equipo>/integrantes

Body:
{
    "id_pokemon": 23,
    "apodo": "Champion",
}
```
donde un Integrante de un equipo debe referenciar a un Pokemon existente (por su ID)
y el endpoint devolverá la información del integrante creado.

#### Agregar un Movimiento a un Integrante
```
POST /api/equipos/<id_equipo>/integrantes/<id_integrante>/movimientos

Body:
{
    "id_movimiento": 228
}
```
donde se debe referenciar a un Movimiento existente (por su ID)
y el endpoint devolverá la información del movimiento agregado.


#### Editar un Integrante de un equipo
```
PUT /api/equipos/<id_equipo>/integrantes/<id_integrante>

Body:
{
    "apodo": "Campeón",
    "movimientos": [228]
}
```
donde un Integrante de un equipo debe referenciar a un Pokemon existente (por su ID)
y el endpoint devolverá la información del integrante creado.

Este endpoint permite agregar múltiples movimientos en una sola interacción a un mismo integrante (además de editar su apodo). Si hay error en alguno de los movimientos (por ejemplo, algún movimiento inválido), debe fallar toda la operación sin haber cambiado nada.
Notar que el id_pokemon no se permite editar. Si se quiere cambiar el Pokemon elegido se debe eliminar el integrante y agregar uno nuevo.

#### Eliminar un Integrante de un equipo
```
DELETE /api/equipos/<id_equipo>/integrantes/<id_integrante>
```