from file_manager import FileManager

input_text = FileManager.get_input_text()
start_word, end_word = 'Original:', 'Tradução:'
start_position, end_position = input_text.index(f'{start_word}\n') + 1, input_text.index(f'{end_word}\n')
FileManager.save_output(input_text, start_position, end_position)
