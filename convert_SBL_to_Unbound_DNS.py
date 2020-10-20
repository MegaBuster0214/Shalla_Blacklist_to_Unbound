# This utility will convert Shalla Blacklists (SBL) from
# http://www.shallalist.de/ to files for use with Unbound DNS. Each category
# from the SBL will have an Unbound include file generated for it.

# imports
import os

# Lets look at the items in the 'BL/' directory. We are looking for directories
# only. Shalla's convention is to have a directory for each blacklist category
# and, if there are no subcategories, have a list of domains and URL's for each
# category with each file named respectively 'domains' and 'urls'. We will add
# the names for each category to a list for use later in file naming. If there
# is a subcategory, then the subcategory will be added to the category list in
# the convention 'category_subcategory' and the top category will be removed.
sbl_cat_root = 'BL/'
sbl_cat_list = []
for item in os.listdir(sbl_cat_root):  # Iterate through items in 'BL/'
    sbl_cat_dir = os.path.join(sbl_cat_root, item)  # Make new path 'BL/'+item
    if os.path.isdir(sbl_cat_dir) is True:  # Verify new path is a directory.
        # This directory check is here to ensure only names of directories will
        # be added to the category list.
        if item not in sbl_cat_list:  # If the category is not already added to
            # the category list, add it.
            sbl_cat_list.append(item)
        for item2 in os.listdir(sbl_cat_dir):  # Check if any directories exist
            # in the category directory. If so, subcategories exist.
            sbl_cat_sub_dir = os.path.join(sbl_cat_dir, item2)  # Make new path
            # 'BL/item/item2' to verify subcategory directories.
            if os.path.isdir(sbl_cat_sub_dir) is True:
                sbl_cat_list.append(item + '_' + item2)  # If 'BL/item/item2'
                # is a directory, append 'category_subcategory' to the category
                # list.
                if item in sbl_cat_list:
                    sbl_cat_list.remove(item)  # Since a subcategory was added
                    # to the category list, the top category is no longer
                    # needed on the list.

# Now that the category list is complete, we will create the Unbound include
# files and populate domains from the SBL 'domains' file for each category into
# a format Unbound can recognize:
# local-zone: "domain.com" redirect
# local-data: "domain.com A 127.0.0.1"

# Check to see if the destination directory for the Unbound include files is
# present. If False, create it.
include_dirname = "include_files"
if os.path.isdir(include_dirname) is False:
    os.mkdir(include_dirname)

# Create a dictionary that will store the location of 'domains' file as the key
# and the new location of the include file as the value.
domains_file_location_dict = {}
for category in sbl_cat_list:
    new_include_file = include_dirname + '/unbound_' + category + '_servers'
    include_file_path = os.path.join(include_dirname, new_include_file)
    if '_' not in category:  # First, add the categories to the dictionary.
        source = 'BL/' + category + '/domains'
        domains_file_location_dict[source] = new_include_file
    else:  # Next, add the subcategories to the dictionary.
        source_list = category.split('_')
        source = 'BL/' + source_list[0] + '/' + source_list[1] + '/domains'
        domains_file_location_dict[source] = new_include_file

# Finally, open both the SBL 'domains' file and the new file for Unbound.
# Get each domain from the 'domains' file and wrap it in the redirect
# statements for unbound.
# Write each statement to the new file for Unbound.
for src, dst in domains_file_location_dict.items():
    source_file = open(src, 'r')
    dest_file = open(dst, 'w')
    for domain in source_file:
        dest_file.write('local-zone: "' + domain.replace('\n', '') +
                        '" redirect' + '\n')
        dest_file.write('local-data: "' + domain.replace('\n', '') +
                        ' A 127.0.0.1"' + '\n')
