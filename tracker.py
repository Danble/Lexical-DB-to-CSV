class Tracker:
  def __init__(self, search_set, main_header):
    self.main_header = main_header
    self.element_counter = {key: 0 for key in search_set}
    self.search_set = search_set
  #TODO create tests for this fn
  def __change_keys_display(self, element):
    header_counter = str(self.element_counter[self.main_header])
    counter = str(self.element_counter[element])
    element += header_counter + ('-' + counter if self.element_counter[element] > 1 and self.main_header != element else '')
    return element
  #TODO create tests for this fn  
  def __handle_counters(self, element):
    if self.main_header == element:
      for key in self.element_counter:
        if key == self.main_header:
          self.element_counter[self.main_header] += 1
        else:
          self.element_counter[key] = 0
    else:
      self.element_counter[element] += 1

  def number_duplicates_in_list(self, pair_entry_list):
    for i in range(len(pair_entry_list)):
      if pair_entry_list[i] in self.search_set:
        self.__handle_counters(pair_entry_list[i])
        pair_entry_list[i] = self.__change_keys_display(pair_entry_list[i])
  