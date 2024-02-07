from fpdf import FPDF
import pandas as pd

# orientation L is horizontal P is vertical
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)
    pdf.line(10,21,200,21)

    for i in range(row["Pages"]):
        pdf.add_page()
# ln 1 ise ondan sonra gelecek metni altına yazar 0 ise iç içe
# recommends size = h
# align yazının ne tarafa hizalanacağını gösterir

pdf.output("output.pdf")
