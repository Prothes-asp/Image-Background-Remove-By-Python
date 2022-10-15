from rembg import remove
from PIL import Image
from tkinter.filedialog import*

Input_Image = askopenfilename()
Open_Image = Image.open(Input_Image)
Output = "bg-remove.png"
Bg_remove = remove(Open_Image)
Bg_remove.save(Output)
print("Successfully ! Remove Background")
