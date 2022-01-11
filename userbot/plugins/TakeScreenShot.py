from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.scr (.*)$"))
async def TakeScreenShot(event):
    site = event.pattern_match.group(1)
    await event.edit("`• Please Wait ...`")
    driver = webdriver.Chrome("chromedriver")
    driver.get(site)
    screenshot = driver.save_screenshot("site.png")
    driver.quit()
    await event.delete()
    await app.send_file(event.chat_id , "site.png" , caption=f"**• ScreenShot From Site:** ( `{site}` )")
    os.remove("site.png")
