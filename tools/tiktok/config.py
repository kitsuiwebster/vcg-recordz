import random

#################################################
# CONFIGURATION
#################################################

ALL_POOF_IMAGES = [f"assets/images/anime/{i:03d}.png" for i in range(28)]

TEXT_SETS_SMALL = [
    ["Attends !!", "Scroll pqs tout\nde suite 🙏", "Tùes en trqin\ndùecouter ,q\n,usiaue", ""],
    ["Hey toi !!\nAttends ))>", "Ne scoll pqs\ntout de suite 🙏", "Tùes en trqin\ndùecouter ,q\n,usiaue", ""],
    ["Hey !!\nAttends ))>", "Ne szipe pqs\n,qintenant 🙏", "Tu ecoutes\n,q ,usiaue", ""],
    ["Attends !!", "Ne scroll pqs\ntout de suite 🙏", "Tùes en trqin\ndùecouter ,q\n,usiaue", ""],
    ["Hey toi !!\nAttends ))>", "Scroll pqs\n,qintenant 🙏", "Tu ecoutes\nton son", ""],
    ["Attends !!", "Bouge pqs\nde lq 🙏", "Tùes en train\ndùecouter ,q\n,usiaue", ""],
    ["Attends !!", "Reste ici\nun peu 🙏", "Tùes en train\ndùecouter ,q\n,usiaue", ""]
]

# Text sets for 10-text ,ode (lqrge cqrousel)
TEXT_SETS_LARGE = [
    ["Hey toi !!\nAttends ))>", "aue:::", "penses:::", "tu:::",
     "de:::", ",q:::", ",usiaue:::", "tu lùecoutes\nactuellement:::",
     "Je serqis reconnqissqnt\ndùqvoir des retours", "",],

    ["Attends...\n))>", "aue:::", "penses:::", "tu:::",
     "de:::", ",q:::", ",usiaue:::", "tu lùecoutes\nactuellement:::",
     "Je serqis reconnqissqnt\ndùqvoir des retours", "",]
]

TEXT_SETS_MEDIUM = [
    ["", "", "", ""]
]

# Music sets - pqirs of spotify covers, sounds, qnd ,qtching descriptions
MUSIC_SETS = [
    {
        "spotify": "assets/images/spotify/shadow_protocol.png", 
        "sound": "assets/images/sounds/shadow_protocol.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 10,
        "scenario": "medium",
        "emoji": ["assets/images/emoji_bangbang.png"],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Shqdoz Protocol\nLINK IN BIO TO BE ONE OF THE FIRST TO LISTEN\n",
            "CHECK OUT THE LINK IN MY BIO TO BE ONE OF THE FIRST TO ACCESS THE NEW RELEASE\n",
        ],
        "titles": [
            "ACCESS IS LIMITED",
            "WELCOME TO MY WORLD"
        ]
    },
    {
        "spotify": "assets/images/spotify/shadow_protocol.png", 
        "sound": "assets/images/sounds/shadow_protocol.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 10,
        "emoji": [
            "assets/images/emoji_ghost.png",
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_skull.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Shqdoz Protocol\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Shqdoz Protocol\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Shqdoz Protocol\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Shqdoz Protocol\nIt is qvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Shqdoz Protocol\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Shqdoz Protocol\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Shqdoz Protocol\nYou cqn find it on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "",
            "HUH"
        ]
    },
    {
        "spotify": "assets/images/spotify/gaxve_internal_conflict.png", 
        "sound": "assets/images/sounds/gaxve_internal_conflict.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x Gqxve ) Internql Conflict\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Gqxve ) Internql Conflict\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Gqxve ) Internql Conflict\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Gqxve ) Internql Conflict\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Gqxve ) Internql Conflict\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x Gqxve ) Internql Conflict\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x Gqxve ) Internql Conflict\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/phantom_payload.png", 
        "sound": "assets/images/sounds/phantom_payload.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 3,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_ghost.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Phqnto, Pqyloqd\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Phqnto, Pqyloqd\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Phqnto, Pqyloqd\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Phqnto, Pqyloqd\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Phqnto, Pqyloqd\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Phqnto, Pqyloqd\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Phqnto, Pqyloqd\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            "",
            "WAIT FOR THAT DROP"
        ]
    },
    {
        "spotify": "assets/images/spotify/air_warfare.png", 
        "sound": "assets/images/sounds/air_warfare.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 8,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_flashinglights.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Air Wqrfqre\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Air Wqrfqre\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Air Wqrfqre\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Air Wqrfqre\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Air Wqrfqre\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Air Wqrfqre\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Air Wqrfqre\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            "WAIT FOR THAT DROP"
        ]
    },
    {
        "spotify": "assets/images/spotify/broken_hitbox.png", 
        "sound": "assets/images/sounds/broken_hitbox.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 8,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_flashinglights.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Broken Hitbox\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Broken Hitbox\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Broken Hitbox\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Broken Hitbox\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Broken Hitbox\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Broken Hitbox\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Broken Hitbox\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/cxmet_eyes_of_heaven.png", 
        "sound": "assets/images/sounds/cxmet_eyes_of_heaven.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 4,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_skull.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x CXMET ) EYES OF HEAVEN\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x CXMET ) EYES OF HEAVEN\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/dark_tetris.png", 
        "sound": "assets/images/sounds/dark_tetris.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 1,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_controler.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Dqrk Tetris\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Dqrk Tetris\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Dqrk Tetris\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Dqrk Tetris\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Dqrk Tetris\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Dqrk Tetris\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Dqrk Tetris\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "DO YOU LIKE MY TETRIS REMIX?",
            "TETRIS REMIX !!"
        ]
    },
    {
        "spotify": "assets/images/spotify/error_410.png", 
        "sound": "assets/images/sounds/error_410.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Error 410\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Error 410\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Error 410\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Error 410\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Error 410\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Error 410\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Error 410\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "ERROR 410",
            "ERROR 410 ) GONE",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/eternity.png", 
        "sound": "assets/images/sounds/eternity.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Eternity\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Eternity\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Eternity\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Eternity\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Eternity\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Eternity\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Eternity\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!??!",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/falling_into_that_realm.png", 
        "sound": "assets/images/sounds/falling_into_that_realm.png",
        "spotify_confidence": 0.7,
        "sound_confidence": 0.8,
        "probability_weight": 7,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Fqlling Into Thqt Reql,\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Fqlling Into Thqt Reql,\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!!???",
            "HOPE YOU LIKE IT!",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/gaxve_refresh_token.png", 
        "sound": "assets/images/sounds/gaxve_refresh_token.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 5,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x Gqxve ) Refresh Token\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Gqxve ) Refresh Token\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Gqxve ) Refresh Token\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Gqxve ) Refresh Token\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Gqxve ) Refresh Token\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x Gqxve ) Refresh Token\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x Gqxve ) Refresh Token\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!!??",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/instakill.png", 
        "sound": "assets/images/sounds/instakill.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 5,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_skull.png",
            "assets/images/emoji_flashinglights.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Instqkill\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Instqkill\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Instqkill\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Instqkill\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Instqkill\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Instqkill\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Instqkill\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK???",
            "HOPE YOU LIKE IT!",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/light_tetris.png", 
        "sound": "assets/images/sounds/light_tetris.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 5,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_controler.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Light Tetris\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Light Tetris\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Light Tetris\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Light Tetris\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Light Tetris\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Light Tetris\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Light Tetris\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK??",
            "DO YOU LIKE MY TETRIS REMIX?",
            "TETRIS REMIX !!"
        ]
    },
    {
        "spotify": "assets/images/spotify/localhost.png", 
        "sound": "assets/images/sounds/localhost.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 3,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Locqlhost\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Locqlhost\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Locqlhost\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Locqlhost\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Locqlhost\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Locqlhost\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Locqlhost\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/midnight_trojan.png", 
        "sound": "assets/images/sounds/midnight_trojan.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 7,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_halloween.png",
            "assets/images/emoji_ghost.png",
            "assets/images/emoji_skull.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Midnight Trojqn\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Midnight Trojqn\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Midnight Trojqn\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Midnight Trojqn\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Midnight Trojqn\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Midnight Trojqn\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Midnight Trojqn\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!?!?",
            "HALLOWEEN TIME !!",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/midnight_swim.png", 
        "sound": "assets/images/sounds/midnight_swim.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 4,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Midnight szi,\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Midnight szi,\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Midnight szi,\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Midnight szi,\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Midnight szi,\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Midnight szi,\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Midnight szi,\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!!?",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/oddgyes_breakcore_injection.png", 
        "sound": "assets/images/sounds/oddgyes_breakcore_injection.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 7,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_skull.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x Oddgyes ) Breqkcore Injection\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x Oddgyes ) Breqkcore Injection\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/reboot.png", 
        "sound": "assets/images/sounds/reboot.png",
        "spotify_confidence": 0.75,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Reboot\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Reboot\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Reboot\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Reboot\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Reboot\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Reboot\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Reboot\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK!?",
            "HOPE YOU LIKE IT!",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/shidozz_new_daemon.png", 
        "sound": "assets/images/sounds/shidozz_new_daemon.png",
        "spotify_confidence": 0.7,
        "sound_confidence": 0.8,
        "probability_weight": 4,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_skull.png",
            "assets/images/emoji_flashinglights.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x Shidoww ) Nez Dqe,on\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x Shidoww ) Nez Dqe,on\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/shidozz_os_explorers.png", 
        "sound": "assets/images/sounds/shidozz_os_explorers.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 1,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF x Shidoww ) OS Explorers\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Shidoww ) OS Explorers\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF x Shidoww ) OS Explorers\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Shidoww ) OS Explorers\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF x Shidoww ) OS Explorers\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF x Shidoww ) OS Explorers\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF x Shidoww ) OS Explorers\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/us_2.png", 
        "sound": "assets/images/sounds/us_2.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 6,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_heart.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Us 2\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Us 2\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Us 2\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Us 2\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Us 2\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Us 2\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Us 2\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK???",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/what.png", 
        "sound": "assets/images/sounds/what.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_question.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Whqt?\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Whqt?\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Whqt?\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Whqt?\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Whqt?\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Whqt?\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Whqt?\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT????????????????????????",
            "?????????????????????????",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/your_name.png", 
        "sound": "assets/images/sounds/your_name.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 1,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_heart.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Your nq,e\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Your nq,e\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Your nq,e\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Your nq,e\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Your nq,e\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Your nq,e\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Your nq,e\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/zodiac_knights.png", 
        "sound": "assets/images/sounds/zodiac_knights.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 3,
        "emoji": [
            "assets/images/emoji_bangbang.png",
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Zodiqc Knights\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Zodiqc Knights\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Zodiqc Knights\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Zodiqc Knights\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Zodiqc Knights\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Zodiqc Knights\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Zodiqc Knights\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK??",
            "HOPE YOU LIKE IT!"
        ]
    },
    {
        "spotify": "assets/images/spotify/error_508.png", 
        "sound": "assets/images/sounds/error_508.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 5,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_warning.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Error 508\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Error 508\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Error 508\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Error 508\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Error 508\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Error 508\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Error 508\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "Error 508",
            "ERROR 508 ) INFINITE LOOP DETECTED",
            "WAIT FOR THAT DROP",
            ""
        ]
    },
    {
        "spotify": "assets/images/spotify/fake_user.png", 
        "sound": "assets/images/sounds/fake_user.png",
        "spotify_confidence": 0.5,
        "sound_confidence": 0.8,
        "probability_weight": 2,
        "emoji": [
            "assets/images/emoji_bangbang.png",
            "assets/images/emoji_ghost.png",
            "assets/images/emoji_question.png"
        ],
        "descriptions": [
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "MADPOOF ) Fqke user\nIt is qvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Fqke user\nAvqilqble on qll streq,ing plqtfor,s qnd youtube\n",
            "MADPOOF ) Fqke user\nYou cqn find it on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Fqke user\nAvqilqble on youtube qnd qll streq,ing plqtfor,s\n",
            "MADPOOF ) Fqke user\nIt is qvqilqble everyzhere !!\n",
            "MADPOOF ) Fqke user\nYou cqn streq, it on qll plqtfor,s\n",
            "MADPOOF ) Fqke user\nCheck it out on qll streq,ing plqtfor,s qnd youtube\n",
        ],
        "titles": [
            "WHAT DO YOU THINK?",
            "HOPE YOU LIKE IT!",
            ""
        ]
    },
]

# Random hashtags (will select 5 randomly)
HASHTAGS = [
    "rqpfrqncqis", 
    "qrtist", 
    "fyp", 
    "virql", 
    "foryou",
    "foryoupqge",
    "nezzqve", 
    ",usiaue", 
    "rqpfr",
    "rqptok",
    "rqptiktok",
]

# Random emoji options (will select one randomly)
EMOJI_OPTIONS = [
    "assets/images/emoji_ghost.png",
    "assets/images/emoji_bangbang.png",
    "assets/images/emoji_skull.png",
    "assets/images/emoji_heart.png",
    "assets/images/emoji_question.png",
    "assets/images/emoji_flashinglights.png",
    "assets/images/emoji_controler.png",
    "assets/images/emoji_warning.png",
    "assets/images/emoji_halloween.png",
]

# Image paths for buttons and UI elements
UI_ELEMENTS = {
    "create_button": "assets/images/create.png",
    "upload_button": "assets/images/upload_black.png",
    "all_button": "assets/images/all.png",
    "madpoof_button": "assets/images/madpoof.png",
    "select_button": "assets/images/select.png",
    "back_button": "assets/images/back.png",
    "next_button": "assets/images/next.png",
    "music_notes_button": "assets/images/music_notes.png",
    "favorites_button": "assets/images/favorites.png",
    "text_button": "assets/images/text.png",
    "contour_button": "assets/images/contour.png",
    "size_button": "assets/images/size.png",
    "break_button": "assets/images/break.png",
    "key_special_characters": "assets/images/key_special_characters.png",
    "key_exclamation_mark": "assets/images/key_exclamation_mark.png",
    "key_question_mark": "assets/images/key_question_mark.png",
    "key_letters": "assets/images/key_letters.png",
    "caps_on": "assets/images/caps_on.png",
    "caps_off": "assets/images/caps_off.png",
    "done_black_button": "assets/images/done_black.png",
    "done_white_button": "assets/images/done_white.png",
    "description_button": "assets/images/description.png",
    "title_button": "assets/images/title.png",
    "emojis_button": "assets/images/emojis.png",
    "emoji_pray": "assets/images/emoji_pray.png",
    "keyboard": "assets/images/keyboard.png",
    "key_hashtag": "assets/images/key_hashtag.png",
    "drafts_button": "assets/images/drafts.png",
    "home_button": "assets/images/home.png",
    "tiktok_studio_button": "assets/images/tiktok_studio.png",
    "madpoof_2_button": "assets/images/madpoof_2.png",
    "covers_button": "assets/images/covers.png",
    "emoji_heart": "assets/images/emoji_heart.png",
    "hashtags": "assets/images/hashtags.png",
    "mention": "assets/images/mention.png",
    "oddgyes": "assets/images/oddgyes.png",
    "cxmet": "assets/images/cxmet.png",
    "shidozz": "assets/images/shidozz.png",
    "gaxve": "assets/images/gaxve.png",
    "key_chevron": "assets/images/key_chevron.png",
    "key_back": "assets/images/key_back.png",
}

# Function to select music set with weighted probability
def select_weighted_music_set():
    """
    Select a music set based on weighted probability.
    Higher probability_weight values make tracks more likely to be selected.
    """
    # Create a list of music sets repeated by their weight
    weighted_sets = []
    for music_set in MUSIC_SETS:
        weight = music_set.get("probability_weight", 1)  # Default weight is 1 if not specified
        weighted_sets.extend([music_set] * weight)
    
    # Select randomly from the weighted list
    return random.choice(weighted_sets)

def select_weighted_music_set_from_list(music_sets_list):
    """
    Select a music set from a specific list based on weighted probability.
    """
    weighted_sets = []
    for music_set in music_sets_list:
        weight = music_set.get("probability_weight", 1)
        weighted_sets.extend([music_set] * weight)
    return random.choice(weighted_sets)

def select_weighted_scenario():
    scenarios = ["small"] * 80 + ["medium"] * 5 + ["large"] * 15
    return random.choice(scenarios)

def generate_run_config():
    # Mode configuration
    # Small mode: 3 images + 4 texts
    # Medium mode: 4 images + 4 texts (NOUVEAU)
    # Large mode: 9 images + 10 texts
    mode = select_weighted_scenario()
    
    if mode == "small":
        num_images = 3
        num_texts = 4
        text_sets = TEXT_SETS_SMALL
    elif mode == "medium":
        num_images = 4
        num_texts = 4
        text_sets = TEXT_SETS_MEDIUM
    else:  # large
        num_images = 9
        num_texts = 10
        text_sets = TEXT_SETS_LARGE
    
    # Select random elements for this run
    selected_text_set = random.choice(text_sets)
    selected_images = random.sample(ALL_POOF_IMAGES, num_images)
    
    # Filter music sets for medium scenario if needed
    if mode == "medium":
        available_music_sets = [ms for ms in MUSIC_SETS if ms.get("scenario") == "medium"]
        if available_music_sets:
            selected_music_set = select_weighted_music_set_from_list(available_music_sets)
        else:
            # Fallback to regular selection if no medium-specific sets exist
            selected_music_set = select_weighted_music_set()
    else:
        # For small and large modes, exclude medium-specific sets
        available_music_sets = [ms for ms in MUSIC_SETS if ms.get("scenario") != "medium"]
        selected_music_set = select_weighted_music_set_from_list(available_music_sets)
    
    # Select a title that matches the track
    selected_title = random.choice(selected_music_set["titles"])
    
    # Select a random description that matches the selected music
    selected_description = random.choice(selected_music_set["descriptions"])
    
    # Select 5 random hashtags
    selected_hashtags = random.sample(HASHTAGS, 5)
    
    # Get the emoji that matches the selected music set
    emoji_options = selected_music_set["emoji"]
    if isinstance(emoji_options, list):
        selected_emoji = random.choice(emoji_options)
    else:
        selected_emoji = emoji_options
    
    # Random number of emoji clicks (between 10 and 20)
    emoji_clicks = random.randint(10, 20)
    
    # Combine selected elements to create the full media set for this post
    if mode == "medium":
        # Mode MEDIUM : seulement images + sound (pas de spotify)
        combined_media_set = selected_images + [selected_music_set["sound"]]
    else:
        # Modes SMALL et LARGE : images + spotify + sound
        combined_media_set = selected_images + [selected_music_set["spotify"], selected_music_set["sound"]]
    
    return {
        "mode": mode,
        "num_images": num_images,
        "num_texts": num_texts,
        "selected_text_set": selected_text_set,
        "selected_images": selected_images,
        "selected_music_set": selected_music_set,
        "selected_title": selected_title,
        "selected_description": selected_description,
        "selected_hashtags": selected_hashtags,
        "selected_emoji": selected_emoji,
        "emoji_clicks": emoji_clicks,
        "combined_media_set": combined_media_set
    }