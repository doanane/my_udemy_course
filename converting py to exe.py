# with the help of pyinstaller package we can convert.
import webbrowser as wb
def workauto():
    chrome__path__ = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #%s coverts to string
    URLS = ("youtube.com",
            "chatgpt.com",
            "github.com",
            "udemy.com",
            "gmail.com",
            "https://www.sportybet.com/gh/?utm_source=google&utm_medium=cpc&utm_campaign=13788232685&utm_content=119620633370&utm_term=sportybet&utm_source=google&utm_medium=cpc&utm_campaign=13788232685&utm_content=119620633370&utm_term=sportybet&gclid=CjwKCAiAxaCvBhBaEiwAvsLmWPOP1dfABZ_U5uwFwdl34VxX_b3y_m-MF36a01pszKPgczYDbPWWcxoCxb4QAvD_BwE"
            "google.com")
    for url in URLS:
        wb.get(chrome__path__).open(url)
workauto()