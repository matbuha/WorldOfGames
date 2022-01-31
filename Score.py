import Utils
import Live
# import json


# this function writing "name" and "score" to TXT file.
def add_score():
    try:
        y = Utils.sum_numbers * 3 + 5
        name = Live.name
        score = str(y)
        with open(Utils.SCORES_FILE_NAME, "w") as file:
            file.write(f'{name}  {score}\n')
        return name, score

    except FileNotFoundError as e:
        print(f"File NOT found! {e.args}")
        return Utils.BAD_RETURN_CODE


"""this function will convert the txt file to json file (not in use right now)"""
# def convert_to_json():
#     # the file to be converted
#     filename = Utils.SCORES_FILE_NAME
#
#     # resultant dictionary
#     dict1 = {}
#
#     # fields in the sample file
#     fields = ['name', 'score']
#
#     with open(filename) as fh:
#         # count variable for employee id creation
#         l = 1
#
#         for line in fh:
#
#             # reading line by line from the text file
#             description = list(line.strip().split(None, 2))
#
#             # for automatic creation of id for each employee
#             sno = 'player' + str(l)
#
#             # loop variable
#             i = 0
#             # intermediate dictionary
#             dict2 = {}
#             while i < len(fields):
#                 # creating dictionary for each employee
#                 dict2[fields[i]] = description[i]
#                 i = i + 1
#
#             # appending the record of each employee to
#             # the main dictionary
#             dict1[sno] = dict2
#             l = l + 1
#
#     # creating json file
#         out_file = open("TextFiles/JsonScore.json", "w")
#         json.dump(dict1, out_file, indent=2)
#         out_file.close()
#         return out_file

