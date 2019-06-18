# Mouse-Trajectory-and-Click-Prediction
Mouse Trajectory and Click Prediction using Recurrent Neural Networks

This repository includes two files: </br>
1.  The ‘Mouse_Tracker.py’ file is a python script that is used to collect the cursor movements. For this purpose, just run the script and browse web with the code running in the background. Once finished browsing, the script should be stopped manually. </br>
2. The second file ‘Mouse Trajectory Prediction.ipynb’ is a jupyter notebook which includes the entire functionality of the following sections:</br>
  i. Dataset Analysis </br>
  ii. Data Cleaning and Pre-processing</br>
  iii. Creation of Supervised Learning Datasets</br>
  iv. Training and Prediction of mouse trajectory and click positions using SimpleRNN and LSTM models with different configurations.</br>
  v. Evaluation and Comparison of all models</br>
  vi. Real-time predictions using the best models</br>
  
The main purpose of this project is to predict that which page the user is going to click on next, based on the trajectory and click positions, so that those pages can be prefetched in the cache of the user during idle time. Thus, when the user clicks on the web page, it instantly loads, thereby reducing the latency of the website. This will result in better user web experience. The main basis of the project is Predictive Prefetching.
  
