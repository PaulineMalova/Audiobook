import pdftotext

from gtts import gTTS

from os.path import splitext
from app.utils import pick_pdf_file


def read_file():
    file_location = pick_pdf_file()
    # open the file in reading (rb) mode and call it f
    with open(file_location, "rb") as f:
        # store a text version of the pdf file f in pdf variable
        pdf = pdftotext.PDF(f)

    string_of_text = ""
    for text in pdf:
        string_of_text += text
    print(string_of_text)

    final_file = gTTS(text=string_of_text, lang="en")  # store file in variable
    outname = splitext(file_location)[0] + ".mp3"
    final_file.save(outname)  # save file to computer
    return f"File saved to device with name: {outname}"
