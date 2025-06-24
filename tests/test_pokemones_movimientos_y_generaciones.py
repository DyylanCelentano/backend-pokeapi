from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from fastapi import HTTPException
import pytest
from sqlmodel import Session

from database.database import Database
from dependencias.dependencias import get_database
from dependencias.dependencias_de_la_db import get_session
from main import app
from modelos.filtros import FiltrosMovimiento, FiltrosPokemon
from modelos.modelos import (
    Estadisticas,
    Generacion,
    Habilidades,
    MovimientoDetallado,
    Pokemon,
    PokemonMovimiento,
    PokemonPorId,
    Tipo,
    Movimiento,
    Equipo,
    EquipooUpsert,
)

from constantes.constantes import (
    MOCK_LISTA_MOVIMIENTOS,
    MOCK_LISTA_POKEMONES,
    MOCK_LISTA_POKEMONES_DE_MOVIMIENTO,
)
from modelos.modelos_de_la_db import PokemonTabla


client = TestClient(app)


@pytest.fixture
def mock_session():
    return MagicMock(spec=Session)


@pytest.fixture
def mock_db():
    return MagicMock(spec=Database)


@pytest.fixture(autouse=True)
def override_dependencies(mock_session, mock_db):
    app.dependency_overrides[get_session] = lambda: mock_session
    app.dependency_overrides[get_database] = lambda: mock_db
    yield
    app.dependency_overrides.clear()


#                       ENDPOINTS POKEMON
#                       GET /api/pokemon/{id}
#                       CASOS DE ERROR
def test_get_pokemon_id_no_encontrado(mock_session, mock_db):
    mock_session.get.return_value = None

    response = client.get("/api/pokemon/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pokemon no encontrado"

    mock_session.get.assert_called_once_with(PokemonTabla, 9999)
    mock_db.get_habilidades.assert_not_called()


def test_get_pokemon_id_invalido_texto(mock_session, mock_db):
    response = client.get("/api/pokemon/abc")

    assert response.status_code == 422
    content = response.json()

    assert (
        content["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )
    mock_session.get.assert_not_called()
    mock_db.get_habilidades.assert_not_called()


def test_get_pokemon_id_negativo(mock_session, mock_db):
    response = client.get("/api/pokemon/-1")
    assert response.status_code == 422
    assert response.json()["detail"] == "El ID no puede ser negativo"

    mock_session.get.assert_not_called()
    mock_db.get_habilidades.assert_not_called()


def test_get_pokemon_completo_exitoso(mock_session, mock_db):

    poke_mock = MagicMock()
    poke_mock.id_pokemon = 1
    poke_mock.nombre = "bulbasaur"
    poke_mock.imagen = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    )
    poke_mock.altura = 0.4
    poke_mock.peso = 6.0
    poke_mock.ataque = 55
    poke_mock.defensa = 40
    poke_mock.ataque_especial = 50
    poke_mock.defensa_especial = 50
    poke_mock.puntos_de_golpe = 35
    poke_mock.velocidad = 90
    mock_generacion1 = MagicMock()
    mock_generacion1.id_generacion = 1
    mock_generacion1.nombre_generacion = "Generación I"

    mock_generacion2 = MagicMock()
    mock_generacion2.id_generacion = 2
    mock_generacion2.nombre_generacion = "Generación II"

    mock_generacion3 = MagicMock()
    mock_generacion3.id_generacion = 3
    mock_generacion3.nombre_generacion = "Generación III"

    mock_generacion4 = MagicMock()
    mock_generacion4.id_generacion = 4
    mock_generacion4.nombre_generacion = "Generación IV"
    poke_mock.generaciones = [
        mock_generacion1,
        mock_generacion2,
        mock_generacion3,
        mock_generacion4,
    ]
    mock_session.get.return_value = poke_mock

    mock_db.get_habilidades.return_value = [{"id": 1, "nombre": "Una habilidad god"}]
    mock_db.obtener_tipos_por_id.return_value = [
        {"id": 1, "nombre": "Normal"},
        {"id": 2, "nombre": "Plantita"},
    ]
    mock_db.get_evoluciones.return_value = [
        {"id": 134, "nombre": "vaporeon"},
        {"id": 135, "nombre": "jolteon"},
        {"id": 136, "nombre": "flareon"},
        {"id": 196, "nombre": "espeon"},
        {"id": 197, "nombre": "umbreon"},
        {"id": 470, "nombre": "leafeon"},
        {"id": 471, "nombre": "glaceon"},
        {"id": 700, "nombre": "sylveon"},
    ]

    mock_db.obtener_movimientos_pokemon.return_value = (
        [],
        [
            {
                "id": 22,
                "nombre": "Látigo Cepa",
                "generacion": {"id": 1, "nombre": "Generación I"},
                "tipo": {"id": 12, "nombre": "Planta"},
                "categoria": "físico",
                "potencia": 45,
                "precision": 100,
                "puntos_de_poder": 25,
                "efecto": "Inflicts regular damage with no additional effect.",
            }
        ],
        [
            {
                "id": 14,
                "nombre": "Látigo de fuego",
                "generacion": {"id": 1, "nombre": "Generación I"},
                "tipo": {"id": 12, "nombre": "Planta"},
                "categoria": "físico",
                "potencia": 45,
                "precision": 100,
                "puntos_de_poder": 25,
                "efecto": "Inflicts regular damage with no additional effect.",
            },
            {
                "id": 33,
                "nombre": "Placaje",
                "generacion": {"id": 1, "nombre": "Generación I"},
                "tipo": {"id": 1, "nombre": "Normal"},
                "categoria": "físico",
                "potencia": 40,
                "precision": 100,
                "puntos_de_poder": 35,
                "efecto": "Inflicts regular damage with no additional effect.",
            },
            {
                "id": 36,
                "nombre": "Derribo",
                "generacion": {"id": 1, "nombre": "Generación I"},
                "tipo": {"id": 1, "nombre": "Normal"},
                "categoria": "físico",
                "potencia": 90,
                "precision": 85,
                "puntos_de_poder": 20,
                "efecto": "User receives 1/4 the damage it inflicts in recoil.",
            },
        ],
    )

    response = client.get("/api/pokemon/1")
    assert response.status_code == 200
    content = response.json()

    assert content["id"] == 1
    assert content["nombre"] == "bulbasaur"
    assert len(content["generaciones"]) == 4
    assert content["estadisticas"]["ataque"] == 55
    assert content["tipos"][0]["nombre"] == "Normal"
    assert content["tipos"][1]["nombre"] == "Plantita"
    assert len(content["evoluciones"]) == 8
    assert content["habilidades"][0]["nombre"] == "Una habilidad god"
    assert content["movimientos_huevo"] == []
    assert content["movimientos_maquina"][0]["id"] == 22
    assert content["movimientos_nivel"][0]["id"] == 14
    assert len(content["movimientos_nivel"]) == 3

    mock_session.get.assert_called_once_with(PokemonTabla, 1)
    mock_db.get_habilidades.assert_called_once_with(mock_session, 1)
    mock_db.obtener_tipos_por_id.assert_called_once_with(mock_session, 1)
    mock_db.get_evoluciones.assert_called_once_with(mock_session, 1)
    mock_db.obtener_movimientos_pokemon.assert_called_once_with(mock_session, 1)

    app.dependency_overrides = {}


### Pokemon con movimientos sólo de una categoría (por nivel, máquina o huevo).
### Pokemon sin movimientos de huevo / sin evoluciones / sin habilidades ocultas.
#               Pokemon con todos los tipos de movimientos (nivel, huevo, máquina).


############ TEST GENERACIONES ##########


def test_generaciones(mock_session, mock_db):

    generaciones = [
        Generacion(id=1, nombre="Generación I"),
        Generacion(id=2, nombre="Generación II"),
        Generacion(id=3, nombre="Generación III"),
        Generacion(id=4, nombre="Generación IV"),
    ]
    mock_db.obtener_generaciones.return_value = generaciones
    response = client.get("/api/generaciones")
    assert response.status_code == 200
    content = response.json()
    assert content[0]["id"] == 1
    assert content[1]["id"] == 2
    assert content[2]["id"] == 3
    assert content[3]["id"] == 4
    mock_db.obtener_generaciones.assert_called_once_with(mock_session)


############ TEST LISTA POKEMON ##########


def test_listar_pokemones_valido(mock_session, mock_db):
    pokemones = MOCK_LISTA_POKEMONES
    mock_db.obtener_pokemones.return_value = pokemones
    response = client.get("/api/pokemon")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)

    assert content[0]["id"] == 1
    assert content[1]["id"] == 6
    assert content[2]["id"] == 30
    assert len(content[2]["generaciones"]) == 8
    assert len(content[2]["tipos"]) == 2
    assert content[2]["tipos"][0]["id"] == 4
    mock_db.obtener_pokemones.assert_called_once_with(mock_session, FiltrosPokemon())


############ TEST LISTA MOVIMIENTOS ##########


def test_listar_movimientos(mock_session, mock_db):
    movimientos = MOCK_LISTA_MOVIMIENTOS
    mock_db.obtener_movimientos.return_value = movimientos
    response = client.get("/api/movimientos")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
    assert len(content) == 4
    assert content[0]["nombre"] == "Destructor"
    assert content[1]["nombre"] == "Golpe Kárate"
    assert content[2]["nombre"] == "Doble Bofetón"
    assert content[3]["nombre"] == "Puño Cometa"
    assert content[0]["id"] == 1
    assert content[1]["id"] == 2
    assert content[2]["id"] == 3
    assert content[3]["id"] == 4
    assert content[1]["generacion"]["id"] == 1
    assert content[1]["categoria"] == "físico"
    assert content[1]["efecto"] == "Has an increased chance for a critical hit."
    mock_db.obtener_movimientos.assert_called_once_with(
        mock_session, FiltrosMovimiento()
    )


############ TEST MOVIMIENTO ESPECIFICO POR ID ##########


def test_movimiento_id_existente_completo(mock_session, mock_db):
    mock_db.obtener_movimiento.return_value = MovimientoDetallado(
        id=3,
        nombre="Doble Bofetón",
        generacion={"id": 1, "nombre": "Generación I"},
        tipo={"id": 1, "nombre": "Normal"},
        categoria="físico",
        potencia=15,
        precision=85,
        puntos_de_poder=10,
        efecto="Hits 2-5 times in one turn.",
        pokemon_por_huevo=MOCK_LISTA_POKEMONES_DE_MOVIMIENTO,
        pokemon_por_maquina=[],
        pokemon_por_nivel=[
            PokemonMovimiento(
                id=5,
                nombre="charmeleon",
                imagen="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
                altura=50.0,
                peso=10.0,
            )
        ],
    )

    response = client.get("/api/movimientos/3")

    assert response.status_code == 200
    content = response.json()

    assert content["id"] == 3
    assert content["tipo"]["id"] == 1
    assert content["generacion"]["nombre"] == "Generación I"
    assert content["tipo"]["id"] == 1
    assert len(content["pokemon_por_huevo"]) == 4
    assert len(content["pokemon_por_maquina"]) == 0
    assert len(content["pokemon_por_nivel"]) == 1

    mock_db.obtener_movimiento.assert_called_once_with(mock_session, 3)
