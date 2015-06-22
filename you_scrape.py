# 
#   Scrapes Video Links from user Playlist
#   and Tests Youtube functionality on Google Chrome
#   Also Downloads audio using youtube-dl
#
#
import os,sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
#
# Classes
#
class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
    	   self.driver=webdriver.Firefox()


	def test_search_in_python_org(self):
            # Click on video link for each song in playlist, fetches url, and then goes back to original page
            # Still Needs Work
            # Only works for first video
            driver = self.driver
            driver.get("https://www.youtube.com/playlist?list=PLIQGt7Pv8OM9waKZbKgXBofPfrJWi7a5T")
            driver.find_element_by_css_selector('.pl-video-thumbnail').click()
            url = driver.current_url
            os.system('youtube-dl -x --extract-audio --audio-format mp3 ' + url)
        
   
	def tearDown(self):
       	 self.driver.close()

# Main Program

if __name__ == "__main__":

	unittest.main()