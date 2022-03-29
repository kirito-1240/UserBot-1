from PIL import Image, ImageDraw, ImageFont

class LogoMaker:
    @staticmethod
    def get_text_size(text, image, font):
        im = Image.new("RGB", (image.width, image.height))
        draw = ImageDraw.Draw(im)
        return draw.textsize(text, font)

    @staticmethod
    def find_font_size(text, font, image, target_width_ratio):
        tested_font_size = 100
        tested_font = ImageFont.truetype(font, tested_font_size)
        observed_width, observed_height = LogoMaker.get_text_size(text, image, tested_font)
        estimated_font_size = (tested_font_size / (observed_width / image.width) * target_width_ratio)
        return round(estimated_font_size)

    @staticmethod
    def make_logo(imgpath, text, font, file_name, **args):
        fill = args.get("fill")
        width_ratio = args.get("width_ratio") or 0.7
        stroke_width = int(args.get("stroke_width"))
        stroke_fill = args.get("stroke_fill")
        img = Image.open(imgpath)
        width, height = img.size
        draw = ImageDraw.Draw(img)
        font_size = LogoMaker.find_font_size(text, font, img, width_ratio)
        font = ImageFont.truetype(font, font_size)
        w, h = draw.textsize(text, font=font)
        draw.text(
            ((width - w) / 2, (height - h) / 2),
            text,
            font=font,
            fill=fill,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        img.save(file_name, "PNG")
