import Observation

from Observation import Observation, read_delimited_file 

observations = read_delimited_file("Observation.txt", lambda x: Observation(x[0], x[1], x[2], x[3], float(x[4])))
