import os
import shutil
from collections import defaultdict

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.file_types = defaultdict(list)

    def classify_files(self):
        """Classifica e organiza arquivos por extensão."""
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                file_extension = filename.split('.')[-1].lower()
                self.file_types[file_extension].append(filename)
        
        self.create_folders_and_move()

    def create_folders_and_move(self):
        """Cria pastas com base nas extensões e move os arquivos para as pastas apropriadas."""
        for file_extension, files in self.file_types.items():
            folder_path = os.path.join(self.directory, file_extension)
            os.makedirs(folder_path, exist_ok=True)

            for file in files:
                source = os.path.join(self.directory, file)
                destination = os.path.join(folder_path, file)
                shutil.move(source, destination)
                print(f'Movendo {file} para {folder_path}')

    def remove_duplicates(self):
        """Remove arquivos duplicados conforme nome."""
        seen_files = set()
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                if filename in seen_files:
                    os.remove(file_path)
                    print(f'Removido: {filename}')
                else:
                    seen_files.add(filename)

    def generate_report(self):
        """Gera um relatório da organização realizada."""
        print("Organização concluída!")
        print(f"Arquivos organizados em: {len(self.file_types)} pastas.")


def main():
    directory = input("Digite o caminho do diretório que deseja organizar: ")
    organizer = FileOrganizer(directory)

    print("Classificando arquivos...")
    organizer.classify_files()

    print("Removendo arquivos duplicados...")
    organizer.remove_duplicates()

    organizer.generate_report()


if __name__ == "__main__":
    main()
