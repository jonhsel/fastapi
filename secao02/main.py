from fastapi import FastAPI

app = FastAPI()

##@app.get('/msg')
@app.get('/')
async def raiz():
    return{"msg": "Fastapi caojuri"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    #para outros terem acessso na mesma rede, o host deve ser 0.0.0.0