import time
import random
import sys

# inspired by https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
def fake_type(words):
    for char in words:
        time.sleep(random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1]))
        sys.stdout.write(char)
        sys.stdout.flush()

while True:
    sys.stdout.write("Please enter the password to unlock the computer: ")
    i = input("")
    if i == "c@teRp1lL3r":
        break
    else:
        sys.stdout.write("\nInvalid attempt, please try again\nEnter Password: ")

fake_type("\nWARNING! New activity detected! Please answer the following security questions to verify your identity:\n")
while True:
    fake_type("\nWhere did I go on August 29?: ")
    i1 = input("")
    if (i1.lower() != "australia"):
        fake_type("\nINCORRECT! Rebooting security questions...\n")
        time.sleep(1)
        continue
    fake_type("\nCorrect! I attended the Bug Conference in Australia on August 29th. Next Question\n")

    fake_type("\nWhat did Dad find in our backyard?: ")
    i2 = input("")
    if (i2.lower() != "bees nest"):
        fake_type("\nINCORRECT! Rebooting security questions...\n")
        time.sleep(1)
        continue
    fake_type("\nCorrect! Dad found a bees nest in our backyard. Next Question\n")

    fake_type("\nName the third origami bug?: ")
    i3 = input("")
    if (i3.lower() != "cicada"):
        fake_type("\nINCORRECT! Rebooting security questions...\n")
        time.sleep(1)
        continue
    fake_type("\nCorrect! The third origami bug was a cicada. Next Question\n")

    fake_type("\nWho showed me their ant farm?: ")
    i4 = input("")
    if (i4.lower() != "samwell"):
        fake_type("\nINCORRECT! Rebooting security questions...\n")
        time.sleep(1)
        continue
    fake_type("\nCorrect! Samwell showed me his ant farm.\n")
    break

s1 = ". . . . . . . . . . \n"
for c in s1:
    time.sleep(0.5)
    sys.stdout.write(c)
    sys.stdout.flush()

fake_type("\n\nSuccessfully logged in. Welcome back Maurice. Opening last opened file...\n")
time.sleep(1)

fake_type("\nDear Jamie,\nIf you are reading this you have passed my trials proving yourself worthy of reading my coveted research.\n\nIt was the month of July 2039. The air was thick with anticipation as I stepped into the dimly lit laboratory. Papers were strewn haphazardly across desks, and the scent of chemicals hung heavy in the air. My heart pounded in my chest as I approached the central table, where a group of researchers had gathered, their faces etched with worry and excitement.\n\nI had always been fascinated by the mysteries of the natural world, but nothing could have prepared me for what we were about to uncover. Months of tireless investigation had led us to this moment, the culmination of our efforts. We had discovered a new species, an enigmatic creature known as the Xenovora Exarachnid.\n\nThe Xenovora Exarachnids were unlike anything the scientific community had ever encountered. Born from the unholy union of ordinary insects and human intelligence, they possessed unparalleled strength and intelligence. Their abilities to adapt and evolve quickly made them a formidable force, capable of overcoming any obstacle in their path. Their knowledge and strength grew at unprecedent rates, overcoming obstacles that took humanity eons in a matter of days.\n\nAs I examined the specimens before me, a chill ran down my spine. These creatures were not merely predators; they were a threat to the delicate balance of nature itself. The implications of our discovery weighed heavily on my conscience. We had unknowingly unleashed a monster upon the world. The Xenovora Exarachnids began to infiltrate human society, disguising themselves as ordinary citizens. They infiltrated government agencies, military organizations, and even high-ranking officials. Their thirst for power and domination knew no bounds, and it seemed that no one was safe from their influence.\n\nAs the chaos unfolded, I became more determined than ever to find a solution to this crisis. I poured over every available resource, studying their weaknesses and trying to understand their biology. But the more I learned, the more I realized that we were hopelessly outmatched.\n\nI notified the Secret Bug Society, the only group capable of understanding the threat to humanity, but was met with resistance. The Xenovora Exarachnids must have infiltrated the ranks of the Society as well. I was ordered to bury my research and fake my disappearance. If I resisted, I would be executed.\n\nJamie, I leave you this knowledge of the Xenovora Exarachnids, for you can be the one to save humanity. The Xenovora Exarachnids may trump humanity in every aspect, but they do not possess human hope. Their cold calculated nature is both their strength and weakness. You, brother, need to tell the world of this danger. I am sure if we humans banded together, hope will prevail and natures delicate balance can once again be restored.\n")

fake_type("\nYou take a few minutes to digest the research your brother unveiled...\n")
time.sleep(10)

fake_type("After pondering over your options, you decide you could either (1) publish Maurice's research and wage war on the Xenovora Exarachnids, or (2) delete Maurice's research and allow humanity to continue in its ignorance.\n")

while (True):
    sys.stdout.write("What do you choose?: ")
    i = input("")
    if i == '1':
        fake_type("\nYou deicde to publish Maurice's research. The world is shocked by your news but, slowly, uncorrupted world leaders follow your lead. With all of humanity on your side, the Xenovora Exarachnids are quickly outnumbered. The war ensues for many decades. For every Xenovora Exarachnid defeated, many more follow suit learning from their fallen brethren's mistakes. One day, all the Xenovora Exarachnids take to the skies as if something or someone is calling to them. In good time, nature's balance is once again restored. As you grow older, you habitually look up at the sky and can't help but wonder where Maurice is...\n\n")
        break
    elif i == '2':
        fake_type("\nYou decide to destroy Maurice's research. After all, ignorance is bliss. You go on to live the rest of your life normally but odd happenings around you continue to catch your eye. Whether that be an extra weird encounter at the coffee shop or actions from notable public figures that are seemingly inexplicable. Yet life goes on. You meet someone, marry them, have kids. But you can't seem to forget the time you spent going through your brother Maurice's things. You can't shake the nagging feeling that the people around you aren't really human. Is your significant other a hyper-intelligent bug creature? It would explain a lot of the quirks they had that you were once attracted to. Does that mean your kids are hybrids? That can't be possible you tell yourself. After all, how can two organisms from different species reproduce? Unless...\n\n")
        break
    else:
        sys.stdout.write("\nPlease input either '1' or '2'\n")

time.sleep(5)

s = "The End."
for char in s:
    time.sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()