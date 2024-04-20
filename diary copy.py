class Diary:
    def __init__(self):
        self._diary_ = []

    def add(self, entry):
        self._diary_.append(entry)

    def all_entries(self):
        return self._diary_ 
    
    def find_best_chunk_for_reading_time(self, wpm, minutes):
        readable_words = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        readable_entries = []
        for entry in self._diary_:
            if entry.count_words() <= readable_words:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
                    readable_entries.append(entry)
        return most_readable 
    
    def contact_list(self):
        contact_list = []
        for entry in self._diary_:
            number_list = entry.extract_number()
            contact_list = contact_list + number_list
        return contact_list

    # CAN I DO THIS IN A WAY THAT I CAN APPEND RATHER THAN CONCATENATE
