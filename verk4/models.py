# -*- coding: utf-8 -*-

# Model - the business logic of the application

# The model is all to do with the data that's to be handled by the application
# and nothing to do with how it's presented / wired into the view
# functions that work with data (files, database, api etc.)

# very simple class
class Actor:

    def __init__(self, name, age, sex, info):
        self.name = name
        self.info = info
        self.age = age
        self.sex = sex


# data
actorInfo = [
"Keanu Charles Reeves, whose first name means 'cool breeze over the mountains' in Hawaiian, was born September 2, "
"1964 in Beirut, Lebanon. He is the son of Patricia Taylor, a showgirl and costume designer, and Samuel Nowlin Reeves,"
" a geologist. Keanu's father was born in Hawaii, of British, Portuguese, Native Hawaiian, and Chinese ancestry,"
" and Keanu's mother is originally from England. After his parents' marriage dissolved, Keanu moved with his mother and younger sister,"
" Kim Reeves, to New York City, then Toronto. Stepfather #1 was Paul Aaron, a stage and film director - he and Patricia divorced within a year,"
" after which she went on to marry (and divorce) rock promoter Robert Miller and hair salon owner Jack Bond. "
"Reeves never reconnected with his biological father. In high school,"
" Reeves was lukewarm toward academics but took a keen interest in ice hockey "
"(as team goalie, he earned the nickname'The Wall') and drama."
" He eventually dropped out of school to pursue an acting career.",

]


actorList = [
Actor("Keanu Reeves", "2.september 1964", "Male", actorInfo[0]), Actor( "Laurence Fishburne", " July 30, 1961", "Male", actorInfo[0])
]

