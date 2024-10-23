{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "0e093974-7be5-4471-a064-7c28e3481bd3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "31131b0e-556a-4eea-9ae9-a48aff7567e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Item:\n",
    "    def __init__(self, name, description='', rarity='common'):\n",
    "        self.name = name\n",
    "        self.description = description\n",
    "        self.rarity = rarity\n",
    "        self._ownership = None  \n",
    "    \n",
    "    def pick_up(self, character):\n",
    "        self._ownership = character\n",
    "        return f\"{self.name} is now owned by {character}\"\n",
    "    \n",
    "    def throw_away(self):\n",
    "        self._ownership = None\n",
    "        return f\"{self.name} is thrown away\"\n",
    "    \n",
    "    def use(self):\n",
    "        if self._ownership:\n",
    "            return f\"{self.name} is used by {self._ownership}\"\n",
    "        return \"No one owns this item.\"\n",
    "    \n",
    "    def __str__(self):\n",
    "        if self.rarity == 'legendary':\n",
    "            return f\"*** {self.name} (Legendary Item) ***\\n{self.description}\\nPrepare for greatness!\"\n",
    "        owner = self._ownership if self._ownership else \"No owner\"\n",
    "        return f\"Item: {self.name}, Rarity: {self.rarity}, Owner: {owner}\"\n",
    "\n",
    "\n",
    "class Weapon(Item):\n",
    "    def __init__(self, name, damage, rarity='common', weapon_type=''):\n",
    "        super().__init__(name, rarity=rarity)\n",
    "        self.damage = damage\n",
    "        self.type = weapon_type\n",
    "        self.active = False\n",
    "        self.attack_modifier = 1.15 if self.rarity == 'legendary' else 1.0\n",
    "    \n",
    "    def equip(self):\n",
    "        if self._ownership:\n",
    "            self.active = True\n",
    "            return f\"{self.name} is equipped by {self._ownership}\"\n",
    "        return \"No one owns this weapon.\"\n",
    "\n",
    "    def use(self):\n",
    "        if self.active:\n",
    "            attack_move = self._attack_move()\n",
    "            return f\"{attack_move} {self.name} is used, dealing {self.damage * self.attack_modifier} damage\"\n",
    "        return \"Weapon must be equipped first.\"\n",
    "\n",
    "\n",
    "class SingleHandedWeapon(Weapon):\n",
    "    def __init__(self, name, damage, rarity='common'):\n",
    "        super().__init__(name, damage, rarity, weapon_type='single-handed')\n",
    "\n",
    "    def _attack_move(self):\n",
    "        return f\"{self._ownership} slashes with {self.name}\"\n",
    "\n",
    "\n",
    "class DoubleHandedWeapon(Weapon):\n",
    "    def __init__(self, name, damage, rarity='common'):\n",
    "        super().__init__(name, damage, rarity, weapon_type='double-handed')\n",
    "\n",
    "    def _attack_move(self):\n",
    "        return f\"{self._ownership} spins with {self.name}\"\n",
    "\n",
    "\n",
    "class Pike(Weapon):\n",
    "    def __init__(self, name, damage, rarity='common'):\n",
    "        super().__init__(name, damage, rarity, weapon_type='pike')\n",
    "\n",
    "    def _attack_move(self):\n",
    "        return f\"{self._ownership} thrusts with {self.name}\"\n",
    "\n",
    "\n",
    "class RangedWeapon(Weapon):\n",
    "    def __init__(self, name, damage, rarity='common'):\n",
    "        super().__init__(name, damage, rarity, weapon_type='ranged')\n",
    "\n",
    "    def _attack_move(self):\n",
    "        return f\"{self._ownership} shoots with {self.name}\"\n",
    "\n",
    "\n",
    "class Shield(Item):\n",
    "    def __init__(self, name, description='', defense=0, rarity='common', broken=False):\n",
    "        super().__init__(name, description, rarity)\n",
    "        self.defense = defense\n",
    "        self.broken = broken\n",
    "        self.active = False\n",
    "        self.defense_modifier = 1.10 if self.rarity == 'legendary' else 1.0\n",
    "        self.broken_modifier = 0.5 if self.broken else 1.0\n",
    "    \n",
    "    def equip(self):\n",
    "        if self._ownership:\n",
    "            self.active = True\n",
    "            return f\"{self.name} is equipped by {self._ownership}\"\n",
    "        return \"No one owns this shield.\"\n",
    "    \n",
    "    def use(self):\n",
    "        if self.active:\n",
    "            defense_value = self.defense * self.defense_modifier * self.broken_modifier\n",
    "            return f\"{self.name} is used, blocking {defense_value} damage\"\n",
    "        return \"Shield must be equipped first.\"\n",
    "\n",
    "\n",
    "class Potion(Item):\n",
    "    def __init__(self, name, potion_type, value):\n",
    "        super().__init__(name)\n",
    "        self.potion_type = potion_type\n",
    "        self.value = value\n",
    "        self.empty = False\n",
    "    \n",
    "    def use(self):\n",
    "        if self.empty:\n",
    "            return \"This potion has already been consumed.\"\n",
    "        if self._ownership:\n",
    "            self.empty = True\n",
    "            return f\"{self._ownership} used {self.name}, {self.potion_type} increased by {self.value}\"\n",
    "        return \"No one owns this potion.\"\n",
    "    \n",
    "    @classmethod\n",
    "    def from_ability(cls, name, owner, potion_type):\n",
    "        potion = cls(name, potion_type, value=50)\n",
    "        potion.pick_up(owner)\n",
    "        return potion\n",
    "\n",
    "\n",
    "class Inventory:\n",
    "    def __init__(self, owner=None):\n",
    "        self.owner = owner\n",
    "        self.items = []\n",
    "\n",
    "    def add_item(self, item):\n",
    "        self.items.append(item)\n",
    "        item.pick_up(self.owner)  \n",
    "        return f\"{item.name} added to {self.owner}'s backpack.\"\n",
    "\n",
    "    def drop_item(self, item):\n",
    "        if item in self.items:\n",
    "            self.items.remove(item)\n",
    "            item.throw_away()  \n",
    "            return f\"{item.name} removed from {self.owner}'s backpack.\"\n",
    "        return f\"{item.name} not found in the backpack.\"\n",
    "\n",
    "    def view(self, item_type=None):\n",
    "        if item_type:\n",
    "            items_of_type = [item for item in self.items if isinstance(item, item_type)]\n",
    "            return [str(item) for item in items_of_type]\n",
    "        return [str(item) for item in self.items]\n",
    "\n",
    "    def __iter__(self):\n",
    "        return iter(self.items)\n",
    "\n",
    "    def __contains__(self, item):\n",
    "        return item in self.items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50811767-c062-4dd5-b2d1-a62c65e17b0d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
