from lark import Lark

spoiler_grammar = """
   start : headed_section+

   headed_section: SEPERATOR section
   SEPERATOR: /\-+/
   section: initial | kis | quests | characters | objectives | bosses | treasure | shops | fusoya | misc | starterkit

   initial: "VERSION: " version "FLAGS: " flags "BINFLAGS: " binflags
   version: "v" DIGIT "." DIGIT "." DIGIT 
   flags: flagbag+ tagbag*
   flagbag: flag value option*
   flag: UCASE_LETTER
   value: WORD | INT ":" CNAME
   option: "/" optiontext
   optiontext: WORD | WORD ":" INT | WORD ":" WORD | WORD ":" INT "," WORD
   tagbag: "-" tags
   tags: WORD | WORD ":" WORD
   binflags: CNAME
   dots.10: "." "."+ 

   kis: "KEY ITEM LOCATIONS (and Pass if Pkey)" kiline+
   kiline: ki dots itemslot 
   ki: "Package" | "SandRuby" | "Baron Key" | "TwinHarp" | "Earth Crystal" | "Magma Key" | "Tower Key" | "Hook" | "Luca Key" | "Darkness Crystal" | "Rat Tail" | "Pan" | "Crystal" | "Legend Sword" | "Adamant" | "Spoon" | "Pink Tail" | "Pass"    
   itemslot: REGION location ["(" slotdesc "slot)"]
   location: LOCTERM | "altar" DIGIT | "pillar chest" DIGIT
   LOCTERM: "item" | "chest item" | "queen item" | "king item" | "destruction item" | "completion" | "reward item" | "trade item" 
   REGION: "Agart" | "Found Yang" | "Lower Bab-il" | "Lunar Subterrane" | "Town of Monsters" | "Antlion Nest" | "Starting" | "Super Cannon" | "Baron Castle" | "Dwarf Castle/Luca" | "Objective" | "Baron Inn" | "Defend Fabul" | "Sealed Cave" | "Baron Basement" | "Cave Magnes" | "Zot" | "Pan" | "Rat Tail" | "D.Mist/Rydia's Mom" | "Wake Yang" | "Cave Bahamut" | "Pink Tail" | "Mist/Package" | "Watery Pass" | "Damcyan" | "Kaipo/SandRuby" | "Mt. Hobs" | "Mysidia" | "Dwarf Castle" | "Lunar Palace" | "Giant of Bab-il" | "Antlion Cave" | "Baron Chocobo Forest" | "Baron Town" | "Black Chocobo Forest" | "Cave Eblana" | "Cave Eblan" | "Eblan Castle" | "Fabul Chocobo Forest" | "Fabul" | "Island Chocobo Forest" | "Kaipo" | "Kokkol's House" | "Land of Monsters" | "Lunar Path" | "Mist Cave" | "Mist Village" | "Mt. Ordeals Chocobo Forest" | "Mt. Ordeals" | "Old Water-way" | "Silvera" | "Sylvan Cave" | "Tomra" | "Toroia Castle" | "Toroia South Chocobo Forest" | "Toroia Town" | "Tower of Bab-il (lower)" | "Tower of Bab-il (upper)" | "Tower of Zot" | "Waterfall" | "Baron" | "Mist" | "Toroia" | "Feymarch" | "Smithy" | "Moon"
   slotdesc: "Pan" | "Tower Key" | "White Spear" | "Asura" | "Ribbon" | "Odin" | "Spoon" | "Sylph" | "Levia" | "Murasame" | "Crystal Sword" | "Masamune"
   
   quests: "QUEST REWARDS" questline+
   questline: itemslot dots (ki | item)

   characters: "CHARACTERS" charline+
   charline: REGION "character" [DIGIT] dots character
   character: WORD

   objectives: "OBJECTIVES" objectiveline+
   objectiveline: INT "." objective
   objective: WORD+

   bosses: "BOSSES" bossline+
   bossline: bosspos dots BOSS
   bosspos: BOSS "position" | "(not available)"
   BOSS: "D.Mist" | "Kaipo Officer/Soldiers" | "Octomamm" | "Antlion" | "MomBomb" | "Fabul gauntlet" | "Milon Z." | "Milon" | "D.Knight" | "Karate" | "Baron Inn Guards" | "Baigan" | "Kainazzo" | "Dark Elf (dragon)" | "Magus Sisters" | "Valvalis" | "Calbrena" | "Golbez" | "Lugae" | "Dark Imps" | "King/Queen Eblan" | "Rubicant" | "EvilWall" | "Asura" | "Leviatan" | "Odin" | "Bahamut" | "Elements" | "CPU" | "Pale Dim" | "Wyvern" | "Plague" | "D.Lunars" | "Ogopogo" | "WaterHag"

   treasure: "TREASURE" treasureloc+
   treasureloc: [REGION dots] item dots [MAP] "-" DETAIL [dots fight]
   item: "(nothing)" | INT "gp" | "Fire Claw" | "Ice Claw" | "Thunder Claw" | "Charm Claw" | "Poison Claw" | "Cat Claw" | "Rod" | "Ice Rod" | "Flame Rod" | "Thunder Rod" | "Change Rod" | "Charm Rod" | "Stardust Rod" | "Lilith Rod" | "Staff" | "Cure Staff" | "Silver Staff" | "Power Staff" | "Lunar Staff" | "Life Staff" | "Silence Staff" | "Shadow Sword" | "Darkness Sword" | "Black Sword" | "Light Sword" | "Excalibur" | "Fire Sword" | "Ice Brand" | "Defense Sword" | "Drain Sword" | "Ancient Sword" | "Slumber Sword" | "Spear" | "Wind Spear" | "Flame Spear" | "Blizzard Spear" | "Dragoon Spear" | "White Spear" | "Drain Spear" | "Gungnir" | "Short Katana" | "Middle Katana" | "Long Katana" | "Ninja Sword" | "Murasame" | "Masamune" | "Assassin Dagger" | "Mute Dagger" | "Whip" | "Chain Whip" | "Blitz Whip" | "Flame Whip" | "Dragon Whip" | "Hand Axe" | "Dwarf Axe" | "Ogre Axe" | "Silver Dagger" | "Dancing Dagger" | "Silver Sword" | "Crystal Sword" | "Shuriken" | "Ninja Star" | "Boomerang" | "Full Moon" | "Dreamer Harp" | "Charm Harp" | "Poison Axe" | "Rune Axe" | "Silver Hammer" | "Earth Hammer" | "Wooden Hammer" | "Avenger" | "Short Bow" | "Cross Bow" | "Great Bow" | "Archer Bow" | "Elven Bow" | "Samurai Bow" | "Artemis Bow" | "Iron Arrows" | "White Arrows" | "Fire Arrows" | "Ice Arrows" | "Lit Arrows" | "Darkness Arrows" | "Poison Arrows" | "Mute Arrows" | "Charm Arrows" | "Samurai Arrows" | "Medusa Arrows" | "Artemis Arrows" | "Iron Shield" | "Shadow Shield" | "Black Shield" | "Paladin Shield" | "Silver Shield" | "Fire Shield" | "Ice Shield" | "Diamond Shield" | "Aegis Shield" | "Samurai Shield" | "Dragoon Shield" | "Crystal Shield" | "Iron Helm" | "Shadow Helm" | "Darkness Helm" | "Black Helm" | "Paladin Helm" | "Silver Helm" | "Diamond Helm" | "Samurai Helm" | "Dragoon Helm" | "Crystal Helm" | "Cap" | "Leather Hat" | "Gaea Hat" | "Wizard Hat" | "Tiara" | "Ribbon" | "Headband" | "Bandanna" | "Ninja Mask" | "Glass Mask" | "Iron Armor" | "Shadow Armor" | "Darkness Armor" | "Black Armor" | "Paladin Armor" | "Silver Armor" | "Fire Armor" | "Ice Armor" | "Diamond Armor" | "Samurai Armor" | "Dragoon Armor" | "Crystal Armor" | "Cloth Armor" | "Leather Armor" | "Gaea Robe" | "Wizard Robe" | "Black Shirt" | "Sorcerer Robe" | "White Shirt" | "Power Shirt" | "Heroine Armor" | "Prisoner Clothes" | "Bard Tunic" | "Karate Gi" | "Black Belt" | "Adamant Armor" | "Ninja Shirt" | "Iron Gauntlet" | "Shadow Gauntlet" | "Darkness Gauntlet" | "Black Gauntlet" | "Paladin Gauntlet" | "Silver Gauntlet" | "Diamond Gauntlet" | "Zeus Gauntlet" | "Samurai Gauntlet" | "Dragoon Gauntlet" | "Crystal Gauntlet" | "Iron Ring" | "Ruby Ring" | "Silver Ring" | "Strength Ring" | "Rune Ring" | "Crystal Ring" | "Diamond Ring" | "Protect Ring" | "Cursed Ring" | "Bomb" | "BigBomb" | "Notus" | "Boreas" | "ThorRage" | "ZeusRage" | "Stardust" | "Succubus" | "Vampire" | "Bacchus" | "Hermes" | "HrGlass1" | "HrGlass2" | "HrGlass3" | "SilkWeb" | "Illusion" | "FireBomb" | "Blizzard" | "Lit-Bolt" | "StarVeil" | "Kamikaze" | "MoonVeil" | "MuteBell" | "GaiaDrum" | "Coffin" | "Grimoire" | "Bestiary" | "Alarm" | "Unihorn" | "Cure1" | "Cure2" | "Cure3" | "Ether1" | "Ether2" | "Elixir" | "Life" | "Soft" | "MaidKiss" | "Mallet" | "DietFood" | "EchoNote" | "Eyedrops" | "Antidote" | "Cross" | "Heal" | "Siren" | "AuApple" | "AgApple" | "SomaDrop" | "Tent" | "Cabin" | "EagleEye" | "Exit" | "Sylph Summon" | "Odin Summon" | "Whistle" | "Asura Summon" | "Baham Summon" | "Carrot" | "Levia Summon"

   fight: "(trap:" TRAPENCOUNTER ")"

   DETAIL: "west room, top" | "west room, bottom" | "west pot" | "west end, right" | "west end, left" | "west cell" | "west" | "weapon" | "water, top" | "water, bottom" | "treasury, right" | "treasury, middle" | "treasury, left" | "top-left pot" | "top row, right" | "top row, middle" | "top row, left" | "top row, 9" | "top row, 8" | "top row, 7" | "top row, 6" | "top row, 5" | "top row, 4" | "top row, 3" | "top row, 2" | "top row, 1" | "top right pot" | "top right chest" | "top right" | "top pot" | "top middle chest" | "top middle" | "top left, through secret path" | "top left chest" | "top left" | "top chest" | "top center-left" | "top" | "tiara room" | "through secret path" | "through northeast secret path" | "square chamber, top right" | "square chamber, top left" | "square chamber, bottom right" | "square chamber, bottom left" | "southwest room, through secret path, right" | "southwest room, through secret path, middle" | "southwest room, through secret path, left" | "southwest entrance" | "southwest" | "southeast corner, right" | "southeast corner, middle" | "southeast corner, left" | "south room chest" | "south grass, right" | "south grass, left" | "south grass" | "shelf" | "secret path second chamber, top" | "secret path second chamber, left" | "secret path first chamber" | "secret path chest" | "rightmost" | "right, through secret path" | "right top chest" | "right side, top chest" | "right side, top" | "right side, bottom chest" | "right side, bottom" | "right right" | "right pot" | "right of entrance" | "right chest" | "right cell, right" | "right cell, left" | "right bottom chest" | "right" | "pot outside Rosa's" | "pot outside inn" | "pot" | "pit chamber, top left" | "pit chamber, right" | "pit chamber, middle" | "pit chamber, bottom right" | "pit chamber, bottom left" | "on bridge to hidden altar" | "northwest exit" | "northeast, top" | "northeast, bottom" | "northeast room chest" | "northeast grass" | "northeast chamber, top" | "northeast chamber, right" | "north room, through secret path" | "north grass" | "north entrance, secret path, top" | "north entrance, secret path, bottom" | "north entrance, right top" | "north entrance, right bottom" | "north entrance, left" | "middle-right cell, right" | "middle-right cell, left" | "middle-left cell, right" | "middle-left cell, left" | "middle right" | "middle left" | "middle chest" | "middle cell, right" | "middle cell, left" | "middle" | "leftmost chest" | "leftmost" | "left, top" | "left, bottom" | "left top" | "left side, top chest" | "left side, bottom chest" | "left pot" | "left of entrance" | "left chest" | "left cell, right" | "left cell, left" | "left bottom" | "left" | "hidden chest" | "grass, top right" | "grass, top" | "grass, left" | "grass, bottom right" | "grass, bottom left" | "grass, bottom" | "grass" | "en route to altar" | "east side, top" | "east side, bottom" | "east room, top" | "east room, bottom-right" | "east room, bottom-left" | "east room chest" | "east left room chest" | "east grass" | "crawlspace, top right" | "crawlspace, top left" | "crawlspace, bottom right" | "chest (U bridge)" | "chest (ring bridge)" | "chest (long bridge)" | "chest (left of crystal room entrance)" | "chest" | "chest" | "center-right" | "center-left" | "center right" | "center" | "by hidden bridge" | "bridge chest" | "bottom, through secret path" | "bottom-right pot" | "bottom row, 9" | "bottom row, 8" | "bottom row, 7" | "bottom row, 6" | "bottom row, 5" | "bottom row, 4" | "bottom row, 3" | "bottom row, 2" | "bottom row, 1" | "bottom right pot" | "bottom right chest" | "bottom right" | "bottom middle chest" | "bottom middle" | "bottom left pot" | "bottom left chest" | "bottom left" | "bottom chest" | "bottom" | "armor" | "through secret path"

   MAP: "West tower 3F" | "West tower 2F" | "West tower 1F" | "Weapon/armor shop" | "Treasury entrance" | "Treasury" | "Treasure platform" | "Trapdoor landing" | "Torch room" | "Throne room" | "Summit" | "Stomach" | "Save Room" | "Save room" | "Save area" | "Rydia's house" | "Rosa's house" | "Poison treasury" | "Pit room" | "Passage to exit (\\\"B2F\\\")" | "Passage" | "Pass to Bab-il (north connection)" | "Pass to Bab-il (east half)" | "Lake" | "Inn" | "House" | "Exterior" | "Exit (\\\"North\\\")" | "Exit" | "Entrance (\\\"South\\\")" | "East wing pot room" | "East tower 3F (king's bedroom)" | "East tower 3F" | "East tower 2F" | "East tower 1F" | "East tower 1F" | "East hall treasury" | "Core B3" | "Core B2" | "Core B1" | "Chest" | "Camp level (\\\"B2F\\\")" | "Box room" | "Behind waterfall" | "Basement" | "B5 to B6 passage" | "B5 (through first interior passage south exit)" | "B5 (second interior passage)" | "B5 (PinkPuff room)" | "B5 (main route)" | "B5 (first interior passage)" | "B4F (first area)" | "B4F" | "B4 (west room)" | "B4 (interior passage)" | "B4" | "B3F to B4F passage" | "B3F (path to house)" | "B3F (northeast area)" | "B3F" | "B2F,(north side, second door from right)" | "B2F to B3F passage" | "B2F (tunnel)" | "B2F (north side, third door from right)" | "B2F (north side, leftmost door)" | "B2F (east half)" | "B2F (west half)" | "B2F" | "B2 (route to altar)" | "B1F to B2F passage" | "B1F (southeast room)" | "B1F (save area)" | "B1F (northwest area)" | "B1F (Fat Chocobo)" | "B1F (entry area)"| "B1F" | "5F (through 4F center-left door)" | "5F (through 4F center door)" | "5F (through 4F center-right door)" | "5F" | "4F (through 3F southeast door)" | "3F (\\\"7th Station\\\")" | "3F" | "2F" | "1F" | "Treasure room" | "East tower B1" | "Access to Old Water-way" | "Hospital" | "Pass to Bab-il (west half)" | "B1" | "B2 (main route)" | "B3" | "B5F" | "B5" | "B6" | "East wing chest room" | "4F" | "7F" | "Falcon level"

   TRAPENCOUNTER: "Warrior x5" | "Warlock/Kary x3" | "Warlock x2/Kary x2" | "ToadLady/TinyToads" | "Staleman/Skulls" | "Staleman x2" | "RedGiant x2" | "Red D./Blue D." | "Red D. x2" | "Procyotes/Juclyotes" | "Molbol x2" | "Mad Ogre x4" | "Mad Ogre x3" | "Last Arm" | "Ghost x6" | "Ghost x6" | "Ghost x6" | "FlameDog" | "DarkTrees/Molbols" | "D.Fossil/Warlock" | "Centpede x2" | "BlackCats/Lamia" | "Behemoth" | "Behemoth" | "Behemoth" | "Alert (Stoneman)" | "Alert (Naga)" | "Alert (FlameDog)" | "Alert (Chimera)"

   shops: "SHOPS" shoploc+
   shoploc: shopline shopsubline*
   shopline: REGION SHOPTYPE dots shopsubline
   shopsubline: item
   SHOPTYPE: "Armor" | "Cafe Item" | "Item" | "Weapon/Armor" | "Weapon" | "Shop"

   fusoya: "FUSOYA SPELLS" fusoyainitial fusoyaline ~ 13
   fusoyainitial: "Initial spells" dots spell ("," spell) ~ 5
   fusoyaline: "Boss" INT dots spell "," spell "," spell
   spell: WORD ["-" DIGIT]

   misc: "MISC" misclines
   misclines: "Hobs spell" dots WORD
   
   starterkit: "STARTER KIT" kitlines+
   kitlines: amount dots item
   amount: INT

   WORD: CHAR+ 
   CHAR: "a".."z" | "A".."Z" | "0".."9" 

   %import common.DIGIT 
   %import common.UCASE_LETTER
   %import common.CNAME
   %import common.INT
   %import common.WS
   %ignore WS
"""


if __name__ == "__main__":
    spoiler_parser = Lark(spoiler_grammar, start="start")
    with open("40000spoilers/test00000.spoiler") as f:
        tree = spoiler_parser.parse(f.read())
        print(tree)
