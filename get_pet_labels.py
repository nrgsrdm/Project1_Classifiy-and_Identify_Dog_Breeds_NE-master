#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nergis ERDEM
# DATE CREATED: 15/11/2024                           
# REVISED DATE: 29/11/2024 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      sonuc_dict - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         idx 0 = pet image label (string)
    """
    # list items in directory with pet images
    dosya_listesi = listdir(image_dir)
    
    # print to check file names 
    print('\n 10 filenames from pet_images folder ')
    
    # create empty list for pet labels
    
    # create empty dictionary    
    sonuc_dict = dict()
    
    # iterate over each file name to save the pet name individually
    for idx in range(0, len(dosya_listesi), 1):
        if dosya_listesi[idx][0] != ".":
            pet_image_dosyaadi = dosya_listesi[idx]
            word_list_pet_image_dosyaadi= pet_image_dosyaadi.lower().split('_')
            pet_adi= ''
            
            for word in word_list_pet_image_dosyaadi:
                if word.isalpha():
                    pet_adi += word + " "
            
            pet_adi = pet_adi.strip()
            print('Filename = ', pet_image_dosyaadi, '    label = ', pet_adi)
            ######################## THE pet names should be saved in a list or sth. --> pet_labels
            # pet_labels.append(pet_adi)
                      
            print('\n{:3d} file: {:>20}'.format(idx + 1, dosya_listesi[idx]))
   
            # count length of empty dictionary
            number_of_items_bos_dic = len(sonuc_dict)
    
            print('\nEmpty dictionary has {} items'.format(number_of_items_bos_dic))
    
            # add every element of pet_labels as a value to the sonuc_dict
            if dosya_listesi[idx] not in sonuc_dict:
                sonuc_dict[dosya_listesi[idx]] = [ pet_adi]# what does filenames refer to, here?
            else:
                print('\nWARNING: key =' , dosya_listesi[idx],  'already exists in sonuc_dict with value =', sonuc_dict[dosya_listesi[idx]])
          
    print('\nPrinting all key-value pairs in dictionary results_dic:')
    for key in sonuc_dict:
          print('\nfilename = ', key, '    pet label = ', sonuc_dict)
    # count length in full dictionary
    number_of_items_tam_dic = len(sonuc_dict)
    print('\nEmpty dictionary has {} items'.format(number_of_items_tam_dic))
    
          
    # Replace None with the results_dic dictionary that you created with this
    # function
    return sonuc_dict
