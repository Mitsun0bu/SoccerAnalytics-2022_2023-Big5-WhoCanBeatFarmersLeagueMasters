import math
import matplotlib.pyplot as plt
from   scipy             import stats
from   mplsoccer         import PyPizza, FontManager


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

    player = dfPlayers.loc[dfPlayers['Joueur'] == targetPlayer].reset_index()
    player = list(player.loc[0])
    player = player[8:]
    
    values = []
    for x in range(len(params)):
        values.append(math.floor(stats.percentileofscore(dfPlayers[params[x]], player[x])))
        
    fontNormal = FontManager('https://github.com/google/fonts/blob/main/ofl/barlowcondensed/BarlowCondensed-Medium.ttf?raw=true')

    paramsEnglish = ["Goals", "On-Target Shots %", "Goals per Shots", "xG (w/o pen.)", "Passes Completed", "Assists", "Key Passes"]
    # Instantiate PyPizza class
    baker = PyPizza(
                        params              = paramsEnglish, # list of parameters
                        straight_line_color = "white",       # color for straight lines
                        straight_line_lw    = 2,             # linewidth for straight lines
                        last_circle_color   = "black",       # linewidth of last circle
                        last_circle_lw      = 5,             # linewidth of last circle
                        other_circle_color  = "white",       # color for straight lines
                        other_circle_lw     = 2,             # linewidth for other circles
                        other_circle_ls     = "--"           # linestyle for other circles
                    )

    # Plot pizza
    fig, ax = baker.make_pizza(
                                values,                                        # list of values
                                figsize           = (10, 10),                  # adjust figsize according to your need
                                color_blank_space = ["#C5C5C5"] * len(params), # use same color to fill blank space
                                blank_alpha       = 0.7,                       # alpha for blank-space colors
                                param_location    = 110,                       # where the parameters will be added
                                # values to be used when plotting slices
                                kwargs_slices=dict(
                                                    facecolor = sliceColor,
                                                    edgecolor = "white",
                                                    zorder    = 2,
                                                    linewidth = 2
                                                  ),
                                # values to be used when adding parameter
                                kwargs_params=dict(
                                                    color          = "#000000",
                                                    fontsize       = 24,
                                                    fontproperties = fontNormal.prop,
                                                    va="center"
                                                  ),
                                # values to be used when adding parameter-values
                                kwargs_values=dict(
                                                    color          = valueColor,
                                                    fontsize       = 18,
                                                    fontproperties = fontNormal.prop,
                                                    zorder         = 3,
                                                    bbox=dict(
                                                                edgecolor = "white",
                                                                facecolor = boxColor,
                                                                boxstyle  = "circle,pad=0.4",
                                                                lw        = 2
                                                              )
                                                  )
                              )

    plt.show()
    fig.set_size_inches(10, 10)
    savePath = "../output/" + targetPlayer + ".png"
    fig.savefig(savePath, dpi = 800, transparent=True)