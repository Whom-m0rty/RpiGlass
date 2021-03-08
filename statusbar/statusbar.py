from .time import get_time_string
from PIL import ImageFont


def show_status_bar(draw):
    font = ImageFont.truetype("arial.ttf", 9)
    time = get_time_string()
    draw.text((60, -2), time,  font=font, fill=255)