ErdosNumber
===========

A program to help determine Erdos number paths using Google Scholar profiles. 

This program uses links to a Google Scholar profile to compile a list of coauthors; this list is compared to the complete list of individuals one or two degrees of separation from Paul Erdos. The output file "matches.txt" gives the first and last names of potential matches.

The data file Erdos1.txt is from Oakland University's Erdos Number Project, http://www.oakland.edu/enp/thedata/.

At the present time, this program is only useful for helping find the path for people with 3 degrees of separation from Paul Erdos (this covers surprisingly many people if you count coauthorships in any academic journal!). A future goal can be to implement a 'true' BFS for arbitrary degrees of separation.

Sample case:
The sample hard-coded case uses Richard Feynman's Google Scholar profile, and outputs the name "FRANK VERNON" in matches.txt. Referring to the Oakland University data, Frank L. Vernon coauthored a paper with Ronald Lewis Graham, who coauthored a paper with Paul Erdos! This gives a three-step path from Feynman to Erdos.
