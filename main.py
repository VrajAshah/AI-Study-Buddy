from src.factories.agent_factory import AgentFactory

from src.logging.logging import get_logger

logger = get_logger(__name__)

agent = AgentFactory.create()

agent.process_document("artificial_intelligence.pdf")
agent.process_document("solar_system.pdf")
agent.process_document("python_programming.pdf")

while True:
    try:
        question = input("> ")
        response = agent.run(question)
        print(response)
    except Exception as e:
        logger.error("Error in main " + str(e))
        logger.exception(e)
