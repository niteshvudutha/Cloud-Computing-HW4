CLOUD COMPUTING HOMEWORK 4 - HW4 – Hadoop data Analysis 
#vuduthnh M12483636 NITESH VUDUTHA

Description:
Program implemented in Map-Reduce that can analyse data of any type of vehicle and gives analysis about the number of accidents for any vehicle

Technologies:
Python

Steps to execute the application :

1. Open putty application. Enter the address as "hadoop-gate-0.eecs.uc.edu"

2. When it prompts for username and password, Authorise using 6+2 credentials.

3. Clone this repository

	https://github.com/niteshvudutha/Cloud-Computing-HW4
	
	All the files in the above repository will be copied into folder that is prompted in command line
	
4. Execute the command - "hadoop fs -put mapper.py ./mapper.py"

5. Execute the command - "hadoop fs -put reducer.py ./reducer.py"

6. Execute the command - "hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/tatavag/nyc.data -output /user/vuduthnh/outputAssignment4/"

7. Now to find the output, Execute the command - "hadoop fs -get outputAssignment4"

8. Now execute - "cd outputAssignment4"

9. Then execute - "cat part-00000"

Now the file is opened in the command line. Here you can find the statistics arranged in 2 columns(vehilce name followed by number of accidents)

Example Output:

D       1
D1      1
DELIV   48