import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import webbrowser

url_label = None
server_process = None

def start_webserver():
    ip = ip_entry.get()
    port = port_entry.get()
    directory = directory_entry.get()

    command = f"python3 -m http.server --bind {ip} {port}"
    try:
        global server_process, status_label
        server_process = subprocess.Popen(command.split(), cwd=directory)
        url = f"http://{ip}:{port}"
        url_label.config(text=url)
        status_label.config(text="Webserver läuft.")
    except Exception as e:
        status_label.config(text=f"Fehler: {str(e)}")

def stop_webserver():
    try:
        global server_process, status_label
        server_process.terminate()
        status_label.config(text="Webserver gestoppt.")
    except Exception as e:
        status_label.config(text=f"Fehler: {str(e)}")

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def copy_url_to_clipboard():
    global url_label
    url = url_label.cget("text")
    app.clipboard_clear()
    app.clipboard_append(url)
    status_label.config(text="URL in Zwischenablage kopiert.")

def open_in_browser():
    url = url_label.cget("text")
    webbrowser.open(url)

def open_website():
    if url_label.cget("text") != "Webserver nicht gestartet.":
        open_in_browser()
    else:
        status_label.config(text="Webserver ist nicht aktiv.")

# GUI erstellen
app = tk.Tk()
app.title("Einfacher Webserver")

# Größe und Hintergrundfarbe der GUI ändern
app.geometry("800x600")
app.configure(bg="#1a1a1a")

# Autor-Anzeige
author_label = tk.Label(app, text="RootGeek", font=("Helvetica", 18, "italic"), fg="#66ff66", bg="#1a1a1a")
author_label.pack(pady=20)

# IP-Adresse Eingabefeld
ip_label = tk.Label(app, text="IP-Adresse:", font=("Helvetica", 16), fg="#66ff66", bg="#1a1a1a")
ip_label.pack()
ip_entry = tk.Entry(app, font=("Helvetica", 16), bg="#333333", fg="#ffffff")
ip_entry.pack(pady=5)

# Port Eingabefeld
port_label = tk.Label(app, text="Port:", font=("Helvetica", 16), fg="#66ff66", bg="#1a1a1a")
port_label.pack()
port_entry = tk.Entry(app, font=("Helvetica", 16), bg="#333333", fg="#ffffff")
port_entry.pack(pady=5)

# Verzeichnis Eingabefeld
directory_label = tk.Label(app, text="Verzeichnis:", font=("Helvetica", 16), fg="#66ff66", bg="#1a1a1a")
directory_label.pack()
directory_entry = tk.Entry(app, font=("Helvetica", 16), bg="#333333", fg="#ffffff")
directory_entry.pack(pady=5)

# Durchsuchen-Button
browse_button = tk.Button(app, text="Durchsuchen", command=browse_directory, font=("Helvetica", 16), bg="#333333", fg="#66ff66")
browse_button.pack(pady=10)

# Frame für Start- und Stopp-Buttons
button_frame1 = tk.Frame(app, bg="#1a1a1a")
button_frame1.pack(pady=10)

# Start-Button
start_button = tk.Button(button_frame1, text="Webserver starten", command=start_webserver, font=("Helvetica", 16), bg="#333333", fg="#66ff66")
start_button.pack(side=tk.LEFT, padx=10)

# Stop-Button
stop_button = tk.Button(button_frame1, text="Webserver stoppen", command=stop_webserver, font=("Helvetica", 16), bg="#333333", fg="#ff6666")
stop_button.pack(side=tk.LEFT, padx=10)

# URL-Anzeige und Kopier-Button
url_label = tk.Label(app, text="Webserver nicht gestartet.", font=("Helvetica", 16), fg="#ffffff", bg="#1a1a1a")
url_label.pack(pady=20)

# Frame für Kopier- und Öffnen-Button
button_frame2 = tk.Frame(app, bg="#1a1a1a")
button_frame2.pack(pady=10)

# Kopier-Button
copy_button = tk.Button(button_frame2, text="URL kopieren", command=copy_url_to_clipboard, font=("Helvetica", 16), bg="#333333", fg="#66ff66")
copy_button.pack(side=tk.LEFT, padx=10)

# Button, um die gestartete Website im Browser zu öffnen
open_browser_button = tk.Button(button_frame2, text="Website öffnen", command=open_website, font=("Helvetica", 16), bg="#333333", fg="#66ff66")
open_browser_button.pack(side=tk.LEFT, padx=10)

# Status-Label
status_label = tk.Label(app, text="", font=("Helvetica", 16), fg="#ffffff", bg="#1a1a1a")
status_label.pack(pady=5)

# Tastaturkürzel (keine Änderungen hier, da bereits vorhanden)

app.mainloop()
