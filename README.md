# Save-The-Energy
This repository contains both the client and server codes for my bachelor project. My project involves using knolwedge graphs to explain predictions that were made regarding energy consumption for both 2017 and 2018 based on the consumption in 2016. 

&nbsp;

I used these 3 notebook from **Kaggle** in my implementation:



1) https://www.kaggle.com/code/cereniyim/save-the-energy-for-the-future-1-detailed-eda
2) https://www.kaggle.com/code/cereniyim/save-the-energy-for-the-future-2-fe-lightgbm/notebook
3) https://www.kaggle.com/code/cereniyim/save-the-energy-for-the-future-3-predictions/notebook

&nbsp;

These notebooks aim to predict a building's energy consumption over 2017 and 2018 using the data from 2016 in 4 different consumpiton categories (electricity, chilled water, steam, hot water) using **ASHRAE** data where:



- The 1st notebook covered understanding the data and the features involved as well as a detailed EDA(Exploratory Data Analysis).
- The 2nd notebook focused on building the optimal machine learning model which turned out to be the **light GBM** model.
- The 3rd notebook focused on generating the predictions using the **light GBM** model and summary for the whole project.


&nbsp;

Using the data and the generated predictions from these notebooks , I started my implementation where I used **Python** to apply 3 different algorithms(**feature selection,feature importance, and decision tree**) with the help of 3 different models(**random forest regressor,gbrt, and decision tree regressor**) to generate explanations for the predictions obtained by the **light GBM** model(used in the notebooks) to determine the most contributing features in these predictions. Then, I used some libraries and functions, to be able to build the knowledge graphs and I also tested my implementation by constructing two graphs, one containing all the features and explanations obtained, while the other contains the essential attributes in terms of all the algorithms of explanation.

&nbsp;

Furthermore, I constructed a simple database consisting of 19 functions using **Python** also. These functions will allow the user to query the knowledge graph for specific information based on the user's input. Finally, I created a front-end web app and connected it to these back-end functions in order to make the query database more user friendly and easier to deal with. I implemented this app using **Anvil**, which is a platform for building web apps with the use of **Python** mainly.

&nbsp;


- Here is the link for the source code of the **Anvil** app: https://anvil.works/build#clone:5B6U2YV67EORTGGG=6ZUQEFWMCSFEEMV3XIQJC233



- Here is the link for the .ipynb **Google Colab** file containing the source code for the explanation algorithms: 
https://colab.research.google.com/drive/1jmPHAJsv9ZPuSEYTErS5-Sha7efxhV6I?usp=sharing



- Here is the link for the .ipynb **Google Colab** file containing the source code for constructing the knowledge graph and the ontology:
https://colab.research.google.com/drive/1NWJ28DYVF9pMpEAzG_WqpYr4dhoSxxgn?usp=sharing


&nbsp;

To be able to run the Anvil app that has the client code, you should first connect the app to the Colab notebook containing the source code for constructing the knowledge graph and the ontology. To do so, you need to :



**1)** Install the **anvil-uplink** library in the Colab environment using the command:
   
   ```
   !pip install anvil-uplink
   ```


**2)** Importing the **anvil.server module**:
   
   ```
   import anvil.server
   ```


**3)** Connect to the Uplink:
   
   ```
   anvil.server.connect("your-uplink-key")
   ```


**4)** Replace **“your-uplink-key”** with the Uplink key from your app:

&nbsp;

Click on the **Settings** icon, then choose **Uplink**.


![Screenshot (1)](https://user-images.githubusercontent.com/87882755/169875847-4e1b5d84-7e04-4374-8658-05446605f6ec.png)

&nbsp;

Then copy the **Uplink key** of the server code,which is the one highlighted in the image below:

![Save The Energy _ Anvil - Google Chrome 23_05_2022 7_11_19 PM](https://user-images.githubusercontent.com/87882755/169875889-3afbc7fc-4ea4-4109-9570-5895a6a91cb5.png)



**5)** Finally, run all the cells of the Colab notebook.


&nbsp;

You will find the line **"@anvil.server.callable"** written before any function in the Colab notebook needed to run the app.If you're done with the previous steps, then you have successfully connected the client code with the server code and you can now run the app! 
