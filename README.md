Particle-Recognition
====================

For the sake of a mildly amusing acronym:

LABRAT (LAngton Blob Recognition and Analysis Toolkit)

====================

This program can be used to analyse indivudual blobs (timepix particle tracks) or entire frames.  It requires any inputted blobs to be in the format of a non-empty list of length-2 tuples, e.g. [(1,2),(2,3)].  The method .analyse() of class impact returns a str describing the particle type, determined according to a branching algorithm with currently semi-arbitrary values.  The method .classify() of class frame returns a dict containing the particle type of each blob in the frame.

TO DO:
====================

Support file reading

Fine-tune branching algorithm

Perhaps implement k-means in n dimensions to check the results of branching algorithm?

Create function to calculate percentages of particles in frame

Other things...
