from modelos.aluno import Aluno  # Importa a classe Aluno do módulo modelos.aluno
from modelos.nota import Nota  # Importa a classe Nota do módulo modelos.nota


def validar_aluno(aluno: Aluno) -> None:
    """
    Valida os dados de um objeto Aluno.

    Args:
        aluno (Aluno): O objeto Aluno a ser validado.

    Raises:
        ValueError: Se alguma das validações falhar.
    """
    if not isinstance(aluno.nome, str) or not aluno.nome:
        raise ValueError("Nome do aluno deve ser uma string não vazia.")

    notas = aluno.notas.to_dict()

    for disciplina in Nota.DISCIPLINAS:
        if disciplina not in notas:
            raise ValueError(f"Disciplina '{disciplina}' está faltando nas notas do aluno.")
        if not isinstance(notas[disciplina], (int, float)) or not (0 <= notas[disciplina] <= 10):
            raise ValueError(f"Nota para '{disciplina}' deve ser um número entre 0 e 10.")
