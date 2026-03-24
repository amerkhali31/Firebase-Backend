from utils.db_utils import delete_by_range, upload_new_prayer_times
from utils.pdf_utils import extract_times_from_year_pdf
import constants

def update_year_times():
    '''
    Last updated times March 23rd 2026. Got times through March 2027
    '''

    # Delete Old Docs
    delete_start = '2025-01-01'
    delete_end   = '2028-01-31'
    delete_by_range(delete_start, delete_end, constants.yearly_collection)

    # Get New Prayer Times
    year = 2026
    data_directory = 'MAGR/data/yearly_times'
    data_file = f'prayers_{year}.pdf'
    data_path = f'{data_directory}/{data_file}'
    prayer_times = extract_times_from_year_pdf(data_path, year)
    upload_new_prayer_times(prayer_times, constants.yearly_collection)


if __name__ == "__main__":
    update_year_times()




# # Upload adhan times to Firestore collection
# for index, row in adhan_times_df.iterrows():
#     doc_id = str(row["date"])  # Convert Date to string (e.g., "2025-01-01")

#     data = {
#         "date": doc_id,  # Add a Date field matching the document ID
#         "fajr": row["fajr"],
#         "sunrise": row["sunrise"],
#         "dhuhr": row["dhuhr"],
#         "asr": row["asr"],
#         "maghrib": row["maghrib"],
#         "isha": row["isha"],
#     }
    
#     db.collection(collection_name).document(doc_id).set(data, merge = True)
#     print(f"Document {doc_id} added to collection {collection_name}.")
# print("All documents added successfully.")