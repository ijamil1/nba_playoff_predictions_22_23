import pandas as pd
import docx 
for i in range(22):
    if i <= 8:
        st = '0'+str(i)
        end = '0'+str(i+1)
    elif i == 9:
        st = '0' + str(i)
        end = str(i+1)
    else:
        st = str(i)
        end = str(i+1)
    team_per_game = './nba_data/{}-{} team per game.docx'.format(st,end)
    player_per_game = './nba_data/{}-{} player per game.docx'.format(st,end)
    team_advanced = './nba_data/{}-{} team advanced stats.docx'.format(st,end)
    opp_per_game = './nba_data/{}-{} opponent per game.docx'.format(st,end)

    doc = docx.Document(team_per_game)
    allText = []
    for docpara in doc.paragraphs:
        allText.append(docpara.text)
    print(allText)
    break