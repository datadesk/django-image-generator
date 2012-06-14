import os
import csv
import statestyle
from image import us_states
from image.models import State
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Loads some data"
    
    def handle(self, *args, **kwds):
        csv_file = open('image/unemployment.csv', 'rU')
        data = list(csv.reader(csv_file))
        csv_file.close()
        for i in data[1:]:
            state = statestyle.get(i[0])
            print 'Loading: %s' % state.name
            State.objects.create(
                name=state.name,
                postal=state.postal,
                unemployment_rate=float(i[1]) / 100,
                svg_path=us_states.paths.get(state.postal),
                color=self.get_color(float(i[1]) / 100),
            )
        print 'Finished'

    def get_color(self, value):
        """
        Takes a value, assigns a breakpoint and gives it a color
        """
        breaks = [0, 0.04, 0.06, 0.08, 0.10, 0.12, 0.15]
        colors = ['#F9EFDD', '#FBEAA5','#FCDC51','#F7B935','#F18A26','#D16228']
        for i in range(len(breaks) - 1):
            if value >= breaks[i] and value < breaks[i+1]:
                break_cat = i
        return colors[break_cat]