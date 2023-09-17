from PIL import Image, ImageDraw , ImageFont

filename="img\IMG_20180630_015553.jpg"

class WaterMarker:
    def __init__(self) -> None:
        self.selected_image= None
        self.water_marked_image= None

    #open and load image
    def load_image(self, filename):
        try:
            with Image.open(filename) as img:
                img.load()
        except:
            print("unable to select image")
        self.selected_image= img
    

    def water_mark(self,text):
        if self.selected_image != None:
            #size of image
            w,h= self.selected_image.size

            #determine position to locate watermark
            x,y= (w-w//3), (h-h//5)

            #determine font size to use
            if x>y:
                font_size=y
            elif y>x:
                font_size= x
            else:
                font_size=x


            fnt= ImageFont.truetype(font='arial.ttf',size= font_size/12)
            #copy image
            img_copy= self.selected_image.copy()
            draw= ImageDraw.Draw(img_copy)

            #add watermark
            draw.text((x,y),text=f'{text} ©',fill=(255,255,255,128),font=fnt)
            self.water_marked_image= img_copy
            img_copy.show()

    def save_img(self, name):
        self.water_marked_image.save(f'{name}.jpg')

if __name__ == "__main__":
    filename="img\IMG_20180630_015553.jpg"
    marker= WaterMarker()
    marker.load_image(filename)
    marker.water_mark('masi madiba')
    marker.save_img('image1')