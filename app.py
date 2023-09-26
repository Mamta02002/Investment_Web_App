from flask import Flask, render_template, request, url_for, redirect

import numpy as np
import pickle
from joblib import dump, load

app=Flask(__name__)
@app.route("/",methods=["GET"])
def hello_world():
    return render_template('index.html')

@app.route("/venture",methods=["GET"])
def venture():
    return render_template('venture.html')

@app.route("/status",methods=["GET"])
def status():
    status = ['News','Games','Publishing','Electronics',
              'Tourism','Software','Advertising','Curated Web',
              'E-Commerce','Health and Wellness','Real Estate',
              'Education','Search','Marketplaces','Restaurants',
              'Media','Hospitality','Health Care Information Technology',
              'Analytics','Fashion','Mobile Commerce','Mobility',
              'Biotechnology','Social Travel','Enterprise Software',
              'Personal Health','Sports','Mobile','Pharmaceuticals',
              'SaaS','Manufacturing','Entertainment','Travel','Designers',
              'Finance','Lifestyle','Chat','File Sharing','Video Chat',
              'Mobile Health','Mobile Security','Social Media','Photography',
              'Fitness','Sales and Marketing','Predictive Analytics',
              'Financial Services','Art','Big Data','Blogging Platforms',
              'Hardware + Software','Social Fundraising','Clean Technology',
              'Services','Outsourcing','Corporate IT','Mobile Social','Messaging',
              'Navigation','Transportation','Wine And Spirits','Maps',
              'Consumer Electronics','Life Sciences','Corporate Training',
              'Artificial Intelligence','Bitcoin','Online Travel','Web Development',
              'Electronic Health Records','Customer Service','3D Printing','3D',
              '3D Technology','Drones','Physicians','Automotive','Retail','Video',
              'Business Analytics','Music','Semiconductors','Web Hosting','Android',
              'Game','Developer APIs','Human Resources','Online Shopping','Security',
              'Flash Storage','Specialty Foods','Networking','Machine Learning',
              'Entrepreneur','Commercial Real Estate','Promotional','Web Design',
              'Cloud Computing','Kids','Interface Design','Pets','Business Services',
              'Women','Venture Capital','Carbon','Health Care','Career Management',
              'Technology','Medical','Distribution','Mobile Games','Internet Marketing',
              'Nanotechnology','Small and Medium Businesses','SEO','Personal Finance',
              'Digital Entertainment','Task Management','Virtual Worlds','Exercise',
              'Public Relations','Telecommunications','Consulting','Television','Local Businesses',
              'Payments','Design','Mobile Payments','Travel & Tourism','Social Games','Creative',
              'Coupons','Water Purification','Twitter Applications','Business Productivity',
              'Communications Hardware','Batteries','Advertising Platforms','Events','EDA Tools',
              'Virtualization','Cloud Infrastructure','Accounting','M2M','Solar','Identity Management',
              'Information Security','Social Media Platforms','Apps','Information Technology',
              'Mining Technologies','Medical Devices','Cloud Management','Brand Marketing',
              'Nonprofits','Recruiting','Healthcare Services','Vertical Search','Internet Radio Market',
              'Technical Continuing Education','P2P Money Transfer','Incentives','Gamification',
              'Internet of Things','Semantic Search','Marketing Automation','Internet','Collectibles',
              'Business Intelligence','Email','Communities','Social Network Media','Ad Targeting',
              'Development Platforms','Mass Customization','Social Media Advertising','Bio-Pharm',
              'Semantic Web','Collaboration','Assisitive Technology','Facebook Applications',
              'Location Based Services','Industrial','Trusted Networks','Data Visualization',
              'Enterprise Search','Social Buying','Optimization','Application Platforms',
              'Outdoors','Lead Generation','Computers','Real Time','Classifieds','Local Based Services',
              'Search Marketing','Auctions','Digital Signage','RIM','Databases','Mobile Advertising',
              'Displays','Digital Media','Social Commerce','Online Scheduling','Hospitals','Outdoor Advertising',
              'Startups','iOS','Clean Energy','App Marketing','Adventure Travel','Legal','Finance Technology',
              'Advice','Advertising Exchanges','Comparison Shopping','Therapeutics','Defense','Aerospace','Consumers','Wireless','DOD/Military','Shopping','Product Development Services','Mobile Analytics','Cloud Data Services','Journalism','Food Processing','Privacy','Match-Making','Business Development','Insurance','Banking','Meeting Software','Energy','Retail Technology','Tablets','Gps','Agriculture','Social Bookmarking','Web CMS','Recycling','Health Services Industry','Public Transportation','Biomass Power Generation','Online Rental','Content Syndication','Sensors','iPhone','Groceries','Human Computer Interaction','Personal Branding','Cars','SMS','Weddings','Distributors','Lighting','Local Search','Computer Vision','Craft Beer','Credit','Cloud Security','Crowdsourcing','Craigslist Killers','Document Management','Animal Feed','Information Services','Construction','Product Design','Consumer Goods','Data Mining','Renewable Energies','Linux','App Stores','Open Source','iPad','Beauty','Enterprises','Stock Exchanges','Financial Exchanges','Big Data Analytics','BPO Services','Colleges','Data Integration','College Recruiting','Alumni','Knowledge Management','Social Media Monitoring','Reviews and Recommendations','Broadcasting','Nutrition','Sustainability','Trading','Material Science','Portals','Home Automation','Graphics','Toys','Smart Grid','Content','Logistics','Chemicals','Virtual Currency','Robotics','Investment Management','Handmade','Crowdfunding','Bioinformatics','Non Profit','Online Dating','Opinions','Consumer Internet','Oil','Reputation','Psychology','Subscription Businesses','Mobile Software Tools','Ticketing','Content Creators','Enterprise Security','Mobile Enterprise','Price Comparison','Hardware','Training','Alternative Medicine','Real Estate Investors','Babies','Homeland Security','Mobile Devices','Developer Tools','Loyalty Programs','PaaS','Application Performance Monitoring','Social Media Marketing','Genetic Testing','Testing','User Experience Design','Email Marketing','Social + Mobile + Local','Video Streaming','QR Codes','Cyber Security','CRM','Distributed Generation','Group Buying','Enterprise Application','Energy Management','Online Video Advertising','Browser Extensions','Photo Sharing','Contact Management','Angels','Data Security','Online Gaming','Deep Information Technology','Augmented Reality','Universities','Web Tools','Dental','Oil & Gas','Visualization','Jewelry','Video Games','Home Decor','Physical Security','Identity','Diabetes','Diagnostics','Oil and Gas','Logistics Company','English-Speaking','Tracking','RFID','Freelancers','E-Commerce Platforms','Productivity Software','Wholesale','Market Research','Industrial Automation','NFC','Content Delivery','Guides','Licensing','Monetization','Audio','Personalization','Brokers','Service Providers','Home & Garden','Professional Services','IT Management','Natural Resources','Neuroscience','Local Advertising','Creative Industries','Film Production','Video Conferencing','Minerals','Unifed Communications','Network Security','VoIP','Direct Marketing','Farmers Market','Consumer Behavior','Language Learning','Baby Accessories','Parenting','Storage','Music Services','Consumer Lending','Social Search','Water','MMO Games','Lifestyle Products','Discounts','Peer-to-Peer','Organic','Project Management','Fantasy Sports','Risk Management','Charity','Collaborative Consumption','Charter Schools','Medical Professionals','Data Privacy','Film','Organic Food','Low Bid Auctions','Shoes','Incubators','Coworking','Gambling','Career Planning','K-12 Education','Employer Benefits Programs','Algorithms','Game Mechanics','IT and Cybersecurity','Teenagers','Biometrics','Cosmetics','mHealth','Synthetic Biology','High Tech','B2B','Tutoring','Enterprise Hardware','Office Space','Infrastructure','Semiconductor Manufacturing Equipment','Data Centers','Gold','Image Recognition','General Public Worldwide','E-Books','Forums','Flowers','Flash Sales','Cooking','Coffee','Online Reservations','IaaS','Credit Cards','CAD','Ediscovery','Leisure','University Students','Boating Industry','Textiles','Customer Support Tools','Proximity Internet','Teachers','Textbooks','Event Management','Tech Field Support','Content Discovery','Spas','Soccer','World Domination','Billing','Text Analytics','Private Social Networking','Gift Card','Moneymaking','Intellectual Property','Embedded Hardware and Software','Emerging Markets','Nightlife','Local','Printing','Home Renovation','Politics','Bridging Online and Offline','Celebrity','MicroBlogging','Social News','Rental Housing','Synchronization','Lead Management','Hotels','Utilities','In-Flight Entertainment','Digital Rights Management','Medical Marijuana Patients','Social Business','Taxis','Staffing Firms','Health and Insurance','Communications Infrastructure','Systems','Artists Globally','All Markets','Auto','Elder Care','Employment','Senior Citizens','Parking','Environmental Innovation','Shared Services','Advanced Materials','Motors','Direct Sales','Casual Games','Entertainment Industry','Architecture','Remediation','Mobile Shopping','Farming','Electrical Distribution','Energy Efficiency','Electric Vehicles','Sales Automation','Sponsorship','Intellectual Asset Management','iPod Touch','Religion','Theatre','Governments','Engineering Firms','Interest Graph','All Students','College Campuses','Performance Marketing','Google Apps','Social Recruiting','Nightclubs','Fleet Management','Windows Phone 7','Independent Music Labels','Green','Educational Games','High Schools','Green Building','WebOS','Professional Networking','Ventures for Good','Natural Language Processing','Procurement','Recipes','PC Gaming','Social CRM','Law Enforcement','New Product Development','Mobile Coupons','Property Management','Sex','Q&A','Product Search','Sporting Goods','Civil Engineers','Video on Demand','Local Coupons','Debt Collecting','Supply Chain Management','Shipping','Funeral Industry','Indoor Positioning','Usability','Concerts','Music Education','Residential Solar','Domains','Doctors','Software Compliance','Registrars','Film Distribution','Freemium','Local Commerce','App Discovery','Wealth Management','Transaction Processing','Translation','Motion Capture','Intelligent Systems','Eyewear','Heavy Industry','China Internet','Virtual Workforces','B2B Express Delivery','TV Production','Corporate Wellness','Interior Design','New Technologies','Skill Assessment','Internet TV','Point of Sale','Data Center Infrastructure','Social Media Management','Unmanned Air Systems','Business Information Systems','Innovation Management','Public Safety','Commodities','Speech Recognition','Mobile Emergency&Health','Face Recognition','Polling','Green Consumer Goods','ICT','Self Development','Musical Instruments','Racing','Retirement','Enterprise Resource Planning','Specialty Retail','Web Browsers','Presentations','Video Processing','Swimming','Kinect','Internet Service Providers','Postal and Courier Services','Humanitarian','Hedge Funds','FreetoPlay Gaming','Surveys','Geospatial','Gift Registries','Musicians','Contact Centers','Golf Equipment','Rapidly Expanding','Social Television','Comics','Mechanical Solutions','Online Auctions','Commercial Solar','Recreation','Video Editing','Clinical Trials','Biotechnology and Semiconductor','Bicycles','Radical Breakthrough Startups','Human Resource Automation','Vacation Rentals','Mobile Video','Smart Building','Visual Search','Internet Infrastructure','Call Center Automation','Telephony','Innovation Engineering','Virtual Goods','Cyber','Group SMS','Plumbers','Lifestyle Businesses','Infrastructure Builders','Families','Cloud-Based Music','Archiving','Social Innovation','Realtors','Lasers','Offline Businesses','Specialty Chemicals','Weird Hardware','Veterinary','Twin-Tip Skis','Governance','Lotteries','Demographies','Certification Test','DIY','Cosmetic Surgery','Energy IT','Custom Retail','Insurance Companies','Gift Exchange','Homeless Shelter','Mac','Government Innovation','Rehabilitation','Sunglasses','Gas','Cable','SNS','Senior Health','Space Travel','Lingerie','Renewable Tech','Enterprise 2.0','Performing Arts','Contests','Advertising Networks','Photo Editing','Google Glass','Home Owners','Mobile Infrastructure','Niche Specific','Data Center Automation','Industrial Energy Efficiency','Biofuels','Personal Data','Internet Technology','Web Presence Management','Quantified Self','Music Venues','Email Newsletters','Natural Gas Uses','Tea','Fraud Detection','Self Storage','Young Adults','Dietary Supplements','Franchises','Writers','Social Opinion Platform','Early-Stage Technology','Enterprise Purchasing','Simulation','Estimation and Quoting','EBooks','Vending and Concessions','Test and Measurement','Automated Kiosk','Social Investing','Baby Boomers','Reading Apps','Fuels','Social Media Agent','Quantitative Marketing','Online Identity','Gadget','Energy Storage','Timeshares','Resorts','Multi-level Marketing','Service Industries','Wind','Clean Technology IT','Rural Energy',
                ]
    return render_template('status.html',c = status)


@app.route("/predict", methods = ["GET","POST"])
def predict():
    if request.method == 'POST':
        # Get the form data as Python ImmutableDict datatype 
        data = request.form
        #return the extracted information
        arr = np.array([[data['a'],data['b'],data['c'],data['d'],data['e'],data['f'],
                         data['g'],data['h'],data['i'],data['j'],data['k']]])
        model = pickle.load('ven_model.pkl','rb')
        result = model.predict(arr.reshape(1,-1))
        result = round(result[0],2)
        
    return render_template('prediction.html',prediction=result)

@app.route("/predict1", methods = ["GET","POST"])
def predict1():
    if request.method == 'POST':
        # Get the form data as Python ImmutableDict datatype 
        data = request.form
        #return the extracted information
        model = pickle.load('st_model.pkl','rb')
        ohe = pickle.load('ohe_market.pkl','rb')
        le = pickle.load('le_status.pkl','rb')

        c= ohe.transform(np.array(f" {data['c']} ").reshape(1,-1)).toarray()
        test_point = [data['a'],data['b']]
        test_point.extend(c[0])
        test_point = np.array(test_point)
        result = le.inverse_transform(model.predict(test_point.reshape(1,-1)))
    return render_template('prediction.html',prediction1=result[0])

if __name__=="__main__":
    app.run(debug=True)
