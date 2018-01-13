class DataRunner:
    def __init__(self,data_filename):
        with open(data_filename, "r") as data_file:
            self.data_lines = data_file.readlines()

        self.parameters = []
        for line in self.data_lines:
            parameter_list = line.split(' | ')
            self.parameters.append((parameter_list[0], parameter_list[1], parameter_list[2]))
    def run(self, out_filename, encryption_function, decryption_function):
        outputs = []

        for parameter in self.parameters:
            TYPE, key, text = parameter
            if TYPE == ENCRYPT:
                outputs.append(encryption_function(text, key))
            else:
                outputs.append(decryption_function(text, key))

        with open(out_filename, 'w') as out_file:
            for output in outputs:
                if output != '':
                    if output[len(output)-1] != '\n':
                        output += '\n'
                    out_file.write(output)

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"