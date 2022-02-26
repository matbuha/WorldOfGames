from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def converting_to_score(difficulty, name):
    try:
        # this code will convert the difficulty to score.
        x = difficulty
        score = (x * 3) + 5
        print(f" Your score is {score} !")

# this code writing "name" and "score" to TXT file.
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(f'{name}  {score}\n')
        return file

    except FileNotFoundError as e:
        print(f"File NOT found! {e.args}")
        return BAD_RETURN_CODE
