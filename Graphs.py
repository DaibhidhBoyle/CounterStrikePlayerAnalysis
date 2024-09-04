!pip install matplotlib
!pip install numpy
!pip install wordCloud

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

cs_matches = {
  "data": {
    "day1": {
      "date": "31-1-2024",
      "matches": [
        {
          "id": 1,
          "rank": 6,
          "captain": True,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 9
              },
              "finalScore": {
                "PlayerScore": 10,
                "EnemyScore": 13
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 2,
          "rank": 6,
          "captain": False,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 1
              },
              "finalScore": {
                "PlayerScore": 11,
                "EnemyScore": 5
              }
            },
            "win": True,
            "forfeit": True
          }
        },
        {
          "id": 3,
          "rank": 6,
          "captain": True,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 5,
                "EnemyScore": 2
              },
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 6
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 4,
          "rank": 6,
          "captain": True,
          "map": "Inferno",
          "matchData": {
            "firstSide": "TSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 4,
                "EnemyScore": 8
              },
              "ct_side": {
                "PlayerScore": 1,
                "EnemyScore": 5
              },
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },

    "day2": {
      "date": "02-2-2024",
      "matches": [
        {
          "id": 5,
          "rank": 6,
          "captain": False,
          "map": "nuke",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "t_side": {
                "PlayerScore": 2,
                "EnemyScore": 6
              },
              "ct_side": {
                "PlayerScore": 5,
                "EnemyScore": 7
              },
              "finalScore": {
                "PlayerScore": 7,
                "EnemyScore": 13
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 6,
          "rank": 6,
          "captain": True,
          "map": "mirage",
          "matchData": {
            "firstSide": "CTSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 3,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 10,
                "EnemyScore": 2
              },
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 4
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 7,
          "rank": 6,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "TSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              },
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 11
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 8,
          "rank": 6,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "t_side": {
                "PlayerScore": 3,
                "EnemyScore": 3
              },
              "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 10
              },
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 9,
          "rank": 6,
          "captain": False,
          "map": "Nuke",
          "matchData": None
        },
        {
          "id": 10,
          "rank": 6,
          "captain": True,
          "map": "Overpass",
          "matchData": {
            "firstSide": "TSIDE",
            "results": {
              "t_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              },
              "ct_side": {
                "PlayerScore": 7,
                "EnemyScore": 1
              },
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 7
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 11,
          "rank": 6,
          "captain": False,
          "map": "Inferno",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "t_side": {
                "PlayerScore": 5,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 0,
                "EnemyScore": 6
              },
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day3": {
      "date": "05-02-2024",
      "matches": [
        {
          "id": 12,
          "rank": 6,
          "captain": True,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 8,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 4,
                "EnemyScore": 8
              },
              "ct_side": {
                "PlayerScore": 4,
                "EnemyScore": 5
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 13,
          "rank": 6,
          "captain": True,
          "map": "Overpass",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 4,
                "EnemyScore": 8
              },
              "ct_side": {
                "PlayerScore": 1,
                "EnemyScore": 5
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day4": {
      "date": "06-02-2024",
      "matches": [
        {
          "id": 14,
          "rank": 6,
          "captain": False,
          "map": "nuke",
          "matchData": None
        },
        {
          "id": 15,
          "rank": 6,
          "captain": False,
          "map": "Inferno",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 11,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 16,
          "rank": 6,
          "captain": False,
          "map": "overpass",
          "matchData": None,
        },
        {
          "id": 17,
          "rank": 6,
          "captain": False,
          "map": "vertigo",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 16
              },
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 5,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day6": {
      "date": "16-02-2024",
      "matches": [
        {
          "id": 18,
          "rank": 5,
          "captain": True,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 4
              },
              "t_side": {
                "PlayerScore": 10,
                "EnemyScore": 2
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 2
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 19,
          "rank": 6,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 10,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              },
              "ct_side": {
                "PlayerScore": 4,
                "EnemyScore": 7
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day7": {
      "date": "17-02-2024",
      "matches": [
        {
          "id": 20,
          "rank": 5,
          "captain": False,
          "map": "anubis",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 6
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 1
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 21,
          "rank": 6,
          "captain": True,
          "map": "Overpass",
          "matchData": {
            "firstSide": "CTside",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 5
              },
              "t_side": {
                "PlayerScore": 4,
                "EnemyScore": 2
              },
              "ct_side": {
                "PlayerScore": 9,
                "EnemyScore": 3
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 22,
          "rank": 6,
          "captain": False,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "CTside",
            "results": {
              "finalScore": {
                "PlayerScore": 6,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 4,
                "EnemyScore": 3
              },
              "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 10
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 23,
          "rank": 6,
          "captain": False,
          "map": "Anubis",
          "matchData": None
        },
        {
          "id": 24,
          "rank": 6,
          "captain": False,
          "map": "Nuke",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 10,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              },
              "ct_side": {
                "PlayerScore": 4,
                "EnemyScore": 7
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day8": {
      "date": "20-02-2024",
      "matches": [
        {
          "id": 25,
          "rank": 6,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
                },
                "t_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
                },
                "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 4
                }
              },
            "win": False,
            "forfeit": False
            }
        },
        {
          "id": 26,
          "rank": 5,
          "captain": False,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 17,
                "EnemyScore": 19
              },
              "t_side": {
                "PlayerScore": 9,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 8,
                "EnemyScore": 12
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 27,
          "rank": 5,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 9
              },
              "t_side": {
                "PlayerScore": 5,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 8,
                "EnemyScore": 2
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 28,
          "rank": 5,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 6
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 1
              }
            },
            "win": True,
            "forfeit": False
          }
        }
      ]
    },
    "day9": {
      "date": "23-02-2024",
      "matches": [
        {
          "id": 29,
          "rank": 5,
          "captain": False,
          "map": "Ancient",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 4,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
              },
              "ct_side": {
                "PlayerScore": 1,
                "EnemyScore": 4
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 30,
          "rank": 6,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 9,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 7
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 31,
          "rank": 5,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 7
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 2
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 32,
          "rank": 6,
          "captain": True,
          "map": "Nuke",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "finalScore": {
                "PlayerScore": 11,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 33,
          "rank": 5,
          "captain": True,
          "map": "Overpass",
          "matchData": {
            "firstSide": "Tside",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 3
              },
              "t_side": {
                "PlayerScore": 9,
                "EnemyScore": 3
              },
              "ct_side": {
                "PlayerScore": 4,
                "EnemyScore": 0
              }
            },
            "win": True,
            "forfeit": False
          }
        }
      ]
    },
    "day10": {
      "date": "26-02-2024",
      "matches": [
        {
          "id": 34,
          "rank": 6,
          "captain": False,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 5,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
              },
              "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 4
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 35,
          "rank": 5,
          "captain": False,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 17,
                "EnemyScore": 19
              },
              "t_side": {
                "PlayerScore": 10,
                "EnemyScore": 8
              },
              "ct_side": {
                "PlayerScore": 7,
                "EnemyScore": 11
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 36,
          "rank": 5,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 9
              },
              "t_side": {
                "PlayerScore": 5,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 8,
                "EnemyScore": 2
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 37,
          "rank": 5,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 6
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 1
              }
            },
            "win": True,
            "forfeit": False
          }
        }
      ]
    },

    "day11": {
      "date": "27-02-2024",
      "matches": [
        {
          "id": 38,
          "rank": 6,
          "captain": False,
          "map": "Anubis",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 10,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 2,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 39,
          "rank": 5,
          "captain": True,
          "map": "Overpass",
          "matchData": None
        },
        {
          "id": 40,
          "rank": 5,
          "captain": False,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "finalScore": {
                "PlayerScore": 11,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 5
              },
              "ct_side": {
                "PlayerScore": 4,
                "EnemyScore": 8
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    },
    "day12": {
      "date": "01-03-2024",
      "matches": [
        {
          "id": 41,
          "rank": 5,
          "captain": True,
          "map": "Anubis",
          "matchData": None
        },
        {
          "id": 42,
          "rank": 5,
          "captain": False,
          "map": "Ancient",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "finalScore": {
                "PlayerScore": 8,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 2,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 6
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 43,
          "rank": 5,
          "captain": True,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 12,
                "EnemyScore": 12
              },
              "t_side": {
                "PlayerScore": 6,
                "EnemyScore": 12
              },
              "ct_side": {
                "PlayerScore": 13,
                "EnemyScore": 4
              }
            },
            "win": True,
            "forfeit": False
          }
        }
      ]
    },
    "day13": {
      "date": "04-03-2024",
      "matches": [
        {
          "id": 44,
          "rank": 5,
          "captain": False,
          "map": "Inferno",
          "matchData": None
        },
        {
          "id": 45,
          "rank": 5,
          "captain": True,
          "map": "Anubis",
          "matchData": {
            "firstSide": "CTSide",
            "results": {
              "finalScore": {
                "PlayerScore": 6,
                "EnemyScore": 12
              },
              "t_side": {
                "PlayerScore": 5,
                "EnemyScore": 1
              },
              "ct_side": {
                "PlayerScore": 1,
                "EnemyScore": 11
              }
            },
            "win": True,
            "forfeit": False
          }
        },
        {
          "id": 46,
          "rank": 5,
          "captain": True,
          "map": "Ancient",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 11,
                "EnemyScore": 13
              },
              "t_side": {
                "PlayerScore": 8,
                "EnemyScore": 4
              },
              "ct_side": {
                "PlayerScore": 3,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        },
        {
          "id": 47,
          "rank": 5,
          "captain": False,
          "map": "Vertigo",
          "matchData": {
            "firstSide": "TSide",
            "results": {
              "finalScore": {
                "PlayerScore": 13,
                "EnemyScore": 16
              },
              "t_side": {
                "PlayerScore": 7,
                "EnemyScore": 7
              },
              "ct_side": {
                "PlayerScore": 6,
                "EnemyScore": 9
              }
            },
            "win": False,
            "forfeit": False
          }
        }
      ]
    }
  }
}


colors = {
    'vertigo': 'cyan', 'ancient': 'forestgreen', 'inferno': 'red',
    'nuke': 'grey', 'mirage': 'salmon', 'anubis': 'darkgoldenrod', 'overpass': 'violet'
}

map_names = {'ancient', 'nuke', 'anubis', 'overpass', 'mirage', 'vertigo', 'inferno'}

map_order = ['ancient', 'nuke', 'anubis', 'overpass', 'mirage', 'vertigo', 'inferno']


def frequency_of_map(cs_matches):
  map_frequency = {}
  for day in cs_matches["data"].values():
    for match in day["matches"]:
      map_name = match["map"].lower()
      if map_name in map_frequency:
        map_frequency[map_name] += 1
      else:
        map_frequency[map_name] = 1
  return map_frequency


def clean_and_analyze_cs_matches(cs_matches):
  cleaned_cs_matches = {'data': {}}

  for day_key, day_data in cs_matches["data"].items():
    cleaned_matches = []
    for match in day_data["matches"]:
      if match.get("matchData") is not None:
        cleaned_matches.append(match)

    cleaned_cs_matches['data'][day_key] = {
      "date": day_data["date"],
      "matches": cleaned_matches
    }

  cleaned_data_map_frequency = frequency_of_map(cleaned_cs_matches)

  return cleaned_cs_matches, cleaned_data_map_frequency

def calculate_wins_losses(cleaned_cs_matches):
  wins = 0
  losses = 0

  for day_data in cleaned_cs_matches["data"].values():
    for match in day_data["matches"]:
      if match.get("matchData"):
        if match["matchData"]["win"]:
          wins += 1
        else:
          losses += 1

  return wins, losses


def frequency_as_wordcloud_with_colors(data, colors, title):
  wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=lambda *args, **kwargs: colors.get(args[0], 'black')).generate_from_frequencies(data)

  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')

  plt.title(title, fontsize=20, pad=20)

  plt.show()

def plot_map_frequency(data_dict, colors, title, xlabel, ylabel):
  map_names = [map_name for map_name in map_order]
  frequencies = [data_dict.get(map_name, 0) for map_name in
                   map_order]

  plt.bar(map_names, frequencies, color=[colors[map_name] for map_name in map_names])

  plt.ylim(bottom=0.5)

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)

  plt.xticks(rotation=45, ha='right')

  plt.show()

def create_side_by_side_bar_chart(
        item_order,
        category1_counts,
        category2_counts,
        xlabel,
        ylabel,
        title,
        label1,
        label2,
        color1='goldenrod',
        color2='darkred',
        secondary_data=None,
        secondary_label=None,
        secondary_color='blue'
  ):

  fig, ax1 = plt.subplots()

  x = range(len(item_order))
  width = 0.35

  ax1.bar(x, category1_counts, width, label=label1, color=color1)
  ax1.bar([i + width for i in x], category2_counts, width, label=label2, color=color2)

  ax1.set_xlabel(xlabel)
  ax1.set_ylabel(ylabel)
  ax1.set_title(title)
  ax1.set_xticks([i + width / 2 for i in x])
  ax1.set_xticklabels(item_order)
  ax1.legend(loc='upper left')

  if secondary_data and secondary_label:
    plot_secondary_data(ax1, item_order, width, secondary_data, secondary_label, secondary_color)

  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()


def plot_secondary_data(ax, item_order, width, secondary_data, secondary_label, secondary_color):
  ax2 = ax.twinx()
  ax2.set_ylabel(secondary_label)
  ax2.set_ylim(0, 100)

  for i, name in enumerate(item_order):
    ax2.plot(i + width / 2, secondary_data[name], marker='o', markersize=8, color=secondary_color)

def plot_side_by_side_bar_chart_by_map_side(item_order,
                                            category1_counts,
                                            category2_counts,
                                            xlabel,
                                            ylabel,
                                            title,
                                            label1,
                                            label2,
                                            colors,
                                            secondary_data,
                                            secondary_label,
                                            secondary_color):

    # Prepare data for plotting based on the specified item order
  fig, ax = plt.subplots()
  bar_width = 0.35

    # Debugging output to check values
  for i, map_name in enumerate(item_order):
    color = colors.get(map_name.lower(), 'grey')

    cat1_bar = category1_counts[i]
    cat2_bar = category2_counts[i]

    ax.bar(i - 0.05, cat1_bar, color=color, width=bar_width, alpha=0.7)
    ax.bar(i + bar_width + 0.05, cat2_bar, color=color, width=bar_width, alpha=0.7)

      # Customize the plot
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Create custom x-axis ticks and labels
  ax.set_xticks(np.arange(len(item_order)) + bar_width / 2)
  ax.set_xticklabels([f"{map_name} {label1}\n{map_name} {label2}" for map_name in item_order], rotation=45,
                       ha='right')

  if secondary_data and secondary_label:
    plot_secondary_data_by_map_side(ax, item_order, secondary_data, secondary_label, secondary_color, bar_width)

    ax2 = ax.twinx()
    ax2.set_ylabel(secondary_label)
    ax2.set_ylim(0, 100)

  plt.tight_layout()
  plt.show()


def plot_secondary_data_by_map_side(ax,
                                    item_order,
                                    secondary_data,
                                    secondary_color,
                                    bar_width):
  for i, map_name in enumerate(item_order):
    player_percentage_tside = secondary_data.get(map_name, {}).get('T_Side_Percentage', 0)
    player_percentage_ctside = secondary_data.get(map_name, {}).get('CT_Side_Percentage', 0)

    ax.scatter(i, player_percentage_tside, color=secondary_color, zorder=5)  # zorder ensures the dot is on top of bars
    ax.scatter(i + bar_width, player_percentage_ctside, color=secondary_color, zorder=5)



def plot_heatmap(map_frequency, title, cmap):

  sorted_maps = sorted(map_frequency.items(), key=lambda x: x[1], reverse=True)

  reordered_maps = []
  for i, (map_name, frequency) in enumerate(sorted_maps):

    if i % 2 == 0:
      reordered_maps.insert(0, (map_name, frequency))
    else:
      reordered_maps.append((map_name, frequency))

  custom_order = [map_name for map_name, _ in reordered_maps]

  heatmap_df = pd.DataFrame(index=custom_order, columns=['Frequency'])
  heatmap_df.index.name = 'Map'

  for map_name in custom_order:
    frequency = map_frequency.get(map_name, 0)
    heatmap_df.at[map_name, 'Frequency'] = frequency

  plt.figure(figsize=(10, 6))
  sns.heatmap(heatmap_df.astype(int), cmap=cmap, annot=True, fmt="d", linewidths=.5)
  plt.title(title)
  plt.ylabel('Map')
  plt.show()







