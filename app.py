from viktor import ViktorController
from viktor.parametrization import ViktorParametrization, Tab, Section, Text, TextField

from pathlib import Path

from viktor.views import WebResult
from viktor.views import WebView



class Parametrization(ViktorParametrization):
    tab_0 = Tab('Introduction')
    
    tab_0.not_in_params_0 = Text("""## Boda-boda drivers - Agent Based Modeling:
This model simulates the behavior of motorcycle taxi drivers (Boda-boda drivers) in Kampala, Uganda. The simulation is based on a multi-agent system, where each agent represents a Boda-boda driver. 
The agents move around the city and interact with each other and with charging stations, which provide charging services for their electric motorcycles. \n

**The included documentation can be found in the three sections above this text!**""")
    
    tab_0.not_in_params_2 = Text("""### Why was this model is created?
The Bodaboda charging model was created as part of the Greenhub Kampala project to research the behavior of Bodaboda drivers and charging stations. The model was recently presented at the eMobility Workshop 2023 held in Kampala, 
where it received attention from researchers and stakeholders in the transportation and energy sectors. 
The model can be used to simulate different scenarios and evaluate the impact of various policies and interventions on the adoption of electric motorcycles, 
as well as on the electricity demand and grid congestion. Overall, the Bodaboda charging model represents a valuable step towards sustainable 
urban mobility and energy systems in Uganda.""")


    tab_1 = Tab('General Technical Explanation')
    tab_1.not_in_params_2 = Text("""## General Technical Explanation:
The simulation runs in discrete time steps, where each time step represents a fixed amount of time (in the simulation, this is set to 1 minute). 
At each time step, the agents perform various actions based on their current state and the state of the environment. 
These actions include moving to a new location, picking up or dropping off passengers, and charging their motorcycles at a charging station. \n

### Where do the passengers go?
The pickup and drop-off location of the passengers is randomly selected on the map. 
The model includes various parameters that can be set to customize the simulation. These include the number of bodaboda drivers, the number and locations of charging stations, 
the charging rates of the batteries, and the number of passengers available at each location.""")

    tab_2 = Tab('Input parameters')
    tab_2.not_in_params_0 = Text("""## Input parameters:
This model can be controlled with different input parameters. While there are default values for the inputs, the parameters can be tuned to your preferences.""")
    
    tab_2.not_in_params_1 = Text("""### Description:
- **Num-drivers:** The total number of drivers in the simulation. \n
- **Number-of-stations:** The total number of battery swapping stations \n
- **Number-of-batteries-per-station:** The number of batteries that each station can store and charge. \n
- **average-trip:** Average trip length in patches; \n
- **average-speed:** The average speed in patches per tick; \n
- **average-num-trips:** The average number of trips per day per boda driver;
- **Power specification** \n
    - **max-power-battery** the maximum charging power of a battery; \n
    - **num-lifecycles**; the maximum lifecycles of a battery\n
    - **max-power-station** the maximum charging power a charging station can provide in total""")

    
    tab_3 = Tab('Output')
    tab_3.not_in_params_3 = Text("""### Output: \n
The model provides output in a few different graphical reprisentations: \n
- **A time indicator** - shows the amount of time that has passed \n
- **Total Electricity Demand of Swapping Stations** \n
    - **Green:** the total amount of electricity that has been charged \n
    - **Orange:**  the amount of available solar energy\n
- **The State of Charge (SOC)** of two different batteries **starting in a charging station**:\n
    - This shows the state of charge of two random batteries a charging station; if one stays all the time at 100, it is never picked up.\n
- **The State of Charge (SOC)** of two different batteries **starting in a Boda**:\n
    - This shows the state of charge of two random batteries a random Boda; it shows when the batteries are swapped and how intesly they are used.
""")



class Controller(ViktorController):
    viktor_enforce_field_constraints = True  # prevents a warning and can be ignored for the purpose of this guide

    label = "ABM Kampala"              # label to be shown in the interface
    parametrization = Parametrization(width=30)
    @WebView('ABM Kampala', duration_guess=1)
    def get_web_view(self, params, **kwargs):
        static_html_path = Path(__file__).parent / 'boda-boda-charging-ruben.html'
        return WebResult.from_path(static_html_path)

    