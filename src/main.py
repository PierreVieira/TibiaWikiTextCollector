from file_manager import FileManager


def find_relationaties_articles(input_text):
    key = 'Artigos relacionados:'
    for line in input_text:
        if key in line:
            return line.replace('\n', '')
    raise ValueError(f'Não existe a chave {key} no texto informado')


def find_word(input_text: str, list_words: list):
    for line in input_text:
        for word in list_words:
            if word + '\n' == line:
                return word
    raise ValueError(f'Valor de palavra não encontrado para {list_words}')


if __name__ == '__main__':
    input_text = FileManager.get_input_text()
    start_words, end_words = ['Original:', 'Texto Original:'], ['Tradução:', 'Tradução']
    try:
        start_word = find_word(input_text, start_words)
    except ValueError:
        start_word = find_relationaties_articles(input_text)
    end_word = find_word(input_text, end_words)
    start_position, end_position = input_text.index(f'{start_word}\n') + 1, input_text.index(f'{end_word}\n')
    FileManager.save_output(input_text, start_position, end_position)
