# Convert Shalla's Blacklist into blocklists for Unbound
This tool will convert Shalla's Blacklist files into blocklists for Unbound DNS server. The goal of making this tool is to allow for simple web content filtering 
through DNS instead of a proxy server. This in turn allows for URL filtering regardless of protocol (HTTP, HTTPS). (Ensure DNS over HTTPS is disabled on your web browser to allow use of your local Unbound DNS Server.)

Please ensure your are authorized to use Shalla's Blacklists per the license page.  http://www.shallalist.de/licence.html

To use this utility: 
1. Download the the latest blacklist archive from http://www.shallalist.de/
2. Extract archive to a directory.
3. Place this script in the same directory as the BL directory.
4. Run the script with Python 3.

After the script runs you should have a new directory named 'include_files'. 
This directory will contain blocklists based on each category from the Shalla blacklist archive.

To use these blocklists in Unbound simply copy them to your Unbound server then add the following to your Unbound configuration file for each blocklist that you would like to use:

include: "<path/to/blocklist>"

Keep in mind, some of these blocklists will cause the memory usage of Unbound to drastically increase.
