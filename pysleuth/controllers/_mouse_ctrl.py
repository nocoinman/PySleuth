from datetime import datetime

from ..core.components import MouseMonitor, saveScreenShot
from ..core.data import Data
from .base import BaseController
from ..configuration import ConfigHandler


class MouseMntrController(BaseController):
    def __init__(self):
        super(MouseMntrController, self).__init__()

        self.worker = MouseMonitor()
        self.worker.initLogger("mouse/clicks")

        self.connectSlots()

    def startWorker(self):
        self.worker.start()

    def connectSlots(self):
        self.worker.SIG_clicked.connect(self, "onMouseClick")

    def onMouseClick(self, x: int, y: int, button: str, pressed: bool):
        msg = f"{'Pressed' if pressed else 'Released'} {button} at ({x}, {y})"
        self.worker.log(msg)

        cfg = ConfigHandler().getComponentSettings("Mouse_Monitor")

        if cfg.capture_screen_on_activity:
            self.grabScreen()

    def grabScreen(self):
        dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
        filePath = Data().getRootDir() / "mouse" / "shots" / f"{dt_string}.jpg"
        saveScreenShot(filePath)
