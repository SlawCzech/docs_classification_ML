import os

import pandas as pd
import cv2
import pytesseract


def text_extractor_training(folder_name):
    '''
    OCR_Engine for text extraction from images in training data (to be labelled):
    source_df: save extracted text for each img file in each category
    '''

    # Folder path
    dir_path = os.path.join('..', 'data', folder_name)

    # List to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    print(res)

    file_list = res

    source_df = pd.DataFrame(columns=['name', 'text', 'target'])

    for i, file in enumerate(file_list):
        img = cv2.imread(os.path.join('..', 'data', folder_name, file))
        try:
            new_item = pd.DataFrame({'name': str(file), 'text': pytesseract.image_to_string(img, lang='eng+pol'),
                                     'target': folder_name}, index=[0])
            source_df = pd.concat([source_df, new_item], ignore_index=True)
        except:
            # if can't extract then give some notes into df
            new_page = pd.DataFrame({'name': str(file), 'text': 'N/A'}, index=[0])
            source_df = pd.concat([source_df, new_page], ignore_index=True)
            continue

        print(f'{file} is done. File number {i}')

    source_df.to_csv(os.path.join('..', 'data', f'{folder_name}_labeled.csv'))


def text_extractor_test(folder_name):
    '''
    OCR_Engine for text extraction from images in test data (no labels):
    source_df: save extracted text for each img file in each category
    '''

    # Folder path
    dir_path = os.path.join('..', 'data', folder_name)

    # List to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    print(res)

    file_list = res

    source_df = pd.DataFrame(columns=['name', 'text'])

    for i, file in enumerate(file_list):
        img = cv2.imread(os.path.join('..', 'data', folder_name, file))
        try:
            new_item = pd.DataFrame({'name': str(file), 'text': pytesseract.image_to_string(img, lang='eng+pol')},
                                    index=[0])
            source_df = pd.concat([source_df, new_item], ignore_index=True)
        except:
            # if can't extract then give some notes into df
            new_page = pd.DataFrame({'name': str(file), 'text': 'N/A'}, index=[0])
            source_df = pd.concat([source_df, new_page], ignore_index=True)
            continue

        print(f'{file} is done. File number {i}')

    source_df.to_csv(os.path.join('..', 'data', f'{folder_name}.csv'))

