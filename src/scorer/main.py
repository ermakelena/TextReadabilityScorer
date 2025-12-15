from analyzer import TextAnalyzer
from document_reader import DocumentReader
from report import generate_report
from simplifier import suggest_improvements

if __name__ == "__main__":
    # Пример запуска анализа текста из файла example.txt
    reader = DocumentReader('example.txt')
    analyzer = TextAnalyzer(reader)
    results = analyzer.analyze()

    # Печать результатов анализа
    generate_report(results)

    # Рекомендации по улучшению
    suggest_improvements(results)