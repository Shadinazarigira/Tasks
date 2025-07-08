
import random

def get_user_word(word_type):
    return input(f"Please enter a {word_type}: ").strip()

def make_fun_story():
    print("Let's create a fun story! Please provide some words.")

    # Get words from user
    user_adj = get_user_word("adjective")
    user_noun = get_user_word("noun")
    user_verb = get_user_word("verb")
    user_place = get_user_word("place")
    user1_adj = get_user_word("adjective")
    user1_noun = get_user_word("noun")
    user1_verb = get_user_word("verb")
    user1_place = get_user_word("place")
    adj1=random.choice([user_adj,user1_adj])
    adj2=random.choice([user_adj,user1_adj])
    noun1=random.choice([user_noun,user1_noun])
    noun2=random.choice([user_noun,user1_noun])
    verb1=random.choice([user_verb,user1_verb])
    verb2=random.choice([user_verb,user1_verb])
    place1=random.choice([user_place,user1_place])
    place2=random.choice([user_place,user1_place])


    story = (
        f"Once upon a time, a {adj1} {noun1} {verb1} through the {place1}. "
        f"There, it met a {adj2} {noun2} who loved to {verb2}. "
        f"Together, they traveled to the {place2} and had the most amazing adventure anyone could imagine!"
    )
    return story

if __name__ == "__main__":
    print("\n" + make_fun_story())
