import random

lec1 = ["Big Band", "Sentimental Journey", "Doris Day", "Popular (pop) music",
       "Race", "vocalist", "jump blues", "Hillbilly", "bluegrass", "sheet music", "copyright", "Victorian Ballad", 
       "industrial revolution", "piano", "Parlour songs", "timbre", "Believe me, If all those endearing young charms"
       , "Tin Pan Alley", "Charles K harris", "After the ball", "1892", "Division of Labours", "Style of TPA", "AABA musical form", "Somewhere over the Rainbow",
       "Fiddle", "Arc of popularity", "Good rocking tonight", "What is music", "1790s to 1830s"]

lec2 = ["1619", "Old Alabama", "Work Song", "Floating pool of verse", "folk music", "self-conciousness", "African Retentions", "Percussive"
        , "Distorted", "Riffs", "motifs", "call and response", "Western music", "1861-1865", "institutionalized racism", 
        "rural to urban shift for blacks", "Ragtime and Jazz", "Characteristics of blues", "Country (Rural) Blues", 
        "Blind Willie McTell", "Robert Johnson", "27 club", "Sweet home chicago"]

lec3 = ["Mechanical reproduction", "phonograph", "1887", "1910s", "What was recorded?", "cutural chauvinism", "1920", "1922", "End of 1920s",
"Record Industry", "Ralph Peer", "Mamie Smith", "Uncle Dave Macon and the Fruit Jar Drinkers: \" Carve that Possum\"", "Carr and Blackwell", 
"City blues", "Television", "1945- 1955", "WDIA Memphis", "Post war Era", "economic prosperity", "Replacement of big band", "Nat King Cole", "Patti Page",
"Baby Boomers", "end of 1950", "Blues & TPA music", "Gospel", "Ray Charles", "Chicago Electric Blues", "Hoochie Coochie Man", 
"Stop-Time", "Muddy Waters", "Aristocrat Records", "Electric Guitars"]

lec4 = ["Cover Version", "Moral Panic", "Little Richard", "Tutti Frutti", "Pat Boone", "The Chords", "The Crew Cuts", "timpani", "Rock & Roll", "Alan Freed", "Western Swing", 
"Rock Around the Clock", "Elvis Presley", "Sam Phillips", "That's Alright Mama/Blue moon of Kentucky", "Walking bass/snap bass", "Slap Echo", 
"The hillbilly cat", "Colonel Tom Parker", "Hound Dog", "68 comeback special", "Death of Elvis"]

lec = ["Chuck Berry", "Themes of Rock & Roll", "Jonny B. Goode", "Maybellene", "What happened in 1959?", "Payola", "Alan Freed (The DJ)", 
"Civil Rights Movement", "Brown vs The Board of Education", "Rosa Parks", "Non violent protest", "The Great Extinction"]

lec6 = ["In between years", "The dance craze", "The Locomotion", "Teen Idols", "Blue Velvet", "The Brill Building", "The Magnetophonon", "Bing Crosby", 
"Les Paul", "Solid body electric guitar", "Multitrack recording", "Phil Sepctor", "Be My Baby", "Wall of Sound", "Surf Music", "The Beach boys"]

lec7 = ["John F. Kennedy", "Civil Right Movements", "November 22, 1963", "Post War Britain", "Skiffle", "John Lennon", "Paul McCartney", "1961 the Beatles", 
        "Brian Epstein", "Parlophone", "Please Please Me", "1963 - 1964 US", "Mersey Beat", "Help & Yesterday", "Bob Dylan", "Tomorrow Never Knows", "Avant-garde music", 
        "March 1966", "Strawberry Fields Forever", "Sgt. Pepper's Lonely Hearts Club Band", "A Day In The Life", "Aleatory techniques", "Concept Albums", "Hippie Aesthetic"]

lec8 = ["The British Blues Revival", "Brian Jones", "Andrew Loog Oldham", "King Bee", "The Beatles / The Rolling Stones", "The Yardbirds", "The Who", 
"Soul Music", "soul to Funk", "Motown", "Maxine Powell", "Cholly Atkins", "The Funk Brothers", "You'd Better Shop Around", "Stop in the Name of Love"]

lec9 = ["Stax", "Otis Redding", "Sam and Dave", "Aretha Franklin", "The Black Panthers", "The Re-Africanization of Black Culture", "James Brown - Funk", "I Feel Good", "Cold Sweat", 
"Cyclical/circular structure"]

lec10 = ["late 1950s to early 1960s", "Why revival?", "Bob Dylan", "Summer of 1965", "The Beats and The Beat Culture", "Hippies", "Psychedelic", "acid rock/psychedelic rock", 
"White Rabbit", "Jimi Hendrix", "Woodstock", "Kent State", "Altamont"]

lec11 = ["Energy Crisis", "August 1974: Watergate", "Vietnam: the fall of Saigon", "1970s", "Hard Rock/Heavy Metal", "Distortion/Tempo/Influence/Lyrics", "Black Sabbath", "Deep Purple", 
"Led Zeppelin"]

lec12 = ["The Origins of Hip Hop", "Precursors of Rap", "Jamaican Toasting", "DJ Kool Herc", "Grand Master Flash", "GM Melle Mel", "Grand Wizard Theodore", "Rapper's Delight", 
"MTV station"]

lectures = [lec1, lec2, lec3, lec4, lec, lec6, lec7, lec8, lec9, lec10, lec11, lec12]


n = int(input())
arr = []
lec = lectures[n - 1]
while len(arr) < len(lec):
    idx = random.randrange(0, len(lec))
    if lec[idx] not in arr:
        print(lec[idx])
        arr.append(lec[idx])
        n = input()
