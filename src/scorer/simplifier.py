from typing import Dict
from analyzer import TextAnalyzer


def suggest_improvements(results: Dict[str, float], min_readability_score: float = 60.0) -> None:
    """
    Формирует список конкретных рекомендаций по улучшению читаемости текста.

    :param results: словарь с результатами анализа
    :param min_readability_score: минимальный порог удобства чтения
    """
    improvements = []

    if results["flesch_reading_ease"] < min_readability_score:
        improvements.append("Используйте более короткие предложения.")
        improvements.append("Избегайте сложных конструкций и длинных слов.")

    if results["flesch_kincaid_grade_level"] >= 12:
        improvements.append("Сделайте текст понятнее для широкой аудитории.")

    if results["gunning_fog_index"] > 12:
        improvements.append("Попробуйте упростить сложные слова и выражения.")

    if improvements:
        print("\nРекомендации по улучшению:")
        for i, suggestion in enumerate(improvements, start=1):
            print(f"{i}. {suggestion}")
    else:
        print("\nВаш текст достаточно прост для восприятия!")