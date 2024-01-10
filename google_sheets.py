import gspread
from database_functions.get_info import get_event_info_list

google_client = gspread.service_account('config_info/eventsmanager-385008-fbee8488f0a6.json')
sheets = google_client.open_by_key('')
worksheet = sheets.worksheet(title="Архив мероприятий")

def add_event_to_archive_sheet(event_id):
    with open("config_info/first_empty_line.txt", 'r') as file:
        line = int(file.read().strip())

    event_info = get_event_info_list(event_id)
    worksheet.update(f"A{line}", event_info[1])
    worksheet.update(f"B{line}", event_info[2])
    worksheet.update(f"C{line}", event_info[3])
    worksheet.update(f"D{line}", f"{event_info[4]}-{event_info[5]}")
    worksheet.update(f"E{line}", event_info[8])
    worksheet.update(f"F{line}", event_info[7])
    worksheet.update(f"G{line}", event_info[6])

    with open('config_info/first_empty_line.txt', 'w') as f:
        f.write(str(line + 1))
