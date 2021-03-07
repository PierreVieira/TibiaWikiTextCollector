class FileManager:
    @staticmethod
    def get_input_text():
        with open('../text_files/input.txt', encoding='utf8') as arq_input:
            return arq_input.readlines()

    @staticmethod
    def save_output(input_text: str, start_position: int, end_position: int):
        remove_lines_unique_n = lambda lista: lista[0] != '\n'
        with open('../text_files/output.txt', 'a', encoding='utf8') as arq_output:
            string_escrita = ''.join(filter(remove_lines_unique_n, input_text[start_position:end_position])) + '\n'
            arq_output.write(string_escrita)
