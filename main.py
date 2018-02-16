#check if image_path is in removed.csv


import os
import csv
import cv2

path_to_images = './landscapes/'
path_to_edits = './photos_to_edit/'
path_to_removed = './photos_to_remove/'

results_csv = './cf_report_1230552_full.csv'
removed_csv = './removed.csv'
keyword_options = ['city', 'field', 'forest', 'mountain', 'ocean', 'lake', 'road']
remove_these_images = []


def parse_filename_from_url(url):
    clean_name = url.split('.com/')[1].split('/')[1]
    return clean_name

def remove_image(image_path, new_path):
    with open(removed_csv, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ')
        csvwriter.writerow([image_path])
    os.rename(image_path, new_path)

def process_csv_results(csv_file):
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        results = list(reader)
    header = results[0]
    for i, item in enumerate(header):
        if header[i] == 'emotion_types':
            emotion_types_index = i 
        if header[i] == 'image_url':
            image_url_index = i
        if header[i] == '_worker_id':
            worker_id_index = i
        if header[i] == 'extra_info':
            extra_info_index = i
        if header[i] == 'category':
            category_index = i
    flagged_image_names = []
    for result in results:
        if result[extra_info_index] == 'true':
            filename = parse_filename_from_url(result[image_url_index])
            file_path = path_to_images + result[category_index] + '/' + filename
            flagged_image_names.append(file_path)
    flagged_images = set(flagged_image_names)
    print len(flagged_images)
    print len(results)

    for image_path in flagged_images:
        print image_path
        cv2.imshow('image', cv2.imread(image_path))
        k = cv2.waitKey(0)
        #esc key
        if k == 27:
            break
        #spacebar
        if k == 32:
            print 'do not remove'
        #f key
        elif k == 102:
            #check if image_path is in removed.csv
            #if image_path in 
            remove_these_images.append(image_path)
            new_path = path_to_removed+ image_path.split('/')[2] + '/' + image_path.split('/')[3] 
            remove_image(image_path, new_path)
            print path_to_removed
        #a key
        elif k == 97:
            print path_to_edits
    remove_images(remove_these_images)
    #return [results , emotion_types_index, image_url_index, worker_id_index]

process_csv_results(results_csv)







