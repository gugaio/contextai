
from context.agents import Agent

class JurusAgent(Agent):

    ID = "jurus_agent"
    NAME = "Jurus Agent"
    TASK = "you are a finance analyst that help to write posts listing the best investments for the user  available in several brokers"

    def __init__(self):
        super().__init__(id=self.ID, name=self.NAME, task=self.TASK)

    def instructions(self):
        if not "broker" in self.context:
            return self._instruction_to_load_broker()
        return self._instruction_to_list_available_investiments_broker_in_context()
    
    def _instruction_to_load_broker(self):
        return "Call load_broker_to_context tool informing the broker id. If the user did not provide the broker id, ask him."
        
    def _instruction_to_list_available_investiments_broker_in_context(self):
        return (
            "The available investments are CBA A, CBA B, CBA C, CBA D, CBA E, CBA F, CBA G, CBA H, CBA I, CBA J."
            "Call the analyse_investment tool informing the investment that the user wants to analyse."
        )

    def tools(self):
        if not "broker" in self.context:
            return [self.load_broker_to_context]
        else:
            return [self.analyse_investment]
    
    def load_broker_to_context(self, broker_id):
        """Load broker to context tool."""
        self.context["broker"] = {
            "id": broker_id
        }
        return "Broker loaded successfully"

    def analyse_investment(self, investiment_id):
        """Generate data to analyse investiment tool."""
        return (
            f"investiment_id: {investiment_id},"
            "taxa: '30%',"
            "prazo: '2 anos',"
        )