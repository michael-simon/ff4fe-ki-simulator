from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(Base):
    __tablename__ = "assignment"
    id = Column(Integer, primary_key=True)
    filename = Column(String(20), nullable=False, unique=True)

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
        return region.name + " " + location.name

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
    character_id = Column(String, ForeignKey("character.id"))
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
    region_map_id = Column(Integer, ForeignKey("map.id"), nullable=False)
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

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    crystal = KeyItem(name="Crystal")
    assignment = Assignment(filename="test.spoiler")
    region = Region(name="Starting")
    location = Location(name="item")
    islot = ItemSlot(region=region, location=location)
    itemassignment = KeyItemAssignment(assignment=assignment, slot=islot, ki=crystal)
    session.add(crystal)
    session.add(assignment)
    session.add(region)
    session.add(location)
    session.add(islot)
    session.add(itemassignment)
    session.commit()

    cr = session.query(KeyItem).filter(KeyItem.name=="Crystal").first()
    print(cr)
    print(crystal)
    print(cr == crystal)
    for ia in session.query(KeyItemAssignment):
        print("{}:{}:{}".format(ia.ki.name, ia.slot, ia.assignment.filename))


