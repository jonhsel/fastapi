from fastapi import APIRouter

router = APIRouter()

@router.app.get('/api/v1/usuarios')
async def get_usuarios():
    return {'info': 'retornando todos os usuários cadastrados'}