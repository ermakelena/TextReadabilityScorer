import re
from typing import Tuple


def count_words(text: str) -> int:
    """Подсчет количества слов."""
    words = text.split()
    return len(words)


def count_sentences(text: str) -> int:
    """Подсчет количества предложений."""
    sentences = re.findall(r'[.?!]+', text)
    return len(sentences)


def count_syllables(word: str) -> int:
    """Подсчет слогов в слове."""
    vowels = 'aeiouy'
    word = word.lower().strip(".,:;")
    if not word:
        return 0
    num_vowels = sum([1 for char in word if char in vowels])
    return max(num_vowels, 1)


def calculate_flesch_reading_ease(total_words: int, total_sentences: int, syllable_count: int) -> float:
    """Вычисление индекса Flesch Reading Ease."""
    return 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (syllable_count / total_words)


def calculate_flesch_kincaid_grade_level(total_words: int, total_sentences: int, syllable_count: int) -> float:
    """Вычисление уровня образования Flesch-Kincaid Grade Level."""
    return 0.39 * (total_words / total_sentences) + 11.8 * (syllable_count / total_words) - 15.59


def calculate_gunning_fog_index(total_words: int, complex_word_count: int, total_sentences: int) -> float:
    """Вычисление индекса Gunning Fog."""
    avg_sentence_length = total_words / total_sentences
    percent_complex_words = (complex_word_count / total_words) * 100
    return 0.4 * (avg_sentence_length + percent_complex_words)


def is_complex_word(word: str) -> bool:
    """Проверка является ли слово сложным (более двух слогов)."""
    return count_syllables(word) > 2


def extract_metrics(text: str) -> Tuple[int, int, int]:
    """
    Возвращает кортеж из общего числа слов, предложений и сложных слов.

    :param text: исходный текст
    :return: tuple of (words, sentences, complex_words)
    """
    words = count_words(text)
    sentences = count_sentences(text)
    complex_words = sum(is_complex_word(w) for w in text.split())
    return words, sentences, complex_words