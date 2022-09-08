import os,sys, subprocess
import PySimpleGUI as sg

##Ref
sg.theme('material2')

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
import fitz

# read pdf file


list_ = os.listdir()
#sg.popup(list_)
str_x=sg.popup_get_text("Enter DPI of conversion? \nHigher DPI produces clearer picture, longer process time and bigger file size.", title="PDF2PNG", default_text="220",image=resource_path("info.png"),
                     grab_anywhere=True)
if str_x== None: sys.exit(0)
if str_x=="": sys.exit(0)
try:
    x1= int(str_x)
except ValueError:
    sg.popup("Please input a Integer number like 200, 150, 320 for dpi, \nHigher DPI produces clearer picture and bigger file size.")
    sys.exit(0)
#finally: pass

#dpi=x1
for file_ in list_:
              name, ext = os.path.splitext(file_)
              # This is going to store the extension type
              #Jumping the ". " character
               # This forces the next iteration,
              # if it is the directory has no extsnsions
              if ext == '':continue
              ext = ext[1:]
              if ext=="pdf" or ext=="PDF":
                  pdf = fitz.open(file_)
                  for page in range(0, len(pdf)):
                      # load pages with index
                      pages = pdf.load_page(page)
                      # take image of page
                      img= pages.get_pixmap(dpi=x1)
                      # save image
                      img.save(f'{file_}_image{page+1}.png')
                      #sys.exit(0)

sg.popup(f"Sucess converted all PDFs into PNG done at DPI {x1}")
sys.exit()
#====================================================================================================
#====================================================================================================
#====================================================================================================






















                  #sg.popup(file_)
# iterate through pdf pages



#sg.popup_get_date()
#The default format is equivalent to "%Y:%m:%d %H:%M:%S". This option has no effect on date-only or time-only tags and ignores timezone information if present. 

#The default output is 
#2012:07:29 dddd/dd/dd
#11:09:56. tt:tt:tt"

#The standard EXIF date/time format is "YYYY:mm:dd HH:MM:SS",

#Erase all data
#exiftool -all= −overwrite_original

#exiftool '-FileName<DateTimeOriginal' -d "%Y-%m-%d %H.%M.%S%%-c.%%e" .  

#exiftool "-DateTimeOriginal=2020:04:04 09:04:02" −overwrite_original *.jpg

# creating a variable and storing the text 
# that we want to search 

