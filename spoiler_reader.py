import lark
from lark import Lark
from lark.visitors import Interpreter
import data_types as types


spoiler_grammar = """
   start : headed_section+

   headed_section: SEPERATOR section
   SEPERATOR: /\-+/
   ?section: initial | kis | quests | characters | objectives | bosses | treasure | shops | fusoya | misc | starterkit

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
   kiline: KI dots itemslot
   KI: "Package" | "SandRuby" | "Baron Key" | "TwinHarp" | "Earth Crystal" | "Magma Key" | "Tower Key" | "Hook" | "Luca Key" | "Darkness Crystal" | "Rat Tail" | "Pan" | "Crystal" | "Legend Sword" | "Adamant" | "Spoon" | "Pink Tail" | "Pass"
   itemslot: REGION location ["(" slotdesc "slot)"]
   ?location: LOCTERM | altar | pillar
   altar: "altar" DIGIT
   pillar: "pillar chest" DIGIT
   LOCTERM: "item" | "chest item" | "queen item" | "king item" | "destruction item" | "completion" | "reward item" | "trade item"
   REGION: "Agart" | "Found Yang" | "Lower Bab-il" | "Lunar Subterrane" | "Town of Monsters" | "Antlion Nest" | "Starting" | "Super Cannon" | "Baron Castle" | "Dwarf Castle/Luca" | "Objective" | "Baron Inn" | "Defend Fabul" | "Sealed Cave" | "Baron Basement" | "Cave Magnes" | "Zot" | "Pan" | "Rat Tail" | "D.Mist/Rydia's Mom" | "Wake Yang" | "Cave Bahamut" | "Pink Tail" | "Mist/Package" | "Watery Pass" | "Damcyan" | "Kaipo/SandRuby" | "Mt. Hobs" | "Mysidia" | "Dwarf Castle" | "Lunar Palace" | "Giant of Bab-il" | "Antlion Cave" | "Baron Chocobo Forest" | "Baron Town" | "Black Chocobo Forest" | "Cave Eblana" | "Cave Eblan" | "Eblan Castle" | "Fabul Chocobo Forest" | "Fabul" | "Island Chocobo Forest" | "Kaipo" | "Kokkol's House" | "Land of Monsters" | "Lunar Path" | "Mist Cave" | "Mist Village" | "Mt. Ordeals Chocobo Forest" | "Mt. Ordeals" | "Old Water-way" | "Silvera" | "Sylvan Cave" | "Tomra" | "Toroia Castle" | "Toroia South Chocobo Forest" | "Toroia Town" | "Tower of Bab-il (lower)" | "Tower of Bab-il (upper)" | "Tower of Zot" | "Waterfall" | "Baron" | "Mist" | "Toroia" | "Feymarch" | "Smithy" | "Moon"
   slotdesc: "Pan" | "Tower Key" | "White Spear" | "Asura" | "Ribbon" | "Odin" | "Spoon" | "Sylph" | "Levia" | "Murasame" | "Crystal Sword" | "Masamune"

   quests: "QUEST REWARDS" questline+
   questline: itemslot dots (KI | ITEM)

   characters: "CHARACTERS" charline+
   charline: REGION "character" [DIGIT] dots CHARACTER
   CHARACTER: "Cecil" | "Rosa" | "Kain" | "Rydia" | "Palom" | "Porom" | "Tellah" | "Yang" | "Cid" | "Edge" | "FuSoYa" | "Edward"

   objectives: "OBJECTIVES" objectiveline+
   objectiveline: INT "." OBJECTIVE
   OBJECTIVE: "Have Kokkol forge Legend Sword with Adamant" | "Defeat the boss of the Mist Cave" | "Destroy the Super Cannon" | "Defend Fabul" | "Conquer the vanilla Ribbon room" | "Complete the Giant of Bab-il" | "Liberate Baron Castle" | "Defeat the Baron Castle basement throne" | "Open the Toroia treasury with the Earth Crystal" | "Drop the Magma Key into the Agart well" | "Launch the Falcon" | "Conquer the vanilla White Spear altar" | "Defeat the bosses of Dwarf Castle" | "Defeat the bosses of Baron Inn" | "Conquer the vanilla Murasame altar" | "Conquer the vanilla Masamune altar" | "Defeat the queen at the Town of Monsters" | "Defeat the king at the Town of Monsters" | "Cure the fever with the SandRuby" | "Complete Cave Magnes" | "Return the Pan to Yang's wife" | "Unlock the Sealed Cave" | "Raise the Big Whale" | "Complete Mt. Ordeals" | "Complete the Tower of Zot" | "Complete the Sealed Cave" | "Trade away the Pink Tail" | "Unlock the sewer with the Baron Key" | "Defeat the boss of Lower Bab-il" | "Unlock the Pass door in Toroia" | "Defeat the boss of the Waterfall" | "Wake Yang with the Pan" | "Burn village Mist with the Package" | "Complete Cave Bahamut" | "Rescue the hostage on Mt. Hobs" | "Break the Dark Elf's spell with the TwinHarp" | "Trade away the Rat Tail" | "Complete the Antlion Nest" | "Conquer the vanilla Crystal Sword altar"

   bosses: "BOSSES" bossline+
   bossline: bossspot dots BOSS
   bossspot: BOSS "position" | "(not available)"
   BOSS: "D.Mist" | "Kaipo Officer/Soldiers" | "Octomamm" | "Antlion" | "MomBomb" | "Fabul gauntlet" | "Milon Z." | "Milon" | "D.Knight" | "Karate" | "Baron Inn Guards" | "Baigan" | "Kainazzo" | "Dark Elf (dragon)" | "Magus Sisters" | "Valvalis" | "Calbrena" | "Golbez" | "Lugae" | "Dark Imps" | "King/Queen Eblan" | "Rubicant" | "EvilWall" | "Asura" | "Leviatan" | "Odin" | "Bahamut" | "Elements" | "CPU" | "Pale Dim" | "Wyvern" | "Plague" | "D.Lunars" | "Ogopogo" | "WaterHag"

   treasure: "TREASURE" treasureloc+
   treasureloc: REGION dots treasuresubloc+
   treasuresubloc: (ITEM | money) dots [MAP] "-" DETAIL [dots fight]
   ?money: INT "gp"
   ITEM: "(nothing)" | "Fire Claw" | "Ice Claw" | "Thunder Claw" | "Charm Claw" | "Poison Claw" | "Cat Claw" | "Rod" | "Ice Rod" | "Flame Rod" | "Thunder Rod" | "Change Rod" | "Charm Rod" | "Stardust Rod" | "Lilith Rod" | "Staff" | "Cure Staff" | "Silver Staff" | "Power Staff" | "Lunar Staff" | "Life Staff" | "Silence Staff" | "Shadow Sword" | "Darkness Sword" | "Black Sword" | "Light Sword" | "Excalibur" | "Fire Sword" | "Ice Brand" | "Defense Sword" | "Drain Sword" | "Ancient Sword" | "Slumber Sword" | "Spear" | "Wind Spear" | "Flame Spear" | "Blizzard Spear" | "Dragoon Spear" | "White Spear" | "Drain Spear" | "Gungnir" | "Short Katana" | "Middle Katana" | "Long Katana" | "Ninja Sword" | "Murasame" | "Masamune" | "Assassin Dagger" | "Mute Dagger" | "Whip" | "Chain Whip" | "Blitz Whip" | "Flame Whip" | "Dragon Whip" | "Hand Axe" | "Dwarf Axe" | "Ogre Axe" | "Silver Dagger" | "Dancing Dagger" | "Silver Sword" | "Crystal Sword" | "Shuriken" | "Ninja Star" | "Boomerang" | "Full Moon" | "Dreamer Harp" | "Charm Harp" | "Poison Axe" | "Rune Axe" | "Silver Hammer" | "Earth Hammer" | "Wooden Hammer" | "Avenger" | "Short Bow" | "Cross Bow" | "Great Bow" | "Archer Bow" | "Elven Bow" | "Samurai Bow" | "Artemis Bow" | "Iron Arrows" | "White Arrows" | "Fire Arrows" | "Ice Arrows" | "Lit Arrows" | "Darkness Arrows" | "Poison Arrows" | "Mute Arrows" | "Charm Arrows" | "Samurai Arrows" | "Medusa Arrows" | "Artemis Arrows" | "Iron Shield" | "Shadow Shield" | "Black Shield" | "Paladin Shield" | "Silver Shield" | "Fire Shield" | "Ice Shield" | "Diamond Shield" | "Aegis Shield" | "Samurai Shield" | "Dragoon Shield" | "Crystal Shield" | "Iron Helm" | "Shadow Helm" | "Darkness Helm" | "Black Helm" | "Paladin Helm" | "Silver Helm" | "Diamond Helm" | "Samurai Helm" | "Dragoon Helm" | "Crystal Helm" | "Cap" | "Leather Hat" | "Gaea Hat" | "Wizard Hat" | "Tiara" | "Ribbon" | "Headband" | "Bandanna" | "Ninja Mask" | "Glass Mask" | "Iron Armor" | "Shadow Armor" | "Darkness Armor" | "Black Armor" | "Paladin Armor" | "Silver Armor" | "Fire Armor" | "Ice Armor" | "Diamond Armor" | "Samurai Armor" | "Dragoon Armor" | "Crystal Armor" | "Cloth Armor" | "Leather Armor" | "Gaea Robe" | "Wizard Robe" | "Black Shirt" | "Sorcerer Robe" | "White Shirt" | "Power Shirt" | "Heroine Armor" | "Prisoner Clothes" | "Bard Tunic" | "Karate Gi" | "Black Belt" | "Adamant Armor" | "Ninja Shirt" | "Iron Gauntlet" | "Shadow Gauntlet" | "Darkness Gauntlet" | "Black Gauntlet" | "Paladin Gauntlet" | "Silver Gauntlet" | "Diamond Gauntlet" | "Zeus Gauntlet" | "Samurai Gauntlet" | "Dragoon Gauntlet" | "Crystal Gauntlet" | "Iron Ring" | "Ruby Ring" | "Silver Ring" | "Strength Ring" | "Rune Ring" | "Crystal Ring" | "Diamond Ring" | "Protect Ring" | "Cursed Ring" | "Bomb" | "BigBomb" | "Notus" | "Boreas" | "ThorRage" | "ZeusRage" | "Stardust" | "Succubus" | "Vampire" | "Bacchus" | "Hermes" | "HrGlass1" | "HrGlass2" | "HrGlass3" | "SilkWeb" | "Illusion" | "FireBomb" | "Blizzard" | "Lit-Bolt" | "StarVeil" | "Kamikaze" | "MoonVeil" | "MuteBell" | "GaiaDrum" | "Coffin" | "Grimoire" | "Bestiary" | "Alarm" | "Unihorn" | "Cure1" | "Cure2" | "Cure3" | "Ether1" | "Ether2" | "Elixir" | "Life" | "Soft" | "MaidKiss" | "Mallet" | "DietFood" | "EchoNote" | "Eyedrops" | "Antidote" | "Cross" | "Heal" | "Siren" | "AuApple" | "AgApple" | "SomaDrop" | "Tent" | "Cabin" | "EagleEye" | "Exit" | "Sylph Summon" | "Odin Summon" | "Whistle" | "Asura Summon" | "Baham Summon" | "Carrot" | "Levia Summon"

   ?fight: "(trap:" TRAPENCOUNTER ")"

   DETAIL: "west room, top" | "west room, bottom" | "west pot" | "west end, right" | "west end, left" | "west cell" | "west" | "weapon" | "water, top" | "water, bottom" | "treasury, right" | "treasury, middle" | "treasury, left" | "top-left pot" | "top row, right" | "top row, middle" | "top row, left" | "top row, 9" | "top row, 8" | "top row, 7" | "top row, 6" | "top row, 5" | "top row, 4" | "top row, 3" | "top row, 2" | "top row, 1" | "top right pot" | "top right chest" | "top right" | "top pot" | "top middle chest" | "top middle" | "top left, through secret path" | "top left chest" | "top left" | "top chest" | "top center-left" | "top" | "tiara room" | "through secret path" | "through northeast secret path" | "square chamber, top right" | "square chamber, top left" | "square chamber, bottom right" | "square chamber, bottom left" | "southwest room, through secret path, right" | "southwest room, through secret path, middle" | "southwest room, through secret path, left" | "southwest entrance" | "southwest" | "southeast corner, right" | "southeast corner, middle" | "southeast corner, left" | "south room chest" | "south grass, right" | "south grass, left" | "south grass" | "shelf" | "secret path second chamber, top" | "secret path second chamber, left" | "secret path first chamber" | "secret path chest" | "rightmost" | "right, through secret path" | "right top chest" | "right side, top chest" | "right side, top" | "right side, bottom chest" | "right side, bottom" | "right right" | "right pot" | "right of entrance" | "right chest" | "right cell, right" | "right cell, left" | "right bottom chest" | "right" | "pot outside Rosa's" | "pot outside inn" | "pot" | "pit chamber, top left" | "pit chamber, right" | "pit chamber, middle" | "pit chamber, bottom right" | "pit chamber, bottom left" | "on bridge to hidden altar" | "northwest exit" | "northeast, top" | "northeast, bottom" | "northeast room chest" | "northeast grass" | "northeast chamber, top" | "northeast chamber, right" | "north room, through secret path" | "north grass" | "north entrance, secret path, top" | "north entrance, secret path, bottom" | "north entrance, right top" | "north entrance, right bottom" | "north entrance, left" | "middle-right cell, right" | "middle-right cell, left" | "middle-left cell, right" | "middle-left cell, left" | "middle right" | "middle left" | "middle chest" | "middle cell, right" | "middle cell, left" | "middle" | "leftmost chest" | "leftmost" | "left, top" | "left, bottom" | "left top" | "left side, top chest" | "left side, bottom chest" | "left pot" | "left of entrance" | "left chest" | "left cell, right" | "left cell, left" | "left bottom" | "left" | "hidden chest" | "grass, top right" | "grass, top" | "grass, left" | "grass, bottom right" | "grass, bottom left" | "grass, bottom" | "grass" | "en route to altar" | "east side, top" | "east side, bottom" | "east room, top" | "east room, bottom-right" | "east room, bottom-left" | "east room chest" | "east left room chest" | "east grass" | "crawlspace, top right" | "crawlspace, top left" | "crawlspace, bottom right" | "chest (U bridge)" | "chest (ring bridge)" | "chest (long bridge)" | "chest (left of crystal room entrance)" | "chest" | "chest" | "center-right" | "center-left" | "center right" | "center" | "by hidden bridge" | "bridge chest" | "bottom, through secret path" | "bottom-right pot" | "bottom row, 9" | "bottom row, 8" | "bottom row, 7" | "bottom row, 6" | "bottom row, 5" | "bottom row, 4" | "bottom row, 3" | "bottom row, 2" | "bottom row, 1" | "bottom right pot" | "bottom right chest" | "bottom right" | "bottom middle chest" | "bottom middle" | "bottom left pot" | "bottom left chest" | "bottom left" | "bottom chest" | "bottom" | "armor" | "through secret path"

   MAP: "West tower 3F" | "West tower 2F" | "West tower 1F" | "Weapon/armor shop" | "Treasury entrance" | "Treasury" | "Treasure platform" | "Trapdoor landing" | "Torch room" | "Throne room" | "Summit" | "Stomach" | "Save Room" | "Save room" | "Save area" | "Rydia's house" | "Rosa's house" | "Poison treasury" | "Pit room" | "Passage to exit (\\\"B2F\\\")" | "Passage" | "Pass to Bab-il (north connection)" | "Pass to Bab-il (east half)" | "Lake" | "Inn" | "House" | "Exterior" | "Exit (\\\"North\\\")" | "Exit" | "Entrance (\\\"South\\\")" | "East wing pot room" | "East tower 3F (king's bedroom)" | "East tower 3F" | "East tower 2F" | "East tower 1F" | "East tower 1F" | "East hall treasury" | "Core B3" | "Core B2" | "Core B1" | "Chest" | "Camp level (\\\"B2F\\\")" | "Box room" | "Behind waterfall" | "Basement" | "B5 to B6 passage" | "B5 (through first interior passage south exit)" | "B5 (second interior passage)" | "B5 (PinkPuff room)" | "B5 (main route)" | "B5 (first interior passage)" | "B4F (first area)" | "B4F" | "B4 (west room)" | "B4 (interior passage)" | "B4" | "B3F to B4F passage" | "B3F (path to house)" | "B3F (northeast area)" | "B3F" | "B2F,(north side, second door from right)" | "B2F to B3F passage" | "B2F (tunnel)" | "B2F (north side, third door from right)" | "B2F (north side, leftmost door)" | "B2F (east half)" | "B2F (west half)" | "B2F" | "B2 (route to altar)" | "B1F to B2F passage" | "B1F (southeast room)" | "B1F (save area)" | "B1F (northwest area)" | "B1F (Fat Chocobo)" | "B1F (entry area)"| "B1F" | "5F (through 4F center-left door)" | "5F (through 4F center door)" | "5F (through 4F center-right door)" | "5F" | "4F (through 3F southeast door)" | "3F (\\\"7th Station\\\")" | "3F" | "2F" | "1F" | "Treasure room" | "East tower B1" | "Access to Old Water-way" | "Hospital" | "Pass to Bab-il (west half)" | "B1" | "B2 (main route)" | "B3" | "B5F" | "B5" | "B6" | "East wing chest room" | "4F" | "7F" | "Falcon level"

   TRAPENCOUNTER: "Warrior x5" | "Warlock/Kary x3" | "Warlock x2/Kary x2" | "ToadLady/TinyToads" | "Staleman/Skulls" | "Staleman x2" | "RedGiant x2" | "Red D./Blue D." | "Red D. x2" | "Procyotes/Juclyotes" | "Molbol x2" | "Mad Ogre x4" | "Mad Ogre x3" | "Last Arm" | "Ghost x6" | "Ghost x6" | "Ghost x6" | "FlameDog" | "DarkTrees/Molbols" | "D.Fossil/Warlock" | "Centpede x2" | "BlackCats/Lamia" | "Behemoth" | "Behemoth" | "Behemoth" | "Alert (Stoneman)" | "Alert (Naga)" | "Alert (FlameDog)" | "Alert (Chimera)"

   shops: "SHOPS" shoploc+
   shoploc: shopline shopsubline+
   shopline: REGION SHOPTYPE dots 
   ?shopsubline: ITEM
   SHOPTYPE: "Armor" | "Cafe Item" | "Item" | "Weapon/Armor" | "Weapon" | "Shop"

   fusoya: "FUSOYA SPELLS" fusoyainitial fusoyaline ~ 13
   fusoyainitial: "Initial spells" dots spell ("," spell) ~ 5
   fusoyaline: "Boss" INT dots spell "," spell "," spell
   spell: WORD ["-" DIGIT]

   misc: "MISC" misclines
   misclines: "Hobs spell" dots WORD

   starterkit: "STARTER KIT" kitlines+
   kitlines: amount dots ITEM
   ?amount: INT

   WORD: CHAR+
   CHAR: "a".."z" | "A".."Z" | "0".."9" | "'" | "-" | "."

   %import common.DIGIT
   %import common.UCASE_LETTER
   %import common.CNAME
   %import common.INT
   %import common.WS
   %ignore WS
"""
class SpoilerHandling(Interpreter):
  def __init__(self, assignment, session):
      self.session = session
      self.assignment = self.accessOrCreate(types.Assignment, filename=assignment)

  def accessOrCreate(self, t, **kwargs):
      retval = self.session.query(t).filter_by(**kwargs).first()
      if not retval:
          retval = t(**kwargs)
          self.session.add(retval)
      return retval

  def start(self, tree):
      self.visit_children(tree)

  def headed_section(self, tree):
      self.visit_children(tree)

  def initial(self, tree):
      self.visit_children(tree)

  def kis(self, tree):
      self.visit_children(tree)

  def kiline(self, tree):
      ki = self.accessOrCreate(types.KeyItem, name=tree.children[0])
      islot = self.visit(tree.children[2])
      kiassignment = self.accessOrCreate(types.KeyItemAssignment, assignment=self.assignment, slot=islot, ki=ki)

  def itemslot(self, tree):
      region = self.accessOrCreate(types.Region, name=tree.children[0])
      if type(tree.children[1]) != lark.Token:
          locationText = self.visit(tree.children[1])
      else:
          locationText = tree.children[1]

      location = self.accessOrCreate(types.Location, name=locationText)
      islot = self.accessOrCreate(types.ItemSlot, region=region, location=location)
      return islot

  def altar(self, tree):
      return "altar " + tree.children[0]

  def pillar(self, tree):
      return "pillar " + tree.children[0]

  def quests(self, tree):
      self.visit_children(tree)

  def questline(self, tree):
      islot = self.visit(tree.children[0])
      item = None
      if tree.children[2].type == "ITEM":
          item = self.accessOrCreate(types.Item, name=tree.children[2])
      elif tree.children[1].type == "KI":
          ki = self.accessOrCreate(types.KeyItem, name=tree.children[2])
      kiassignment = self.accessOrCreate(types.KeyItemAssignment, assignment=self.assignment, slot=islot, item=item)

  def characters(self, tree):
      self.visit_children(tree)

  def charline(self, tree):
      # REGION DIGIT DOTS CHARACTER
      region = self.accessOrCreate(types.Region, name=tree.children[0])
      region_index = None
      if len(tree.children) > 3:
        region_index = tree.children[1]
      character = self.accessOrCreate(types.Character, name=tree.children[-1])
      charassignment = self.accessOrCreate(types.CharacterAssignment, assignment=self.assignment, region=region, region_index=region_index, character=character)

  def objectives(self, tree):
      self.visit_children(tree)

  def objectiveline(self, tree):
      assignment_id = tree.children[0]
      objective = self.accessOrCreate(types.Objective, name = tree.children[1])
      objectiveassignment = self.accessOrCreate(types.ObjectiveAssignment, assignment=self.assignment, assignment_id=assignment_id, objective=objective)

  def bosses(self, tree):
      self.visit_children(tree)
   
  def bossline(self, tree):
      boss_position = self.visit(tree.children[0])
      if not boss_position:
          return
      boss = self.accessOrCreate(types.Boss, name=tree.children[2])
      bossasssignment = self.accessOrCreate(types.BossAssignment, assignment=self.assignment, boss=boss, boss_position=boss_position)

  def bossspot(self, tree):
      retval = None
      if len(tree.children) > 0:
          retval = self.accessOrCreate(types.Boss, name=tree.children[0])
      return retval
  
  def treasure(self, tree):
      self.visit_children(tree)
  
  def treasureloc(self, tree):
       region = self.accessOrCreate(types.Region, name=tree.children[0])
       for value in tree.children[2:]:
           item, money, region_map, map_detail, fight = self.visit(value)
           treasureassignment = self.accessOrCreate(types.TreasureAssignment, assignment=self.assignment, region=region, item=item, money=money, region_map=region_map, map_detail=map_detail, fight=fight)
  
  def treasuresubloc(self, tree):
      item = None
      money = None
      region_map = None
      fight = None
      if tree.children[0].type == "ITEM":
          item = self.accessOrCreate(types.Item, name=tree.children[0])
      elif tree.children[0].type == "INT":
          money = self.accessOrCreate(types.MoneyAmount, money=tree.children[0])
      if tree.children[2].type == "MAP":
          region_map = self.accessOrCreate(types.Map, name=tree.children[2])
          map_detail = self.accessOrCreate(types.Detail, name=tree.children[3])
      else:
          map_detail = self.accessOrCreate(types.Detail, name=tree.children[2])
      if tree.children[-1].type == "TRAPENCOUNTER":
          fight = self.accessOrCreate(types.Fight, name=tree.children[-1])
      return (item, money, region_map, map_detail, fight)

  def shops(self, tree):
       self.visit_children(tree)

  def shoploc(self, tree):
       region, shoptype = self.visit(tree.children[0])
       for value in tree.children[2:]:
           item = self.accessOrCreate(types.Item, name=value)
           treasureassignment = self.accessOrCreate(types.ShopAssignment, assignment=self.assignment, region=region, shop=shoptype, item=item)

  def shopline(self, tree):
       region = self.accessOrCreate(types.Region, name=tree.children[0])
       shoptype = self.accessOrCreate(types.ShopType, name=tree.children[1])
       return (region, shoptype)

  def starterkit(self, tree):
       self.visit_children(tree)

  def kitlines(self, tree):
       amount = tree.children[0]
       item = self.accessOrCreate(types.Item, name=tree.children[2])
       self.accessOrCreate(types.StarterKitAssignment, assignment=self.assignment, amount=amount, item=item)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///data_final.db')
    types.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in range(0,40000):
        spoiler_parser = Lark(spoiler_grammar, start="start")
        filename = "40000spoilers/test{:0>5}.spoiler".format(i)
        with open(filename) as f:
            try:
                tree = spoiler_parser.parse(f.read())
                SpoilerHandling(assignment=filename, session=session).visit(tree)
                session.commit()
                print("Success: {}".format(i), flush=True)
            except Exception as e:
                print("Failure: {}{}".format(e,i), flush=True)
