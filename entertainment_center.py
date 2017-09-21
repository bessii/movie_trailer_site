import media
import fresh_tomatoes

'''create instances of class movie'''
leap = media.Movie("Leap!",
                   "An orphan girl chases her dreams of becoming a ballerina.",
                   "http://nextoons.ir/wp-content/uploads/2017/08/Leap-"
                   "2016-Poster-6.jpg",
                   "https://www.youtube.com/watch?v=h-huA2o6OOY")

spork = media.Movie("Spork",
                    "A frizzy-haired, pink-cheeked outcast named Spork tries "
                    "navigate her way through the annals of junior high.",
                    "https://images-na.ssl-images-amazon.com/images/I"
                    "/81c0Pzi2E7L._SL1500_.jpg",
                    "https://www.youtube.com/watch?v=VDma1UM1FCk")                 
annie = media.Movie("Annie",
                    "Little Annie lives a hard knock life with her"
                    "calculating mother when suddenly everything changes",
                    "https://s3-ap-southeast-2.amazonaws.com/fna-wordpress-web"
                    "site06/wp-content/uploads/2016/10/25022919/Annie-2014-"
                    "960x14401.jpg",
                    "https://www.youtube.com/watch?v=nasLuiP-1E0")
lala_land = media.Movie("La la land",
                        "Sebastian and Mia are drawn by a common desire to do "
                        "what they love. Suddenly success hits and their "
                        "dreams threaten to rip them apart.",
                        "https://pics.filmaffinity.com/la_la_land-262021831-"
                        "large.jpg",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")
beauty_and_the_beast = media.Movie("Beauty and the beast",
                                   "A beautiful young woman imprisoned by a "
                                   "beast in his castle.",
                                   "https://images-na.ssl-images-amazon.com/"
                                   "images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFt"
                                   "ZTgwODExMDQzMTI@._V1_UX182_CR0,0,182,268"
                                   "_AL_.jpg",
                                   "https://www.youtube.com/watch?v=OvW_L8"
                                   "sTu5E")
lego_batman = media.Movie("The Lego Batman movie",
                          "For Batman to  save the city from the Joker's "
                          "hostile takeover,he may have to drop the lone"
                          "vigilante thing, try to work with others and maybe,"
                          " learn to lighten up.",
                          "https://images-na.ssl-images-amazon.com/images/M"
                          "/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZT"
                          "gwOTAyNzU3MDI@._V1_UX182_CR0,"
                          "0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=rGQUKzSDhrg")
wonder_woman = media.Movie("Wonder Woman",
                           "Diana, princess of the Amazons, trained to be an "
                           "unconquerable warrior leaves home for the first " 
                           "time,fights in a war to end all wars. "
                           "She finally discovers her true powers and destiny",
                           "http://cdn.collider.com/wp-content/uploads/2017"
                           "/03/justice-league-wonder-woman-poster.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")
hidden_figures = media.Movie("Hidden Figures",
                             "Three very brilliant African-american women "
                             "serve as the brains behind one of the greatest "
                             "operations in history.",
                             "https://i.ytimg.com/vi/U386EMeWo3I"
                             "/movieposter.jpg",
                             "https://www.youtube.com/watch?v=RK8xHq6dfAo")
spider_man = media.Movie("Spider-Man: Homecoming",
                         "A young Spider-Man begins to navigate his "
                         "newfound identity as the web-slinging superhero.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9"
                         "/Spider-Man"
                         "_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=U0D3AOldjMU")
descendants = media.Movie("Descendants 2",
                          "Mal returns to the Isle of the Lost.",
                          "https://a.dilcdn.com/bl/wp-content/uploads/sites"
                          "/25/2017/01/D2-Heroes-Key-Art.jpg",
                          "https://www.youtube.com/watch?v=g0FLzL7c49c")

'''array of the listed movies above'''
movies = [leap, spork, annie, lala_land, beauty_and_the_beast, lego_batman,
          wonder_woman, hidden_figures, spider_man, descendants]
'''function call to open fresh_tomatoes.html'''
fresh_tomatoes.open_movies_page(movies)
