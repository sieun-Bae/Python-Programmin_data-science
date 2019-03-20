{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type a number that stands for month: 3\n",
      "The month abbreviation is Mar.\n"
     ]
    }
   ],
   "source": [
    "####Lab03_Sieun Bae####\n",
    "# A program to print the abbreviation of a month, given its number\n",
    "\n",
    "def main():\n",
    "# months is used as a lookup table\n",
    "    months = \"JanFebMarAprMayJunJulAugSepOctNovDec\"\n",
    "\n",
    "# get a number stands for a month from a user\n",
    "    n = int(input(\"type a number that stands for month (1-12): \"))\n",
    "\n",
    "# compute starting position of month n in months\n",
    "    pos = (n-1) * 3\n",
    "\n",
    "# Grab the appropriate slice from months monthAbbrev = months[pos:pos+3]\n",
    "    monthAbbrev = months[pos:pos+3]\n",
    "\n",
    "# print the result\n",
    "    print (\"The month abbreviation is\", monthAbbrev + \".\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type a number that stands for month: 12\n",
      "The month abbreviation is Dec.\n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
