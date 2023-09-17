from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from marking import WaterMarker

marker= WaterMarker()


image_name= None

def select_file():
    global image_name
    file_types= (('All files', '*.*'),)
    file_name= filedialog.askopenfilename(
        title="Select image",
        initialdir='.',
        filetypes=file_types,

    )
    image_name= file_name
    if file_name !=None:
        showinfo(
            title="Selected file",
            message=file_name

        )

def water_mark():
    marker.load_image(image_name)
    text_input= water_mark_text.get()
    text_entry.delete(0,END)
    marker.water_mark(text_input)

def save_image():
    n=1
    marker.save_img(f'image_{n}')
    n+=1
# ----------------------------------------GUI-----------------------------------------------------------
root= Tk()
root.title('Watermark Maker')
root.minsize(width=400, height=200)
main_frame= ttk.Frame(root,padding="3 3 12 12")
main_frame.grid(column=0,row=0,sticky=(N,E,S,W))




btn_select= ttk.Button(main_frame,text="Select picture", command=select_file , width=80)
btn_select.grid(column=0, row=1, columnspan=2)

water_mark_label= ttk.Label(main_frame,text='Enter watermark text:', width=40)
water_mark_label.grid(column=0, row=2)

water_mark_text= StringVar()
text_entry= ttk.Entry(main_frame, width=40 , textvariable=water_mark_text)
text_entry.grid(column=1, row=2,columnspan=2)

generate_btn= ttk.Button(main_frame, text="watermark image",width=40, command=water_mark)
generate_btn.grid(column=1,row=3)


btn_save= ttk.Button(main_frame, text="Save Image", width=40, command=save_image)
btn_save.grid(column=1, row=4)







root.mainloop()
