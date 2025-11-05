{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ddf9468-f275-4429-8886-a252988eb9ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "class FitnessPredictor:\n",
    "    \"\"\"\n",
    "    Simulates a Deep Learning model that predicts the functional fitness \n",
    "    (e.g., expression level) of a synthetic DNA sequence.\n",
    "    \"\"\"\n",
    "    \n",
    "    def __init__(self, target_sequence='ATTGCAGCTA'):\n",
    "        self.target_sequence = target_sequence\n",
    "        self.alphabet = {'A': 0, 'T': 1, 'C': 2, 'G': 3}\n",
    "\n",
    "    def _calculate_score(self, sequence):\n",
    "        score = 0\n",
    "        min_len = min(len(sequence), len(self.target_sequence))\n",
    "        \n",
    "        for i in range(min_len):\n",
    "            if sequence[i] == self.target_sequence[i]:\n",
    "                score += 1\n",
    "        \n",
    "        score -= abs(len(sequence) - len(self.target_sequence)) * 0.5\n",
    "        \n",
    "        return max(0, score / len(self.target_sequence))\n",
    "\n",
    "    def evaluate_fitness(self, sequence: str) -> float:\n",
    "        if not sequence:\n",
    "            return 0.0\n",
    "        return self._calculate_score(sequence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e448da9-1140-482c-9833-b9711b0a83f5",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
