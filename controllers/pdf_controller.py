from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDF_controller():
        

    def generar_pdf(self,productos):
        try:
            # Nombre del archivo PDF
            archivo_pdf = "productos_listado.pdf"
            c = canvas.Canvas(archivo_pdf, pagesize=letter)
            ancho, alto = letter

            # Título del PDF
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, alto - 50, "Listado de Productos")

            # Cabecera de la tabla
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, alto - 80, "ID")
            c.drawString(150, alto - 80, "Descripción")
            c.drawString(450, alto - 80, "Precio")

            # Rellenar filas con datos
            c.setFont("Helvetica", 10)
            y = alto - 100
            for producto in productos:
                c.drawString(50, y, str(producto[0]))  # ID
                c.drawString(150, y, str(producto[1]))  # Descripción
                c.drawString(450, y, f"${producto[2]:.2f}")  # Precio
                y -= 20

                # Salto de página si se llena
                if y < 50:
                    c.showPage()
                    y = alto - 50
                    c.setFont("Helvetica", 10)

            # Guardar PDF
            c.save()
            print(f"PDF generado con éxito: {archivo_pdf}")

        except Exception as e:
            print(f"Error al generar el PDF: {e}")
