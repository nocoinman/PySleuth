from pathlib import Path
import os

from ..base import singleton
from ..configuration import ConfigHandler

@singleton
class Data:
    def __init__(self):
        subDirs = set()
        subDirs.add(self.getRootDir() / "mouse" / "shots")
        subDirs.add(self.getRootDir() / "screen")

        for subDir in subDirs:
            if os.path.exists(subDir):
                continue
            os.makedirs(subDir)

    def getRootDir(self):
        root = ConfigHandler().getSettingsGeneral().save_data_to
        return Path(os.path.join(root, "data"))

    def newLogFile(self, name: str):
        return self.getRootDir() / name
