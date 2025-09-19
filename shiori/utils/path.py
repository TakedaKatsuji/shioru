from pathlib import Path

class ProjectPath:
    def __init__(self, root_dir=None, save_dst=""):
        self.root_dir = Path().home().joinpath("project/shioru") if root_dir is None else root_dir
        self.save_root_dir = self.root_dir.joinpath("src/.vuepress/public/assets/images")
        self.save_dir = self.save_root_dir.joinpath(save_dst)