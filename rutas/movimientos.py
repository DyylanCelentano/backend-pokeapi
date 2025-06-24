from fastapi import APIRouter, Depends
from dependencias.dependencias import DatabaseDep
from dependencias.dependencias_de_la_db import SessionDep
from modelos.filtros import FiltrosMovimiento
from modelos.modelos import Movimiento, MovimientoDetallado

router = APIRouter()


@router.get("/")
def obtener_movimientos(
    session: SessionDep,
    db: DatabaseDep,
    filtros: FiltrosMovimiento = Depends(),
) -> list[Movimiento]:
    movimientos = db.obtener_movimientos(session, filtros)
    return movimientos


@router.get("/{id}")
def obtener_movimiento_id(
    session: SessionDep, db: DatabaseDep, id: int
) -> MovimientoDetallado:
    movimiento = db.obtener_movimiento(session, id)

    return movimiento
