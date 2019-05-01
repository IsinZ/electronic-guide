class Exhibit:
    def __init__(self, ex_id, name, century, image_path, info_path):
        self.ex_id = ex_id
        self.name = name
        self.century = century
        self.image_path = image_path
        self.info_path = info_path
        
    def _print(self):
        print(self.ex_id)
        print(self.name)
        print(self.century)
        print(self.image_path)
        print(self.info_path)
        