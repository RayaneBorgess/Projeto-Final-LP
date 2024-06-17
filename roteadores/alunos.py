import uuid  # Importa o módulo uuid para gerar IDs únicos
from typing import Dict  # Importa os tipos Dict e Any do módulo typing para anotação de tipos

from fastapi import APIRouter, HTTPException, Request  # Importa os módulos necessários do FastAPI

from dados.db import ler_dados, salvar_dados  # Importa as funções ler_dados e salvar_dados do módulo dados.db
from modelos.aluno import Aluno  # Importa a classe Aluno do módulo modelos.aluno
from validacoes.aluno import validar_aluno  # Importa a função validar_aluno do módulo validacoes.aluno

# Cria um roteador para definir as rotas relacionadas aos alunos
router = APIRouter()


@router.post("/alunos/", response_model=None)
async def adicionar_aluno(request: Request):
    """
    Adiciona um novo aluno.

    Args:
        request (Request): A solicitação HTTP contendo os dados do aluno.

    Returns:
        Dict[str, Any]: Um dicionário contendo os dados do aluno adicionado.
    """
    aluno_data = await request.json()
    notas = aluno_data.get("notas", {})

    aluno_obj = Aluno(nome=aluno_data["nome"], notas=notas)
    try:
        validar_aluno(aluno_obj)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    aluno_obj.id = str(uuid.uuid4())

    dados = ler_dados()
    dados[aluno_obj.id] = aluno_obj
    salvar_dados(dados)
    return aluno_obj.to_dict()


@router.get("/alunos/{aluno_id}", response_model=None)
def obter_aluno(aluno_id: str):
    """
    Obtém os dados de um aluno pelo ID.

    Args:
        aluno_id (str): O ID do aluno.

    Returns:
        Dict[str, Any]: Um dicionário contendo os dados do aluno.
    """
    dados = ler_dados()
    if aluno_id not in dados:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return dados[aluno_id].to_dict()


@router.get("/alunos/", response_model=None)
def listar_alunos():
    """
    Lista todos os alunos.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo os dados de todos os alunos.
    """
    dados = ler_dados()
    return [aluno.to_dict() for aluno in dados.values()]


@router.delete("/alunos/", response_model=None)
def remover_alunos_sem_notas():
    """
    Remove alunos que não possuem notas registradas em nenhuma disciplina.

    Returns:
        Dict[str, str]: Uma mensagem indicando quantos alunos foram removidos.
    """
    dados = ler_dados()
    ids_para_remover = [id for id, aluno in dados.items() if all(nota == 0 for nota in aluno.notas.to_dict().values())]
    for id in ids_para_remover:
        del dados[id]
    salvar_dados(dados)
    return {"message": f"{len(ids_para_remover)} alunos removidos."}


@router.delete("/alunos/{aluno_id}", response_model=None)
def deletar_aluno(aluno_id: str):
    """
    Deleta um aluno pelo ID.

    Args:
        aluno_id (str): O ID do aluno.

    Returns:
        Dict[str, str]: Uma mensagem indicando que o aluno foi deletado com sucesso.
    """
    dados = ler_dados()
    if aluno_id not in dados:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    del dados[aluno_id]
    salvar_dados(dados)
    return {"message": "Aluno deletado com sucesso."}
