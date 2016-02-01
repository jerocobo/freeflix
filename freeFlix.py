"""author: VIvek Sah
  filename: freeFlix.py v3.0
  description: takes the search input from command line. searches putlocker.is database for that movie, 
  gets te source file, and opens the file in a browser
"""  

from selenium import webdriver
from Tkinter import *
import re
import subprocess
from selenium.webdriver.common.by import By
import sys
import os
import time
# import tkMessageBox
import Tkinter as tkinter
import tkMessageBox as mbox
from sys import platform as _platform

def finder(movie_name):
  #start the headless browser
  if _platform == "darwin":
     phantom_js = os.getcwd()+'/phantomjs/bin/phantomjs'
     vlc_path = "/Applications/VLC.app/Contents/MacOS/VLC"
  elif _platform == "win32":
     phantom_js = os.getcwd()+'/phantomjs/bin/phantomjs.exe'
     vlc_path = "C:\Program Files (x86)/VideoLAN/VLC/vlc.exe"
     
  driver = webdriver.PhantomJS(phantom_js)
  #driver = webdriver.firefox()
  if movie_name[0] != "tv":

    movie_name = ("".join((elem+ "-") for elem in movie_name))[:-1] 
    movie_name = movie_name.lower()
    driver.get("http://putlocker.is/search/search.php?q="+movie_name)
    search_links = driver.find_elements_by_tag_name("a")    
    
    for link in search_links:
      if "watch-"+movie_name in link.get_attribute('href'):
        movie_identifier = re.search('watch-(.+?)-online', link.get_attribute('href')).group(1)
        print "found: "+ movie_identifier

        #"if yu want to play 300, it will play 300-rise-of-an-empire, so compare the movie name length and see if it plays the required movie"
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

  else:
    tv_name = ("".join((elem+ "-") for elem in movie_name))[2:-4]  #+ "tvshow-season-" + movie_name[-2] + "-episode-"+movie_name[-1]
    print "Playing "+ tv_name + "season: " + movie_name[-2] + " Episode: " + movie_name[-1]
    movie = "http://putlocker.is/watch"+ tv_name + "tvshow-season-" + movie_name[-2] + "-episode-"+movie_name[-1] + "-online-free-putlocker.html"    

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
    if movie_name[0] != "tv":
      element = driver.find_element_by_class_name("jwdownloaddisplay")
      link_1 = element.get_attribute("href")
    else:
      source = driver.page_source
      if "<html" in source:
        try:
          result = re.search("{file:(.*)}]", source).group(1).split(",")[-2].split(":")[-1].strip('"')
          link_1 = "http:"+result
        except:
          element = driver.find_element_by_class_name("jwdownloaddisplay")
          link_1 = element.get_attribute("href")
      else:
        print "Page displayed differently this time, try again"      

    print "All set...Get some popcorns or pineapples...playing though VLC"
   
    #subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC", link_1])
    print("here")
    subprocess.Popen([vlc_path, link_1])    
 
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


if __name__ == "__main__":
  finder(sys.argv[1:])
