from utils.db_utils import delete_by_range
import constants

def main():
    '''
    Last updated times March 23rd 2026. Got times through March 2027
    '''
    delete_start = '2025-02-01'
    delete_end   = '2026-01-31'

    # only need to do once. Deletes old docs
    #delete_by_range(delete_start, delete_end, constants.yearly_collection)

if __name__ == "__main__":
    main()