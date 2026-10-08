
# Pass 01
- use a smaller data set






  # Project 1 – To Do List
  
  ## Problem Definition
  
  1. State the business problem. Translate the business problem into a Data Science problem by stating what kind of problem it is ( supervised vs unsupervised ) and whether it is a classification, regression, or clustering problem.  Mention which model will be used, if known.
  
  ## Data Collection
  
  2. Load Pandas, Numpy, and Matplotlib modules
  3. Load data Train.csv from AWS S3.
  
  ## Data Cleaning
  
  4. Examine the data using tools we have used in class. You should be identifying the various columns such as ...
      • target column
      • feature columns
      • identifier columns
      • null columns
      • null rows
  Tools you should be using include, but are not limited to:
      • head
      • tail
      • shape
      • size
      • info
      • describe
      • nunique
      • unique
      • isnull/isna
  5. NOTE: the ‘target’ column indicates a successful transaction (‘1’) or a no-transaction (‘0’). Verify these are the only values in that column, and that there are no nulls.
  6. If there are data cleaning issues, develop recommendations for how to deal with them.  Specifically, handle these common issues:
      • identifer columns
      • target column with null counts
      • feature columns with high null counts
      • feature columns with low null counts
      • feature columns with medium null counts
  
  
  ## Exploratory Data Analysis
  
  Produce some visual analysis of the data.  Recall that Gaussian Naive Bayes assumes the features are normally distributed and independent. Note: you might have to do multiple plots in groups.
  
  7. Check the distributions of all variables by plotting.
  8. Check the correlation values between all **feature columns** to ensure there are no substantial correlations between features. This is important to support the decision to classify the ‘target’ using Naïve Bayes.
  9. Create two data frames: one with all successful transactions, one with all unsuccessful transactions. **Make sure they are copies and not slices**.
  
  ## Data Processing
  
  ### Single Cross-validation ( CV )
  
  10. Create two data sets: one with all the feature columns (everything except for Unnamed: 0, ID_code and target) and one with just the target. Make sure they are copies and not slices.  And make sure they are the correct dimensions.
  11. Define an empty Gaussian Naïve Bayes model using Sklearn.
  12. Divide the two data sets you created in step #10 into training and testing subsets, i.e. train-test split.
  13. Train ( fit ) the model using the training subset of the dataset.
  14. Test the model ( predict ) using the testing subset of the dataset.
  15. Calculate and report the accuracy.
  16. Present a confusion matrix and heatmap
  17. Present the results of a Classification Report (sklearn.metrics.classification_report).
  
  ### Multiple Cross-validation ( CV )
  
  18. Perform a cross-validation loop and record the accuracy of your model during each iteration.
  19. Report the mean accuracy. How does it compare to the accuracy you calculated for the Single CV?
  20. Plot a histogram of the accuracy scores you generated in your cross-validation loop. What do you notice about the distribution of accuracy scores?
  21. Present a confusion matrix and heatmap
  22. Present the results of a Classification Report (sklearn.metrics.classification_report).  What do you notice?  That is, how do the different metrics compare to each other?
  
  ### Balanced data set
  
  The training data is very skewed towards non-successful transactions (about 90% of the training data has ‘target’==0).
  
  23. Remove enough non-successful transaction rows so that your remaining training data is 50%/50% split between successful and non-successful transactions. Hint: you can use the data frames you created in step #9.
  24. Repeat the multiple cross-validation process on this data set.
  25. Report what your mean accuracy for this balanced data set.
  26. Plot a histogram of the accuracy scores you generated in your cross-validation loop. What do you notice about the distribution of accuracy scores?
  27. Present a confusion matrix and heatmap
  28. Present the results of a Classification Report (sklearn.metrics.classification_report).  What do you notice?  That is, how do the different metrics compare to each other?
  
  ## Data Visualization
  
  29. Compare the accuracy results of your multiple cross-validation with the whole training data and the balanced training data
  30. Present the confusion matrix and heatmap
  31. Present the results of your Classification Report (sklearn.metrics.classification_report)
  
  ## Communicate the Results
  
  32. Communicate the results of your analysis.
  
  ## Submit Final Project
  
  33. Save ( commit ) your finished Jupyter notebook to your Project 1 GitHub repo.

