import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from tools.scraper_tools import ScraperTool

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")
os.environ["OPENAI_API_KEY"] = openai_api_key


#### CURRENT TOOLS AVAILABLE WITHIN CREW AI
##---------------------------------------##
#### SerperDevTool: Google Serper Search
#### ScrapeWebsiteTool: Scrape Website
#### DirectoryReadTool: Directory Read
#### FileReadTool: File Read
#### SeleniumScrapingTool: Selenium Scraper
#### DirectorySearchTool: Directory RAG Search
#### PDFSearchTool: PDF RAG Search
#### TXTSearchTool: TXT RAG Search
#### CSVSearchTool: CSV RAG Search
#### XMLSearchTool: XML RAG Search
#### JSONSearchTool: JSON RAG Search
#### DOCXSearchTool: DOCX RAG Search
#### MDXSearchTool: MDX RAG Search
#### PGSearchTool: PG RAG Search
#### WebsiteSearchTool: Website RAG Search
#### GitHubSearchTool: Github RAG Search
#### YoutubeVideoSearchTool: Youtube Video RAG Search
#### YoutubeChannelSearchTool: Youtube Channel RAG Search


scrape_tool = ScraperTool().scrape


# Define your agents with roles and goals
class NewsletterCrew:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        scraper = Agent(
            role="Summarizer of Websites",
            goal="Ask the user for a list of URLs, then use the WebsiteSearchTool to then scrape the content, and provide the full content to the writer agent so it can then be summarized",
            backstory="""You work at a leading tech think tank.
      Your expertise is taking URLs and getting just the text-based content of them.""",
            verbose=True,
            allow_delegation=False,
            tools=[scrape_tool],
        )
        writer = Agent(
            role="Tech Content Summarizer and Writer",
            goal="Craft compelling short-form content on AI advancements based on long-form text passed to you",
            backstory="""You are a renowned Content Creator, known for your insightful and engaging articles.
      You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True,
        )

        # Create tasks for your agents
        task1 = Task(
            description=f"""Take a list of websites that contain AI content, read/scrape the content and then pass it to the writer agent
      
      here are the URLs from the user that you need to scrape: {self.urls}""",
            agent=scraper,
        )

        task2 = Task(
            description="""Using the text provided by the scraper agent, develop a short and compelling/interesting short-form summary of the 
      text provided to you about AI""",
            agent=writer,
        )

        # Instantiate your crew with a sequential process
        NewsletterCrew = Crew(
            agents=[scraper, writer],
            tasks=[task1, task2],
            verbose=2,  # You can set it to 1 or 2 to different logging levels
        )

        NewsletterCrew.kickoff()


if __name__ == "__main__":
    print("## Welcome to Newsletter Writer")
    print("-------------------------------")
    urls = input(
        dedent(
            """
      What is the URL you want to summarize?
    """
        )
    )

    newsletter_crew = NewsletterCrew(urls)
    result = newsletter_crew.run()
    print("\n\n########################")
    print("## Here is the Result")
    print("########################\n")
    print(result)
