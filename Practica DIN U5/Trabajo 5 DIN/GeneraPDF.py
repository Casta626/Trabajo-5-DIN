def generaPDF(self):
    
        outfile = "result.pdf"

        template = PdfReader("template.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)

        canvas = Canvas(outfile)

        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)

        ystart = 455

        canvas.drawString(122, ystart, label1.text())

        # Ponemos la fecha de hoy
        today = datetime.today()
        canvas.drawString(455, ystart, today.strftime('%F'))

        # Lo ideal es partir de una posición y jugar con el tamaño de la fuente
        # En este caso, cada línea son 28 puntos
        canvas.drawString(294, ystart, label2.text())
        # canvas.drawString(230, ystart-28, self.data['apellidos'])

        canvas.drawString(175, ystart-(32), label3.text())

        canvas.drawString(290, ystart-(32), label4.text())

        # canvas.drawString(423, ystart-(32), label5.text())

        # canvas.drawString(168, ystart-(2*32), self.data['n_perifericos'])

        # canvas.drawString(285, ystart-(2*32), self.data['perifericos'])

        # canvas.drawString(128, ystart-(3*32), self.data['direccion'])

        canvas.drawString(472, ystart-(3*32), "Python")

        # canvas.drawString(472, ystart-(2*32), self.data['prueba'])

        # Sería posible establecer un límite en el número de caracteres:
        # field.setMaxLength(25)

        # Reemplazamos los saltos de línea por espacios en los comentarios
        comments = label5.text().replace('\n', ' ')
        if comments:
            # Separamos el texto de la primera línea (más corta que el resto)
            lines = textwrap.wrap(comments, width=65)
            # Nos quedamos la primera línea
            first_line = lines[0]
            # Guardamos el resto en remainder
            remainder = ' '.join(lines[1:])

            # Separamos el resto con una anchura mayot
            lines = textwrap.wrap(remainder, 75)
            # Nos quedamos con las cuatro primeras que son el máximo (sin incluir la primera)
            lines = lines[:4]

            # Escribimos la primera línea
            canvas.drawString(147, ystart-(4*32), first_line)
            # Y luego las otras cuatro
            for n, l in enumerate(lines, 1):
                canvas.drawString(80, ystart-(4*32) - (n*32), l)

        canvas.save()
        QMessageBox.information(self, "Finalizado", "Se ha generado el PDF")

        finish = self.wizard.button(QWizard.FinishButton)