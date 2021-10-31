from tkinter import *
import pytube
from tkinter import filedialog
from tkinter.ttk import *
import tkinter
from pytube.__main__ import YouTube
import pafy


window=Tk()
window.geometry('800x700')
window.title('Youtube video/audio downloader')
window.config(bg='black')

direct=''
def open_path():
    download_name.config(text='')
    download_size.config(text='')
    download_loc.config(text='')
    global direct
    direct=filedialog.askdirectory()
    path_holder.config(text=direct)

def download():
    url=link_ent.get()
    Selected=types.get()

    if len(url)<1:
        link_error.config(text='Please insert URL')
    if len(direct)<1:
        path_error.config(text='Please select path')
    else:
        link_error.config(text='')
        path_error.config(text='')
        try:
            Yt=YouTube(url)
            try:
                if(Selected==options[0]):
                    typ=Yt.streams.get_highest_resolution()
                elif(Selected==options[1]):
                    typ=Yt.streams.filter(progressive=True,file_extension='mp4').first()
                elif(Selected==options[2]):
                    typ=pafy.new(url).audiostreams
                try:
                    if(Selected==options[2]):
                        typ[2].download(direct)
                        link_ent.delete(0,'end')
                        path_holder.config(text='\t\t\t       ')
                        download_out.config(text="Downloaded successfully",foreground='green')

                        name=typ[2].title
                        size=typ[2].get_filesize()/1024/1024
                        size=round(size,1)
                        download_name.config(text="Name:"+name)
                        download_size.config(text="Size:"+str(size)+"Mb")
                        download_loc.config(text="Path:"+direct) 
                        
                    else:
                        typ.download(direct) 
                        link_ent.delete(0,'end')
                        path_holder.config(text='\t\t\t       ')
                        download_out.config(text="Downloaded successfully",foreground='green')

                        name=typ.title
                        size=typ.filesize/1024000
                        size=round(size,1)
                        download_name.config(text="Name:"+name)
                        download_size.config(text="Size:"+str(size)+"Mb")
                        download_loc.config(text="Path:"+direct) 
                except:
                    download_out.config(text='Download failed',foreground='red')
            except:
                download_out.config(text='Having Error',foreground='red')
        except:
            path_error.config(text='Insert valid path')

heading=Label(window,text='Youtube video/audio downloader',foreground='white',background='black',font=('monotype corsiva',30,'bold','italic'))
heading.pack(anchor="center",pady=20)

link=Label(window,text='Link :',foreground='white',background='black',font=('monotype corsiva',15))
link.pack(anchor='nw',padx=30,pady=20)

entry_url=StringVar()
link_ent=Entry(window,width=78,textvariable=entry_url)
link_ent.place(x=170,y=116)

link_error=Label(window,foreground='red',background='black',font=('monotype corsiva',15))
link_error.pack(anchor='n',padx=30,pady=0)

path=Label(window,text='Path :',foreground='white',background='black',font=('monotype corsiva',15))
path.pack(anchor='nw',padx=30,pady=0)

path_holder=Label(window,text="\t\t\t  ",foreground='black',background='white',width=50)
path_holder.place(x=170,y=185)

path_style=tkinter.ttk.Style()
path_style.configure('PT.TButton',background='white',foreground='black',font=('nonotype corsiva',15))

path_btn=Button(window,width=10,text='select path',style='PT.TButton',command=open_path)
path_btn.place(x=520,y=185)

path_error=Label(window,foreground='red',background='black',font=('monotype corsiva',15))
path_error.pack(anchor='n',padx=30,pady=0)

download_type=Label(window,text='Download type :',foreground='white',background='black',font=('monotype corsiva',15))
download_type.pack(anchor='w',padx=30,pady=2)

options=["High Quality","Low Quality","Audio"]

types=tkinter.ttk.Combobox(window,values=options,width=20)
types.current(0)
types.place(x=170,y=255)

download_style=tkinter.ttk.Style()
download_style.configure('DD.TButton',background='white',foreground='black',font=('nonotype corsiva',15))

download_btn=Button(window,width=44,text='Download',style='PT.TButton',command=download)
download_btn.pack(anchor='center',padx=30,pady=20)

download_out=Label(window,foreground='white',background='black',font=('monotype corsiva',15))
download_out.pack(anchor='center',pady=10)

download_name=Label(window,foreground='white',background='black',font=('monotype corsiva',15))
download_name.pack(anchor='nw',padx=30,pady=10)

download_size=Label(window,foreground='white',background='black',font=('monotype corsiva',15))
download_size.pack(anchor='nw',padx=30,pady=10)

download_loc=Label(window,foreground='white',background='black',font=('monotype corsiva',15))
download_loc.pack(anchor='nw',padx=30,pady=10)

window.mainloop()