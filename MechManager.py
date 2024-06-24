import const
from Box import BoxInterface
from GameField import FieldInterface
import matplotlib.pyplot as plt
from const import *


class MechanicManager:
    def __init__(self, screen, load_method):
        self.bgen = BoxInterface.Interface(screen)
        self.fgen = FieldInterface.Interface(self.bgen)
        self.load_method = load_method
        self.objects = load_method.objects
        self.objects_statuses = {}
        self.objects_coordination = {}
        self.objects_see = {}
        self.objects_size = (100, 100)

    def claim_info(self):
        for obj in self.objects.values():
            see, status, self.objects_coordination[obj] = obj.access_info()
            self.objects_see[obj] = STATUS_SEE[see[-1]]
            self.objects_statuses[obj] = STATUS_INTERPRETATION[status]

    def calculation(self, cal=False):
        for obj in self.objects.values():
            status = self.objects_statuses[obj]
            coordination = self.objects_coordination[obj]
            move = self.objects_see[obj]

            self.bgen.create_boxes(status, coordination, move)
            self.bgen.set_boxes(status)
            self.bgen.load_boxes()

            self.fgen.get_cor_info()
            self.fgen.chb()
            const.SCREEN_COUNT += 1

            if cal and const.SCREEN_COUNT%24 == 0:
                const.SCREEN_COUNT = 0
                DPI = 72
                points = [point for point in self.fgen.get_boxes() if type(point) is not int]
                fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
                ax = plt.subplot()
                self.fgen.draw(ax)

                ax.scatter([p.x for p in points], [p.y for p in points], s=4)
                ax.set_xticks([])
                ax.set_yticks([])

                reg = self.fgen.see_region(coordination[0] - 12, coordination[1] - 50, 20, 100)
                self.fgen.in_dots(reg)
                found_points = self.fgen.found_points()
                ax.scatter([p.x for p in found_points], [p.y for p in found_points],
                           facecolors='none', edgecolors='r', s=32)
                reg.draw(ax, c='r')
                ax.invert_yaxis()
                plt.tight_layout()
                plt.savefig('logs\search-quadtree.png')

            self.bgen.uptime_freshening()
            self.fgen.dhb()





