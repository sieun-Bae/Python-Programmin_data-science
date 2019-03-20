{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Program to create a file of usernames in batch mode."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    print(\"This Program creates a file of usernames from a file of names.\")\n",
    "    \n",
    "    infileName = input(\"What file are the names in?\")\n",
    "    outfileName = input(\"What file should the usernames go in?\")\n",
    "    \n",
    "    infile = open(infileName, 'r')\n",
    "    outfile = open(outfileName, 'w')\n",
    "    \n",
    "    for line in infile: #infile.readlines()\n",
    "        first, last = line.split() #space is the default\n",
    "        uname = (first[0] + last[:7]).lower()\n",
    "        print(uname, file=outfile)\n",
    "        \n",
    "    infile.close()\n",
    "    outfile.close()\n",
    "    \n",
    "    print(\"Usernames have been written to\", outfileName)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This Program creates a file of usernames from a file of names.\n",
      "What file are the names in?fullname.txt\n",
      "What file should the usernames go in?username.txt\n",
      "Usernames have been written to username.txt\n"
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
