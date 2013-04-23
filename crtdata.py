#Python script to generate GraphML file 
import csv 
#We're going to use the really handy networkx graph library: easy_install networkx 
import networkx as nx 
import urllib
   
#Create a directed graph object 
DG=nx.DiGraph()   
#Open data file in universal newline mode 
reader=csv.DictReader(open("ufo3.csv","rU")) 
  
#Define a variable to act as a deal node ID counter 
dcid=0  

#The graph is a bimodal/bipartite graph containing two sorts of node - sighting details and place 
#An identifier is minted for each row, identifying the sightings 
#attributes are used to sighting nodes 
#Identify columns used to annotate nodes taking string values 
nodeColsStr=['Sighting Date', 'Reported Date', 'Shape', 'Time']

locList = []  

#Each row defines a sight 
for row in reader:     
	
	#Set ID for the each entry     
	sightID='sight'+str(dcid)     

	#Add a node for the sighting     
	DG.add_node(sightID,typ='sight')     

	#Annotate the deal node with string based attributes 
	print "Writing ", row['Sighting Date']
	
	for sight in nodeColsStr:         
		DG.node[sightID][sight]=row[sight]      

	#If the cell in a Place or location column
	# Add a node if it does not exist
	if not row['Place'] in locList:
		print "Creating node ", row['Place']
		locationID = row['Place']
		DG.add_node(locationID, typ="location")
		locList.append(row['Place'])
	
	## draw an edge between the sighting and the location
		
	DG.add_edge(sightID, row['Place'])  

	#Increment the node ID counter     
	dcid=dcid+1  

#write graph
nx.write_graphml(DG, 'ufo3.graphml')
	