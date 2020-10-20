# Convert Shalla's Blacklist into blocklists for Unbound
Convert Shalla's Blacklist files into blocklists for Unbound DNS server

Please ensure your are authorized to use Shalla's Blacklists per the license page.  http://www.shallalist.de/licence.html

To use this utility: 
1. Download the the latest blacklist archive from http://www.shallalist.de/
2. Extract archive to folder.
3. Place this script in the same directory as the BL directory.
4. Run the script with Python 3.

After the script runs you should have a new directory named 'include_files'. 
This directory will contain blocklists based on each category from the Shalla blacklist archive.

To use these blocklists in Unbound simply copy them to your Unbound servern then add the following to your Unbound configuration file:

include: "<path/to/blocklist>"

Keep in mind, some of these blocklists will cause the memory usage of Unbound to drastically increase.
