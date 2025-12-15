from typing import Dict
from analyzer import TextAnalyzer


def generate_report(analysis_results: Dict[str, float]) -> None:
    """
    Генерирует отчёт по проведённому анализу текста.

    :param analysis_results: словарь с результатом анализа
    """
    print("\n*** Отчет о читаемости текста ***\n")
    print(f"Flesch Reading Ease: {analysis_results['flesch_reading_ease']:.2f}")
    print(f"Flesch-Kincaid Grade Level: {analysis_results['flesch_kincaid_grade_level']:.2f}")
    print(f"Gunning Fog Index: {analysis_results['gunning_fog_index']:.2f}\n")