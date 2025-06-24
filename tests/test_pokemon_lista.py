from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from database.database import Database
from dependencias.dependencias import get_database
from main import app
from modelos.modelos import Pokemon

client = TestClient(app)

mock_db = MagicMock(Database)
app.dependency_overrides[get_database] = lambda: mock_db

#                               GET /api/pokemon
#                               Casos de error:

###         Parámetro tipo inexistente → /api/pokemon?tipo=9999 → 400 (bad request)


def test_listar_pokemones_con_nombre_parcial_invalido():
    response = client.get("/api/pokemon?nombre_parcial=123")
    assert response.status_code == 200
    assert response.json() == []


def test_combinacion_sin_resultados():
    mock_db.obtener_pokemones.return_value = []
    response = client.get("/api/pokemon?tipo=4&nombre_parcial=xyz")

    assert response.status_code == 200
    content = response.json()
    assert content == []


#                               Casos borde
###         Búsqueda con tipo válido pero nombre parcial muy corto → /api/pokemon?nombre_parcial=n.
###
###
#                               Casos generales


def test_buscador_nombre_corto_con_tipo_valido():
    # Configurar datos de prueba
    mock_db.obtener_pokemones.return_value = [
        {
            "id": 1,
            "nombre": "Pikachu",
            "imagen": "img",
            "altura": 4,
            "peso": 60,
            "ataque": 55,
            "defensa": 40,
            "ataque_especial": 50,
            "defensa_especial": 50,
            "puntos_de_golpe": 35,
            "velocidad": 90,
            "tipos": ["Eléctrico"],
            "habilidades": ["Estática"],
            "movimientos": ["Impactrueno"],
            "evoluciones": ["Raichu"],
        }
    ]

    # Realizar la búsqueda con nombre parcial corto y tipo válido
    response = client.get("/api/pokemon?nombre_parcial=p&tipo=1")

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    assert content[0]["nombre"] == "Pikachu"


def test_buscador_nombre_corto_sin_resultados():
    # Configurar datos de prueba
    mock_db.obtener_pokemones.return_value = []

    # Realizar la búsqueda con nombre parcial corto
    response = client.get("/api/pokemon?nombre_parcial=n")

    assert response.status_code == 200
    assert response.json() == []


def test_buscador_nombre_completo():
    # Configurar datos de prueba
    mock_db.obtener_pokemones.return_value = [
        {
            "id": 1,
            "nombre": "Pikachu",
            "imagen": "img",
            "altura": 4,
            "peso": 60,
            "ataque": 55,
            "defensa": 40,
            "ataque_especial": 50,
            "defensa_especial": 50,
            "puntos_de_golpe": 35,
            "velocidad": 90,
            "tipos": ["Eléctrico"],
            "habilidades": ["Estática"],
            "movimientos": ["Impactrueno"],
            "evoluciones": ["Raichu"],
        }
    ]

    # Realizar la búsqueda con nombre completo
    response = client.get("/api/pokemon?nombre_parcial=pikachu")

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    assert content[0]["nombre"] == "Pikachu"


def test_buscador_nombre_con_mayusculas():
    # Configurar datos de prueba
    mock_db.obtener_pokemones.return_value = [
        {
            "id": 1,
            "nombre": "Pikachu",
            "imagen": "img",
            "altura": 4,
            "peso": 60,
            "ataque": 55,
            "defensa": 40,
            "ataque_especial": 50,
            "defensa_especial": 50,
            "puntos_de_golpe": 35,
            "velocidad": 90,
            "tipos": ["Eléctrico"],
            "habilidades": ["Estática"],
            "movimientos": ["Impactrueno"],
            "evoluciones": ["Raichu"],
        }
    ]

    # Realizar la búsqueda con mayúsculas
    response = client.get("/api/pokemon?nombre_parcial=PIKACHU")

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    assert content[0]["nombre"] == "Pikachu"
