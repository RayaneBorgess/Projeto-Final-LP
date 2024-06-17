import json  # Importa o módulo JSON para ler e escrever arquivos JSON
from typing import Dict  # Importa o tipo Dict do módulo typing para anotação de tipos
from modelos.aluno import Aluno  # Importa a classe Aluno do módulo modelos.aluno

# Define o caminho do arquivo onde os dados dos alunos serão armazenados
ARQUIVO_DADOS = "dados/alunos.json"


def ler_dados() -> Dict[str, Aluno]:
    """
    Lê os dados dos alunos a partir do arquivo JSON.

    Returns:
        Dict[str, Aluno]: Um dicionário onde as chaves são IDs de alunos e os valores são objetos Aluno.
    """
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados_json = json.load(arquivo)
            return _converter_dados_para_alunos(dados_json)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def salvar_dados(dados: Dict[str, Aluno]) -> None:
    """
    Salva os dados dos alunos no arquivo JSON.

    Args:
        dados (Dict[str, Aluno]): Um dicionário onde as chaves são IDs de alunos e os valores são objetos Aluno.
    """
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        dados_json = _converter_alunos_para_dados(dados)
        json.dump(dados_json, arquivo, indent=4, ensure_ascii=False)


def _converter_dados_para_alunos(dados_json: Dict[str, Dict]) -> Dict[str, Aluno]:
    """
    Converte um dicionário JSON em um dicionário de objetos Aluno.

    Args:
        dados_json (Dict[str, Dict]): Um dicionário JSON onde as chaves são IDs de alunos e os valores são dicionários de dados dos alunos.

    Returns:
        Dict[str, Aluno]: Um dicionário onde as chaves são IDs de alunos e os valores são objetos Aluno.
    """
    return {id_aluno: Aluno.from_dict(dados_aluno) for id_aluno, dados_aluno in dados_json.items()}


def _converter_alunos_para_dados(dados: Dict[str, Aluno]) -> Dict[str, Dict]:
    """
    Converte um dicionário de objetos Aluno em um dicionário JSON.

    Args:
        dados (Dict[str, Aluno]): Um dicionário onde as chaves são IDs de alunos e os valores são objetos Aluno.

    Returns:
        Dict[str, Dict]: Um dicionário JSON onde as chaves são IDs de alunos e os valores são dicionários de dados dos alunos.
    """
    return {id_aluno: aluno.to_dict() for id_aluno, aluno in dados.items()}
