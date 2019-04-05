

import http.server
import socketserver
import csv
import os
PORT = 8216


__author__ = 'Shamim'
if __name__ == '__main__':


    characters = []
    appearances = []
    character_episodes = []
    page_data = []


    class Movies:
        def __init__(self, name):
            self.name = name
        # Fetching characters data


        def users(self):
            with open('characters.csv', 'r') as user_file:
                spam_reader = csv.reader(user_file)
                for row in spam_reader:
                    characters.append(row)
            return characters
        # Fetching episode_per_season data


        def apprearancee(self):
            with open('episode_per_season.csv', 'r') as appearance_file:
                spam_reader = csv.reader(appearance_file)
                for row in spam_reader:
                    appearances.append(row)
            return appearances
        # Fetching characters and their episods


        def userAppearance(self):
            for character in characters:
                name = character[0]
                for appearance in appearances:
                    if appearance[1] == name:
                        appear = [appearance[2], appearance[3], appearance[0]]
                        character_episodes.append(appear)
            with open('userApearence.html', 'w') as data_file:
                csv_writer = csv.writer(data_file, delimiter='\n')
                s = "Number of episodes, , died_in_season,season" + str(character_episodes)
                csv_writer.writerow(s)
            return character_episodes
        # Fetching all characters, death season and episod number


        def pageData(self):
            x = 0
            while x < 20:
                episode = appearances[x][2]
                death_season = appearances[x][3]
                list_both = [episode, death_season]
                list_final = list_both + characters
                page_data.append(list_final)
                x += 1
            with open('pageData.html', 'w') as data_file:
                csv_writer = csv.writer(data_file, delimiter='\n')
                csv_writer.writerow(page_data)
            return page_data


    viewer = Movies("shamim")
    viewer.users()
    viewer.apprearancee()
    viewer.userAppearance()
    viewer.pageData()
# server


Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("server on port", PORT)
httpd.serve_forever()
