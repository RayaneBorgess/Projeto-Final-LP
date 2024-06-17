from fastapi import FastAPI  # Importa o módulo FastAPI para criar a aplicação

from roteadores import alunos, notas  # Importa os roteadores dos módulos alunos e notas

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Inclui os roteadores para gerenciar rotas relacionadas a alunos e notas
app.include_router(alunos.router)
app.include_router(notas.router)


@app.get("/")
def read_root():
    """
    Rota raiz que retorna uma mensagem de boas-vindas.

    Returns:
        Dict[str, str]: Um dicionário contendo a mensagem de boas-vindas.
    """
    return {"message": "Sistema de Gestão de Notas Escolares"}


if __name__ == "__main__":
    import uvicorn  # Importa o módulo uvicorn para rodar a aplicação

    # Inicia a aplicação com o servidor uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
