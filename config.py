import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # Get absolute path to CA certificate
    ca_path = Path(__file__).parent / 'ca.pem'
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'sslmode': 'require',
            'sslrootcert': str(ca_path),
            'connect_timeout': 5
        }
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    NEWS_SOURCES = {
        "TechCrunch": "https://techcrunch.com/feed/",
    "TheVerge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss",
    "HackerNews": "https://news.ycombinator.com/rss",
    "ArsTechnica": "http://feeds.arstechnica.com/arstechnica/index",
    "BBC":"https://www.bbc.co.uk/news/technology/rss.xml",
    "Quanta Magazine":"https://www.quantamagazine.org/feed/",
    "Science Magazine":"https://www.sciencemag.org/rss/news_current.xml",
    "Nature":"https://www.nature.com/nature.rss",
    "Scientific American":"https://www.scientificamerican.com/feed/",
    "IEEE Spectrum":"https://spectrum.ieee.org/rss",
    "Science Daily":"https://www.sciencedaily.com/rss/all.xml",
    "MIT Technology Review":"https://www.technologyreview.com/feed/",
    "Gizmodo":"https://gizmodo.com/rss",
    "Mashable":"https://mashable.com/feed/",
    "CNET":"https://www.cnet.com/rss/news/",
    "Engadget":"https://www.engadget.com/rss.xml",
    "VentureBeat":"https://venturebeat.com/feed/",
    "TheNextWeb":"https://thenextweb.com/feed/",
    "Fast Company":"https://www.fastcompany.com/rss",
    "Inc":"https://www.inc.com/rss",
    "Entrepreneur":"https://www.entrepreneur.com/rss",
    "Bloomberg":"https://www.bloomberg.com/technology",
    "Reuters":"https://www.reuters.com/tools/rss",
    "Financial Times":"https://www.ft.com/technology",
    "Wall Street Journal":"https://www.wsj.com/news/technology",
    "New York Times":"https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "The Guardian":"https://www.theguardian.com/technology/rss",
    "The Register":"https://www.theregister.com/Design/News_RSS_Feed.xml",
    "ZDNet":"https://www.zdnet.com/news/rss.xml",
    "Techmeme":"https://www.techmeme.com/feed.xml",
    "Slashdot":"https://slashdot.org/index2.rss",
    "DZone":"https://dzone.com/rss",
    "ReadWrite":"https://readwrite.com/feed/",
    "Vox":"https://www.vox.com/rss/index.xml",
    "The Atlantic":"https://www.theatlantic.com/technology/feed/",
    "The Verge":"https://www.theverge.com/rss/index.xml",
    "GigaOM":"https://gigaom.com/feed/",
    "TechSpot":"https://www.techspot.com/backend.xml",
    "TechRadar":"https://www.techradar.com/rss",
    "Digital Trends":"https://www.digitaltrends.com/rss",
    "PCMag":"https://www.pcmag.com/rss",
    "Tom's Hardware":"https://www.tomshardware.com/feeds/all",
    "AnandTech":"https://www.anandtech.com/rss",
    "ExtremeTech":"https://www.extremetech.com/feed",
    "BGR":"https://bgr.com/feed/",
    "Lifehacker":"https://lifehacker.com/rss",
    "How-To Geek":"https://www.howtogeek.com/feed/",
    "MakeUseOf":"https://www.makeuseof.com/rss/",
    "TechHive":"https://www.techhive.com/rss",
    "PCWorld":"https://www.pcworld.com/index.rss",
    "Computerworld":"https://www.computerworld.com/index.rss",
    "Network World":"https://www.networkworld.com/index.rss",
    "InfoWorld":"https://www.infoworld.com/index.rss",
    "ITworld":"https://www.itworld.com/index.rss",
    "CIO":"https://www.cio.com/index.rss",
    "CSO":"https://www.csoonline.com/index.rss",
    "Dark Reading":"https://www.darkreading.com/rss_simple.asp",
    "SC Magazine":"https://www.scmagazine.com/home/feed/",
    "SecurityWeek":"https://www.securityweek.com/rss",
    "Krebs on Security":"https://krebsonsecurity.com/feed/",
    "Threatpost":"https://threatpost.com/feed/",
    "The Hacker News":"https://feeds.feedburner.com/TheHackersNews",
    "CyberScoop":"https://www.cyberscoop.com/feed/",
    "BleepingComputer":"https://www.bleepingcomputer.com/feed/",
    "Ars Technica":"https://arstechnica.com/feed/",


    }