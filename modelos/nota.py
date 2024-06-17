from typing import Dict, Any  # Importa os tipos Dict e Any do módulo typing para anotação de tipos

class Nota:
    DISCIPLINAS = ["Linguagem de Programação", "Engenharia de Software", "Algoritmos", "Estrutura de Dados"]
    # Lista de disciplinas para as quais as notas são registradas

    def __init__(self, notas: Dict[str, float] = None):
        """
        Inicializa um novo objeto Nota.

        Args:
            notas (Dict[str, float], opcional): Um dicionário de notas. As chaves são os nomes das disciplinas e os valores são as notas.
        """
        self.notas = {}  # Inicializa o dicionário de notas vazio
        if notas:
            for disciplina, nota in notas.items():
                if disciplina in self.DISCIPLINAS:
                    self.notas[disciplina] = round(nota, 1)  # Arredonda a nota para uma casa decimal

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto Nota em um dicionário.

        Returns:
            Dict[str, Any]: Um dicionário contendo as notas.
        """
        return self.notas

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Nota':
        """
        Cria um objeto Nota a partir de um dicionário.

        Args:
            data (Dict[str, Any]): Um dicionário contendo as notas.

        Returns:
            Nota: Um objeto Nota.
        """
        return Nota(notas=data)
