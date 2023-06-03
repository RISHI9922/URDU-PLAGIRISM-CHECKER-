import nltk
from mtranslate import translate
from nltk.tokenize import word_tokenize

def translate_to_english(text):
    translation = translate(text, 'en', 'ur')
    return translation

def calculate_similarity(text1, text2):
    tokens1 = word_tokenize(text1)
    tokens2 = word_tokenize(text2)

    intersection = set(tokens1) & set(tokens2)
    union = set(tokens1) | set(tokens2)
    similarity = len(intersection) / len(union)

    return similarity

def find_dissimilar_words(text1, text2):
    words1 = set(word_tokenize(text1))
    words2 = set(word_tokenize(text2))

    dissimilar_words = words1.symmetric_difference(words2)

    return dissimilar_words

def main():
    nltk.download('punkt')

    urdu_text1 = "تم سب پہلے بیشک اپنی کوششیں کیوں نہیں کرتے؟"
    urdu_text2 = "تم کیوں اپنی کوششیں نہیں کرتے؟"

    english_text1 = translate_to_english(urdu_text1)
    english_text2 = translate_to_english(urdu_text2)

    similarity_score = calculate_similarity(english_text1, english_text2)
    dissimilar_words = find_dissimilar_words(urdu_text1, urdu_text2)

    print(f"Similarity score: {similarity_score * 100:.2f}%")
    print("Dissimilar words:")
    for word in dissimilar_words:
        print(word)

if __name__ == "__main__":
    main()
