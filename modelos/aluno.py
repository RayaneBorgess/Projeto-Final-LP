import uuid  # Importa o módulo uuid para gerar IDs únicos para cada aluno
from typing import Dict, Any  # Importa os tipos Dict e Any do módulo typing para anotação de tipos

from modelos.nota import Nota  # Importa a classe Nota do módulo modelos.nota


class Aluno:
    def __init__(self, nome: str, id: str = None, notas: Dict[str, float] = None):
        """
        Inicializa um novo objeto Aluno.

        Args:
            nome (str): O nome do aluno.
            id (str, opcional): O ID do aluno. Se não for fornecido, um novo UUID será gerado.
            notas (Dict[str, float], opcional): Um dicionário de notas. Se não for fornecido, um objeto Nota vazio será criado.
        """
        self.id = id or str(uuid.uuid4())  # Gera um novo UUID se nenhum ID for fornecido
        self.nome = nome
        self.notas = Nota(
            notas) if notas is not None else Nota()  # Cria um objeto Nota com as notas fornecidas ou um vazio

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto Aluno em um dicionário.

        Returns:
            Dict[str, Any]: Um dicionário contendo os dados do aluno.
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "notas": self.notas.to_dict()
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Aluno':
        """
        Cria um objeto Aluno a partir de um dicionário.

        Args:
            data (Dict[str, Any]): Um dicionário contendo os dados do aluno.

        Returns:
            Aluno: Um objeto Aluno.
        """
        notas = data.get("notas", {})
        return Aluno(id=data.get("id"), nome=data["nome"], notas=notas)
