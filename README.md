# ham-radio-license-practice-quiz
Python-based quiz to help study for the amateur radio license exams.

## Description

This is a utility I wrote in my free time to help me study for my
upgraded amateur radio license examinations.  It's simple and does
little more than serve as a faster alternative to flashcards.  All
relevant schematics and figures can be found in the [question_media](./question_media/)
folder.

## How to run:

> `python3 SimpleQuiz.py`

```
Starting simple Python quiz.
Press CTRL + C at any time to quit.

Choose a class level:
	1. Tech
	2. General
	3. Extra
 > 1

Opening question pool: question_pools/techclass20182022.json

What is meant by "repeater offset?"
	a - The difference between a repeater’s transmit frequency and its receive frequency
	b - The repeater has a time delay to prevent interference
	c - The repeater station identification is done on a separate frequency
	d - The number of simultaneous transmit frequencies used by a repeater
 > a
Correct!
Score: 1 out of 1


Press ENTER to continue...
```

## FCC Requirements to Pass License Classes
|Class	                |Questions Given    |Minimum Passing Score
|-                      |-                  |-
|Technician Class	    |35	                |26
|General Class	        |35	                |26
|Amateur Extra Class	|50	                |37

## License Question Pool Sizes
|Class	                |Total Pool Size    |Sections |Diagrams
|-                      |-                  |-        |-
|Technician Class	    |423                |?        |3
|General Class	        |454                |?        |1
|Amateur Extra Class	|622                |?        |10