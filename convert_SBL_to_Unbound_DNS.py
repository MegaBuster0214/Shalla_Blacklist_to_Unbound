# This utility will convert blacklists from http://www.shallalist.de/ to an
# include file for Unbound DNS.
# ### STEPS ### #
# 1. Create a list of subdirectories in the BL directory.
# 2. For the name of each subdirectory, create an Unbound include file with the
#    name unbound_<SUB_DIR_NAME>_server

# imports
import os


sbl_cat_root = 'BL/'
sbl_cat_list = []
# Create a list of SBL categories and subcategories by appending the
# subdirectory names from the root of the SBL tree.
for item in os.listdir(sbl_cat_root):
    sbl_cat_dir = os.path.join(sbl_cat_root, item)
    if os.path.isdir(sbl_cat_dir) is True:
        for item2 in os.listdir(sbl_cat_dir):
            sbl_cat_sub_dir = os.path.join(sbl_cat_dir, item2)
            if os.path.isdir(sbl_cat_sub_dir) is True:
                sbl_cat_list.append(item + '_' + item2)
            elif item not in sbl_cat_list:
                sbl_cat_list.append(item)


# Check to see if the destination directory for the Unbound include files is
# present. If False, create it.
unbound_dirname = "unbound_include_files"
if os.path.isdir(unbound_dirname) is False:
    os.mkdir(unbound_dirname)

# Create the Unbound include files, per SBL category, and populate domains
# from the SBL in Unbound format. This format consists of taking the domain
# provided by the SBL and redirecting to LOCALHOST (127.0.0.1).
for category in sbl_cat_list:
    print(category)
    source = 'BL/' + category + '/domains'
    destination = unbound_dirname + '/unbound_' + category + '_servers'
    unbound_include_file = os.path.join(unbound_dirname, category)
    #if os.path.isfile(unbound_include_file) is False:
        #print(unbound_include_file)
        # with open(source, 'r') as source_file:
          #  pass
        # with open(destination, 'w') as dest_file:


# local-zone: "1-1ads.com" redirect
# local-data: "1-1ads.com A 127.0.0.1"
