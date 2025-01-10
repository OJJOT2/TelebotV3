import telebot
import http.client
import json
import time
from datetime import datetime
import threading
import pytz

TOKEN = "7577429699:AAFDna2WDWzLRhQehvVUyjVqIwyPd7-Ix7A"
bot = telebot.TeleBot(TOKEN)
conn = http.client.HTTPSConnection("udemy-paid-courses-for-free-api.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "9b440ee187msh29987a6568674e8p1ac199jsnf546c2c45e5a",
    'x-rapidapi-host': "udemy-paid-courses-for-free-api.p.rapidapi.com"
}
autosend_time = ""


def get_courses(query):
    try:
        # if query ==None:
        #     conn.request("GET", "/rapidapi/courses/?page=1&page_size=10", headers=headers)
        # else:
        #     conn.request("GET", f"/rapidapi/courses/?page=1&page_size=10&query={query}", headers=headers)
        # res = conn.getresponse()
        # data = res.read()
        # print(data)
        data = b'{"courses":[{"name":"CBT: Cognitive Behavioral Therapy For Anxiety And Depression","category":"CBT Cognitive Behavioral Therapy","image":"https://img-c.udemycdn.com/course/480x270/4455066_9f98_2.jpg","actual_price_usd":399000.0,"sale_price_usd":0.0,"sale_end":"2025-01-10T20:52:00","description":"CBT: Cognitive Behavioral Therapy For Anxiety And Depression, Define how CBT could treat anxiety, depression and panic, certification, skills for dealing with ...","url":"https://www.udemy.com/course/cbt-cognitive-behavioral-therapy-for-anxiety-and-depression/?couponCode=00C8A635EB6FF6D013F6","clean_url":"https://www.udemy.com/course/cbt-cognitive-behavioral-therapy-for-anxiety-and-depression/"},{"name":"100% OFF- Python And Flask Framework Complete Course","category":"Flask","image":"https://img-c.udemycdn.com/course/480x270/3407178_5bd8_3.jpg","actual_price_usd":24.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T02:46:00","description":"Python And Flask Framework Complete Course, Depth Introduction To Python Programming And Python Web framework Flask.\\r\\nCourse Description\\r\\nThis course is a ...","url":"https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?couponCode=2FA8E12A82CA9E38B840","clean_url":"https://www.udemy.com/course/flask-framework-complete-course-for-beginners/"},{"name":"Comprehensive Course on Enterprise Risk Management","category":"Business","image":"https://img-c.udemycdn.com/course/480x270/5110692_6c60_4.jpg","actual_price_usd":84.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T04:32:00","description":"An enterprise risk management course typically provides students with an in-depth understanding of the concepts, tools, and techniques used to identify, assess, and manage risks to an organization\xe2\x80\x99s capital and earnings. The course may cover topics such as: Different types of risks, including financial, operational, strategic, compliance, and reputational risks Risk management frameworks, such as ISO 31000 or COSO, and how to apply them to an organization Techniques for assessing and measuring risks, including quantitative and qualitative methods Risk management tools and techniques, such as risk mapping, scenario planning, If you\xe2\x80\x99re looking for a course to understand the architecture of risk management based on the newest ISO 31000 standard (2018), this is the course you are looking for. If you\xe2\x80\x99re looking to be practical: to study the tools in assessing the risks, you might have to look for ISO 31010 or other materials to enhance your understanding. Learn how to motivate your employees/colleagues to manage risk on their own without constant prodding, cajoling, and reminders. Bolster your image as an authoritative, confident decision-maker by managing risk instead of letting it manage you! Earn a certificate from Udemy upon course completion and use it in a LinkedIn post. This course is backed by a 30-day refund policy. If you\xe2\x80\x99re not completely satisfied, simply request a refund through your dashboard.","url":"https://www.udemy.com/course/enterprise-risk-management_course/?couponCode=CDF8CAADDB2AECE23CCE","clean_url":"https://www.udemy.com/course/enterprise-risk-management_course/"},{"name":"Cold Email for Beginners: Basic Cold Email Success Guide","category":"Cold Email","image":"https://img-c.udemycdn.com/course/480x270/6360037_831a.jpg","actual_price_usd":0.0,"sale_price_usd":0.0,"sale_end":"2025-01-11T05:03:00","description":"Unlock the power of cold emailing and take your business, career, or side hustle to the next level with this comprehensive, beginner-friendly course! Cold emailing is one of the most effective and cost-efficient ways to reach potential clients, partners, employers, and collaborators. In today\xe2\x80\x99s digital world, mastering this skill can be the key to expanding your network, increasing sales, landing job opportunities, and opening doors to exciting new ventures. Whether you\xe2\x80\x99re an entrepreneur looking to grow your business, a freelancer seeking new clients, or a job seeker hoping to make valuable connections, this course will teach you everything you need to know to successfully use cold emailing as a powerful tool for growth. This course is designed to help you build your cold emailing strategy from the ground up, with easy-to-follow instructions and real-world examples to ensure your outreach is as effective as possible. In this course, you\xe2\x80\x99ll start by learning the basics of cold emailing, including what it is, why it works, and how it can help you connect with the right people. You\xe2\x80\x99ll also discover how to craft compelling, personalized emails that grab attention, stand out in crowded inboxes, and get results. From writing irresistible subject lines to developing concise and persuasive email content, you\xe2\x80\x99ll learn how to engage your recipients from the first word. As you progress, we\xe2\x80\x99ll dive into advanced strategies for automating and scaling your cold email campaigns, so you can reach more people in less time while maintaining a personal touch. You\xe2\x80\x99ll also learn how to track the performance of your emails, analyze key metrics, and optimize your outreach for better results. Automation and tracking will allow you to refine your campaigns and continuously improve your cold emailing techniques. In addition to the practical aspects of writing and sending emails, this course covers crucial legal and ethical considerations you need to know before hitting \xe2\x80\x9csend.\xe2\x80\x9d Learn about the CAN-SPAM Act, GDPR, and other regulations that govern cold emailing. By the end of this course, you\xe2\x80\x99ll have a clear understanding of how to ensure your cold emails are compliant, ethical, and effective. By the end of this course, you\xe2\x80\x99ll be ready to craft and send your own cold emails with confidence. You\xe2\x80\x99ll have the tools and strategies to generate leads, build lasting business relationships, secure job interviews, and grow your network. Whether you\xe2\x80\x99re a total beginner or have some experience with cold emailing, this course will equip you with the knowledge and skills you need to achieve success in your email outreach efforts. Join now and start mastering the art of cold emailing today! Get ready to take action, build connections, and unlock new opportunities that could change your business or career.","url":"https://www.udemy.com/course/cold-email-for-beginners-basic-cold-email-success-guide-tareq-hajj/?couponCode=A6BC34AB089E48DF378D","clean_url":"https://www.udemy.com/course/cold-email-for-beginners-basic-cold-email-success-guide-tareq-hajj/"},{"name":"The SEO Link Building Course Back link building SEO tutorial","category":"Link Building","image":"https://img-c.udemycdn.com/course/480x270/3227123_9c86.jpg","actual_price_usd":59.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T06:12:00","description":"No description available","url":"https://www.udemy.com/course/seo-link-building-course/?couponCode=B61369A1E833FDC0B020","clean_url":"https://www.udemy.com/course/seo-link-building-course/"},{"name":"Essential Excel With Tips Trick Shortcuts and Job Success","category":"Excel","image":"https://img-c.udemycdn.com/course/480x270/5313324_8cc2.jpg","actual_price_usd":49.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T06:50:00","description":"Those who desire to develop their skills in Excel should enroll in this course. You\xe2\x80\x99ll pick up new techniques, hints, functions, and shortcuts that will boost your productivity and efficiency at work. This course was developed to show Excel users how to avoid typical spreadsheet pitfalls and unlock Excel\xe2\x80\x99s full potential. We are confident that taking this course will help you gain the abilities you need because all the knowledge that is covered in it and that you will learn is exactly what we wish we had known when we first started using the Excel tool in a professional setting. We\xe2\x80\x99ll dive into a broad range of Excel formulas & functions, including: Lookup/Reference functions Statistical functions Formula-based formatting Date & Time functions Logical operators Dynamic Array formulas Text functions By the end of the course you\xe2\x80\x99ll be writing robust, elegant formulas from scratch, allowing you to: Easily build dynamic tools & Excel dashboards to filter, display and analyze your data Create your own formula-based Excel formatting rules Join datasets from multiple sources with XLOOKUP, INDEX & MATCH functions Manipulate dates, times, text, and arrays Automate tedious and time-consuming tasks using cell formulas and functions in Excel If you\xe2\x80\x99re looking for the course with all of the advanced Excel formulas and functions that you need to know to become an absolute Excel ninja, you\xe2\x80\x99ve found it.","url":"https://www.udemy.com/course/essential-excel-with-tips-trick-shortcuts-and-job-success/?couponCode=5F666A88E6299A879B30","clean_url":"https://www.udemy.com/course/essential-excel-with-tips-trick-shortcuts-and-job-success/"},{"name":"Complete MS Office and Web Design Development Course","category":"Microsoft","image":"https://img-c.udemycdn.com/course/480x270/5315174_1660.jpg","actual_price_usd":74.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T06:50:00","description":"Welcome to this comprehensive course that covers the essentials of MS Word, Excel, PowerPoint, HTML, CSS, and WordPress. Whether you\xe2\x80\x99re a student, professional, or someone looking to enhance their digital skills, this course is designed to provide you with a solid foundation in these widely-used tools and technologies. In the first part of the course, we will dive into the world of Microsoft Office. You\xe2\x80\x99ll learn how to create professional-looking documents using MS Word, including formatting text, adding images and tables, and creating templates. In MS Excel, we\xe2\x80\x99ll cover the fundamentals of data management, formulas, functions, and charts to help you effectively analyze and present data. Moving on to MS PowerPoint, you\xe2\x80\x99ll discover how to create captivating presentations by mastering slide design, transitions, animations, and multimedia integration. The second part of the course focuses on web development. We\xe2\x80\x99ll start with HTML, the building block of every webpage. You\xe2\x80\x99ll learn how to structure content, create links, add images, and incorporate basic styling. Then, we\xe2\x80\x99ll delve into CSS, which allows you to enhance the visual appeal of your web pages. You\xe2\x80\x99ll understand how to apply styles, manage layouts, and create responsive designs that adapt to different devices. Finally, we\xe2\x80\x99ll explore WordPress, a popular content management system (CMS) used to create and manage websites. You\xe2\x80\x99ll learn how to install WordPress, customize themes, create pages and blog posts, and leverage plugins to extend functionality. Whether you\xe2\x80\x99re a beginner or have some experience with WordPress, this section will empower you to build and maintain your own websites without any coding knowledge. Throughout the course, you\xe2\x80\x99ll have hands-on exercises, quizzes, and projects to reinforce your learning. By the end, you\xe2\x80\x99ll have a solid understanding of these tools and technologies, enabling you to boost your productivity, create professional documents and presentations, and develop engaging websites. So, let\xe2\x80\x99s embark on this learning journey together and unlock the full potential of these versatile tools and technologies.","url":"https://www.udemy.com/course/complete-ms-office-and-web-design-development-course/?couponCode=2C9BEA20DBC75DF13435","clean_url":"https://www.udemy.com/course/complete-ms-office-and-web-design-development-course/"},{"name":"Ethical Hacking: Linux Privilege Escalation","category":"Ethical Hacking","image":"https://img-c.udemycdn.com/course/480x270/4678800_f8f2.jpg","actual_price_usd":19.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T10:26:00","description":"No description available","url":"https://www.udemy.com/course/ethical-hacking-linux-privilege-escalation/?couponCode=BEWISE","clean_url":"https://www.udemy.com/course/ethical-hacking-linux-privilege-escalation/"},{"name":"Excel Malware Investigation: Tools & Techniques","category":"Cyber Security","image":"https://img-c.udemycdn.com/course/480x270/6296033_e931.jpg","actual_price_usd":54.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T10:37:00","description":"Discover the Secrets of Excel-Based Malware Are you aware that Excel can be a powerful tool for cybercriminals? Learn how to protect yourself and others by gaining the skills necessary to identify, investigate, and respond to Excel-based malware. In our course,\xc2\xa0 Excel Malware Investigation: Tools & Techniques , you\xe2\x80\x99ll delve into the methods used by attackers and the defensive skills you need to combat them. What You\xe2\x80\x99ll Learn: Introduction to Microsoft Excel Security : Understand how Excel features can be exploited and why attackers target Excel documents. Macros and Their Misuse : Learn about macros, their legitimate uses, and how attackers use them to create malware. Hands-on Malware Demo : Watch a live demo of how Excel files are weaponized to help connect theoretical concepts to practical scenarios. Identify Malicious Scripts : Gain experience in identifying hidden scripts and understanding malicious behavior in Excel files. Tools and Techniques : Get hands-on with analysis tools that will help you detect and mitigate threats in Excel spreadsheets. Why Take This Course? Excel is commonly used in day-to-day operations, and that makes it an attractive target for cybercriminals. Understanding how attackers use Excel for malicious purposes and how to detect these attacks can be invaluable whether you\xe2\x80\x99re working in cybersecurity, IT, or just want to be more cyber-aware. This course is designed to be highly practical and hands-on. You will watch real malware demonstrations and learn how to use specialized tools to analyze and investigate Excel malware. No matter your current skill level, you\xe2\x80\x99ll walk away with valuable knowledge that will make a real difference in your ability to secure your environment. Who Should Enroll? Cybersecurity Professionals : Stay ahead of emerging threats and add Excel malware investigation to your skillset. IT Administrators : Equip yourself to detect and prevent malicious Excel files in your organization. Students & Enthusiasts : Gain practical experience with real-world malware scenarios and elevate your cybersecurity knowledge. Course Highlights Live Demonstrations : Witness Excel malware in action and understand the full attack lifecycle. Practical Tools : Install and use analysis tools to help you become adept at identifying malicious scripts. Step-by-Step Guidance : Learn in an easy-to-follow way, making complex topics accessible for everyone. Enroll Now and Gain the Skills to Protect Against Excel-Based Cyber Threats Excel malware attacks are on the rise, and gaining expertise in analyzing these threats is a valuable skill in today\xe2\x80\x99s cybersecurity landscape. By enrolling in\xc2\xa0 Excel Malware Investigation: Tools & Techniques , you\xe2\x80\x99re taking the first step to becoming a critical defender in the digital world.","url":"https://www.udemy.com/course/excel-malware-investigation/?couponCode=WISEDAY","clean_url":"https://www.udemy.com/course/excel-malware-investigation/"},{"name":"PowerShell Regular Expressions: Regex Master Class","category":"IT & Software","image":"https://img-c.udemycdn.com/course/480x270/5921432_3194_2.jpg","actual_price_usd":44.99,"sale_price_usd":0.0,"sale_end":"2025-01-11T11:48:00","description":"If You want to  Master PowerShell Regular Expressions (Regex) , Then this course is for you. If your want to unlock the power of regular expressions? Look no further! In this course, we dive into the fascinating world of  regex  and explore how it can supercharge your PowerShell scripting. In this Course, you will learn: Fundamentals of regular expressions:  Understand the syntax, metacharacters, and quantifiers used in regex patterns. Pattern matching techniques:  Learn how to construct regex patterns to match specific text patterns, including literal strings, character classes, and anchors. Capturing and grouping:  Explore advanced regex features such as capturing groups and backreferences to extract and manipulate data from complex text strings. Regex in PowerShell scripting:  Integrate regular expressions seamlessly into your PowerShell scripts to automate text processing tasks, file manipulation, and data extraction. Best practices and optimization:  Discover tips and techniques for writing efficient and maintainable regex patterns, avoiding common pitfalls, and optimizing performance. By the end of this course, you\xe2\x80\x99ll have the skills and confidence to wield regular expressions like a seasoned PowerShell pro, enabling you to tackle a wide range of text processing challenges with ease and efficiency. Whether you\xe2\x80\x99re parsing log files, extracting information from documents, or transforming text data, mastering PowerShell regular expressions will empower you to take your automation capabilities to the next level.","url":"https://www.udemy.com/course/powershell-masterclass/?couponCode=E0F3CA5EF1F1D1B86C27","clean_url":"https://www.udemy.com/course/powershell-masterclass/"}],"total":77}'
        with open("courses_sent.txt", "a") as file:
            file.write(f"{get_formatted_date()} : ")
            file.write(str(data))
            file.write("\n")
        courses_data = json.loads(data.decode("utf-8"))
        print(courses_data)
        courses = []
        return courses_list(courses_data)

    except Exception as e:
        print(f"Error: {e}")
        return ["error"]

def courses_list(courses_data):
    courses = []
    for course in courses_data.get("courses", []):
        title = course.get("name")
        title = f"[ {title} ]"
        url = course.get("url")
        category = course.get("category")
        price_b = course.get("actual_price_usd")
        price_a = course.get("sale_price_usd")
        sale_end = calculate_remaining_time(course.get("sale_end"))
        description = course.get("description")
        courses.append(f"{title}\ncategory: {category}\ndescription: {description[:150]}...\nactual price: {price_b}$\nSale price: {price_a}$\n Sale end: {sale_end}\n[Link to course] ({url})\n------\n")
    return courses

def calculate_remaining_time(sale_end: str):
    sale_end_format = "%Y-%m-%dT%H:%M:%S"
    sale_end_datetime = datetime.strptime(sale_end, sale_end_format)
    current_datetime = datetime.now()
    time_difference = sale_end_datetime - current_datetime
    days_remaining = time_difference.days
    hours_remaining = time_difference.seconds // 3600
    minutes_remaining = (time_difference.seconds % 3600) // 60
    remaining_time_parts = []
    if days_remaining > 0:
        remaining_time_parts.append(f"{days_remaining} days")
    if hours_remaining > 0:
        remaining_time_parts.append(f"{hours_remaining} hours")
    if minutes_remaining > 0:
        remaining_time_parts.append(f"{minutes_remaining} minutes")
    remaining_time = " ".join(remaining_time_parts)
    return remaining_time

def get_formatted_date():
    current_time = datetime.now(pytz.timezone('Africa/Cairo'))
    return current_time.strftime("%d/%m/%y (%I:%M %p)")

def load_allowed_chat_ids(filename="allowed_chat_ids.txt"):
    try:
        with open(filename, "r") as file:
            return set(int(line.strip()) for line in file if line.strip().isdigit())
    except FileNotFoundError:
        print(f"Error: {filename} not found. No users are authorized.")
        return set()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return set()

def auth_user(message):
    user_id = message.from_user.id
    allowed_chat_ids = load_allowed_chat_ids()
    return [user_id in allowed_chat_ids, user_id]

@bot.message_handler(commands=['add_chat_id'])
def add_chat_id(message):
    try:
        if auth_user(message)[0]:  # Only admins can add new IDs
            new_chat_id = int(message.text.replace("/add_chat_id", "").strip())
            with open("allowed_chat_ids.txt", "a") as file:
                file.write(str(new_chat_id))
                file.write("\n")
            bot.reply_to(message, f"Chat ID {new_chat_id} has been added to the allowed list.")
        else:
            bot.reply_to(message, f"Unauthorized access.\nuser: {auth_user(message)[1]}")
    except ValueError:
        bot.reply_to(message, "Invalid chat ID. Please provide a valid integer.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['list_chat_ids'])
def list_chat_ids(message):
    if auth_user(message)[0]:
        allowed_chat_ids = load_allowed_chat_ids()
        if allowed_chat_ids:
            bot.reply_to(message, f"Allowed Chat IDs:\n{', '.join(map(str, allowed_chat_ids))}")
        else:
            bot.reply_to(message, "No chat IDs are currently allowed.")
    else:
        bot.reply_to(message, f"Unauthorized access.\nuser: {auth_user(message)[1]}")

@bot.message_handler(commands=['courses'])
def courses(message):
    if auth_user(message)[0]:
        courses = get_courses(None)
        bot.reply_to(message, f"Free Courses for Today {get_formatted_date()} !\n\n" + "\n\n".join(courses[:5]))
        bot.reply_to(message, f"Free Courses for Today {get_formatted_date()} !\n\n" + "\n\n".join(courses[5:]))
        print(f"process done to user: {auth_user(message)[1]}")
    else:
        bot.reply_to(message,f"Unautorized access?\nuser: {auth_user(message)[1]}")

@bot.message_handler(commands=['search_courses'])
def search_courses(message):
    if auth_user(message)[0]:
        query = message.text.replace("/search_courses", "").strip()
        query = str(query).replace(" ", "%20")
        if query:
            courses = get_courses(query)
            if courses:
                bot.reply_to(message, f"Here are some free courses on {query} For Today ({get_formatted_date()}):\n\n" + "\n\n".join(courses[:5]))
                bot.reply_to(message,f"Here are some free courses on {query} For Today ({get_formatted_date()}):\n\n" + "\n\n".join(courses[5:]))
            else:
                bot.reply_to(message, "No courses found with that tag. Please try another tag.")
        else:
            bot.reply_to(message, "Please provide a tag to search for, e.g., /search_courses python")
    else:
        bot.reply_to(message, f"unautorized access?\nuser: {auth_user(message)[1]}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = (
        "Hello! I can help you find free Udemy courses. Here are the available commands:\n\n"
        "/courses - Get a list of free courses\n"
        "/search_courses <tag> - Search for free courses by tag (e.g., python, data science)\n"
        "/send_daily_courses - Get today's free courses manually\n"
        "/set_course_reminder <time> - Set a daily reminder for free courses (e.g., 08:00)\n"
        "/cancel_course_reminder - Cancel your daily reminder"
    )
    bot.reply_to(message, help_text)

bot.polling(none_stop=True)