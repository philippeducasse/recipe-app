from recipes.models import Recipe   #you need to connect parameters from books model
from io import BytesIO 
import base64
import matplotlib.pyplot as plt

#define a function that takes the ID
def get_recipename_from_id(val):
   #this ID is used to retrieve the name from the record
   recipeName=Recipe.objects.get(id=val)
   #and the name is returned back
   return recipeName

def get_graph():
   #create a Bytes IO buffer for the image
   buffer = BytesIO()

   #create a plot with bytresIo object as a file-like object . Ser´t format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retreive the content of the file.
   image_png = buffer.getvalue()

   #encode the bytes-like object
   graph = base64.b64encode(image_png)

   # decode to get the string  as output
   graph = graph.decode('utf-8')

   #free up the memory of the buffer
   buffer.close()

   # return the image/graph
   return graph

#data: pandas dataframe
def get_chart(search_type, data, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
   plt.switch_backend('AGG')

   #specify figure size
   fig=plt.figure(figsize=(6,3))

   #select chart_type based on user input from the form

   if search_type == '#1':
       #generate pie chart based on the ingredients.
       #The recipe names are sent from the view as labels
       labels=kwargs.get('labels') 
       title =kwargs.get('title')

       plt.pie(data, labels= labels)
       plt.title(title)

   elif search_type == '#2':
       #plot line chart based on date on x-axis and price on y-axis
       labels=kwargs.get('labels') 
       title =kwargs.get('title')
       plt.bar(data, labels = labels)
       plt.title(title)
   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart =get_graph() 
   return chart

        # https://www.geeksforgeeks.org/how-to-create-pie-chart-from-pandas-dataframe/# 
        # fix Makefile / install make