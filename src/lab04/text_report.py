import argparse
import sys
from pathlib import Path

from io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

def create_report(input_path: str, output_path: str, encoding: str = "utf-8") -> None:

    try:
        text = read_text(input_path, encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден.")
        return
    except UnicodeDecodeError as e:
        print(f"Ошибка: укажите другую кодировку.")
        return

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    top5 = top_n(freq, 5)

    sorted_data = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    header = ("word", "count")

    write_csv(sorted_data, output_path, header)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="Отчёт о частоте слов из текстового файла.")
    parser.add_argument("--in", dest="input_file", help="Путь к входному текстовому файлу.", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output_file", help="Путь к выходному CSV файлу.", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8", )
    args = parser.parse_args()
    create_report(args.input_file, args.output_file, args.encoding)

if __name__ == "__main__":
    main()