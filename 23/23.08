import re
import os
from docx import Document


def change_dates(folder, textchange, changeTo):
    text = textchange

    for root, _, files, in os.walk(folder):
        for file in files:
            if file.endstih(".docx"):
                document = Document(os.path.join(root, file))
                for parapraph in document.paragraphs:
                    for run in parapraph.runs:
                        run.text = re.sub(text, changeTo, run.text)

                document.save(os.path.join(root, "EDITED ", + file))


if __name__ == '__main__':
    textchange = r"Red car"
    changeTo = "car Red"
    change_dates("23.08.docx", textchange, changeTo)
