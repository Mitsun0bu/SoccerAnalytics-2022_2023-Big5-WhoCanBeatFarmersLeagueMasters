# DATA SOURCES

# https://fbref.com/fr/comps/Big5/shooting/joueurs/Statistiques-Les-5-grands-championnats-europeens
# https://fbref.com/fr/comps/Big5/passing/joueurs/Statistiques-Les-5-grands-championnats-europeens


import random
from   parsing     import getPlayerDataFrame, getPlayerNamesList
from   myTemplates import generateRadarFigure
from   myRadars    import generateStrikerRadar


pathExcelFile           = "../data/data_big5.xlsx"
pathCsvFile             = "../data/data_big5.csv"

pathFont                = "../fonts"

posList                 = ["AT", "MTAT"]

colorPsg                = ["#003D71", "#EA161F"]
colorManCity            = ["#92C6F7", "#821310"]


pathLogoPsg             = "../img/logoPsg.png"
pathLogoManCity         = "../img/logoManCity.png"


pathLogoBundesliga      = "../img/logoBundesliga.png"
pathLogoLaLiga          = "../img/logoLaLiga.png"
pathLogoLigue1          = "../img/logoLigue1.png"
pathLogoPremierLeague   = "../img/logoPremierLeague.png"
pathLogoSerieA          = "../img/logoSerieA.png"

title                   = "Can You Beat\nFarmers' League Masters ?\n\nSeason 2022-2023"

pathPhotoMbappé         = "../img/Mbappé.png"
pathPhotoHaaland        = "../img/Haaland.png"

pathRadarMbappé         = "../output/Kylian Mbappé.png"
pathRadarHaaland        = "../output/Erling Haaland.png"


dfStrikers              = getPlayerDataFrame(pathExcelFile, pathCsvFile, posList)

strikerNamesList        = getPlayerNamesList(dfStrikers)

params                  = list(dfStrikers.columns)
params                  = params[7:]

# contender               = random.choice(strikerNamesList)
# print(contender)
contender               = "Marcus Rashford"
colorContender          = ["#E1422C", "#FFE634"]
pathLogoContenderClub   = "../img/logoManU.png"
pathLogoContenderLeague = pathLogoPremierLeague
pathPhotoContender      = "../img/Marcus Rashford.png"
pathRadarContender      = "../output/" + contender + ".png"


for striker in strikerNamesList:
    if striker == "Kylian Mbappé":
        generateStrikerRadar(dfStrikers, striker, params, colorPsg[0], colorPsg[1], 'white')
        generateRadarFigure("K. Mbappé", "23", "11", "10", "2", pathFont, title, colorPsg[0], pathLogoPsg, pathLogoLigue1, pathPhotoMbappé, pathRadarMbappé)
    elif striker == "Erling Haaland":
        generateStrikerRadar(dfStrikers, striker, params, colorManCity[0], colorManCity[1], 'white')
        generateRadarFigure("E. Haaland", "22", "11", "17", "3", pathFont, title, colorManCity[0], pathLogoManCity, pathLogoPremierLeague, pathPhotoHaaland, pathRadarHaaland)
    elif striker == contender:
        generateStrikerRadar(dfStrikers, striker, params, colorContender[0], colorContender[1], "black")
        generateRadarFigure("M. Rashford", "24", "11", "3", "2", pathFont, title, colorContender[0], pathLogoContenderClub, pathLogoContenderLeague, pathPhotoContender, pathRadarContender)