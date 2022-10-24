import matplotlib.pyplot as plt
from   matplotlib        import font_manager
from   matplotlib        import rcParams
from   pylab             import text
from   PIL               import Image


def generateRadarFigure(playerName, playerAge, nGames, nGoals, nAssists, pathFont, title, clubColor, pathLogoClub, pathLogoLeague, pathPhotoPlayer, pathRadar):

    fontDir = [pathFont]
    for font in font_manager.findSystemFonts(fontDir):
        font_manager.fontManager.addfont(font)
    rcParams['font.family'] = "DIN"
    
    layout = [
                ["logo"]       * 2 + ["title"] * 6 + ["logo2"] * 2,
                ["logo"]       * 2 + ["title"] * 6 + ["logo2"] * 2,
                ["logo"]       * 2 + ["title"] * 6 + ["logo2"] * 2,
                ["space"]      * 10,
                ["playerName"] * 2 + ["graphTitle"] * 8,
                ["player"]     * 2 + ["graph"] * 8,
                ["player"]     * 2 + ["graph"] * 8,
                ["player"]     * 2 + ["graph"] * 8,
                ["space2"]     * 2 + ["graph"] * 8, 
                ["playerInfo"] * 2 + ["graph"] * 8,
                ["playerInfo"] * 2 + ["graph"] * 8,
                ["playerInfo"] * 2 + ["graph"] * 8,
                ["playerInfo"] * 2 + ["graph"] * 8,
                ["footer"]     * 10,
             ]
    
    
    fig = plt.figure(figsize = (10,10))
    
    templateSection = fig.subplot_mosaic(layout)
    
    modified = ""
    for x in range(len(layout)):
        for y in range(len(layout[x])):
            toModify = layout[x][y]
            if toModify != modified:
                # ANNOTATION FOR DEBUG
                # templateSection[toModify].annotate(
                #                             xy   = (.5,.5),
                #                             text = toModify,
                #                             ha   = "center",
                #                             va   = "center",
                #                             size = 20
                #                         )
                # CREATE BOXES FOR EACH ELEMENT OF THE TEMPLATE
                templateSection[toModify].tick_params(
                                                axis        = 'both', # changes apply to both axis
                                                which       = 'both', # major and minor ticks are affected
                                                bottom      = False,  # ticks along the bottom edge are off
                                                top         = False,  # ticks along the top edge are off
                                                left        = False,  # ticks along the left edge are off
                                                labelbottom = False,  # labels along the bottom edge are off
                                                labelleft   = False   # labels along the left edge are off
                                            )
                templateSection[toModify].axis("off")
                
                modified = toModify
    
    
    # ADD CLUB LOGO
    logoClubImage = Image.open(pathLogoClub)
    templateSection["logo"].imshow(logoClubImage)
    
    
    # ADD TITLE
    templateSection["title"].annotate(
                                xy   = (.5,.5),
                                size = 20,
                                text = title,
                                weight = "bold",
                                ha   = "center",
                                va   = "center"
                            )
    
    
    # ADD LEAGUE LOGO
    logoLeagueImage = Image.open(pathLogoLeague)
    templateSection["logo2"].imshow(logoLeagueImage)
    
    
    # ADD PLAYER PHOTO
    photoPlayerImage = Image.open(pathPhotoPlayer)
    templateSection["player"].imshow(photoPlayerImage)
    
    
    # ADD PLAYER NAME
    infoName = playerName
    templateSection["playerName"].annotate(
                                            xy     = (0.12, 1),
                                            text   = infoName,
                                            size   = 20,
                                            color  = "#FFE634",
                                            weight = "bold",
                                            ha     = "left",
                                            va     = "top",
                                            bbox   = dict(
                                                            boxstyle   = "square",
                                                            facecolor  = clubColor,
                                                            edgecolor  = "none"
                                                         )
                                          )
    
    # ADD GRAPH TITLE
    graphTitle = "Percentile Rank VS \"Big5\" Strikers"
    templateSection["graphTitle"].annotate(
                                            xy     = (0.155, 1),
                                            text   = graphTitle,
                                            size   = 20,
                                            color  = "#FFE634",
                                            weight = "bold",
                                            ha     = "left",
                                            va     = "top",
                                            bbox   = dict(
                                                            boxstyle   = "square",
                                                            facecolor  = clubColor,
                                                            edgecolor  = "none"
                                                         )
                                          )
    
    # ADD PLAYER INFO   
    infoAge     = "Age\n\t\t| "          + playerAge + " y.o.\n"
    infoGames   = "Games Played\n\t\t| " + nGames    + "\n"
    infoGoals   = "Goals\n\t\t| "        + nGoals    + "\n"
    infoAssists = "Assists\n\t\t| "      + nAssists
    infoText    = infoAge + infoGames + infoGoals + infoAssists
    templateSection["playerInfo"].annotate(
                                            xy   = (0.12, 1),
                                            text   = infoText,
                                            size   = 14,
                                            color  = '#FFE634',
                                            weight = "bold",
                                            ha     = "left",
                                            va     = "top",
                                            bbox   = dict(
                                                            boxstyle   = "square",
                                                            facecolor  = clubColor,
                                                            edgecolor  = "none"
                                                         )
                                         )

    
    # ADD GRAPH
    radar = Image.open(pathRadar)
    templateSection["graph"].imshow(radar)
    
    
    # ADD FOOTER
    footerText = "Data from : FBRef / Statsbomb\t\t\t\t\t\tViz inspired by : @mckayjohns\t\t\t\t\t\tMade in : Python"
    templateSection["footer"].annotate(
                                        xy     = (0, 0),
                                        text   = footerText,
                                        size   = 12,
                                        color  = "black",
                                        weight = "bold",
                                        ha     = "left",
                                        va     = "top",
                                        bbox   = dict(
                                                        boxstyle   = "square",
                                                        facecolor  = "#D9D4C0",
                                                        edgecolor  = "none"
                                                     )
                                      )
    
    # SAVE FIGURE
    fig.set_size_inches(10, 10)
    savePath = "../output/" + playerName + "Final.png"
    fig.savefig(savePath, dpi = 800)