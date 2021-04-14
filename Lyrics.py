def refrain():
    print("Refrain\n\n"
        + "Strangers waitin'\n"
        + "Up and down the boulevard\n"
        + "Their shadows searchin' in the night\n"
        + "Streetlight people\n"
        + "Livin' just to find emotion\n"
        + "Hidin' somewhere in the night\n"
        )
def chorus():
    for x in range(1,4):
        if x == 2:
            feeling = ""
        else:
            feeling = "to that feeling"
        if x == 1:
            print("Chorus\n")
        print("Don't stop believin'\n"
            + "Hold on %s\n" % feeling
            + "Streetlight people"
            )

# Verse 1
print("Verse 1\n\n"
    + "Just a small-town girl\n"
    + "Livin' in a lonely world\n"
    + "She took the midnight train goin' anywhere\n"
    + "Just a city boy\n"
    + "Born and raised in South Detroit\n"
    + "He took the midnight train goin' anywhere\n"
    )

# Instrumental

# Verse 2
print("Verse 2\n\n"
    + "A singer in a smoky room\n"
    + "The smell of wine and cheap perfume\n"
    + "For a smile, they can share the night\n"
    + "It goes on and on and on and on\n"
    )

#Pre-Chorus
refrain()

#Verse 3
print("Verse 3\n\n"
    + "Workin' hard to get my fill\n"
    + "Everybody wants a thrill\n"
    + "Payin' anything to roll the dice just one more time\n"
    + "Some will win, some will lose\n"
    + "Some are born to sing the blues\n"
    + "Oh, the movie never ends\n"
    + "It goes on and on and on and on\n"
    )

#Pre-Chorus
refrain()

#Guitar Solo

#Chorus
chorus()
