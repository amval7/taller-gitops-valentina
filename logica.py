def calcular_estadisticas_notas(notas):
    """
    Calcula estadísticas básicas sobre una lista de calificaciones numéricas.
    """
    # Caso 1: Lista vacía
    if not notas:
        return {
            "total": 0,
            "promedio": 0.0,
            "aprobados": 0,
            "reprobados": 0,
            "nota_maxima": 0.0,
            "nota_minima": 0.0
        }
    
    # Caso 2: Lista con notas
    total = len(notas)
    suma = sum(notas)
    promedio = round(suma / total, 2)
    aprobados = sum(1 for nota in notas if nota >= 3.0)
    reprobados = total - aprobados
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    return {
        "total": total,
        "promedio": promedio,
        "aprobados": aprobados,
        "reprobados": reprobados,
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima
    }
