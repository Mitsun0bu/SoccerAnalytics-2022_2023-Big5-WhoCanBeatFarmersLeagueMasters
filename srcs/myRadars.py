import math
import matplotlib.pyplot as plt
from   scipy             import stats
from   mplsoccer         import PyPizza, FontManager


def getPlayerRawValues(dfPlayers, targetPlayer):
    playerRawValues = []
    playerRawValues = dfPlayers.loc[dfPlayers['Joueur'] == targetPlayer].reset_index()
    playerRawValues = list(playerRawValues.loc[0])
    playerRawValues = playerRawValues[8:]
    return playerRawValues


def getPlayerPercentileValues(dfPlayers, params, playerRawValues):
    playerPercentileValues = []
    for x in range(len(params)):
        playerPercentileValues.append(math.floor(stats.percentileofscore(dfPlayers[params[x]], playerRawValues[x])))
    return playerPercentileValues


def saveRadar(fig, savePath):
    fig.set_size_inches(10, 10)
    fig.savefig(savePath, dpi = 800, transparent=True)


def generateStrikerRadar(dfPlayers, targetPlayer, params, sliceColor, boxColor, valueColor):
    '''
    Parameters :
        dfPlayers    : DataFrame
        targetPlayer : string
        params       : list 
        sliceColor   : string
        boxColor     : string
        valueColor   : string

    Returns :
        Generate a radar for a given player and save it in output folder
    '''

    # HANDLE FONT
    fontLink               = 'https://github.com/google/fonts/blob/main/ofl/barlowcondensed/BarlowCondensed-Medium.ttf?raw=true'
    fontNormal             = FontManager(fontLink)

    # GET RAW VALUES FOR THE TARGETED PLAYER FROM DATA FRAME
    playerRawValues        = getPlayerRawValues(dfPlayers, targetPlayer)
    
    # CONVERT RAW VALUES TO PRECENTILE VALUES
    playerPercentileValues = getPlayerPercentileValues(dfPlayers, params, playerRawValues)

    # TRANSLATE THE PARAMETERS OF THE RADAR FROM FRENCH TO ENGLISH
    paramsEnglish          = [
                                "Goals",
                                "On-Target Shots %",
                                "Goals per Shots",
                                "xG (w/o pen.)",
                                "Passes Completed",
                                "Assists",
                                "Key Passes"
                             ]

    # INSTANTIATE PyPizza CLASS
    baker                  = PyPizza(
                                        params              = paramsEnglish,
                                        straight_line_color = "white",
                                        straight_line_lw    = 2,
                                        last_circle_color   = "black",   
                                        last_circle_lw      = 5,
                                        other_circle_color  = "white",
                                        other_circle_lw     = 2,
                                        other_circle_ls     = "--"
                                    )

    # MAKE THE RADAR PLOT
    fig, ax                = baker.make_pizza(
                                                playerPercentileValues,
                                                figsize           = (10, 10),
                                                color_blank_space = ["#C5C5C5"] * len(params), # RADAR BACKGROUND COLOR
                                                blank_alpha       = 0.7,
                                                param_location    = 110,
                                                # SLICES PARAMETERS
                                                kwargs_slices     = dict(
                                                                            facecolor = sliceColor,
                                                                            edgecolor = "white",
                                                                            zorder    = 2,
                                                                            linewidth = 2
                                                                        ),
                                                # RADAR PARAMETERS PARAMETERS 
                                                kwargs_params     = dict(
                                                                            color          = "black",
                                                                            fontsize       = 24,
                                                                            fontproperties = fontNormal.prop,
                                                                            va             = "center"
                                                                        ),
                                                # RADAR VALUES PARAMETERS
                                                kwargs_values     = dict(
                                                                            color          = valueColor,
                                                                            fontsize       = 18,
                                                                            fontproperties = fontNormal.prop,
                                                                            zorder         = 3,
                                                                            bbox           = dict(
                                                                                                    edgecolor = "black",
                                                                                                    facecolor = boxColor,
                                                                                                    boxstyle  = "circle,pad=0.4",
                                                                                                    lw        = 2
                                                                                                )
                                                                        )
                                                )


    savePath               = "../output/" + targetPlayer + ".png"
    saveRadar(fig, savePath)