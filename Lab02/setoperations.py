{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "98e08a9b-fb6f-478f-b20a-267f25b03243",
   "metadata": {},
   "outputs": [],
   "source": [
    "#data set for examples\n",
    "data = [1,2,3,4,5,6,7,8,9,10]\n",
    "\n",
    "#defines the make_set function\n",
    "def make_set(data):\n",
    "    data_set = []\n",
    "    if data == None:\n",
    "        return []\n",
    "\n",
    "#checks the data se to make sure there are no repeated numbers    \n",
    "    fixed_list = []\n",
    "    for item in data:\n",
    "        if item not in fixed_list:\n",
    "            fixed_list.append(item)\n",
    "    return fixed_list\n",
    "\n",
    "#defines the is_set function\n",
    "def is_set(data):\n",
    "    if data is None:\n",
    "        return False\n",
    "\n",
    "#Checks the data list and returns whether it is a set(True) or not (False)\n",
    "    fixed_list = []\n",
    "    for item in data:\n",
    "        if item in fixed_list:\n",
    "            return False\n",
    "        fixed_list.append(item)\n",
    "    return True\n",
    "\n",
    "#defines the union(setA, setB) function\n",
    "def union(setA, setB):\n",
    "    if not is_set(setA) or not is_set(setB):\n",
    "        return []\n",
    "\n",
    "    list_union = make_set(setA + setB)\n",
    "    return list_union\n",
    "\n",
    "#defines the intersection(setA, setB function)\n",
    "\n",
    "def intersection(setA, setB):\n",
    "    if not is_set(setA) or not is_set(setB):\n",
    "        return []\n",
    "\n",
    "    intersection_list = []\n",
    "    for item in setA:\n",
    "        if item in setB and item not in intersection_list:\n",
    "            intersectino_list.append(item)\n",
    "\n",
    "    return intersection_list\n",
    "        \n",
    "    \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1d9356fb-59ee-4c3e-9624-fb6c1fe5c5d0",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'intersection' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[39], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m intersection([\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m], [\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m3\u001b[39m])\n",
      "\u001b[0;31mNameError\u001b[0m: name 'intersection' is not defined"
     ]
    }
   ],
   "source": [
    "intersection([1,2], [2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "728361e1-3562-4da5-9bec-4c4e9877f748",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a182448-5896-452f-9271-22887f558126",
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
