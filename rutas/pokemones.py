from fastapi import APIRouter, HTTPException, Depends
from dependencias.dependencias import DatabaseDep
from dependencias.dependencias_de_la_db import SessionDep
from modelos.modelos import Pokemon, PokemonPorId, PokemonLista, Generacion
from modelos.modelos_de_la_db import PokemonTabla
from modelos.filtros import FiltrosPokemon

router = APIRouter()


@router.get("/")
def obtener_pokemones(
    session: SessionDep,
    db: DatabaseDep,
    filtros: FiltrosPokemon = Depends(),
) -> list[PokemonLista]:
    pokemones = db.obtener_pokemones(session, filtros)
    return pokemones


@router.get("/{id}", response_model=PokemonPorId)
def get_pokemon(session: SessionDep, id: int, db: DatabaseDep):
    if id < 0:
        raise HTTPException(status_code=422, detail="El ID no puede ser negativo")

    pokemon_obtener = session.get(PokemonTabla, id)
    if pokemon_obtener is None:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado")
    habilidades = db.get_habilidades(session, id)
    generaciones = [
        Generacion(id=generacion.id_generacion, nombre=generacion.nombre_generacion)
        for generacion in pokemon_obtener.generaciones
    ]
    tipos = db.obtener_tipos_por_id(session, id)
    evoluciones = db.get_evoluciones(session, id)
    movimientos_huevo, movimientos_maquina, movimientos_nivel = (
        db.obtener_movimientos_pokemon(session, id)
    )

    return PokemonPorId(
        id=pokemon_obtener.id_pokemon,
        nombre=pokemon_obtener.nombre,
        imagen=pokemon_obtener.imagen,
        altura=pokemon_obtener.altura,
        peso=pokemon_obtener.peso,
        generaciones=generaciones,
        tipos=tipos,
        habilidades=habilidades,
        estadisticas={
            "ataque": pokemon_obtener.ataque,
            "defensa": pokemon_obtener.defensa,
            "ataque_especial": pokemon_obtener.ataque_especial,
            "defensa_especial": pokemon_obtener.defensa_especial,
            "puntos_de_golpe": pokemon_obtener.puntos_de_golpe,
            "velocidad": pokemon_obtener.velocidad,
        },
        evoluciones=evoluciones,
        movimientos_huevo=movimientos_huevo,
        movimientos_maquina=movimientos_maquina,
        movimientos_nivel=movimientos_nivel,
    )
