from .time import get_time_string
from PIL import ImageFont


def show_status_bar(draw):
    font = ImageFont.truetype("arial.ttf", 7)
    time = get_time_string()
    draw.text((0, -2), time,  font=font, fill=255)