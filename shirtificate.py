from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 36)
        self.cell(0, 100, 'CS50 Shirtificate!', ln=1, align='C')

pdf = PDF()
pdf.add_page()

# Position and dimensions of the image
x = 50  # X coordinate
y = 100  # Y coordinate
width = 100  # Image width
height = 100  # Image height

pdf.image(r"C:\Users\ME\cs50bysomi\shirtificate.png", x, y, width, height)

pdf.set_y(10)  # Adjust the vertical position
pdf.set_x((pdf.w - pdf.get_string_width('CS50 Shirtificate')) / 2)  # Center horizontally
pdf.set_font('helvetica', '', 20)
pdf.set_text_color(255,255,255)  
pdf.cell(90, 250, 'Somi took CS50!', align='C')
pdf.ln(10)
pdf.output("shirtificate.pdf")
