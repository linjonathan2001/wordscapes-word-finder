# wordscapes-word-finder
Wordscapes Word Finding Algorithm with modifiable valid word list. 

This program takes in letters and finds all valid words in Wordscapes.

## Running
Start the run.py script to start up the GUI:
```
python3 run.py
```
Enter letters into the ``Letters`` field and click ``Find Words``.
To remove words from your local list, click on any outputted word and press ``Remove Selected Word`` or the delete key.

## Old Scripts
In the old scripts directory, there are previous versions of the wordscapes-word-finder. 
wordscapeswordfinder.py-- The first iteration. Very slow because it calculates the powerset of the set of characters of a word and compares each to the valid word list.
wordscapeswordfinder2.py-- The improved algorithm without the GUI.
wordscapeswordremover.py-- The word removing script, which combined with wordscapeswordfinder2.py, makes up the main algorithms of run.py.

Note: txt file with Wordscapes words is in the process of being updated to accurately reflect the valid words in Wordscapes  
