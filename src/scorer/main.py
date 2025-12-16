from analyzer import TextAnalyzer
from document_reader import DocumentReader
from report import generate_report, select_metrics, show_metric_selection_menu
from simplifier import suggest_improvements
import os

# Определяем базовую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# BASE_DIR теперь = text_scorer
TEXTS_DIR = os.path.join(BASE_DIR, "texts")


def main():
    print("Анализатор читаемости текста")
    print("=" * 50)

    while True:
        print("\n" + "=" * 50)
        print("Главное меню:")
        print("1. Анализировать текст")
        print("2. Выйти")
        print("=" * 50)

        main_choice = input("Ваш выбор (1-2): ").strip()

        if main_choice == "2":
            print("Выход из программы.")
            break
        elif main_choice != "1":
            print("Неверный выбор.")
            continue

        # Выбор файла для анализа
        print("\nВыберите текст для анализа:")
        print("1. Легкий (easy.txt)")
        print("2. Средний (medium.txt)")
        print("3. Сложный (hard.txt)")
        print("4. Свой файл")

        file_choice = input("Ваш выбор (1-4): ").strip()

        if file_choice == "1":
            file_path = os.path.join(TEXTS_DIR, "easy.txt")
        elif file_choice == "2":
            file_path = os.path.join(TEXTS_DIR, "medium.txt")
        elif file_choice == "3":
            file_path = os.path.join(TEXTS_DIR, "hard.txt")
        elif file_choice == "4":
            file_path = input("Введите полный путь к файлу: ").strip()
            if not os.path.isabs(file_path):
                file_path = os.path.abspath(file_path)
        else:
            print("Неверный выбор.")
            continue

        # Проверка существования файла
        if not os.path.exists(file_path):
            print(f"Ошибка: файл '{file_path}' не найден!")
            continue

        try:
            # Анализ текста
            print(f"\nЗагружаю файл: {os.path.basename(file_path)}")
            reader = DocumentReader(file_path)
            analyzer = TextAnalyzer(reader)
            results = analyzer.analyze()

            # Выбор формата отчета
            print("\nФормат отчета:")
            print("1. Текстовый вывод")
            print("2. JSON файл")
            print("3. Оба формата")

            format_choice = input("Выберите формат (1-3): ").strip()
            format_map = {"1": "text", "2": "json", "3": "both"}
            output_format = format_map.get(format_choice, "text")

            # Цикл выбора метрик
            while True:
                print(f"\nАнализ файла: {os.path.basename(file_path)}")
                metric_choice = show_metric_selection_menu()

                if metric_choice == "exit":
                    print("Возврат в главное меню.")
                    break

                # Выбор метрик с использованием select_metrics
                selected_metrics = select_metrics(results, metric_choice)

                # Генерация отчета
                if metric_choice == "average":
                    print("\n" + "=" * 50)
                    print("Средний показатель читаемости:")
                    print("=" * 50)
                    avg_score = selected_metrics['average_readability']
                    print(f"Средняя читаемость: {avg_score:.2f}/100")

                    # Интерпретация среднего показателя
                    if avg_score >= 70:
                        print("Интерпретация: Текст легко читается")
                    elif avg_score >= 40:
                        print("Интерпретация: Средняя сложность")
                    else:
                        print("Интерпретация: Текст сложен для чтения")
                    print("=" * 50)
                else:
                    # Используем generate_report для выбранных метрик
                    print(generate_report(selected_metrics, output_format))

                # Показываем рекомендации только для полного отчета
                if metric_choice == "all":
                    suggest_improvements(results)

                # Предлагаем выбрать другие метрики
                again = input("\nВыбрать другие метрики для этого файла? (да/нет): ").strip().lower()
                if again not in ["да", "yes", "y", "д"]:
                    break

        except FileNotFoundError:
            print(f"Ошибка: файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Ошибка при анализе: {type(e).__name__}: {e}")


if __name__ == "__main__":
    # Проверка структуры проекта
    if not os.path.exists(TEXTS_DIR):
        print(f"Внимание: папка с текстами не найдена: {TEXTS_DIR}")
        print("Создайте папку 'texts' в корне проекта и добавьте файлы:")
        print("- easy.txt, medium.txt, hard.txt")

    main()