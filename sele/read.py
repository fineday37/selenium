import yaml
# import os


class Readyaml:
    def __init__(self, yaml_name):
        self.yaml_name = yaml_name

    def read_yaml(self):
        with open(self.yaml_name, 'r', encoding="utf-8") as f:
            msxy_page = yaml.load(stream=f.read(), Loader=yaml.Loader)
        return msxy_page


if __name__ == '__main__':
    print(Readyaml('../sele/api.yaml').read_yaml()[0]["name"]["xing"])
# fs = open(os.getcwd() + "./api.yaml", encoding="UTF-8")
# datas = yaml.load(fs)
# print(datas)
