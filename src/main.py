import nltk
import nltk.corpus
import nltk.stem
import nltk.tokenize
import sklearn
import sklearn.metrics
import sklearn.naive_bayes
import sklearn.neighbors
import sklearn.svm
import sklearn.tree

from InquirerPy import inquirer
from InquirerPy.utils import patched_print
from engine import collect, search, train, predict_link
from story import story_text
from utils import err, success, is_valid_url
from index import inverted_index


def main():
    while (True):
        option = inquirer.select(
            message="What do you want to do?",
            choices=[
                "Collect new documents",
                "Index documents",
                "Search for a query",
                "Train ML classifier",
                "Predict a link",
                "Your story",
                "Exit"
            ],
        ).execute()

        if option == "Collect new documents":
            collect()

        elif option == "Index documents":
            inverted_index()

        elif option == "Search for a query":
            query = inquirer.text(message="Enter your query:").execute()
            search(query)

        elif option == "Train ML classifier":
            train()

        elif option == "Predict a link":
            link = inquirer.text(message="Enter a link:").execute()
            if (not is_valid_url(link)):
                err("Invalid link provided!")

            else:
                predict_link(link)

        elif option == "Your story":
            story()

        elif option == "Exit":
            proceed = inquirer.confirm(message="Are you sure?", default=True).execute()
            if (proceed):
                exit()

        patched_print()

    return


def story():
    with open("story.txt", "w") as file:
        file.write(story_text)

    success("Your story is saved in story.txt!")
    return


if (__name__ == "__main__"):
    main()
