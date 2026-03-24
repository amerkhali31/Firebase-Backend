
import re
import pandas as pd
import pdfplumber
from datetime import date

def extract_times_from_year_pdf(data_path: str, year: int):

    '''
    Convert raw pdf into dicts that have a full year worth of prayer times formatted how they should be for firebase.

    Args:
    data_path (str): Full path for the pdf to extract prayer times from.

    Returns: Pandas df Day Fajr Sunrise Dhuhr Asr Maghrib Isha
    '''
    
    COLUMNS = ["Day", "Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    ROW_PATTERN = re.compile(
        r"^(\d{1,2})\s+"
        r"(\d{2}:\d{2} [AP]M)\s+"
        r"(\d{2}:\d{2} [AP]M)\s+"
        r"(\d{2}:\d{2} [AP]M)\s+"
        r"(\d{2}:\d{2} [AP]M)\s+"
        r"(\d{2}:\d{2} [AP]M)\s+"
        r"(\d{2}:\d{2} [AP]M)$"
    )
    MONTH_PATTERN = re.compile(
        r"^(January|February|March|April|May|June|"
        r"July|August|September|October|November|December)\s+\d{4}"
    )
    MONTH_NUMBER = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    # ── Extract ───────────────────────────────────────────────────────────────────
    monthly_dataframes = {}

    with pdfplumber.open(data_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            lines = text.split("\n")

            month_name = None
            for line in lines:
                m = MONTH_PATTERN.match(line.strip())
                if m:
                    month_name = m.group(1)
                    break

            if not month_name:
                continue

            rows = []
            for line in lines:
                match = ROW_PATTERN.match(line.strip())
                if match:
                    rows.append(list(match.groups()))

            if rows:
                df = pd.DataFrame(rows, columns=COLUMNS)
                df["Day"] = df["Day"].astype(int)
                monthly_dataframes[month_name] = df

    # ── Build Firebase docs ───────────────────────────────────────────────────────
    firebase_docs = {}  # { "2026-01-01": { prayer time data }, ... }

    for month_name, df in monthly_dataframes.items():
        month_num = MONTH_NUMBER[month_name]

        for _, row in df.iterrows():
            doc_id = date(year, month_num, int(row["Day"])).strftime("%Y-%m-%d")

            firebase_docs[doc_id] = {
                "date":    doc_id,
                "fajr":    row["Fajr"],
                "sunrise": row["Sunrise"],
                "dhuhr":   row["Dhuhr"],
                "asr":     row["Asr"],
                "maghrib": row["Maghrib"],
                "isha":    row["Isha"],
            }
    
    return firebase_docs

if __name__ == '__main__':
    year = 2026
    data_directory = 'MAGR/data/yearly_times'
    data_file = f'prayers_{year}.pdf'
    data_path = f'{data_directory}/{data_file}'
    extract_times_from_year_pdf(data_path, year)