import xlwt
import os


def Write(logs, results):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("test")
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = "time"
    font.bold = True
    font.underline = True
    font.italic = True
    style.font = font
    worksheet.write(0, 0, "诛仙")
    worksheet.write(0, 1, "龙族", style)
    for log, number in logs.items():
        worksheet.write(number, 0, log)
    for result, num in results.items():
        worksheet.write(result, 1, num)
    workbook.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), "class.xls"))


if __name__ == '__main__':
    logs = {"info": 1, "debug": 2, "error": 3}
    results = {1: "ok", 2: "no", 3: "no"}
    Write(logs, results)
