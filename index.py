import matplotlib.pyplot as plt
from collections import Counter

def analyze_text(text):
    cleaned_text = text.replace(" ", "").lower()
    alphabet_set = set(cleaned_text)
    
    # Підраховуємо частоти кожного символу
    char_count = Counter(cleaned_text)
    
    # Фільтруємо символи за частотою >= 10
    filtered_chars = [(char, count) for char, count in char_count.items() if count >= 10]

    print("Використаний алфавіт (в алфавітному порядку):")
    print(sorted(alphabet_set))
    
    print("\nЧастоти повторень символів:")
    sorted_by_frequency = sorted(filtered_chars, key=lambda x: x[1], reverse=True)
    for char, freq in sorted_by_frequency:
        print(f"{char}: {freq}")
    
    # Побудова гістограм за частотами символів по спаданню
    plot_histogram(sorted_by_frequency, "Частота символів за спаданням")

    # Підрахунок біграм та їх виведення
    bigrams = [cleaned_text[i:i+2] for i in range(len(cleaned_text)-1)]
    bigram_count = Counter(bigrams)
    filtered_bigrams = [(bigram, count) for bigram, count in bigram_count.items() if count >= 10]
    sorted_bigrams_by_frequency = sorted(filtered_bigrams, key=lambda x: x[1], reverse=True)
    print("\nЧастоти біграм:")
    for bigram, freq in sorted_bigrams_by_frequency:
        print(f"{bigram}: {freq}")
    plot_histogram(sorted_bigrams_by_frequency, "Частота біграм")

    # Підрахунок тріґрам та їх виведення
    trigrams = [cleaned_text[i:i+3] for i in range(len(cleaned_text)-2)]
    trigram_count = Counter(trigrams)
    filtered_trigrams = [(trigram, count) for trigram, count in trigram_count.items() if count >= 10]
    sorted_trigrams_by_frequency = sorted(filtered_trigrams, key=lambda x: x[1], reverse=True)
    print("\nЧастоти тріґрам:")
    for trigram, freq in sorted_trigrams_by_frequency:
        print(f"{trigram}: {freq}")
    plot_histogram(sorted_trigrams_by_frequency, "Частота тріґрам")

    # Підрахунок чотириграм та їх виведення
    fourgrams = [cleaned_text[i:i+4] for i in range(len(cleaned_text)-3)]
    fourgram_count = Counter(fourgrams)
    filtered_fourgrams = [(fourgram, count) for fourgram, count in fourgram_count.items() if count >= 10]
    sorted_fourgrams_by_frequency = sorted(filtered_fourgrams, key=lambda x: x[1], reverse=True)
    print("\nЧастоти чотириграм:")
    for fourgram, freq in sorted_fourgrams_by_frequency:
        print(f"{fourgram}: {freq}")
    plot_histogram(sorted_fourgrams_by_frequency, "Частота чотириграм")

# Функція для побудови гісграм
def plot_histogram(data, title):
    if len(data) == 0:
        print(f"Немає даних для побудови гістограми для {title}")
        return
    plt.figure(figsize=(10, 5))
    labels, values = zip(*data)
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel("Символи/Пари/Трійки/Чотириграми")
    plt.ylabel("Частота")
    plt.xticks(rotation=90)
    plt.show()

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху до файлу.")
        return ""

def main():
    file_path = "text.txt" 
    text = read_text_from_file(file_path)
    if text:
        analyze_text(text)

if __name__ == "__main__":
    main()
