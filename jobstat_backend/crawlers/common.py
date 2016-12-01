import os


def check_or_create_save_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print "Created folder for saved results: %s" % folder_path
