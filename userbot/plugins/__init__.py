from userbot import app , START_TIME , DATABASE_ITEMS
from Config import Config
from userbot.utils import ocr_space_file , chunks , convert_time , bash , restart_app , load_plugins , convert_bytes , take_screen_shot , runcmd
from telethon import events
from moviepy.editor import VideoFileClip , AudioFileClip
from datetime import datetime
from PIL import Image
from pathlib import Path
from asyncio import sleep
from selenium import webdriver
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidLength , LanguageNotSupportedException
import heroku3
import logging
import math
import importlib
import glob
import shlex
import functools
import random
import requests
import os
import asyncio
import sys
import traceback
import time
import ffmpeg
import io
import shutil
import pornhub
import requests
if os.path.exists("data.json"):
    DATA = open("data.json" , "r").read()
else:
    with open("data.json" , "w") as file:
    file.write(DATABASE_ITEMS)
    DATA = open("data.json" , "r").read()
