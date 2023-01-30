
from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for row_cnt in range(1, len(contacts_list)):
  for col_cnt in range(3):
    tmp_name_data = contacts_list[row_cnt][col_cnt].split(" ", maxsplit=3)
    for x in range(len(tmp_name_data)):
      contacts_list[row_cnt][col_cnt + x] = tmp_name_data[x]

pattern = r'(8|\+7)?\W*(\d{3})\W*(\d{3})\W*(\d{2})\W*(\d{2})'
substitution = r'+7 (\2) \3 \4 \5 '

for x_row in range(len(contacts_list)):
  contacts_list[x_row][5] = re.sub(pattern, substitution, re.sub(r"(\(|\)|\s)", r"", contacts_list[x_row][5])).strip()

header = contacts_list.pop(0)

result_list = []
for row_cnt in range(len(contacts_list)):
  is_in = False
  for rl_row_cnt in range(len(result_list)):
    name_cnt = 0
    if contacts_list[row_cnt][0] == result_list[rl_row_cnt][0]:
      name_cnt += 1
    if contacts_list[row_cnt][1] == result_list[rl_row_cnt][1]:
      name_cnt += 1
    if contacts_list[row_cnt][2] == result_list[rl_row_cnt][2]:
      name_cnt += 1
    if name_cnt >= 2:
      is_in = True
      cur_result_row = rl_row_cnt
  if is_in == True:
    for cell_cnt in range(len(result_list[cur_result_row])):
        if not result_list[cur_result_row][cell_cnt]:
          result_list[cur_result_row][cell_cnt] = contacts_list[row_cnt][cell_cnt]
  else:
    result_list.append(contacts_list[row_cnt])

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerow(header)
  datawriter.writerows(result_list)