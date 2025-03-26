from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schema.curso_schema import CursoSchema
from core.deps import get_session

router = APIRouter()


#POST curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, 
                            aulas=curso.aulas,
                            horas=curso.horas)
    db.add(novo_curso)
    await db.commit()

    return novo_curso

@router.get_cursos('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos
    
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session))
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalars_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        