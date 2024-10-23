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
   "execution_count": 104,
   "id": "31131b0e-556a-4eea-9ae9-a48aff7567e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class Item:\n",
    "    def __init__(self, name, description='', rarity='common'):\n",
    "        self.name = name\n",
    "        self.description = description\n",
    "        self.rarity = rarity\n",
    "        self._ownership = None  # None means no owner initially\n",
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
    "        owner = self._ownership if self._ownership else \"No owner\"\n",
    "        return f\"Item: {self.name}, Rarity: {self.rarity}, Owner: {owner}\"\n",
    "\n",
    "\n",
    "\n",
    "class Weapon(Item):\n",
    "    def __init__(self, name, damage, rarity='common', weapon_type=''):\n",
    "        super().__init__(name, rarity=rarity)\n",
    "        self.damage = damage\n",
    "        self.type = weapon_type\n",
    "        self.active = False\n",
    "        # Set attack modifier based on rarity\n",
    "        self.attack_modifier = 1.15 if self.rarity == 'legendary' else 1.0\n",
    "    \n",
    "    def equip(self):\n",
    "        if self._ownership:\n",
    "            self.active = True\n",
    "            return f\"{self.name} is equipped by {self._ownership}\"\n",
    "        return \"No one owns this weapon.\"\n",
    "    \n",
    "    def use(self):\n",
    "        if self.active:\n",
    "            return f\"{self.name} is used, dealing {self.damage * self.attack_modifier} damage\"\n",
    "        return \"Weapon must be equipped first.\"\n",
    "\n",
    "\n",
    "\n",
    "class Shield(Item):\n",
    "    def __init__(self, name, description='', defense=0, rarity='common', broken=False):\n",
    "        super().__init__(name, description, rarity)\n",
    "        self.defense = defense\n",
    "        self.broken = broken\n",
    "        self.active = False\n",
    "        # Set defense modifier based on rarity\n",
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
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "7b213d6f-0a4e-4a11-b4fd-e4713a90566d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Belthronding is now owned by Beleg\n",
      "Belthronding is equipped by Beleg\n",
      "Belthronding is used, dealing 5750.0 damage\n",
      "Wooden Lid is now owned by Beleg\n",
      "Wooden Lid is equipped by Beleg\n",
      "Wooden Lid is used, blocking 2.5 damage\n",
      "Wooden Lid is thrown away\n",
      "Wooden Lid is used, blocking 2.5 damage\n",
      "Beleg used Atk Potion Temp, attack increased by 50\n",
      "This potion has already been consumed.\n",
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65bcf2c4-a1b4-49ed-a587-69d15561bebe",
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
