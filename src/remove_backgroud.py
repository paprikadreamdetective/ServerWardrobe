import os
from datetime import datetime
from rembg import remove

# Ahorita toma como parametro un directorio con imagenes como input
# y guarda las imagenes sin fondo en otro directorio de salida respaldando las originales
# Se necesitaria de cambiar la logicapara que reciva las imagenes de una peticion HTTP
# y las almacene en nuestra DB de prendas


class BackgroudRemover:
    def __init__(self, input_folder, output_folder) -> None:
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        today = datetime.now().strftime('%d/%m/%Y, %H: %M:')
        processed_folder = os.path.join(self.output_folder, today)
        os.makedirs(processed_folder, exist_ok=True)

        for filename in os.listdir(self.input_folder):
            if filename.endswith(('.png', 'jpg', 'jpeg')):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(processed_folder, filename)
                self._remove_backgroud(input_path, output_path)
                self._move_originals(input_path, processed_folder)

    def _remove_backgroud(self, input_p, output_p):
        with open(input_p, 'rb') as inp, open(output_p, 'wb') as outp:
            backgroud_output = remove(inp.read())
            outp.write(backgroud_output)

    def _move_originals(self, input_p, destination):
        originals_folder = os.path.join(destination, 'originals')
        os.makedirs(originals_folder, exist_ok=True)

        filename = os.path.basename(input_p)
        new_path = os.path.join(originals_folder, filename)
        os.rename(input_p, new_path)


if __name__ == '__main__':
    input_folder = "input"
    output_folder = "output"

    remover = BackgroudRemover(input_folder, output_folder)
    remover.process_images()
