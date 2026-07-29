from .rule_based_decision_engine import RuleBasedDecisionEngine

class WorkFlowRegistry:

    def __init__(self):
        self._workflows = {}

    def register(self, workflow_type, handler):

        self._workflows[workflow_type] = handler

    def get(self, workflow_type):

        if workflow_type not in self._workflows:

            raise ValueError(f"No workflow registered for {workflow_type}")

        return self._workflows[workflow_type]