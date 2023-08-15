import PyPDF2
from easygui import fileopenbox, filesavebox

class PdfHandler:
    """ Classe para lidar com as operações dos arquivos pdf.
    """

    def __init__(self):
        """ Método construtor.
        """

        self.paths = []
        self.merger = PyPDF2.PdfMerger()

    def get_files(self) -> None:
        """ Exibe uma caixa de seleção para que o usuário selecione os 
        arquivos .pdf que serão mesclados.
        """

        self.paths = fileopenbox(
            title="Selecionar arquivos", 
            filetypes=["*.pdf"], 
            multiple=True
        )

    def merge_files(self) -> None:
        """ Realiza a mesclagem dos arquivos .pdf previamente selecionados.
        """

        if self.paths:
            for file in self.paths:
                if ".pdf" in file:
                    self.merger.append(f"{file}")
        else:
            print("Nenhuma pasta selecionada!")

    def select_destination_folder(self) -> None:
        """ Exibe uma caixa de seleção para que o usuário selecione o local de 
        salvamento e o nome do arquivo .pdf mesclado.
        """

        destination_file_path = filesavebox(
            title="Salvar Arquivo",
            default=".pdf", 
            filetypes=["*.pdf"]
        )

        self.merger.write(f"{destination_file_path}")