from models import Curso

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2:{
        "titulo": "algoritmos e logica de programação",
        "aulas": 58,
        "horas": 84
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
#async def get_curso(curso_id):
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})

        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!"
        )

@app.post('/cursos')
async def post_cursos(curso = Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com ID {curso.id}")
    



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True,  reload=True)