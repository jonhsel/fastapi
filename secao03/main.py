from models import Curso

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from typing import List, Optional

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
       # curso.update({"id": curso_id})

        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!"
        )

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
#async def post_curso(curso: Optional[Curso]=None):
async def post_curso(curso: Curso):
    '''if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Já existe um curso com ID {curso.id}")'''
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return  curso
    
@app.put('/cursos')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Não existe um curso com esse {curso_id}.")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True,  reload=True)