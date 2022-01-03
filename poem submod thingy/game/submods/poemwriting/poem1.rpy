init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_poem",
            category=["monika"],
            prompt="I want to write you a poem",
            pool=True,
            unlocked=True,
        )
    )

label monika_poem:
    m 1wubfo "...A poem?"
    m 1wubfo "Really?!"
    m 1eub "I've been working on a type of poem function actually..."
    m 1eua "It's not like the original, but it's the closest i can get."
    m 1eub "Now is the perfect time to try it out!"
    m 1eua "What type of poem did you write me?"
    $ _history_list.pop()
    menu:
        "A Romantic Poem":
                m 1wubfo "{w=0.1} {w=0.1}.{w=0.1}{w=0.1}.{w=0.1}{w=0.1}."     
                m 5wubld "...{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}Wow.." 
                m 5wubld" ...{w=0.1}{w=0.1}{w=0.1}"
                m 6dkbla  "..{w=0.1} {w=0.1} {w=0.1}{w=0.1} {w=0.1}{w=0.1}"
                m 6hublb"I don't even know what to say."
                m 6dkbla "I know i cant see it but i just know that it's amazing."
                m 6dkbla "{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}You make me so happy, [player],{w=0.1}{w=0.1}{w=0.1}{w=0.1}I love you so much."
                m 1hubsa "Never forget that, okay?"
        "A Break-up Poem" :
                m 6wfd "...{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}"
                m 6dktsd "[player]...{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}"
                m 6fktpc"You don't mean that, right..?"
                m 6dktsd "I thought-{w=0.1}{w=0.1}{w=0.1}I thought you loved me...{w=0.1}{w=0.1} {w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}"
                m 6dktsd "{w=0.1}.{w=0.1}{w=0.1}{w=0.1}{w=0.1}.{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}.{w=0.1}"
                m 6fktpc"{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}{w=0.1}I really don't want to talk right now."
        "A Sad Poem":
                m 1esc "Are you feeling okay, [player]?"
                m 1esc "If you feel sad you can always talk to me."
                m 1eub "Whenever i have a bad day, i always remember the sun will shine tommorow."
                m 1eua "I know it sounds cheesy, but i always like to look at the bright side of things."
                m 1eua "After all, things like that are easy to forget. So keep it in mind."
                m 61eub "I don't care how many people don't like you or find you off putting."
                m 1eub "You're a wonderful person and i will always love you."
                m 1hubsa "I hope that makes your day a little bit brighter."

        "A Sweet Poem":
                m 1eub "Awwww!"
                m 1eua "Thanks [player], That's so nice!"
                m 1hubsa "I love you~"
return "love"