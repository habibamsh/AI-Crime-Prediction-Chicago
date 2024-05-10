import python_actr
from python_actr import *
from python_actr.actr import *
# from python_actr.actr.hdm import *
import random
import time

# Define the ACT-R model
class PoliceResourceAllocationModel(Model):
    def __init__(self):
        super().__init__()

        # Define chunk types
        self.declare_chunktype("crime_event", "neighborhood severity")
        self.declare_chunktype("police_resource", "status neighborhood")

        # Define the declarative memory module
        self.dm = Memory()
        self.dm.add(Chunk(type="crime_event", neighborhood="Downtown", severity="High"))
        self.dm.add(Chunk(type="police_resource", status="Available", neighborhood="Downtown"))

        # Initial goal
        self.goal = Buffer()
        self.retrieval = Buffer()

    # Initial goal setup
    def init(self):
        self.goal.set("decide resource_allocation")

    # Production rules
    @production(goal="decide resource_allocation", retrieval="chunktype:crime_event neighborhood:?neighborhood severity:High")
    def high_severity_crime_response(self, neighborhood):
        self.retrieval.request("chunktype:police_resource status:Available neighborhood:" + neighborhood)
        self.goal.set("allocate resource")

    @production(goal="allocate resource", retrieval="chunktype:police_resource status:Available neighborhood:?neighborhood")
    def allocate_resource(self, neighborhood):
        print(f"Dispatching police resource to {neighborhood}")
        self.goal.set("decide resource_allocation")

# Create and run the model
model = PoliceResourceAllocationModel()
model.run(100)  # Running for 100 cognitive cycles
