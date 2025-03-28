from fastapi import APIRouter

from api.v1.endpoints import curso


api_router = APIRouter()
api_router.include_router(curso.router, prefix="/cursos", tags=["cursos"])

#Endpoint completo
# api/v1/cursos/
# api/v1/cursos/{curso_id}
# api/v1/cursos/{curso_id}/alunos
# api/v1/cursos/{curso_id}/alunos/{aluno_id}
# api/v1/cursos/{curso_id}/alunos/{aluno_id}/notas