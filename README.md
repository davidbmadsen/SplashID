# SplashID
SplashTrend Media Experimental Content Identifier

**Warning!** Produces large amounts of image files with long search queries. Use with caution!

**Current functionality:**
- Download, rescale and split video into frames
- Hash frames to bool arrays of size `hash_size`^2 
- Compare hashes to assets
- Filter results and plot

**How to use:**

Run ImageHashTest.py 

**Dependencies:**
ImageHash, YouTube-DL, OpenCV2, Requests, BeautifulSoup, MatPlotLib, PIL, Scipy.Signal

**Known issues:**
As this is written in Python, it is *really* slow
