from firebase_admin import firestore, initialize_app
from firebase_client import db
from google.cloud.firestore_v1 import FieldFilter

def delete_by_range(start_date: str, end_date: str, collection: str):
    
    '''
    Delete documents who's date are between the start and end dates given in YYYY-MM-DD format.
    Each document's name is it's date
    '''

    collection_ref = db.collection(collection)
    start_ref = collection_ref.document(start_date)
    end_ref = collection_ref.document(end_date)

    # Query using document ID (__name__)
    docs = collection_ref \
        .where(filter=FieldFilter("__name__", ">=", start_ref)) \
        .where(filter=FieldFilter("__name__", "<=", end_ref)) \
        .stream()

    # Batch delete (recommended)
    batch = db.batch()
    count = 0

    for doc in docs:
        batch.delete(doc.reference)
        count += 1

        # Firestore batch limit is 500
        if count % 500 == 0:
            batch.commit()
            batch = db.batch()

    # Commit remaining
    batch.commit()

    print(f"Deleted {count} documents")


def upload_new_prayer_times(prayer_times, collection):
    # Firestore max 500 ops per batch
    BATCH_SIZE = 500

    items = list(prayer_times.items())

    for i in range(0, len(items), BATCH_SIZE):
        batch = db.batch()
        chunk = items[i : i + BATCH_SIZE]

        for doc_id, data in chunk:
            ref = db.collection(collection).document(doc_id)
            batch.set(ref, data)

        batch.commit()
        print(f"Committed batch {i // BATCH_SIZE + 1} ({len(chunk)} docs)")