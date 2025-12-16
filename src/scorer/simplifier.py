from typing import Dict
import json
from datetime import datetime


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

        # Сохранение рекомендаций в JSON
        save_recommendations(results, improvements)
    else:
        print("\nВаш текст достаточно прост для восприятия!")


def save_recommendations(results: Dict[str, float], improvements: list) -> None:
    """
    Сохраняет рекомендации в JSON файл.

    :param results: результаты анализа
    :param improvements: список рекомендаций
    """
    recommendations_data = {
        "timestamp": datetime.now().isoformat(),
        "original_metrics": results,
        "improvements": improvements,
        "min_readability_score": 60.0
    }

    filename = f"improvements_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recommendations_data, f, ensure_ascii=False, indent=2)

    print(f"\nРекомендации сохранены в файл: {filename}")