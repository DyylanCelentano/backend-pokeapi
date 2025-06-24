import os
from modelos.modelos import (
    EquipoListado,
    Integrante,
    IntegranteDeEquipoUpsert,
    Movimiento,
    Pokemon,
    Equipo,
    Generacion,
    PokemonMovimiento,
    PokemonIntegrante,
    Estadisticas,
)
from modelos.modelos_de_la_db import EquipoTabla, MovimientoTabla

METODO_MOVIMIENTO = {"huevo": 2, "nivel": 1, "maquina": 4}

ID_ESPANOL = 7
RUTA_ABSOLUTA_PROYECTO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUTA_DATA_CSV = os.path.join(RUTA_ABSOLUTA_PROYECTO, "data")
SQLITE_FILE_PATH = os.path.join(RUTA_ABSOLUTA_PROYECTO, "database.db")

RUTA_MOVES_CSV = os.path.join(RUTA_DATA_CSV, "moves.csv")
RUTA_MOVE_NAMES_CSV = os.path.join(RUTA_DATA_CSV, "move_names.csv")
RUTA_GENERATION_CSV = os.path.join(RUTA_DATA_CSV, "generation.csv")
RUTA_GENERATION_NAMES_CSV = os.path.join(RUTA_DATA_CSV, "generation_names.csv")
RUTA_POKEMON_GENERATIONS_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_generations.csv")
RUTA_TYPE_NAMES_CSV = os.path.join(RUTA_DATA_CSV, "type_names.csv")
RUTA_MOVE_DAMAGE_CLASS_PROSE_CSV = os.path.join(
    RUTA_DATA_CSV, "move_damage_class_prose.csv"
)
RUTA_MOVE_EFFECT_PROSE_CSV = os.path.join(RUTA_DATA_CSV, "move_effect_prose.csv")
RUTA_POKEMON_MOVES_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_moves.csv")
RUTA_POKEMON_CSV = os.path.join(RUTA_DATA_CSV, "pokemon.csv")
RUTA_POKEMON_TYPES_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_types.csv")

RUTA_POKEMON_ABILITIES_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_abilities.csv")
RUTA_ABILITY_NAMES_CSV = os.path.join(RUTA_DATA_CSV, "ability_names.csv")
RUTA_POKEMON_STATS_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_stats.csv")
RUTA_STAT_NAMES_CSV = os.path.join(RUTA_DATA_CSV, "stat_names.csv")
RUTA_STATS_CSV = os.path.join(RUTA_DATA_CSV, "stats.csv")

RUTA_POKEMON_EVOLUTIONS_CSV = os.path.join(RUTA_DATA_CSV, "pokemon_evolutions.csv")
RUTA_TYPE_EFFICACY_CSV = os.path.join(RUTA_DATA_CSV, "type_efficacy.csv")

GENERACIONES = [
    {"id": 1, "nombre": "Generación I"},
    {"id": 2, "nombre": "Generación II"},
    {"id": 3, "nombre": "Generación III"},
    {"id": 4, "nombre": "Generación IV"},
    {"id": 5, "nombre": "Generación V"},
    {"id": 6, "nombre": "Generación VI"},
    {"id": 7, "nombre": "Generación VII"},
    {"id": 8, "nombre": "Generación VIII"},
]
EQUIPO1 = Equipo(
    id=1,
    nombre="404 not found",
    generacion=Generacion(id=6, nombre="Generacion VI"),
    integrantes=[],
)
EQUIPO2 = Equipo(
    id=2,
    nombre="los 4 fantasticos",
    generacion=Generacion(id=3, nombre="Generacion III"),
    integrantes=[],
)
POKEMON1 = Pokemon(
    id=30,
    nombre="Nidoran",
    imagen="una imagen",
    generaciones=GENERACIONES,
    tipos=[],
    altura=8,
    peso=9,
)
POKEMON2 = Pokemon(
    id=2,
    nombre="Charmander",
    imagen="una imagen",
    generaciones=[{"id": 8, "nombre": "Generación VIII"}],
    tipos=[],
    altura=10,
    peso=11,
)

MOCK_LISTA_EQUIPOS = [
    EquipoListado(
        id=1,
        nombre="los testeadores",
        generacion=Generacion(id=8, nombre="Generacion VIII"),
        cantidad_integrantes=6,
    ),
    EquipoListado(
        id=2,
        nombre="los testeadores 2 la venganza de los tests",
        generacion=Generacion(id=8, nombre="Generacion V"),
        cantidad_integrantes=2,
    ),
    EquipoListado(
        id=3,
        nombre="los testeadores 3 el origen de los tests",
        generacion=Generacion(id=8, nombre="Generacion II"),
        cantidad_integrantes=3,
    ),
]
MOCK_EQUIPO_CREAR1 = Equipo(
    id=1,
    nombre="los testeadores 4 el test fantasma",
    generacion=Generacion(id=5, nombre="Generacion V"),
    integrantes=[],
)
MOCK_EQUIPO_CREAR2 = Equipo(
    id=1,
    nombre="los testeadores 4 el test fantasma",
    generacion=Generacion(id=8, nombre="Generacion VIII"),
    integrantes=[],
)
MOCK_INTEGRANTE_ACTUALIZADO = IntegranteDeEquipoUpsert(
    apodo="el champion", movimientos=[228, 229, 230, 231]
)
MOCK_EQUIPO_CREAR_CON_INTEGRANTE = Equipo(
    id=1,
    nombre="los testeadores 4 el test fantasma",
    generacion=Generacion(id=5, nombre="Generacion V"),
    integrantes=[
        Integrante(
            id=1,
            apodo="perrito",
            # TODO: Aplicar esta modificacion en los tests porque se cambia el modelo un poco
            pokemon=PokemonIntegrante(
                id=30,
                nombre="nidorino",
                imagen="una imagen",
                # TODO: Cambiar el cero por valores correspondientes de testeo
                estadisticas={
                    "ataque": 0,
                    "defensa": 0,
                    "ataque_especial": 0,
                    "defensa_especial": 0,
                    "puntos_de_golpe": 0,
                    "velocidad": 0,
                },
                generaciones=[],
                tipos=[],
            ),
            movimientos=[],
        )
    ],
)
MOCK_EQUIPO_ACTUALIZAR = Equipo(
    id=1,
    nombre="los testeadors 5 el test contraataca",
    generacion=Generacion(id=8, nombre="Generacion VIII"),
    integrantes=[],
)

MOCK_INTEGRANTE_ELIMINAR = Integrante(
    id=1,
    apodo="perrito",
    # TODO: Aplicar esta modificacion en los tests porque se cambia el modelo un poco
    pokemon=PokemonIntegrante(
        id=30,
        nombre="nidorina",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
        # TODO: Cambiar el cero por valores correspondientes de testeo
        estadisticas={
            "ataque": 0,
            "defensa": 0,
            "ataque_especial": 0,
            "defensa_especial": 0,
            "puntos_de_golpe": 0,
            "velocidad": 0,
        },
        generaciones=[{"id": 1, "nombre": "Generación I"}],
        tipos=[{"id": 4, "nombre": "Veneno"}],
    ),
    movimientos=[],
)

MOCK_LISTA_POKEMONES = [
    Pokemon(
        id=1,
        nombre="bulbasaur",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        altura=0.7,
        peso=6.9,
        generaciones=[],
        tipos=[],
    ),
    Pokemon(
        id=6,
        nombre="charizard",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        altura=1.7,
        peso=90.5,
        generaciones=[
            {"id": 1, "nombre": "Generación I"},
            {"id": 2, "nombre": "Generación II"},
            {"id": 3, "nombre": "Generación III"},
            {"id": 4, "nombre": "Generación IV"},
            {"id": 5, "nombre": "Generación V"},
            {"id": 6, "nombre": "Generación VI"},
            {"id": 7, "nombre": "Generación VII"},
            {"id": 8, "nombre": "Generación VIII"},
        ],
        tipos=[
            {"id": 4, "nombre": "Veneno"},
        ],
    ),
    Pokemon(
        id=30,
        nombre="nidorina",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
        altura=0.8,
        peso=20.0,
        generaciones=[
            {"id": 1, "nombre": "Generación I"},
            {"id": 2, "nombre": "Generación II"},
            {"id": 3, "nombre": "Generación III"},
            {"id": 4, "nombre": "Generación IV"},
            {"id": 5, "nombre": "Generación V"},
            {"id": 6, "nombre": "Generación VI"},
            {"id": 7, "nombre": "Generación VII"},
            {"id": 8, "nombre": "Generación VIII"},
        ],
        tipos=[
            {"id": 4, "nombre": "Veneno"},
            {"id": 12, "nombre": "Planta"},
        ],
    ),
    Pokemon(
        id=5,
        nombre="charmeleon",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
        altura=0,
        peso=0,
        generaciones=[
            {"id": 1, "nombre": "Generación I"},
            {"id": 2, "nombre": "Generación II"},
            {"id": 3, "nombre": "Generación III"},
            {"id": 4, "nombre": "Generación IV"},
            {"id": 5, "nombre": "Generación V"},
            {"id": 6, "nombre": "Generación VI"},
            {"id": 7, "nombre": "Generación VII"},
            {"id": 8, "nombre": "Generación VIII"},
        ],
        tipos=[
            {"id": 10, "nombre": "Fuego"},
        ],
    ),
]
MOCK_LISTA_MOVIMIENTOS = [
    Movimiento(
        id=1,
        nombre="Destructor",
        generacion={"id": 1, "nombre": "Generación I"},
        tipo={"id": 1, "nombre": "Normal"},
        categoria="físico",
        potencia=40,
        precision=100,
        puntos_de_poder=35,
        efecto="Inflicts regular damage with no additional effect.",
    ),
    Movimiento(
        id=2,
        nombre="Golpe Kárate",
        generacion={"id": 1, "nombre": "Generación I"},
        tipo={"id": 2, "nombre": "Lucha"},
        categoria="físico",
        potencia=50,
        precision=100,
        puntos_de_poder=25,
        efecto="Has an increased chance for a critical hit.",
    ),
    Movimiento(
        id=3,
        nombre="Doble Bofetón",
        generacion={"id": 1, "nombre": "Generación I"},
        tipo={"id": 1, "nombre": "Normal"},
        categoria="físico",
        potencia=15,
        precision=85,
        puntos_de_poder=10,
        efecto="Hits 2-5 times in one turn.",
    ),
    Movimiento(
        id=4,
        nombre="Puño Cometa",
        generacion={"id": 1, "nombre": "Generación I"},
        tipo={"id": 1, "nombre": "Normal"},
        categoria="físico",
        potencia=18,
        precision=85,
        puntos_de_poder=15,
        efecto="Hits 2-5 times in one turn.",
    ),
]

MOCK_LISTA_POKEMONES_DE_MOVIMIENTO = [
    PokemonMovimiento(
        id=1,
        nombre="bulbasaur",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        altura=0.7,
        peso=6.9,
    ),
    PokemonMovimiento(
        id=6,
        nombre="charizard",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        altura=1.7,
        peso=90.5,
    ),
    PokemonMovimiento(
        id=30,
        nombre="nidorina",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
        altura=0.8,
        peso=20.0,
    ),
    PokemonMovimiento(
        id=5,
        nombre="charmeleon",
        imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
        altura=0,
        peso=0,
    ),
]

MOCK_MOV_228 = MovimientoTabla(
    id_movimiento=228,
    nombre="Destructor",
    id_generacion_del_movimiento=2,
    id_tipo_del_movimiento=1,
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_229 = MovimientoTabla(
    id_movimiento=229,
    nombre="Destructor",
    id_generacion_del_movimiento=1,
    id_tipo_del_movimiento=5,
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_230 = MovimientoTabla(
    id_movimiento=230,
    nombre="Destructor",
    id_generacion_del_movimiento=1,
    id_tipo_del_movimiento=1,
    categoria="físico",
    potencia=330,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_231 = MovimientoTabla(
    id_movimiento=231,
    nombre="Destructor",
    id_generacion_del_movimiento=1,
    id_tipo_del_movimiento=1,
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_232 = MovimientoTabla(
    id_movimiento=232,
    nombre="Destructora",
    id_generacion_del_movimiento=2,
    id_tipo_del_movimiento=2,
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)

MOCK_MOV_MOSTRAR_231 = Movimiento(
    id=231,
    nombre="Destructor",
    generacion={"id": 1, "nombre": "Generación I"},
    tipo={"id": 1, "nombre": "Normal"},
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_MOSTRAR_230 = Movimiento(
    id=230,
    nombre="Destructor",
    generacion={"id": 1, "nombre": "Generación I"},
    tipo={"id": 1, "nombre": "Normal"},
    categoria="físico",
    potencia=330,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_MOSTRAR_229 = Movimiento(
    id=229,
    nombre="Destructor",
    generacion={"id": 1, "nombre": "Generación I"},
    tipo={"id": 5, "nombre": "Roca"},
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)
MOCK_MOV_MOSTRAR_228 = Movimiento(
    id=228,
    nombre="Destructor",
    generacion={"id": 2, "nombre": "Generación II"},
    tipo={"id": 1, "nombre": "Normal"},
    categoria="físico",
    potencia=40,
    precision=100,
    puntos_de_poder=35,
    efecto="Inflicts regular damage with no additional effect.",
)

MOCK_EQUIPO_CREAR_TABLA = EquipoTabla(
    id_equipo=1,
    nombre_equipo="los testeadores 4 el test fantasma",
    id_generacion_del_equipo=5,
    integrantes=[],
)
