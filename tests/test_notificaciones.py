def generar_notificaciones(eventos):
    eventos_procesados = set()
    notificaciones = []

    for evento in eventos:
        if evento["id"] not in eventos_procesados:
            eventos_procesados.add(evento["id"])
            notificaciones.append(evento)

    return notificaciones


def test_no_generar_notificaciones_duplicadas():
    eventos = [
        {"id": "like-001", "tipo": "like"},
        {"id": "like-001", "tipo": "like"},
        {"id": "like-001", "tipo": "like"}
    ]

    resultado = generar_notificaciones(eventos)

    assert len(resultado) == 1
