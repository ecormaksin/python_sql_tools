class FileWriter:
    @classmethod
    def append(cls, file_path_str: str, content: str):
        with open(file_path_str, "a", encoding="utf-8") as file_obj:
            file_obj.write(content + "\n")

    @classmethod
    def tee_append(cls, file_path_str: str, content: str):
        print(content)
        cls.append(file_path_str=file_path_str, content=content)
