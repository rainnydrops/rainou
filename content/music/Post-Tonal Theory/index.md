---
title: Post-Tonal Theory
updated: 2025-01-08 01:49:08Z
created: 2024-09-09 17:18:26Z
---

# Post-Tonal

## Collection
## Referencial Collection
- Subsets of the 12 chromatic PCs
- Organized under certain logic
## 12-ToneTechnique
- Use of single tone
- Use the entire 12 PC to aggregate
## Overview of the Pitch Class
All the pitch class collection can be summarized as certain "key scale", the way to find this key scale is via its pitch class -> normal form -> prime form (which gives the interval of this scale) -> for details: check the referencial table 
1. Series of pitch found on sheet: Mi, Fa, Sol sharp
2. translate subset of pitch class: referencial Collection from the pitch clock face: `5,4,8`
3. Calculate the Normal form (the most compressed way of the Series of pitch) : `[4,5,8]`
4. Find its prime form: (steps or the 'key' scale of the pitch subset): `(014)`
-> Chech the referencial collection for `(014)`
-> We know that the series of pitch 'Mi, Fa, Sol sharp' uses the 'scale' of (014) (instead of the usual major/minor scale we known of)

## Notation Format
Pitch Class Set: `(0, 1, 7)`
Normal Form: `[11, 0, 2, 5, 8]`
Prime Form: `(0126)`

## Pitch and Pitch Class
- **Pitch**: specific note at a certain frequency
- **Octave Equivalence**: Set of CDEFGAB (or any set of notes that are) of a octave apart are called Octave Equivalence
- **Enhamonic equivalence**: A# is the same as Bb (different notes when referring to the same pitch)
- **Pitch-Class**: All the octave of the note and their enharmonic equivalence about the same C pitch, C1-C2-C3-C4, these are called in the same pitch class.
- **Pitch-Class interval**: distance between the pitch in semi-tone
- **Pitch intervals**: Different pitch space round the clock face.
	- Ordered pitch interval (opi); measured by a +/- sign (+ for going up), (- for going down)

## Interval series
The interval series can be used to analyze the atonal piece, the piece that cannot be explained with the traditional harmony theory can use these method to find the logic of the piece.
- **Order Pitch Interval (opi)**: direction of the interval indicated by +/- sign
	- Emphasis: **directional interval size**
	- -3, +5
- **Unordered Pitch-Class Interval (upci)**: measure of the interval size of the pitch
	- Empasis: **undirectional** (no sign), **interval size** only
	- 4, 12, 16
- **Ordered Pitch-Class Interval (opci)**: direction based on the clock face.
	- Emphasis: **directional**, **clock face** (mod 12 system)
	- -3, 11 (within the mod 12 range)
- **Unordered Pitch-Class Interval (upci)**: shortest distance around the clock face, this number will never go larger than 6
	- Emphasis: **undirectional**, **clock face** (mod 12 system), shortest distance of the inverval on the clock face
	- 0,1,2,3,4,5,6

## Forms
- Normal Form: Motive for the post-tonal music. The most compressed way of writing a pitch-class set
	- used to recognize and compare pitch-class sets in post-tonal music
	- represented in square brackets.
	- e.g. `[11, 2, 4, 7]`
	- Rules for putting sets into normal form:
		1. Write pc out in order as an ascending scale; the ordering that has the smallest interval between the first and last pc is the normal form (check OPCI)
		2. If there is a tie for Rule 1, the normal form will pack pc most closely to one end or the other (large intervals will be concentrated at the top or the bottom)
		3. If there is a more than one normal form, prefer the one that is most packed at the bottom (smaller interval at the bottom, larger intervals on top)
	- For example: given 4, 7, 2, 11 
		Ascending order: 2, 4, 7, 11
		`2 4 7 11`	-> 11 - 2 = 9
		`4 7 11 2`	-> 2 - 4 = (-2) mod12 = 10
		`7 11 2 4`	-> 4 - 7 = (-3) mod12 = 9
		`11 2 4 7`	-> 7 - 11 = (-4) mod12 = 8
		Chose the number with the smallest
		Normal Form = `11 2 4 7`
		If there are two set of pitch with the same number, then do the calculation internally to determine the smallest compact form. For example if there was two form that gave the number 8. Do the internal math `2-11`, `4-2`, `7-4`, compare each pair and choose the pitch set that first gave the smallest number

## Transposition
- Shift the pitch up by n
	- Do the math: Tn(x)=y iff y=x+n
	- Perform the addition by x

## Inversion
- Another way of transposing the melody
	- To find an inversion of `I5[1, 3, 4, 7]`
		- `5 - 1` = 4
		- `5 - 3` = 2
		- `5 - 4` = 1
		- `5 - 7` = 10
		Inversion form I5 is `4, 2, 1, 10`
		To normalize this form `[10, 1, 2, 4]`
		- Note the property between **Inversion form** and **Normal Form**  `[4, 2, 1, 10]` and `[10, 1, 2, 4]`, they are backward listed
		- Note the property between pre-inversion `[1, 3, 4, 7]` and Inversion normal form `[10, 1, 2, 4]`. They add up to be I**5** `1+4, 3+2, 4+1, 7+10`
![Screenshot 2024-09-20 at 19.06.54.png](1.png)
Use of basketball diagram to find out the inversion. Note that the inversion are oftentlly inverted.
![Screenshot 2024-09-20 at 19.28.28.png](2.png)



![Answer is [C#, D#, F#, G#]](../../_resources/Screenshot%202024-09-20%20at%2019.29.21.png)

![Screenshot 2024-09-20 at 19.32.29.png](3.png)

## Prime Form
- Notated as: `(0123)`
- The interval of the pitch class set from the Normal Form
- Derived from the Normal Form 
- Counting starting 0
- i.e. Normal Form `[1,5,6,7]`, interval size is `4,1,1`, put the interval size in order is `1,1,4`, add the consecutive interval size starting from 0 is `(0126)`


## Set Class
- The list of set classes contains all of the possible existing prime form
- Gives all the summary for the specific Prime Form
- Includes a complementary sets
- Column 1: Prime Form
- Column 7: Complementary Form of the selected Prime Form
- Column 2 & 6: Name of the Form
- Column 3 & 5: Interval vector
	*Interval vector is how many times the interval appears in the selected Prime Form or Complementary Form arranged in the following table (Star represent number of time for the interval in Prime Form)

| 1 | 2 | 3 | 4 | 5 | 6 |
| :-: | :-: | :-: | :-: | :-: | :-: |
| * | * | * | * | * | * |

- Column 4: Number of levels of symmetry
	- Left: number of levels of transpositional symmetry
	- Right: number of levels of inversional symmetry
	- If the number is more than 2, it means that after two transposition or two inversion, they will map on itself.
		- For example, for the whole tone series (02468T), they will map onto themself 6 times. Think about when transpose by two, all the interval vector will map onto itself,. Since there are total of 12 tones, every second tone they will map onto itself.

# List of Class (Reference)
![Two Chord](4.png)

![Trichords](5.png)


![Tetrachords](6.png)

![Pentachords](7.png)

![Hexachords](8.png)

# Atonal Spotlight - Things that can be explored
- Use of the same loop and repeat in atonal, rhythm ties the whole piece together.,
- Explore the mix from Tonal and Atonal theory
- Explore the property of the piano overtone harmony
- Explore with equal temperament/microtone and overtone series (Sax, Violin, etc)
- Using a certain instruments special technic heavily


# 12 Tone-techniques
- Referential Collections: Subset of 12 Chromatic PCs
- 12-Tone Technique: revolve around a single “tone” but use the entire 12 PC aggregate
- Tonal harmony means the chord are build based on a certain pitch
- **Diatonic collection**: Tonal harmony used in a different way
![Atonal Harmony used in a different way](9.png)
- **Whole Tone Collection**
	- Best representation is Debussy's work
	- Subsets of this collection contain various tritones
![Reference to Voile by Debussy](10.png)
- **Octatonic Collection**: This 8-note scale alternates between half
and whole step. Also called diminish scale because it include two of
versions of the diminished seventh chord (incllude the third)
	- Sounds pretty & hunting (due to with dissonance)
	- 
![Screenshot 2024-10-09 at 11.50.46.png](11.png)
- Hexatonic Scale: 6 notes collection, alternate between semi-tone and minor third
	- i.e. `[0,1,4,5,8,9]`
![Screenshot 2024-10-09 at 12.03.08.png](12.png)

# Twelve Tone Series
- Set: Ordered sequence of the 12-tone series.
- Series: 
	- also called a 'tone row'
	- lines of pitch class
	- contain all twelve pitch classes (one of each)
	- Occurs in a particular order
	- If the tone row is '7, 4, 3, 6, 1, 5, 2, 11, 10, 0, 9, 8', the order are sticted in this order throughout.
- Usually the first series encountered in the piece is considered as the 'prime', the rest are calculated based on that
- Note that P2 means to calculate based on the pitch 4, Px means starting with x, i.e. P2, means pitch class with starting of 2. This always refer to the relationship of the first pitch in its prime order. Everything else is calculated based on the starting note.
- T4: Translation series starting at 4
- I4: Inversion series starting at pitch 4
- R4: Starting retrograde with the last in pitch 4
- RI4: Starting retrograde-inversion with the last in pitch 4
## Transposition
With a transposed ordering, each pitch class in the row is altered by some interval but the **interval succession remains the same**

![Transpolition](13.png)
- When transposed, all the interval stays the same.

## Retrograde
- The prime ordering is played in reverse, think of: 
	- The ordering of the pitch classes is reversed
	- Interval is reversed AND by its mod 12 complement
![Retrograde](14.png)
Note R2 refer to the last member of the pitch in the serie, which is also the first pitch of P2
- When retrograded, the interval flipped, (from 2 to 1 is -1, after retrograded from 1 to 2 is +1)

## Inversion
Interval is replaced with their mod 12 counterpart: `1` becomes `11` or `-1`  becomes `+1`
![Inversion](15.png)
- The interval changes to their counterpart after inversion

## Retrograde-Inversion
Applys the retrodrade to the set and then inversion (or vise versa)
- Interval remain the same but in reverse order (If started with 1, then the last interval is 1)
![Retrograde-Inversion](16.png)

## 12x12 Matrix

![12x12 Matrix](17.png)


![More example to the 12x12 Matrix](18.png)

- Read from left to right is the P set
- Read from right to left is the R set
- Read from top to bottom is the I set
- Read from bottom to top is the RI set
- Best to construct it on a transposition bases
- Can double check if the matrix is right by cheching if the pitch in the middle is aligned

## Composition with 12 tones
- Notes are allowed to be repeated if not messing up the order
- Some advaced 12 tones may use certain notes as a reference point to repeat notes under a certain rules.
- 12-tones may seem very random and not sound good, best way to do it is to subdivide it into smaller section of the interval series with certain order, like the set that uses the following interval: (014), (014), (014)
![Example of (014)](19.png)

## Invariant
Things that do not change no matter however the series are transformed, examples are:
- Intervals
- Subset of PCs
- Pair or set that remain the same after transformation:
![Subset Invariant](20.png)

![Chords that map onto themself after transformation](21.png)

![Paired Invariant, 8 is mapped to 10, but 10 is also mapped to 8](22.png)

## Some example

![12-tone system in a repertoire](23.png)

# Neo-Reimannian
- Move from one chord to another via one pitch changes. 
- All the chords sounds connected but not via a tranditional harmonic structure
- Between each chord, only one note is shifting at a time.
![Transformational Analysis](24.png)

## Primary Transformation
- Neo-Reimannian theory can be represented with a Tonnetz: Tone Network
	- diagonal connections show major or minor third
	- L: Leading Tone Exchange
	- P: Parallel
	- R: Relative
![Tonnetz](25.png)

![Usually follow a specific type of sequence](26.png)

![More Example: Der Dopplegän ger (Schubert)](27.png)

## Secondary Tranformation
- By combining the primary LPR operations = secondary transformation
- Order of combination heavity matter can change the result
	- S: **Slide** (LPR) maintains the triadic third but root and fifth move by a semitone
	- N: **Nebenverwandt** (RLP) Triadic root becomes fifth, and modes switch
	- M: **Modalverwandt** (PRL) Triadic fifth becomes the root, and modes switch
![Secondary Tranformation](28.png)
## Contemporary Example
- Used a lot in the movie setting
- "A Beautiful Mind": "Breaking the Code"
![Screenshot 2024-11-21 at 02.37.13.png](29.png)

![Screenshot 2024-11-21 at 02.37.29.png](30.png)


![Screenshot 2024-11-21 at 02.37.43.png](31.png)

![Screenshot 2024-11-21 at 02.38.22.png](32.png)


# Post-Tonal and beyond
1. Theory Harmony: Common Practice
2. Tonal Harmony: Jazz
3. Tonal Harmony Exteded: 
	- Neo-Riemannian Analysis
	- Parsimonious voice-leading and transformational cycle to explain non-functional harmonic progression. 
	- Schenkerian Analysis
	- Reductive Analysis: how to make a phrasing expressive, dynamic and drive forward.
		- Scheleton Melody
4. Pst Tonal Music:12 Tone
5. Spectromusic (using spectrogram (quarter flat, quarter sharp)
	- Minimalism
	- rhythm and meter
6.Cross genre approaches