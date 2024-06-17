import statistics  # Importa o módulo statistics para cálculos estatísticos

from fastapi import APIRouter, HTTPException  # Importa os módulos necessários do FastAPI

from dados.db import ler_dados  # Importa a função ler_dados do módulo dados.db

# Cria um roteador para definir as rotas relacionadas às notas
router = APIRouter()


@router.get("/notas/disciplina/{disciplina}", response_model=None)
def recuperar_notas_disciplina(disciplina: str):
    """
    Recupera as notas dos alunos para uma disciplina específica, ordenadas em ordem crescente.

    Args:
        disciplina (str): O nome da disciplina.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo os nomes dos alunos e suas notas.
    """
    dados = ler_dados()
    alunos_com_notas = [
        {"nome": aluno.nome, "nota": aluno.notas.to_dict().get(disciplina, 0)}
        for aluno in dados.values()
        if disciplina in aluno.notas.to_dict()
    ]
    if not alunos_com_notas:
        raise HTTPException(status_code=404, detail=f"Nenhuma nota encontrada para a disciplina '{disciplina}'.")
    alunos_com_notas.sort(key=lambda x: x["nota"])
    return alunos_com_notas


@router.get("/notas/estatisticas/{disciplina}", response_model=None)
def calcular_estatisticas_disciplina(disciplina: str):
    """
    Calcula estatísticas de desempenho (média, mediana e desvio padrão) das notas dos alunos para uma disciplina específica.

    Args:
        disciplina (str): O nome da disciplina.

    Returns:
        Dict[str, float]: Um dicionário contendo as estatísticas de desempenho.
    """
    dados = ler_dados()
    notas = [
        aluno.notas.to_dict().get(disciplina, 0)
        for aluno in dados.values()
        if disciplina in aluno.notas.to_dict()
    ]
    if not notas:
        raise HTTPException(status_code=404, detail="Nenhuma nota encontrada para a disciplina especificada.")

    media = round(statistics.mean(notas), 1)
    mediana = round(statistics.median(notas), 1)
    desvio_padrao = round(statistics.stdev(notas), 1) if len(notas) > 1 else 0.0

    return {
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao
    }


@router.get("/notas/desempenho/baixo/{disciplina}", response_model=None)
def alunos_desempenho_baixo(disciplina: str):
    """
    Recupera os alunos com desempenho abaixo do esperado (nota menor que 6.0) em uma disciplina específica.

    Args:
        disciplina (str): O nome da disciplina.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo os nomes dos alunos e suas notas abaixo do esperado.
    """
    dados = ler_dados()
    alunos_abaixo = [
        {"nome": aluno.nome, "nota": aluno.notas.to_dict().get(disciplina, 0)}
        for aluno in dados.values()
        if disciplina in aluno.notas.to_dict() and aluno.notas.to_dict().get(disciplina, 0) < 6.0
    ]
    if not alunos_abaixo:
        raise HTTPException(status_code=404,
                            detail=f"Nenhum aluno com desempenho baixo encontrado para a disciplina '{disciplina}'.")
    return alunos_abaixo
