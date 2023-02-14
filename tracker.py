class Tracker:
  def __init__(self, search_set, main_header):
    self.main_header = main_header
    self.element_counter = {main_header: 0}
    self.search_set = search_set
      
  def number_duplicates_in_list(self, pair_entry_list):
    for i in range(len(pair_entry_list)):
      if pair_entry_list[i] in self.search_set:
        if self.main_header == pair_entry_list[i]:
          self.element_counter[self.main_header] += 1
        pair_entry_list[i] = pair_entry_list[i] + str(self.element_counter[self.main_header])
  