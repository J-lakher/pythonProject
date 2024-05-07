import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.youtube.com/channel/UCwN36lJrxe8RD7OZ-FsIDkw")
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="yellow")
img.save("jagriti_channel.png")

