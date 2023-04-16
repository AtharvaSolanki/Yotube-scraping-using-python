from youtube_statistics import YTstats
from pytube import YouTube
from pytube import Channel
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import simpledialog

input_ui = tk.Tk()  
input_ui.withdraw() 
user=simpledialog.askinteger("Input","If you have video url, please enter 1 \nIf you have channel url, please enter 2 .\t\t\t\t\t",parent=input_ui)
#user=int(input("If you have video link, please enter 1 , If you have channel link, please enter 2"))
if user==1:
    #video=str(input('Enter Video URL '))
    video=simpledialog.askstring('Video',"Enter Video Url\t\t\t\t",parent=input_ui)
    x=YouTube(video)
    channelId=x.channel_id
    curl=x.channel_url
    c=Channel(curl)
    cname=c.channel_name
    print("channel Name =" , cname)
    print("channel Id =" , channelId)
    print("channel url =" , curl)
else:
    #url = str(input('Enter Channel URL '))
    url=simpledialog.askstring("Channel","Enter Channel Url\t\t\t\t",parent=input_ui)

    # get html content from the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    # extract and print channel's ID
    channelId=soup.find("meta", itemprop="channelId")['content']
    print(channelId)
API_KEY="AIzaSyDs1FSxbBA7UJZofrSXj0k8WPdjCC1fxqg"
channel_id=channelId
yt= YTstats(API_KEY,channel_id)
#yt.get_channel_statistics()
#yt.dump()

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump() 
#yt.get_channel_video_data()



