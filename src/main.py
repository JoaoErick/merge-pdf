from models import PdfHandler

def main():
    try:
        pdf_handler = PdfHandler()
        pdf_handler.get_files()
        pdf_handler.merge_files()
        pdf_handler.select_destination_folder()

        print("\nOs arquivos selecionados foram mesclados com sucesso!\n")
    except Exception:
        print("\nOps! Aconteceu algum problema durante a mesclagem.\n")

if __name__ == "__main__":
    main()
