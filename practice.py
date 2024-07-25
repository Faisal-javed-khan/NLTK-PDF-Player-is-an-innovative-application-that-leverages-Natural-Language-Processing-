import tkinter as tk
from tkinter import filedialog
import PyPDF2
from nltk import sent_tokenize
import pyttsx3

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_file_entry.delete(0, tk.END)
        pdf_file_entry.insert(0, file_path)

def play_nltk():
    file_path = pdf_file_entry.get()

    if file_path:
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""

                print("Number Of Pages: ",len(pdf_reader.pages))

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

                sentences = sent_tokenize(text)
                # Do something with the sentences, for now, let's just print them.
                for sentence in sentences:
                    engine.say(text)
                    engine.runAndWait()
                    # print(sentence)

        except Exception as e:
            print(f"Error reading PDF: {e}")

# Create the main window
root = tk.Tk()
root.title("NLTK PDF Player")

# engine = pyttsx3.init()
engine = pyttsx3.init(driverName='sapi5')
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', rate-50)


# Get the list of available voices
voices = engine.getProperty('voices')

# Print available voices
for voice in voices:
    print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

# Set the voice (you can choose a different index based on the available voices)
engine.setProperty('voice', voices[1].id)

# Create widgets
pdf_file_label = tk.Label(root, text="PDF File:")
pdf_file_entry = tk.Entry(root, width=40)
select_button = tk.Button(root, text="Select", command=select_pdf)
play_button = tk.Button(root, text="Play", command=play_nltk)

# Arrange widgets using the grid geometry manager
pdf_file_label.grid(row=0, column=0, padx=10, pady=10)
pdf_file_entry.grid(row=0, column=1, padx=10, pady=10)
select_button.grid(row=0, column=2, padx=10, pady=10)
play_button.grid(row=1, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
