
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import itertools
import spacy
nlp=spacy.load('en_core_web_sm')
data={
	"name": "Apple Curry Turkey Pita",
	"ingredients":[
        {
            "quantity":0.5,
            "unit":"tablespoon",
            "name":"salt"
        },
        {
            "quantity":1,
            "unit":"teaspoons",
            "name":"paprika"
        },
        {
            "quantity":0.5,
            "unit":"pound",
            "name":"cooked turkey, cut into chunks"
        }
	],
    "steps":[
        "Heat oil in a skillet over medium-high heat. Stir in onion and lemon juice. Cook until onion is tender. Mix in turkey, season with curry powder and continue cooking until heated through.",
        "Remove from heat. Stir in apple. Stuff pitas with the mixture. Drizzle with yogurt to serve."
    ]
}

text=data["steps"]
text=str(text)
print(text)
for token in nlp(text):
 print(token.text,'=>',token.dep_,'=>',token.head.text)




    

    