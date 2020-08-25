import random
import copy
import math
random.seed()

statistics = []
single_run_statistics = {"Optional Spots In Pool": 0, "Optional Spots Chosen For KI": 0}

key_items = [
  "CRYSTAL",
  "DARKNESS",
  "MAGMAKEY",
  "HOOK",
  "RATTAIL",
  "TWINHARP",
  "PINKTAIL",
  "EARTH",
  "BARONKEY",
  "TOWERKEY",
  "LUCAKEY",
  "ADAMANT",
  "LEGEND",
  "SANDRUBY",
  "PACKAGE",
  "PAN",
  "SPOON",
  "PASS",
]

key_item_count = len(key_items) - 1

ki_key_to_desc = {
    "STARTING": "Receiving the starting item during the opening Baron Castle cutscene",
    "ANTLION": "Completing the Antlion's Nest",
    "FABUL":    "Defending Fabul",
    "ORDEALS": "Entering the mirror room atop Mt. Ordeals",
    "BARONINN":"Defeating the Baron Inn bosses",
    "BARON": "Liberating Baron Castle",
    "EDWARD":"Speaking to Edward in Toroia Castle*",
    "MAGNES": "Completing Cave Magnes",
    "ZOT": "Completing the Tower of Zot",
    "BABIL": "Defeating the boss of lower Bab-il",
    "CANNON": "Destroying the Super Cannon",
    "DWARF": "Defeating the Dwarf Castle bosses",
    "SEALED": "Completing the Sealed Cave",
    "FEYMARCH": "In the 'Rat Tail chest' in the Town of Summons",
    "SHEILA": "Speaking to Yang's wife after finding Yang in the Sylph Cave",
    "PAN":"Returning the Pan to Yang's wife after using it to wake him up",
    "ADAMANT":"Trading the Rat Tail in the Adamant Grotto",
    "SYLPH": "From the Sylphs when waking Yang in the Sylph Cave",
    "ASURA": "By defeating the queen of the Town of Monsters",
    "LEVIATAN": "By defeating the king of the Town of Monsters",
    "ODIN": "By defeating the ghost on the throne under Baron Castle",
    "BAHAMUT": "By completing Cave Bahamut",
    "MURASAME": 0,
    "CRYSTALSWORD": 0,
    "WHITESPEAR": 0,
    "RIBBONLEFT": 0,
    "RIBBONRIGHT": 0,
    "MASAMUNE": 0,
}

main_ki_positions = {
    "STARTING": 0,
    "ANTLION": 0,
    "FABUL": 0,
    "ORDEALS": 0,
    "BARONINN": 0,
    "BARON": 0,
    "EDWARD": 0,
    "MAGNES": 0,
    "ZOT": 0,
    "BABIL": 0,
    "CANNON": 0,
    "DWARF": 0,
    "SEALED": 0,
    "FEYMARCH": 0,
    "SHEILA": 0,
    "PAN": 0,
    "ADAMANT": 0,
}

ki_requirements = {
    "STARTING": set([]),
    "ANTLION": set([]),
    "FABUL": set([]),
    "ORDEALS": set([]),
    "BARONINN": set([]),
    "BARON": set(["BARONKEY"]),
    "EDWARD": set([]),
    "MAGNES": set(["TWINHARP"]),
    "ZOT": set(["EARTH"]),
    "BABIL": set(["MAGMAKEY"]),
    "CANNON": set(["MAGMAKEY", "TOWERKEY"]),
    "DWARF": set(["MAGMAKEY"]),
    "SEALED": set(["MAGMAKEY", "LUCAKEY"]),
    "FEYMARCH": set(["MAGMAKEY"]),
    "SHEILA": set(["MAGMAKEY"]),
    "PAN": set(["MAGMAKEY", "PAN"]),
    "ADAMANT": set(["HOOK", "ADAMANT"]),
    "SYLPH": set(["MAGMAKEY", "PAN"]),
    "ASURA": set(["MAGMAKEY"]),
    "LEVIATAN": set(["MAGMAKEY"]),
    "ODIN": set(["BARONKEY"]),
    "BAHAMUT": set(["DARKNESS"]),
    "MURASAME": set(["DARKNESS"]),
    "CRYSTALSWORD": set(["DARKNESS"]),
    "WHITESPEAR": set(["DARKNESS"]),
    "RIBBONLEFT": set(["DARKNESS"]),
    "RIBBONRIGHT": set(["DARKNESS"]),
    "MASAMUNE": set(["DARKNESS"]),
}

summon_ki_positions = {
    "SYLPH": 0,
    "ASURA": 0,
    "LEVIATAN":  0,
    "ODIN": 0,
    "BAHAMUT": 0,
}

moon_ki_positions = {
    "MURASAME": 0,
    "CRYSTALSWORD": 0,
    "WHITESPEAR": 0,
    "RIBBONLEFT": 0,
    "RIBBONRIGHT": 0,
    "MASAMUNE": 0,
}

pool = list(main_ki_positions.keys())

"""
    Start with the pool of main quest key item positions.
    If Ksummon and/or Kmoon are set,
        Randomly select half the slots made available by Ksummon and/or Kmoon, rounded up, and add them to the pool.
        Generate a random number N from 0…1.
        Determine the greatest integer K, where N < 1/(2^K).
        Add K more of the available summon/moon slots to the pool.
        Reserve the remaining unselected summon/moon slots.
    If Ktrap is set,
        For each dungeon containing trapped chests,
            Generate a random number N from 0…1.
            Determine the greatest integer K, where N < 1/(2^K).
            Select (K + 2) random trapped chests in the dungeon and add them to the pool (or all of them, if there are fewer than K + 2).
            Reserve the remaining unused trapped chests.
    Randomly assign key items among the slots in the pool.
    The remaining unassigned slots in the pool, as well as the reserved slots from the summon/moon/trap steps, will receive non-key-item rewards.
"""
for trials in range(1,100000):
    valid = False
    while valid == False:
        now_statistics = copy.copy(single_run_statistics)
        possible_extras = list(summon_ki_positions.keys()) + list(moon_ki_positions.keys())
        N = random.random()
        K = 0
        while (N < (1 / math.pow(2,(K+1)))) and (K < math.floor(len(possible_extras)/2)):
            K += 1
        K += min(math.ceil(len(possible_extras)/2), len(possible_extras))
        now_statistics["Optional Spots In Pool"] = K
        spots_chosen = random.sample(possible_extras, K)
        final_pool = pool + spots_chosen
        final_dict  = copy.copy(main_ki_positions)
        final_dict.update(summon_ki_positions)
        final_dict.update(moon_ki_positions)
        #print(final_pool)
        dependencies = {}
        key_item_number = 1
        selections = random.sample(final_pool, key_item_count)
        dependencies = {}
        valid = True
        for key in selections:
            final_dict[key] = key_items[key_item_number]
            dependencies[key_items[key_item_number]] = key
            key_item_number += 1

        #print(dependencies)
        #print(final_dict)

        collectable = set([])
        stop = False
        while not stop:
            starting_collectable = collectable.copy()
            for value in key_items:
                if value == "CRYSTAL":
                    continue
                can_get_ki = ki_requirements.get(dependencies.get(value, None), set([]))
                #print(value)
                #print(can_get_ki)
                if can_get_ki <= collectable:
                    collectable.add(value)
            #print(collectable)
            #print(starting_collectable)
            if len(starting_collectable) == len(collectable):
                stop = True

        if len(collectable) < key_item_count:
            valid = False
            #print("Failure")
            #print(final_dict)

    #print('.')
    for key in spots_chosen:
        if final_dict[key] != 0:
            now_statistics["Optional Spots Chosen For KI"] += 1

    statistics.append(now_statistics)

histogram = {"Spots in Pool": {}, "KIs in Spots": {}}
for trial in statistics:
    value = trial["Optional Spots In Pool"]
    histogram["Spots in Pool"][value] = histogram["Spots in Pool"].get(value, 0) + 1

    value = trial["Optional Spots Chosen For KI"]
    histogram["KIs in Spots"][value] = histogram["KIs in Spots"].get(value, 0) + 1

print(histogram)
