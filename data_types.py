from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(Base):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True)
    filename = Column(String(50), nullable=False, unique=True)

class KeyItem(Base):
    __tablename__ = 'key_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

class ItemSlot(Base):
    __tablename__ = "item_slot"
    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey("region.id"), nullable=False)
    region = relationship(Region, primaryjoin=region_id == Region.id)
    location_id = Column(Integer, ForeignKey("location.id"), nullable=False)
    location = relationship(Location, primaryjoin=location_id == Location.id)

    def __repr__(self):
        return self.region.name + " " + self.location.name

class KeyItemAssignment(Base):
    __tablename__ = "key_item_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    slot_id = Column(Integer, ForeignKey("item_slot.id"), nullable=False)
    slot = relationship(ItemSlot, primaryjoin=slot_id == ItemSlot.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"))
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)
    item_id = Column(Integer, ForeignKey("item.id"))
    item = relationship(Item, primaryjoin=item_id == Item.id)


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(6), nullable=False, unique=True)

class CharacterAssignment(Base):
    __tablename__ = "character_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"))
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    region_id = Column(Integer, ForeignKey("region.id"))
    region = relationship(Region, primaryjoin=region_id == Region.id)
    region_index = Column(Integer)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship(Character, primaryjoin=character_id == Character.id)

class Objective(Base):
    __tablename__ = "objective"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)

class ObjectiveAssignment(Base):
    __tablename__ = "objective_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    objective_id = Column(Integer, ForeignKey("objective.id"), nullable=False)
    objective = relationship(Objective, primaryjoin=objective_id == Objective.id)


class Boss(Base):
    __tablename__ = "boss"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

class BossAssignment(Base):
    __tablename__ = "boss_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    boss_id = Column(Integer, ForeignKey("boss.id"), nullable=False)
    boss = relationship(Boss, primaryjoin=boss_id == Boss.id)
    boss_position_id = Column(Integer, ForeignKey("boss.id"), nullable=False)
    boss_position = relationship(Boss, primaryjoin=boss_position_id == Boss.id)

class MoneyAmount(Base):
    __tablename__ = "money_amount"
    id = Column(Integer, primary_key=True)
    money = Column(Integer, nullable=False, unique=True)

class Map(Base):
    __tablename__ = "map"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

class Detail(Base):
    __tablename__ = "detail"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

class Fight(Base):
    __tablename__ = "fight"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

class TreasureAssignment(Base):
    __tablename__ = "treasure_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    region_id = Column(Integer, ForeignKey("region.id"), nullable=False)
    region = relationship(Region, primaryjoin=region_id == Region.id)
    item_id = Column(Integer, ForeignKey("item.id"))
    item = relationship(Item, primaryjoin=item_id == Item.id)
    money_id = Column(Integer, ForeignKey("money_amount.id"))
    money = relationship(MoneyAmount, primaryjoin=money_id == MoneyAmount.id)
    region_map_id = Column(Integer, ForeignKey("map.id"))
    region_map = relationship(Map, primaryjoin=region_map_id == Map.id)
    map_detail_id = Column(Integer, ForeignKey("detail.id"), nullable=False)
    map_detail = relationship(Detail, primaryjoin=map_detail_id == Detail.id)
    fight_id = Column(Integer, ForeignKey("fight.id"))
    fight = relationship(Fight, primaryjoin=fight_id == Fight.id)


class ShopType(Base):
    __tablename__ = "shop_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

class ShopAssignment(Base):
    __tablename__ = "shop_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    region_id = Column(Integer, ForeignKey("region.id"), nullable=False)
    region = relationship(Region, primaryjoin=region_id == Region.id)
    shoptype_id = Column(Integer, ForeignKey("shop_type.id"), nullable=False)
    shop = relationship(ShopType, primaryjoin=shoptype_id == ShopType.id)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    item = relationship(Item, primaryjoin=item_id == Item.id)

class StarterKitAssignment(Base):
    __tablename__ = "starter_kit_assignment"
    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignment.id"), nullable=False)
    assignment = relationship(Assignment, primaryjoin=assignment_id == Assignment.id)
    amount = Column(Integer, nullable=False)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    item = relationship(Item, primaryjoin=item_id == Item.id)

'''
# The stuff below is additional data to start building out requirements, sphere calculations, etc. Uncomment and run with the understanding it was never made a clean executable, but is closer to scripting

class SlotRequirementsAnd(Base):
    __tablename__ = "slot_requirements_and"
    id = Column(Integer, primary_key=True)
    slot_id = Column(Integer, ForeignKey("item_slot.id"), nullable=False)
    slot = relationship(ItemSlot, primaryjoin=slot_id == ItemSlot.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

class SlotRequirementsOr(Base):
    __tablename__ = "slot_requirements_or"
    id = Column(Integer, primary_key=True)
    slot_id = Column(Integer, ForeignKey("item_slot.id"), nullable=False)
    slot = relationship(ItemSlot, primaryjoin=slot_id == ItemSlot.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

class BossRequirementsAnd(Base):
    __tablename__ = "boss_requirements_and"
    id = Column(Integer, primary_key=True)
    boss_id = Column(Integer, ForeignKey("boss.id"), nullable=False)
    boss = relationship(Boss, primaryjoin=boss_id == Boss.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

class BossRequirementsOr(Base):
    __tablename__ = "boss_requirements_or"
    id = Column(Integer, primary_key=True)
    boss_id = Column(Integer, ForeignKey("boss.id"), nullable=False)
    boss = relationship(Boss, primaryjoin=boss_id == Boss.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

class ObjectiveRequirementsAnd(Base):
    __tablename__ = "objective_requirements_and"
    id = Column(Integer, primary_key=True)
    objective_id = Column(Integer, ForeignKey("objective.id"), nullable=False)
    objective = relationship(Objective, primaryjoin=objective_id == Objective.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

class ObjectiveRequirementsOr(Base):
    __tablename__ = "objective_requirements_or"
    id = Column(Integer, primary_key=True)
    objective_id = Column(Integer, ForeignKey("objective.id"), nullable=False)
    objective = relationship(Objective, primaryjoin=objective_id == Objective.id)
    key_item_id = Column(Integer, ForeignKey("key_item.id"), nullable=False)
    ki = relationship(KeyItem, primaryjoin=key_item_id == KeyItem.id)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.sql.expression import exists
    from sqlalchemy import and_
    engine = create_engine('postgresql+psycopg2://postgres:********@localhost/ff4fe_spoilers', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objective_requirements_and = [
        ["Have Kokkol forge Legend Sword with Adamant", "Legend Sword", "Adamant"],
        ["Destroy the Super Cannon", "Tower Key"],
        ["Conquer the vanilla White Spear altar", "Darkness Crystal"],
        ["Trade away the Pink Tail", "Hook", "Pink Tail"],
        ["Trade away the Rat Tail", "Hook", "Rat Tail"],
        ["Drop the Magma Key into the Agart well", "Magma Key"],
        ["Raise the Big Whale", "Darkness Crystal"],
        ["Conquer the vanilla Ribbon room", "Darkness Crystal"],
        ["Unlock the Sealed Cave", "Luca Key"],
        ["Complete the Sealed Cave", "Luca Key"],
        ["Launch the Falcon", "Luca Key"],
        ["Wake Yang with the Pan", "Pan"],
        ["Return the Pan to Yang's wife", "Pan"],
        ["Complete Cave Magnes", "TwinHarp"],
        ["Break the Dark Elf's spell with the TwinHarp", "TwinHarp"],
        ["Cure the fever with the SandRuby", "SandRuby"],
        ["Conquer the vanilla Murasame altar", "Darkness Crystal"],
        ["Unlock the sewer with the Baron Key", "Baron Key"],
        ["Complete the Tower of Zot", "Earth Crystal"],
        ["Open the Toroia treasury with the Earth Crystal", "Earth Crystal"],
        ["Burn village Mist with the Package", "Package"],
        ["Defeat the Baron Castle basement throne", "Baron Key"],
        ["Liberate Baron Castle", "Baron Key"],
        ["Conquer the vanilla Masamune altar", "Darkness Crystal"],
        ["Unlock the Pass door in Toroia", "Pass"],
        ["Complete Cave Bahamut", "Darkness Crystal"],
        ["Complete the Giant of Bab-il", "Darkness Crystal"],
        ["Conquer the vanilla Crystal Sword altar", "Darkness Crystal"]
    ]
    objective_requirements_or = [
        ["Destroy the Super Cannon", "Magma Key", "Hook"],
        ["Unlock the Sealed Cave", "Magma Key", "Hook"],
        ["Complete the Sealed Cave", "Magma Key", "Hook"],
        ["Defeat the king at the Town of Monsters", "Magma Key", "Hook"],
        ["Defeat the queen at the Town of Monsters", "Magma Key", "Hook"],
        ["Return the Pan to Yang's wife", "Magma Key", "Hook"],
        ["Wake Yang with the Pan", "Magma Key", "Hook"],
        ["Defeat the boss of Lower Bab-il", "Magma Key", "Hook"],
        ["Defeat the bosses of Dwarf Castle", "Magma Key", "Hook"],
    ]

    boss_requirements_and = [
        ["Kaipo Officer/Soldiers", "Package"],
        ["King/Queen Eblan", "Hook"],
        ["Rubicant", "Hook"],
        ["Elements", "Darkness Crystal"],
        ["Odin", "Baron Key"],
        ["Dark Elf (dragon)", "TwinHarp"],
        ["CPU", "Darkness Crystal"],
        ["Baigan", "Baron Key"],
        ["Kainazzo", "Baron Key"],
        ["Valvalis", "Earth Crystal"],
        ["Dark Imps", "Tower Key"],
        ["EvilWall", "Luca Key"],
        ["Wyvern", "Darkness Crystal"],
        ["Pale Dim", "Darkness Crystal"],
        ["Bahamut", "Darkness Crystal"],
        ["Ogopogo", "Darkness Crystal"],
        ["Plague", "Darkness Crystal"],
        ["D.Lunars", "Darkness Crystal"]
    ]
    boss_requirements_or = [
        ["Calbrena", "Magma Key", "Hook"],
        ["Golbez", "Magma Key", "Hook"],
        ["Asura", "Magma Key", "Hook"],
        ["Lugae", "Magma Key", "Hook"],
        ["Dark Imps", "Magma Key", "Hook"],
        ["Leviatan", "Magma Key", "Hook"],
        ["EvilWall", "Magma Key", "Hook"],
    ]


    slot_requirements_and = [
            ["Rat Tail", "Hook", "Rat Tail"],
            ["Pink Tail", "Hook", "Pink Tail"],
            ["Sealed Cave", "Luca Key"],
            ["Baron Castle", "Baron Key"],
            ["Baron Basement", "Baron Key"],
            ["Super Cannon", "Tower Key"],
            ["Lunar Subterrane", "Darkness Crystal"],
            ["Cave Bahamut", "Darkness Crystal"],
            ["Wake Yang", "Pan"],
            ["Pan", "Pan"],
            ["Cave Magnes", "TwinHarp"],
            ["Zot", "Earth Crystal"],
            ]
    slot_requirements_or = [
            ["Found Yang", "Magma Key", "Hook"],
            ["Town of Monsters", "Magma Key", "Hook"],
            ["Super Cannon", "Magma Key", "Hook"],
            ["Wake Yang", "Magma Key", "Hook"],
            ["Dwarf Castle/Luca", "Magma Key", "Hook"],
            ["Sealed Cave", "Magma Key", "Hook"],
            ["Lower Bab-il", "Magma Key", "Hook"],
            ["Town of Monsters", "Magma Key", "Hook"],
            ]

    for requirement in objective_requirements_and:
        objective = session.query(Objective).filter(Objective.name == requirement[0]).first()
        for ki_name in requirement[1:]:
            ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
            s = ObjectiveRequirementsAnd(objective=objective, ki=ki)
            session.add(s)

    for requirement in objective_requirements_or:
        objective = session.query(Objective).filter(Objective.name == requirement[0]).first()
        for ki_name in requirement[1:]:
            ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
            s = ObjectiveRequirementsOr(objective=objective, ki=ki)
            session.add(s)

    for requirement in boss_requirements_and:
        boss = session.query(Boss).filter(Boss.name == requirement[0]).first()
        for ki_name in requirement[1:]:
           ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
           s = BossRequirementsAnd(boss=boss, ki=ki)
           session.add(s)

    for requirement in boss_requirements_or:
        boss = session.query(Boss).filter(Boss.name == requirement[0]).first()
        for ki_name in requirement[1:]:
            ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
            s = BossRequirementsOr(boss=boss, ki=ki)
            session.add(s)

    ki_list = []
    for requirement in slot_requirements_and:
        slotList = session.query(ItemSlot).join(Region).filter(Region.name == requirement[0])
        for slot in slotList:
            print(slot)
            for ki_name in requirement[1:]:
                ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
                print(ki)
                ki_list.append(ki)
                s = SlotRequirementsAnd(slot=slot, ki=ki)
                session.add(s)

    for requirement in slot_requirements_or:
        slotList = session.query(ItemSlot).join(Region).filter(Region.name == requirement[0])
        for slot in slotList:
            print(slot)
            for ki_name in requirement[1:]:
                ki = session.query(KeyItem).filter(KeyItem.name == ki_name).first()
                print(ki)
                ki_list.append(ki)
                s = SlotRequirementsOr(slot=slot, ki=ki)
                session.add(s)
    session.commit()


    print([ k.name for k in ki_list[0:2] ])
    #item_slot = session.query(ItemSlot).join(SlotRequirementsAnd).first()
    slotreqs = session.query(SlotRequirementsAnd).filter(~SlotRequirementsAnd.key_item_id.in_(k.id for k in ki_list[0:2]))
    for item in slotreqs.all():
        print(item.slot.region.name)
    item_slot = session.query(ItemSlot). \
            join(SlotRequirementsAnd, and_(
            SlotRequirementsAnd.slot_id == ItemSlot.id,
            SlotRequirementsAnd.key_item_id.in_(k.id for k in ki_list[0:2]))). \
            filter(~exists().
                where(and_(SlotRequirementsAnd.slot_id == ItemSlot.id, ~SlotRequirementsAnd.key_item_id.in_(k.id for k in ki_list[0:2]))).correlate(ItemSlot)).first()
    print(item_slot.region.name)
'''
