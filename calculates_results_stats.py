#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Nergis ERDEM
# DATE CREATED: 15/11/2024                           
# REVISED DATE: 29/11/2024
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(sonuc_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    sonuc_stats_dic = dict()
    
    # The results statistics dictionary will have the following format:
    # key = statistic's name (e.g. n_correct_dogs, pct_correct_dogs, n_correct_breed, pct_correct_breed)
    # value = statistic's value (e.g. 30, 100%, 24, 80%)
    # example_dictionary = {'n_correct_dogs': 30, 'pct_correct_dogs': 100.0, 'n_correct_breed': 24, 'pct_correct_breed': 80.0}
    
#    This dictionary should contain the following keys:
#            /n_images - number of images
#            /n_dogs_img - number of dog images
#            /n_notdogs_img - number of NON-dog images
#            /n_match - number of matches between pet & classifier labels
#            /n_correct_dogs - number of correctly classified dog images
#            /n_correct_notdogs - number of correctly classified NON-dog images
#            /n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs

    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    
    sonuc_stats_dic['n_images'] = 0 #
    sonuc_stats_dic['n_dogs_img'] = 0 #
    sonuc_stats_dic['n_notdogs_img'] = 0 #
    sonuc_stats_dic['n_match'] = 0
    sonuc_stats_dic['n_correct_dogs'] = 0 #
    sonuc_stats_dic['n_correct_notdogs'] = 0 #
    sonuc_stats_dic['n_correct_breed'] = 0  #
    
    # process through the results dictionary
    for key in sonuc_dic:
        # counting images
        sonuc_stats_dic['n_images'] = len(sonuc_dic)
        
        #Label Matches NExactly
        if sonuc_dic[key][2] == 1:
            sonuc_stats_dic['n_match'] += 1
        
        if sonuc_dic[key][3] == 1: # Label Dog
            
            # Number of Dog Images
            sonuc_stats_dic['n_dogs_img'] += 1
            
            if sonuc_dic[key][4] == 1: # Dog classified as dog
                # Number of Correct Dog matches
                sonuc_stats_dic['n_correct_dogs'] += 1
            
            # Number of Correct Breed matches
            if sonuc_dic[key][2] == 1: # Matching image and classifier
                sonuc_stats_dic['n_correct_breed'] += 1
        
        else: # Label isn't a NOT Dog, sonuc_dic[key][3] == 0
            #Not Dog Images Number
            sonuc_stats_dic['n_notdogs_img'] += 1
            
            if sonuc_dic[key][4] == 0: # Classifier Lable is NOT Dog
                # Classified Correct Non-Dog matches Number
                sonuc_stats_dic['n_correct_notdogs'] += 1
                
                
       
        sonuc_stats_dic['pct_match'] = sonuc_stats_dic['n_match'] / sonuc_stats_dic['n_images'] * 100
           
        if sonuc_stats_dic['n_dogs_img'] > 0:
            sonuc_stats_dic['pct_correct_dogs'] = sonuc_stats_dic['n_correct_dogs'] / sonuc_stats_dic['n_dogs_img'] * 100
            sonuc_stats_dic['pct_correct_breed'] = sonuc_stats_dic['n_correct_breed'] / sonuc_stats_dic['n_dogs_img'] * 100
        else:
            sonuc_stats_dic['pct_correct_dogs'] = 0
            sonuc_stats_dic['pct_correct_breed'] = 0
    
        if sonuc_stats_dic['n_notdogs_img'] > 0:
            sonuc_stats_dic['pct_correct_notdogs'] = sonuc_stats_dic['n_correct_notdogs'] / sonuc_stats_dic['n_notdogs_img'] * 100
        else:
            sonuc_stats_dic['pct_correct_notdogs'] = 0
            
  
    return sonuc_stats_dic
