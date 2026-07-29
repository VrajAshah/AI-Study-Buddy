from src.factories.agent_factory import AgentFactory

agent = AgentFactory.create()

agent.process_document("01_article_text.pdf")

while True:
    question = input("> ")
    response = agent.run(question)
    print(response)
