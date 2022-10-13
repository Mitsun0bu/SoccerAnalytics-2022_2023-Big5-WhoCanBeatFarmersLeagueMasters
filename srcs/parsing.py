import pandas as pd


def getPlayerDataFrame(pathExcelFile, pathCsvFile, posList):
    '''
    Parameters :
        pathExcelFile : string
        pathCsvFile   : string
        posList       : string
        
    Returns :
        A DataFrame containing only the players who plays at given position(s) 
    '''
    excelFile     = pd.read_excel(pathExcelFile)
    excelFile.to_csv(
                        pathCsvFile, 
                        index  = None,
                        header = True
                    )
    dfPlayers     = pd.read_csv(pathCsvFile)
    dfPlayers     = dfPlayers.loc[(dfPlayers['Pos'].isin(posList))]
    return dfPlayers


def getPlayerNamesList(dfPlayers):
    '''
    Parameters :
        dfPlayers : DataFrame
        
    Returns :
        A list containing the name of the players from the df passed as parameter
    '''
    playerNamesList = []
    for player, pos in dfPlayers[['Joueur', 'Pos']].itertuples(index=False):
            playerNamesList.append(player)
    return playerNamesList