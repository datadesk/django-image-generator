import os
from image.models import State
from django.conf import settings
from django.template.loader import get_template, Context
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Saves out an image"
    
    def handle(self, *args, **kwds):
        # Set the output paths
        target = settings.MAP_IMAGE_DIR
        os.path.exists(target) or os.makedirs(target)
        svg_file = os.path.join(target, 'us_states.svg')
        # Render the SVG
        template = get_template('us_states.svg.html')
        svg_string = template.render(Context({
            'objects': State.objects.all()
        }))
        # Write the SVG to system
        outfile = open(svg_file, "w")
        outfile.write(svg_string)
        outfile.close()
        # Convert the SVG to PNG
        cmd = 'java -jar %s -m image/png -bg 255.255.255.255 %s' % (
            settings.BATIK_PATH,
            svg_file
        )
        os.popen(cmd)