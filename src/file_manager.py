class FileManager:
    @staticmethod
    def save_output(input_text: str, start_position: int, end_position: int):
        with open('../text_files/output.txt', 'w', encoding='utf8') as arq_output:
            arq_output.write(''.join(filter(lambda lista: lista[0] != '\n', input_text[start_position:end_position])))

    @staticmethod
    def get_input_text():
        with open('../text_files/input.txt', encoding='utf8') as arq_input:
            return arq_input.readlines()
