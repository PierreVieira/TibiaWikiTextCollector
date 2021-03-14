def only_not_n(lista):
    return lista[0] != '\n'


class FileManager:
    @staticmethod
    def get_input_text():
        with open('../text_files/input.txt', encoding='utf8') as arq_input:
            return list(filter(only_not_n, arq_input.readlines()))

    @staticmethod
    def save_output(input_text: str, start_position: int, end_position: int):
        with open('../text_files/output.txt', 'a', encoding='utf8') as arq_output:
            string_escrita = ''.join(input_text[start_position:end_position]) + '\n'
            arq_output.write(string_escrita)
