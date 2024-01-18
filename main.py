from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from PIL import Image
from os import remove


def paste_image_to_pdf(pdf_path, image_path, output_path, x, y, page_number):
    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()

    for page_n in range(len(pdf_reader.pages)):
        pdf_page = pdf_reader.pages[page_n]
        if page_n == page_number:
            image = Image.open(image_path)
            image_width, image_height = image.size
            packet = canvas.Canvas("__temp.pdf")
            packet.drawImage(image_path, x, y, width=image_width, height=image_height, mask='auto')
            packet.save()
            pdf_page.merge_page(PdfReader("__temp.pdf").pages[0])
            remove("__temp.pdf")
        pdf_writer.add_page(pdf_page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)


if __name__ == "__main__":
    pdf_path = 'test.pdf'               # Path to src pdf
    image_path = 'test_signature.png'   # Path to sugnature
    output_path = 'output.pdf'          # Path to dist pdf
    x_coordinate = 50                   # X-coordinate
    y_coordinate = 50                   # Y-coordinate
    paste_image_to_pdf(pdf_path=pdf_path, image_path=image_path, output_path=output_path, x=x_coordinate,
                       y=y_coordinate, page_number=0)
