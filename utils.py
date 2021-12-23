def get_valid_input(input_instruction, input_options):
    input_instruction += f' {input_options} :'
    input_ = input(input_instruction)
    while input_.lower() not in input_options:
        input_ = input(input_instruction)
    return input_

