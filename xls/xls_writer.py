import xlsxwriter

from UI.settings_window import SettingsWindow
from database.entities.cleaning_session import CleaningSession
from database.entities.client import Client


def write_invoice(full_path, client, t2c, invoice_nr, tax_date, terms, month, due_by, sessions):
    workbook = xlsxwriter.Workbook(full_path)
    worksheet = workbook.add_worksheet()

    invoice_title_format = workbook.add_format()
    invoice_title_format.set_bold()
    invoice_title_format.set_font("Arial")
    invoice_title_format.set_font_size(18)

    arial_10_format = workbook.add_format()
    arial_10_format.set_font("Arial")
    arial_10_format.set_font_size(10)

    arial_10_bold_format = workbook.add_format()
    arial_10_bold_format.set_bold()
    arial_10_bold_format.set_font("Arial")
    arial_10_bold_format.set_font_size(10)

    arial_10_bold_bordered = workbook.add_format()
    arial_10_bold_bordered.set_bold()
    arial_10_bold_bordered.set_font("Arial")
    arial_10_bold_bordered.set_font_size(10)
    arial_10_bold_bordered.set_border()

    arial_10_bold_bordered_no_bottom = workbook.add_format()
    arial_10_bold_bordered_no_bottom.set_bold()
    arial_10_bold_bordered_no_bottom.set_font("Arial")
    arial_10_bold_bordered_no_bottom.set_font_size(10)
    arial_10_bold_bordered_no_bottom.set_border()
    arial_10_bold_bordered_no_bottom.set_bottom(0)

    sans_11_bold_format = workbook.add_format()
    sans_11_bold_format.set_bold()
    sans_11_bold_format.set_font("Sans")
    sans_11_bold_format.set_font_size(11)

    calibri_11_format = workbook.add_format()
    calibri_11_format.set_font("Calibri")
    calibri_11_format.set_font_size(11)

    calibri_11_bold_format = workbook.add_format()
    calibri_11_bold_format.set_bold()
    calibri_11_bold_format.set_font("Calibri")
    calibri_11_bold_format.set_font_size(11)

    arial_14_bold_format = workbook.add_format()
    arial_14_bold_format.set_bold()
    arial_14_bold_format.set_font("Arial")
    arial_14_bold_format.set_font_size(14)
    arial_14_bold_format.set_bg_color("#000000")
    arial_14_bold_format.set_font_color("#ffffff")

    worksheet.set_column(4, 4, 12)

    worksheet.merge_range("A2:I2", "Invoice", cell_format=invoice_title_format)

    worksheet.write("A4", "To:", arial_10_bold_format)
    worksheet.write("A5", client.name, sans_11_bold_format)
    worksheet.write("A6", "Address:", calibri_11_format)
    worksheet.write("A7", client.address_line_i, calibri_11_format)
    worksheet.write("A8", client.address_line_ii, calibri_11_format)
    worksheet.write("A9", f"Post Code: {client.post_code}")
    worksheet.write("A10", f"Phone {client.phone}", calibri_11_bold_format)

    worksheet.write("F4", t2c.name, sans_11_bold_format )
    worksheet.write("F5", "Address:", calibri_11_format)
    worksheet.write("F6", t2c.address_line_i, calibri_11_format)
    worksheet.write("F7", t2c.address_line_ii, calibri_11_format)
    worksheet.write("F8", f"Post Code: {t2c.post_code}")
    worksheet.write("F9", f"Phone {t2c.phone}", sans_11_bold_format)

    worksheet.merge_range("A14:I14", "Invoice", cell_format=arial_14_bold_format)
    worksheet.merge_range("B15:D15", "Invoice Number", cell_format=arial_10_bold_bordered)
    worksheet.write_number("E15", invoice_nr, workbook.add_format({
        'font': 'Calibri',
        'font_size': 11,
        'border': 1,
        "center_across": 1
    }))

    worksheet.merge_range("F15:G15", "Tax Date", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1
    }))

    worksheet.merge_range("H15:I15", tax_date, cell_format=workbook.add_format({
        'font': 'Calibri',
        'font_size': 11,
        'border': 1,
        'align': "Right"
    }))

    worksheet.merge_range("B16:D16", "Description:", cell_format=arial_10_bold_bordered_no_bottom)
    worksheet.merge_range("F16:G16", "Terms", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1
    }))
    worksheet.merge_range("H16:I16", f"{terms} Days", cell_format=workbook.add_format({
        'font': "Calibri",
        'font_size': 11,
        'border': 1,
        'align': "Right"
    }))
    worksheet.merge_range("B17:D17", "Cleaning services fee", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1,
        'bottom': 0,
        'top': 0
    }))

    worksheet.merge_range("B18:D18", "for month of", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1,
        'top': 0,
    }))

    worksheet.merge_range("E16:E18", month, cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1,
        'align': "Center"
    }))

    worksheet.merge_range("F17:G18", "Payment Due By", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'bold': 1,
        'border': 1,
    }))

    worksheet.merge_range("H17:I18", f"{due_by}", cell_format=workbook.add_format({
        'font': 'Arial',
        'font_size': 10,
        'align': "Right",
        'border': 1
    }))

    worksheet.merge_range("A20:B20", "Date", cell_format=arial_14_bold_format)
    worksheet.merge_range("C20:D20", "Amount per", cell_format=arial_14_bold_format)
    worksheet.merge_range("E20:G20", "Quantity(hours)", cell_format=arial_14_bold_format)
    worksheet.merge_range("H20:I20", "Gross", cell_format=arial_14_bold_format)

    row_idx = 21
    gross_total = 0
    for s in sessions:
        worksheet.merge_range(f"A{row_idx}:B{row_idx}", s.date, cell_format=workbook.add_format({
            'font': "Calibri",
            'font_size': 11,
            'align': "Right",
            'border': 1
        }))

        worksheet.merge_range(f"C{row_idx}:D{row_idx}", s.price, cell_format=workbook.add_format({
            'font': "Calibri",
            'font_size': 11,
            'align': "Right",
            'border': 1,
            'num_format': '£ ##.00'
        }))

        worksheet.merge_range(f"E{row_idx}:F{row_idx}", s.quantity, cell_format=workbook.add_format({
            'font': "Calibri",
            'font_size': 11,
            'align': "Right",
            'border': 1,
            'num_format': '##.00'
        }))

        worksheet.merge_range(f"G{row_idx}:I{row_idx}", s.price * s.quantity, cell_format=workbook.add_format({
            'font': "Calibri",
            'font_size': 11,
            'align': "Right",
            'border': 1,
            'num_format': '£ ##.00'
        }))

        row_idx += 1
        gross_total += s.price * s.quantity

    row_idx += 1
    worksheet.merge_range(f"F{row_idx}:G{row_idx}", "Gross Total", cell_format=workbook.add_format({
        'font': "Arial",
        'font_size': 14,
        'bold': 1
    }))

    worksheet.merge_range(f"H{row_idx}:I{row_idx}", gross_total, cell_format=workbook.add_format({
        'font': "Arial",
        'font_size': 14,
        'bold': 1,
        'num_format': '£ ###.00',
        'border': 1
    }))

    row_idx += 2
    worksheet.merge_range(f"B{row_idx}:H{row_idx+1}", "Please send the payment to Team 2 Clean Clean 98 sort code 20-45-45,acc no 80160229.The payment must be received in 7 days maximum after this invoice was issued.", cell_format=workbook.add_format({
        'font': "Arial",
        'font_size': 8,
        'text_wrap': 1,
        'align': 'center'
    }))


    workbook.close()


def main():
    client = Client()
    client.name = "Unit L3"
    client.address_line_i = "The Maltings"
    client.address_line_ii = "Station Road, Sawbridgeworth"
    client.post_code = "CM2 19JX"
    client.phone = "07875342642"

    t2c = Client()
    t2c.name = "Team 2 Clean 98"
    t2c.address_line_i = "18 Guelph's Lane"
    t2c.address_line_ii = "Thaxted, Dunmow"
    t2c.post_code = "CM6 2PT"
    t2c.phone = "07787194616"

    t2c = SettingsWindow.get_settings()

    sessions = []
    c = CleaningSession()
    c.date = "5/2/2021"
    c.price = 12.0
    c.quantity = 4
    sessions.append(c)

    c = CleaningSession()
    c.date = "12/2/2021"
    c.price = 12.0
    c.quantity = 4
    sessions.append(c)
    sessions.append(c)
    sessions.append(c)

    write_invoice("test.xlsx", client, t2c, 1265, '3-Mar-2021', 7, "February", "10-Mar-2021", sessions)

if __name__ == "__main__":
    main()
