from fastapi import FastAPI
from routes import curso_router
from routes import usuario_router

app = FastAPI()

app.include_router(curso_router.router, tags=['Cursos'], prefix='/api/v1')
app.include_router(usuario_router.router, tags=['Usuários'], prefix='/api/v1')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True, debug=True)