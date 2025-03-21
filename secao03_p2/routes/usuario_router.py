from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/usuarios')
async def get_usuarios():
    return {'info': 'retornando todos os usuários cadastrados'}