import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def test():
  print("run")

def open_file(window,text_edit):
  askopenfilename(filetypes=[("Text Files","*.txt")])

  if not filepath:
    return

  text_edit.delete(1.0,tk.END)
  with open(filepath,"r") as f:
    content = f.read()
    text_edit.insert(tk.END,content)
  window.title(f"Open file: {filepath}")
def save_file(window,text_edit):
  filepath = asksaveasfilename(filetypes=[("Text Files","*.txt")])

  if not filepath:
     return

  with open(filepath,"w") as f:
     content = text_edit.get(1.0,tk.END)
     f.write(content)
  window.title(f"Save file: {filepath}")


def main():
  window=tk.Tk()
  window.title("Text editor")

  text_edit=tk.Text(window,font="Arial 12 bold")
  text_edit.grid(row=0,column=1)

  frame=tk.Frame(window,relief=tk.RAISED,bd=2)
  save_button=tk.Button(frame,text="Save",font="Arial 12 bold",command=lambda: save_file(window,text_edit))
  open_button=tk.Button(frame,text="Open",font="Arial 12 bold",command=lambda: open_file(window,text_edit))        
  save_button.grid(row=0,column=0)
  open_button.grid(row=1,column=0,padx=10,pady=10)
  frame.grid(row=0,column=0,sticky="ns")
  
  window.mainloop()

main()
