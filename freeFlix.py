"""author: VIvek Sah
  filename: freeFlix.py v3.0
  description: takes the search input from command line. searches putlocker.is database for that movie, 
  gets te source file, and opens the file in a browser
"""  

from selenium import webdriver
import re
import subprocess
from selenium.webdriver.common.by import By
import sys
import os
from rottentomatoes import RT
import time
# import tkMessageBox
import Tkinter as tkinter
import tkMessageBox as mbox
def finder(movie_name):

  movie_name = ("".join((elem+ "-") for elem in movie_name))[:-1]
  print movie_name                     
  movie_name = movie_name.lower()
  driver = webdriver.PhantomJS(os.getcwd()+'/phantomjs/bin/phantomjs')
  driver.get("http://putlocker.is/search/search.php?q="+movie_name)
  search_links = driver.find_elements_by_tag_name("a")
  
  
  for link in search_links:
    if "watch-"+movie_name in link.get_attribute('href'):
      
      movie_identifier = re.search('watch-(.+?)-online', link.get_attribute('href')).group(1)
      print "found: "+ movie_identifier

      "if yu want to play 300, it will play 300-rise-of-an-empire, so compare the movie name length and see if it plays the required movie"
      movie_name_split = movie_identifier.split("-")
       
      if len(movie_name_split) - len(movie_name.split("-"))  ==1:
        try:
          movie_name_split[-1] = int(movie_name_split[-1])
          movie = link.get_attribute('href')
          print "got the movie link"
          break
        except:
          pass 
          
      elif len(movie_name.split("-")) == len(movie_name_split):
        movie = link.get_attribute('href')
        print "got the movie link"
        break
      else:
        pass 
  source = ''
  try: #this try should be 
    driver.get(movie) 
  
    link_element = driver.find_elements_by_tag_name("iframe")
    for link in link_element:
      
      if "thevideo" in link.get_attribute('src'):
        req_link = link.get_attribute('src')
        print "found the source file, YAY!!"
        break
    
    driver.get(req_link)
    element = driver.find_element_by_class_name("jwdownloaddisplay")
    link_1 = element.get_attribute("href")

    print "All set...playing " + "".join((elem+ " ") for elem in movie_identifier.split("-") )+ "though VLC"
   
    # name_as
    movie_data= RT('99q4spp2b4t89wghwjy55jz7').feeling_lucky("".join((elem+ " ") for elem in movie_identifier.split("-") ))
    # print movie_data
    print "Ratings:\nCritics Rating : "+  str(movie_data['ratings']['critics_score']) + "*"*movie_data['ratings']['critics_score'] + "\nAudience Rating: "+   str(movie_data['ratings']['audience_score']) + "*"*movie_data['ratings']['audience_score']
    print  "Synopsis:"+ str(movie_data['synopsis']) 

   
    subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", link_1])
    # print links[-3]
 
  except:
    if "File was deleted" in source:
      print "Oops, movie was deleted"
      window = tkinter.Tk()
      window.wm_withdraw()
      mbox.showinfo('my app','Oops, movie was deleted')
    else:  
      print "movie not found" 
      window = tkinter.Tk()
      window.wm_withdraw()
      mbox.showinfo('my app','movie not found')
    driver.quit()     

finder(sys.argv[1:])
# finder("skyfall")

# print "hello"

