class Tracker:
  def __init__(self, search_set, main_header):
    self.main_header = main_header
    self.element_counter = {key: 0 for key in search_set}
    self.search_set = search_set
      
  def number_duplicates_in_list(self, pair_entry_list):
    for i in range(len(pair_entry_list)):
      if pair_entry_list[i] in self.search_set:
        if self.main_header == pair_entry_list[i]:
          for key in self.element_counter:
            if key == self.main_header:
              self.element_counter[self.main_header] += 1
            else:
              self.element_counter[key] = 0
          pair_entry_list[i] = pair_entry_list[i] + str(self.element_counter[self.main_header])
        else:
          self.element_counter[pair_entry_list[i]] += 1
          pair_entry_list[i] = pair_entry_list[i] + str(self.element_counter[self.main_header]) + ('-' + str(self.element_counter[pair_entry_list[i]]) if self.element_counter[pair_entry_list[i]] > 1 else '')
  