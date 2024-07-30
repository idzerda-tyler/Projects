import tkinter as tk
import youtubeDL as youtube

root = tk.Tk()
root.title("YouTube Downloader 3000")
root.geometry("300x150")
root.resizable(False, False)

url = tk.StringVar(root)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

url_entry = tk.Label(frame, text="Enter URL:")
url_entry.pack(fill='x', expand=True)

entry = tk.Entry(frame, textvariable=url)
entry.pack(fill='x', expand=True)
entry.focus()

run = tk.Button(frame, text='RUN', command=lambda: (youtube.youtubeDL(url.get())))
run.pack(pady=10)



root.mainloop()
