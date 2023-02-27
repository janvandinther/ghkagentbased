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
    tab_2.not_in_params_1 = Text("""### Input parameters:\n
- **Num-drivers:** The total number of drivers in the simulation. \n
- **Number-of-stations:** The total number of battery swapping stations \n
- **Number-of-batteries-per-station:** The number of batteries that each station can store and charge. \n
- **Threshold-dc:** The battery percentage where the drivers starts looking for a DC charging station.  \n
- **num-of-dc:**  Number of DC charging spots in a station. \n
- **perc-stations-dc** percentage of stations that have fast charging capability \n
- **average-trip:** Average trip length in patches; \n
    - **deviation-trip:** Deviation in patches per trip. \n
- **average-speed:** The average speed in patches per tick; \n
    - **deviation-speed:**  \n 
- **average-num-trips:** TBA; \n
    - **deviation-num-trips:** \n
- **Power specification** \n
    - **max-power-battery** the maximum charging power of a battery; \n
    - **num-lifecycles**; the maximum lifecycles of a battery\n
    - **max-power-station** the maximum charging power a charging station can provide in total""")

    
    tab_3 = Tab('Why this model is designed')
    tab_3.not_in_params_3 = Text("""### Motivation: \n
Models like these can be used to gain insights into complex systems and phenomena. By running the simulation with different input parameters and scenarios, researchers and policymakers 
can explore "what if" scenarios and test various policies and interventions to see their potential impact on the system. 
For example, they could explore the impact of building more charging stations or increasing the number of batteries per bodaboda driver on the overall utilization of the charging infrastructure. \n
In addition, models like these can also help electricity companies plan for future infrastructure needs. By understanding the potential growth of electric vehicle usage and the corresponding 
demand for charging, they can invest in the development of additional charging stations and other infrastructure to support the increasing demand for electricity. 
    """)
class Controller(ViktorController):
    viktor_enforce_field_constraints = True  # prevents a warning and can be ignored for the purpose of this guide

    label = "ABM Kampala"              # label to be shown in the interface
    parametrization = Parametrization(width=30)
    @WebView('ABM Kampala', duration_guess=1)
    def get_web_view(self, params, **kwargs):
        static_html_path = Path(__file__).parent / 'boda-boda-charging-new.html'
        return WebResult.from_path(static_html_path)

    