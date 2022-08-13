from .model import Atividades


def editar_atividade(id):
    atividade = Atividades.query.filter_by(id=id).first()
    atividade.status = "concluído"
    atividade.save()
    return atividade
    