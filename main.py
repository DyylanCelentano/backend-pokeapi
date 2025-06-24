from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from dependencias.dependencias_sql import init_engine
from dependencias.dependencias_de_la_db import init_engine
from rutas.index import api_router
from dependencias.dependencias import inicializar_deps
from seed import seed


def main():
    init_engine()
    inicializar_deps()
    seed()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

main()


@app.get("/")
def root():
    return {"message": "Pokemon API"}
